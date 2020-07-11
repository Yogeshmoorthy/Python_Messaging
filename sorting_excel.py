import pandas as pd
import date_time
import re

date_to_use = date_time.today()

lis_date = list(date_to_use)

gro_list=pd.read_csv(r'G:\grocery_list_updated.csv')
gro_list.head()
for date in gro_list.columns:
	if date in date_to_use:
		new_df = gro_list.loc[:,['Items',date]]
		updated_new_df=new_df.dropna(axis=0)
		total_spend = ('Total Spend Today',updated_new_df[date].sum())
print(updated_new_df)
print(type(updated_new_df))
