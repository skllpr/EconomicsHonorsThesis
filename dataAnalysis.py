import numpy as np
import pandas as pd
import statsmodels.api as sm
data = pd.read_csv('DataEconHonorsThesis.csv')
#convert free reduced into percentile
data['freeReduced'] = data['freeReduced']*100
science = data['Science Proficiency']
math = data['Math Proficiency']
overall = data['Overall Proficiency']
x = data.drop(['Science Proficiency','Math Proficiency','Overall Proficiency'], axis=1)
#x = x['freeReduced', 'ASD Population', 'Distances', 'Facility']
features = list(x.iloc[:, 0:].columns)
features.insert(0,'intercept')
x = x.values
#print(x)
#print(overall)
#n_jobs = -1 means all processors
print('overall')
X2 = sm.add_constant(x)
est = sm.OLS(overall, X2)
overall_fit = est.fit()
print(overall_fit.summary2(xname=features))
print("RSE:",overall_fit.scale**.5)
print('\n\n\n\n\n\n\n')


print('science')
X2 = sm.add_constant(x)
est = sm.OLS(science, X2)
science_fit = est.fit()
print(science_fit.summary2(xname=features))
print("RSE:",science_fit.scale**.5)
print('\n\n\n\n\n\n\n')


print('math')
X2 = sm.add_constant(x)
est = sm.OLS(math, X2)
math_fit = est.fit()
print(math_fit.summary2(xname=features))
print("RSE:",math_fit.scale**.5)
print('\n\n\n\n\n\n\n')


print('─' * 100)




x = data.drop(['Science Proficiency','Math Proficiency','Overall Proficiency', 'Facility'], axis=1)
#x = x['freeReduced', 'ASD Population', 'Distances', 'Facility']
features = list(x.iloc[:, 0:].columns)
features.insert(0,'intercept')
x = x.values
#print(x)
#print(overall)
#n_jobs = -1 means all processors
print('overall, no facility')
X2 = sm.add_constant(x)
est = sm.OLS(overall, X2)
overall_fit = est.fit()
print(overall_fit.summary2(xname=features))
print("RSE:",overall_fit.scale**.5)
print('\n\n\n\n\n\n\n')

print('science, no facility')
X2 = sm.add_constant(x)
est = sm.OLS(science, X2)
science_fit = est.fit()
print(science_fit.summary2(xname=features))
print("RSE:",science_fit.scale**.5)
print('\n\n\n\n\n\n\n')

print('math, no facility')
X2 = sm.add_constant(x)
est = sm.OLS(math, X2)
math_fit = est.fit()
print(math_fit.summary2(xname=features))
print("RSE:",math_fit.scale**.5)
print('\n\n\n\n\n\n\n')