import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

#df = pd.read_csv('Elad.csv', encoding= 'unicode_escape')
df = pd.read_csv('C:\\Users\\andra\\OneDrive\\Documents\\python\\mlr\\Elad.csv', encoding= 'utf-8')
#print(df)
df=df.dropna(axis=0, how='any')
df_array = df.values
print(df_array)
#train_group = [2,3,4,5,6,7,8,9,10,11,12,13,14,15] #all Z
train_group = [0,1,2,3] #all Z
values = df_array[:,train_group] 
#values = []
        #['Z','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13'])
reframed = pd.DataFrame(values, columns = 
        ['Ar_MFt','Ingatlan_nm','Telek_nm','Allapot'])
#X,Y = reframed[['T1','T2','T3','T4','T5','T6','T7','T8','T9','T10','T11','T12','T13']] , 
X,Y = reframed[['Ingatlan_nm','Telek_nm','Allapot']], reframed [['Ar_MFt']]


est = sm.OLS(Y, X)
#est = sm.GLS(Y, X)
est2 = est.fit()
print(est2.summary())
