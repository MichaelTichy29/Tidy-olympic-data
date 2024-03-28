#General structure and cleaning of the olymoic data.
import pandas as pd
import numpy as np




df_ol = pd.read_csv('dataset_olympics.csv', encoding = 'cp850')
#print(df_ol.columns)


#shape of the original dataset
print("original olympic data set")
print(df_ol.shape)
print("") 


# Test for empty cells
y = df_ol.isnull().sum()
z = df_ol.shape
print(df_ol.shape)
for k in range (0,z[1]): 
    print(y[k])
    print(df_ol.columns[k])
    print("")

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

### outlier weight
mean = np.mean(df_ol.Weight)
std = np.std(df_ol.Weight)
print(" ")
print("mean weight = ", mean)
print("std weight = ", std)
weight_z = (df_ol.Weight - mean)/std
# apply threshold
threshold = 3
print("outlier")
print(weight_z[weight_z >= threshold])
### outlier age
mean = np.mean(df_ol.Age)
std = np.std(df_ol.Age)
print(" ")
print("mean age = ", mean)
print("std age = ", std)
age_z = (df_ol.Age - mean)/std
# apply threshold
threshold = 3
print("outlier")
print(age_z[age_z >= threshold])

print("")
print("For the height")
dftest = df_ol.nlargest(10, 'Height')
del dftest['ID']
del dftest['Name']
del dftest['Team']
del dftest['NOC']
del dftest['Year']
del dftest['Games']
del dftest['Season']
del dftest['City']
del dftest['Medal']
print(dftest)



dftest = df_ol.nsmallest(10, 'Height')
del dftest['ID']
del dftest['Name']
del dftest['Team']
del dftest['NOC']
del dftest['Year']
del dftest['Games']
del dftest['Season']
del dftest['City']
del dftest['Medal']
print(dftest)

print("")
print("For the weight")
dftest = df_ol.nlargest(10, 'Weight')
del dftest['ID']
del dftest['Name']
del dftest['Team']
del dftest['NOC']
del dftest['Year']
del dftest['Games']
del dftest['Season']
del dftest['City']
del dftest['Medal']
print(dftest)



dftest = df_ol.nsmallest(10, 'Weight')
del dftest['ID']
del dftest['Name']
del dftest['Team']
del dftest['NOC']
del dftest['Year']
del dftest['Games']
del dftest['Season']
del dftest['City']
del dftest['Medal']
print(dftest)

print("")
print("For the age")
dftest = df_ol.nlargest(10, 'Age')
del dftest['ID']
del dftest['Name']
del dftest['Team']
del dftest['NOC']
del dftest['Year']
del dftest['Games']
del dftest['Season']
del dftest['City']
del dftest['Medal']
print(dftest)

dftest = df_ol.nsmallest(10, 'Age')
del dftest['ID']
del dftest['Name']
del dftest['Team']
del dftest['NOC']
del dftest['Year']
del dftest['Games']
del dftest['Season']
del dftest['City']
del dftest['Medal']
print(dftest)



df_hei = pd.read_csv('average-height-by-year-of-birth.csv', encoding = 'cp850')
print(df_hei.columns)


#shape of the original dataset
print("original height data set")
print(df_hei.shape)
print("") 


# Test for empty cells
y = df_hei.isnull().sum()
z = df_hei.shape
print(df_hei.shape)
for k in range (0,z[1]): 
    print(y[k])
    print(df_hei.columns[k])
    print("")


###########
# Cleansing of olympic data
###########

# Duplicates: 
df_ol = df_ol.drop_duplicates()    
print("shape without duplicates", df_ol.shape)


##
#Dropna for analytics
##

#Dataset to analyse the height
df_ol_cl_hei = df_ol.dropna(subset = ['Height'])
print("shape for height analyse", df_ol_cl_hei.shape)

#Dataset to analyse the weight
df_ol_cl_wei = df_ol.dropna(subset = ['Weight'])
print("shape for weight analyse", df_ol_cl_wei.shape)

#Dataset to analyse the height and weight
df_ol_cl_all = df_ol.dropna(subset = ['Weight', 'Height', 'Age'])
print("shape for generall analyse", df_ol_cl_all.shape)



###################
# Fill with mean as estimation
###################


##
#For the height
##

# split for gender
df_estw = df_ol.drop(df_ol[df_ol['Sex'] == "M"].index)
df_estm = df_ol.drop(df_ol[df_ol['Sex'] == "W"].index)

# general mean for men an women
akt_dfh = df_estm.dropna(subset = ['Height'])
meanm = akt_dfh['Height'].mean()
akt_dfh = df_estw.dropna(subset = ['Height'])
meanw = akt_dfh['Height'].mean()
print("mean for men", meanm)
print("mean for women", meanw)



df_ol = df_ol.fillna({'Height':-1})


sports = np.unique(df_estm['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estm.drop(df_estm[df_estm['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Height'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = meanm
    else:
        meanh = akt_dfh['Height'].mean()
    if s == "Fencing":
        print("fencing mean of height is", meanh)    
    df_ol.loc[((df_ol.Sex == "M") & (df_ol.Sport == s) & (df_ol.Height == -1)), 'Height'] = meanh
    
        
sports = np.unique(df_estw['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estw.drop(df_estw[df_estw['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Height'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = meanw
    else:
        meanh = akt_dfh['Height'].mean()
        df_ol.loc[((df_ol.Sex == "W") & (df_ol.Sport == s) & (df_ol.Height == -1)), 'Height'] = meanh

##
#For the weight
##

# general mean for men an women
akt_dfh = df_estm.dropna(subset = ['Weight'])
meanm = akt_dfh['Weight'].mean()
akt_dfh = df_estw.dropna(subset = ['Weight'])
meanw = akt_dfh['Weight'].mean()

df_ol = df_ol.fillna({'Weight':-1})


sports = np.unique(df_estm['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estm.drop(df_estm[df_estm['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Weight'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = meanm
    else:
        meanh = akt_dfh['Weight'].mean()
    df_ol.loc[((df_ol.Sex == "M") & (df_ol.Sport == s) & (df_ol.Weight == -1)), 'Weight'] = meanh
    
        
sports = np.unique(df_estw['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estw.drop(df_estw[df_estw['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Weight'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = meanw
    else:
        meanh = akt_dfh['Weight'].mean()
        df_ol.loc[((df_ol.Sex == "W") & (df_ol.Sport == s) & (df_ol.Weight == -1)), 'Weight'] = meanh

    

##
#For the Age
##

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
        meanh = meanm
    else:
        meanh = akt_dfh['Age'].mean()
    df_ol.loc[((df_ol.Sex == "M") & (df_ol.Sport == s) & (df_ol.Age == -1)), 'Age'] = meanh
    
        
sports = np.unique(df_estw['Sport'])
sport1 = sports.tolist()
for s in sport1:
    akt_df = df_estw.drop(df_estw[df_estw['Sport'] != s].index)
    akt_dfh = akt_df.dropna(subset = ['Age'])
    z = akt_dfh.shape
    if z[0] == 0: 
        meanh = meanw
    else:
        meanh = akt_dfh['Age'].mean()
        df_ol.loc[((df_ol.Sex == "W") & (df_ol.Sport == s) & (df_ol.Weight == -1)), 'Age'] = meanh

##########
# Enrich the data
##########





