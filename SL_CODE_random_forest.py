# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 13:59:59 2024

@author: jim47
"""

#import important libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
import numpy as np
from patsy import dmatrices
from pandas import DataFrame, Series
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score

#import the dataset that we will use for our prediction model 
SL_table = pd.read_csv("D:\data analysis_2\Case Studies\slpredictions\Phase 1\sl_final_table.csv")

#make the model

x = ['xg_pg_H','xg_pg_H','btts_perc_H','fts_perc_H','cs_perc_H','over_perc_H','under_perc_H','cards_against_per_game_H','corners_for_pg_H','corners_against_pg_H',
     'xg_pg_A','xg_pg_A','btts_perc_A','fts_perc_A','cs_perc_A','over_perc_A','under_perc_A','cards_against_per_game_A','corners_for_pg_A','corners_against_pg_A']

y = 'result'

train, test = train_test_split(SL_table, test_size=0.20)
model = RandomForestClassifier(n_estimators=100)
model.fit(train[x], train[y])

test['result_hat'] = model.predict(test[x])
test['correct'] = (test['result_hat'] == test[y])
test['correct'].mean()

#crossval
model = RandomForestClassifier(n_estimators=100)
res = cross_val_score(model, SL_table[x], SL_table[y], cv=20)
res.mean()

# feature importance
model = RandomForestClassifier(n_estimators=100)
model.fit(SL_table[x], SL_table[y])  # running model fitting on entire dataset
Series(model.feature_importances_, x).sort_values(ascending=False)
