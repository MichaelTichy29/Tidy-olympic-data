# Enrichment of the olympic data
import pandas as pd
import numpy as np


import statistics


df_ol = pd.read_csv('dataset_olympics.csv', encoding = 'cp850')
#print(df_ol.columns)


#shape of the original dataset
print("original olympic data set")
print(df_ol.shape)
print("") 

"""
# outlier height
mean = np.mean(df_ol.Height)
std = np.std(df_ol.Height)
print(" ")
print("mean height = ", mean)
print("std height = ", std)
height_z = (df_ol.Height - mean)/std
# apply threshold
threshold = 3
print("outlier")
print(height_z[height_z >= threshold])
"""



namenliste = ['Country', 'P_NOC', 'P_Birth_Year', 'M', 'F']
#df = pd.read_csv('mental_health_c.csv', encoding = 'cp850', names = namenliste)

df_hei = pd.read_csv('average-height-by-year-of-birth.csv', encoding = 'cp850',header=0, names = namenliste)
#print(df_hei.columns)





#shape of the original dataset
print("original height data set")
print(df_hei.shape)
print("") 
#print(df_hei.iloc[0:5])

###########
# Cleansing of olympic data
###########

# Duplicates: 
df_ol = df_ol.drop_duplicates()    
print("shape without duplicates", df_ol.shape)



#################
# Enrich the data
#################

###
# Trasformation of unit
###

df_ol["Height feet"] = round(df_ol["Height"] * 0.0328084, 1)
df_ol["Weight lbs"] = round(df_ol["Weight"] * 2.20462, 1)

dftest = df_ol
#print(dftest.columns)
dftest = dftest.drop(['Sex', 'Age', 'Team', 'NOC', 'Games',
       'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'], axis = 1)




#### Doppelt:
###############################################
###############################################
    
# split for gender
df_estw = df_ol.drop(df_ol[df_ol['Sex'] == "M"].index)
df_estm = df_ol.drop(df_ol[df_ol['Sex'] == "W"].index)


# general mean for men an women
akt_dfh = df_estm.dropna(subset = ['Age'])
meanm = akt_dfh['Age'].mean()
akt_dfh = df_estw.dropna(subset = ['Age'])
meanw = akt_dfh['Age'].mean()

df_ol = df_ol.fillna({'Age':-1})


sports = np.unique(df_estm['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estm.drop(df_estm[df_estm['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Age'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = int(meanm)
    else:
        meanh = int(akt_dfh['Age'].mean())
    df_ol.loc[((df_ol.Sex == "M") & (df_ol.Sport == s) & (df_ol.Age == -1)), 'Age'] = meanh
    
        
sports = np.unique(df_estw['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estw.drop(df_estw[df_estw['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Age'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = int(meanw)
    else:
        meanh = int(akt_dfh['Age'].mean())
    df_ol.loc[((df_ol.Sex == "W") & (df_ol.Sport == s) & (df_ol.Weight == -1)), 'Age'] = meanh


#####Ende Doppelt:
###############################################
###############################################




df_ol["Birth_Year"] = df_ol["Year"] - df_ol["Age"]
 
###
# Join the mean for the height
###

df_height_long = df_hei.melt(id_vars=['Country', 'P_NOC', 'P_Birth_Year'], var_name='Sex', value_name='Pop_Height')

del df_height_long['Country'] 



# Umbenennen NOC in der height tabelle
df_height_long.P_NOC = df_height_long.P_NOC.replace('NLD', 'NED')
df_height_long.P_NOC = df_height_long.P_NOC.replace('DNK', 'DEN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BGR', 'BUL')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GRC', 'GRE')
df_height_long.P_NOC = df_height_long.P_NOC.replace('TCD', 'CHA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('CHL', 'CHI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('NIC', 'NCA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('NGA', 'NGR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('DZA', 'ALG')
df_height_long.P_NOC = df_height_long.P_NOC.replace('KWT', 'KUW')
df_height_long.P_NOC = df_height_long.P_NOC.replace('ARE', 'UAE')
df_height_long.P_NOC = df_height_long.P_NOC.replace('LBN', 'LIB')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MYS', 'MAS')
df_height_long.P_NOC = df_height_long.P_NOC.replace('IRN', 'IRI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('ZAF', 'RSA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('TZA', 'TAN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('SDN', 'SUD')
df_height_long.P_NOC = df_height_long.P_NOC.replace('LBY', 'LBA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('PSE', 'PLE')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BRN', 'BRU')
df_height_long.P_NOC = df_height_long.P_NOC.replace('SAU', 'KSA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BHR', 'BRN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('IDN', 'INA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('PHL', 'PHI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('AGO', 'ANG')
df_height_long.P_NOC = df_height_long.P_NOC.replace('ATG', 'ANT')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BHS', 'BAH')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BGD', 'BAN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BRB', 'BAR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BMU', 'BER')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BTN', 'BHU')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BLZ', 'BIZ')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BWA', 'BOT')
df_height_long.P_NOC = df_height_long.P_NOC.replace('BFA', 'BUR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('KHM', 'CAM')
df_height_long.P_NOC = df_height_long.P_NOC.replace('COG', 'CGO')
df_height_long.P_NOC = df_height_long.P_NOC.replace('CRI', 'CRC')
df_height_long.P_NOC = df_height_long.P_NOC.replace('HRV', 'CRO')
df_height_long.P_NOC = df_height_long.P_NOC.replace('SLV', 'ESA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('FJI', 'FIJ')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GMB', 'GAM')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GNB', 'GBS')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GNQ', 'GEQ')
df_height_long.P_NOC = df_height_long.P_NOC.replace('DEU', 'GER')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GRD', 'GRN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GTM', 'GUA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('GIN', 'GUI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('HTI', 'HAI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('HND', 'HON')
df_height_long.P_NOC = df_height_long.P_NOC.replace('LVA', 'LAT')
df_height_long.P_NOC = df_height_long.P_NOC.replace('LBR', 'LBR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MDG', 'MAD')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MYS', 'MAL')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MWI', 'MAW')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MNG', 'MGL')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MUS', 'MRI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MRT', 'MTN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('MMR', 'MYA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('NPL', 'NEP')
df_height_long.P_NOC = df_height_long.P_NOC.replace('NER', 'NIG')
df_height_long.P_NOC = df_height_long.P_NOC.replace('OMN', 'OMA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('PRY', 'PAR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('PRT', 'POR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('PRI', 'PUR')
df_height_long.P_NOC = df_height_long.P_NOC.replace('WSM', 'SAM')
df_height_long.P_NOC = df_height_long.P_NOC.replace('SYC', 'SEY')
df_height_long.P_NOC = df_height_long.P_NOC.replace('KNA', 'SKN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('SVN', 'SLO')
df_height_long.P_NOC = df_height_long.P_NOC.replace('SLB', 'SOL')
df_height_long.P_NOC = df_height_long.P_NOC.replace('LKA', 'SRI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('CHE', 'SUI')
df_height_long.P_NOC = df_height_long.P_NOC.replace('TON', 'TGA')
df_height_long.P_NOC = df_height_long.P_NOC.replace('TGO', 'TOG')
df_height_long.P_NOC = df_height_long.P_NOC.replace('URY', 'URU')
df_height_long.P_NOC = df_height_long.P_NOC.replace('VNM', 'VIE')
df_height_long.P_NOC = df_height_long.P_NOC.replace('VUT', 'VAN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('VCT', 'VIN')
df_height_long.P_NOC = df_height_long.P_NOC.replace('ZMB', 'ZAM')
df_height_long.P_NOC = df_height_long.P_NOC.replace('ZWE', 'ZIM')



# jahr: > 1996 -> 1996
# jahr: < 1896 -> 1896
df_ol["P_Birth_Year"] = df_ol["Birth_Year"]
df_ol["P_Birth_Year"] = np.where(df_ol["Birth_Year"] > 1996, 1996, df_ol["P_Birth_Year"])
df_ol["P_Birth_Year"] = np.where(df_ol["Birth_Year"] < 1896, 1896, df_ol["P_Birth_Year"])


# reordering not or not all the time existing countries
df_ol["P_NOC"] = df_ol["NOC"]
df_ol.P_NOC = df_ol.P_NOC.replace('URS', 'RUS')
df_ol.P_NOC = df_ol.P_NOC.replace('EUN', 'RUS')
df_ol.P_NOC = df_ol.P_NOC.replace('AHO', 'NED')
df_ol.P_NOC = df_ol.P_NOC.replace('ANZ', 'AUS')
df_ol.P_NOC = df_ol.P_NOC.replace('ARU', 'NED')
df_ol.P_NOC = df_ol.P_NOC.replace('BOH', 'AUT')
df_ol.P_NOC = df_ol.P_NOC.replace('LIE', 'AUT')

df_ol.P_NOC = df_ol.P_NOC.replace('CAY', 'CUB')
df_ol.P_NOC = df_ol.P_NOC.replace('CRT', 'GRE')
df_ol.P_NOC = df_ol.P_NOC.replace('FRG', 'GER')
df_ol.P_NOC = df_ol.P_NOC.replace('GDR', 'GER')
df_ol.P_NOC = df_ol.P_NOC.replace('IOA', 'GER')
df_ol.P_NOC = df_ol.P_NOC.replace('ROT', 'GER')
df_ol.P_NOC = df_ol.P_NOC.replace('SAA', 'GER')
df_ol.P_NOC = df_ol.P_NOC.replace('UNK', 'GER')

df_ol.P_NOC = df_ol.P_NOC.replace('GUM', 'MEX')
df_ol.P_NOC = df_ol.P_NOC.replace('ISV', 'USA')
df_ol.P_NOC = df_ol.P_NOC.replace('ISB', 'GBR')
df_ol.P_NOC = df_ol.P_NOC.replace('MON', 'FRA')
df_ol.P_NOC = df_ol.P_NOC.replace('NBO', 'BRU')
df_ol.P_NOC = df_ol.P_NOC.replace('RHO', 'ZIM')
df_ol.P_NOC = df_ol.P_NOC.replace('SMR', 'ITA')
df_ol.P_NOC = df_ol.P_NOC.replace('TPE', 'CHN')
df_ol.P_NOC = df_ol.P_NOC.replace('WIF', 'IND')
df_ol.P_NOC = df_ol.P_NOC.replace('YMD', 'YEM')
df_ol.P_NOC = df_ol.P_NOC.replace('YUG', 'CRO')
df_ol.P_NOC = df_ol.P_NOC.replace('TCH', 'CZE')
df_ol.P_NOC = df_ol.P_NOC.replace('MAL', 'THA')
df_ol.P_NOC = df_ol.P_NOC.replace('ASA', 'SAM')
df_ol.P_NOC = df_ol.P_NOC.replace('VNM', 'VIE')
df_ol.P_NOC = df_ol.P_NOC.replace('SCG', 'SRB')
df_ol.P_NOC = df_ol.P_NOC.replace('UAR', 'UAE')
df_ol.P_NOC = df_ol.P_NOC.replace('YAR', 'YEM')


df_oln = df_ol.merge(df_height_long, on=['Sex', 'P_Birth_Year', 'P_NOC'], how = "left")


dftest1 = df_oln[(df_oln['Pop_Height'].isnull() == True)]
unique_vals = np.unique(dftest1['NOC'].apply(str))
nr_vals = len(unique_vals)
print ("number of values for the feature {}: {} -- {}".format("NOC", nr_vals, unique_vals))



dftest = df_oln[(df_oln['Pop_Height'].isnull() == True)]
nat = np.unique(dftest['P_NOC'])
nat1 = nat.tolist()
df_oln = df_oln.fillna({'Pop_Height':-1})
for s in nat1:
    akt_df = df_height_long.drop(df_height_long[df_height_long['P_NOC'] != s].index)
    #For men
    akt_dfh = akt_df.drop(akt_df[akt_df['Sex'] == "F"].index)
    df_oln.loc[((df_oln.Sex == "M") & (df_oln.P_NOC == s) & (df_oln.Pop_Height == -1)), 'Pop_Height'] = meanh
    #For women
    akt_dfh = akt_df.drop(akt_df[akt_df['Sex'] == "M"].index)
    meanh = akt_dfh['Pop_Height'].mean()
    df_oln.loc[((df_oln.Sex == "F") & (df_oln.P_NOC == s) & (df_oln.Pop_Height == -1)), 'Pop_Height'] = meanh
    



# Deleting of help columns
del df_oln['P_NOC']
del df_oln['P_Birth_Year']




###
# Estimation of standard deviation
###
# estimated over the kind of sport for each sex.

   
# split for gender
df_estw = df_ol.drop(df_ol[df_ol['Sex'] == "M"].index)
df_estm = df_ol.drop(df_ol[df_ol['Sex'] == "W"].index)


# general mean for men an women
akt_dfh = df_estm.dropna(subset = ['Height'])
values = akt_dfh['Height'].tolist()
var_h = statistics.variance(values)
stdm = var_h**0.5
#
akt_dfh = df_estw.dropna(subset = ['Height'])
values = akt_dfh['Height'].tolist()
var_h = statistics.variance(values)
stdw = var_h**0.5


#Default
df_oln["stdvar_sport"] = -1


# For men
sports = np.unique(df_estm['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estm.drop(df_estm[df_estm['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Height'])
    z = akt_dfh.shape
    if z[0] < 2: 
        stdfill = stdm
    else:
        values = akt_dfh['Height'].tolist()
        var_h = statistics.variance(values)
        stdfill = var_h**0.5
    df_oln.loc[((df_oln.Sex == "M") & (df_ol.Sport == s)), 'stdvar_sport'] = stdfill
    
#For women        
sports = np.unique(df_estw['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estw.drop(df_estw[df_estw['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Height'])
    z = akt_dfh.shape
    if z[0] < 2: 
        stdfill = stdw
    else:
        values = akt_dfh['Height'].tolist()
        var_h = statistics.variance(values)
        stdfill = var_h**0.5
    df_oln.loc[((df_oln.Sex == "F") & (df_ol.Sport == s)), 'stdvar_sport'] = stdfill

df_oln["z_value"] = (df_oln["Height"] - df_oln["Pop_Height"])/df_oln["stdvar_sport"]

threshold = 3
print("outlier")
print(df_oln.z_value[df_oln.z_value >= threshold])



