import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

dados = pd.read_csv('./train.csv')

dados = dados.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis = 1)

dados = dados.set_index(['PassengerId'])
dados = dados.rename(columns = {'Survived': 'target'}, inplace=False)

dados['sex_f'] = np.where(dados['Sex'] == 'female', 1, 0)

dados['Pclass1'] = np.where(dados['Pclass'] == 1, 1, 0)
dados['Pclass2'] = np.where(dados['Pclass'] == 2, 1, 0)
dados['Pclass3'] = np.where(dados['Pclass'] == 3, 1, 0)

dados = dados.drop(['Pclass', 'Sex'], axis=1)

dados.fillna(0, inplace=True)

x_train, x_test, y_train, y_test = train_test_split(
    dados.drop(['target'], axis=1), dados['target'], test_size = 0.3, random_state = 1224)

rndforest = RandomForestClassifier(n_estimators=1000, criterion='gini',max_depth=5)

rndforest.fit(x_train, y_train)

propabilidade = rndforest.predict_proba(dados.drop('target', axis=1))[:,1]
classificacao = rndforest.predict(dados.drop('target', axis=1))

dados['probabilidade'] = propabilidade
dados['classificacao'] = classificacao

print(dados.head())