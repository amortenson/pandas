from pandas import *
import pandas as pd

playerData = pd.read_csv('stats/Master.csv', usecols = ['playerID', 'nameFirst', 'nameLast', 'nameGiven'])
HRdata = pd.read_csv('stats/Batting.csv', usecols = ['HR', 'playerID', 'yearID'])

#HRdata1 = HRdata.ix[:,['playerID','HR']].groupby('playerID', as_index = False).sum()
#HRtop = HRdata1[HRdata1.HR > 400].sort('HR', ascending = False)
#HRleaders = pd.merge(HRtop, playerData, on = 'playerID').ix[:,['HR','nameFirst','nameLast']]

HRtop = HRdata[HRdata.HR > 50].sort('HR', ascending = False)
HRleaders = pd.merge(HRtop, playerData, on = 'playerID').ix[:,['HR','nameFirst','nameLast', 'yearID']]

HRleaders.to_csv('HRleaders.csv', index_label = "Rank")
#print HRleaders.to_json()
#print HRleaders.to_html()



