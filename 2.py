import pandas as pd
data=pd.read_csv('titanic.csv')
print(data.info())
print(data['Sex'].value_counts())
print(data['Survived'].value_counts())
print(data.groupby('Sex')['Survived'].value_counts())
print(data.groupby('Pclass')['Survived'].value_counts())
print(data['Age'].describe())
data['FamilySize']=data['Parch']+data['SibSp']+1
print(data['FamilySize'][15])
print(data.groupby('Survived')['Age'].mean())
print(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)].count())
print(data[(data['Age'] < 18) & (data['Parch'] == 0)].count())