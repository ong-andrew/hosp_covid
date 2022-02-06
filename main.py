import pandas as pd
import datetime
from datetime import date, timedelta

data = 'https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/hospital.csv'

mergeKV = {'Selangor': 'Sel & WP',
'W.P. Kuala Lumpur': 'Sel & WP',
'W.P. Putrajaya': 'Sel & WP'
}

labuan = {'W.P. Labuan': 'Labuan'}

malaysia = {'Johor': 'Malaysia',
'Kedah': 'Malaysia',
'Kelantan': 'Malaysia',
'Melaka': 'Malaysia',
'Negeri Sembilan': 'Malaysia',
'Pahang': 'Malaysia',
'Perak': 'Malaysia',
'Perlis': 'Malaysia',
'Pulau Pinang': 'Malaysia',
'Sabah': 'Malaysia',
'Sarawak': 'Malaysia',
'Selangor': 'Malaysia',
'Terengganu': 'Malaysia',
'Sel & WP': 'Malaysia',
'W.P. Kuala Lumpur': 'Malaysia',
'W.P. Labuan': 'Malaysia',
'W.P. Putrajaya': 'Malaysia'
}

#Write Malaysia to CSV
start = date.today() - timedelta(days = 90)
df = pd.read_csv(data, usecols=['date','state','hosp_pui','hosp_covid'], parse_dates=['date'])
sum_covid = df['hosp_covid'] + df['hosp_pui']
df['hospitalised'] = sum_covid
df.state = df.state.replace(malaysia)
df = df.groupby(['date','state']).sum().reset_index()
df = df[df.date.dt.date >= start] # 90 days

df.to_csv('test1.csv', mode='w',index=False)

#Append states to CSV
start = date.today() - timedelta(days = 90)
df = pd.read_csv(data, usecols=['date','state','hosp_covid','hosp_pui'], parse_dates=['date'])
sum_covid = df['hosp_covid'] + df['hosp_pui']
df['hospitalised'] = sum_covid
df.state = df.state.replace(mergeKV)
df.state = df.state.replace(labuan)
df = df.groupby(['date','state']).sum().reset_index()
df = df[df.date.dt.date >= start] # 90 days

df.to_csv('test1.csv', mode='a', header=False,index=False)


