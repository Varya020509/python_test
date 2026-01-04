import pandas as pd
pd.set_option('display.max_columns',None)
data = pd.read_csv('titanic.csv')
new_data = data.dropna()
# print(data.info())
# print(data.describe())
# k = data[data.Sex== "male"]
# print((data.Sex == "male").sum())
# print((data.Pclass == 1).sum())
# print(data['Survived'].value_counts())
# a = data[data.Sex == 'female']
# b = data[data.Sex == 'male']
# print(((data.Survived == 1).sum()*100)/(data.Survived).count())
# print(((a.Survived == 1).sum()*100)/(a.Survived.count()))
# print(((b.Survived == 1).sum()*100)/(b.Survived).count())
# srp = data[data.Pclass == 1]
# trk = data[data.Pclass == 3]
# print(((srp.Fare.sum())/(srp.Fare.count())))
# print (((trk.Survived==1).sum()*100)/(trk.Survived).count())
# print(data['Age'].describe())
# data['FamilySize']=data['Parch']+data['SibSp']+1
# print(data['FamilySize'][15])
# print(data.groupby('Survived')['Age'].mean())
# print(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)].count())
# print(data[(data['Age'] < 18) & (data['Parch'] == 0)].count())
