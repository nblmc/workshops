import pandas as pd 

meters_csv = pd.read_csv("./parking_meters_boston.csv")


#free_saturdays = meters_csv[~ meters_csv['PAY_POLICY'].str.contains('SAT', na=False)]
#print(free_saturdays)
#count(free_saturdays)

pay_policy = meters_csv.PAY_POLICY.apply(pd.Series)
#ay_policy = pay_policy.rename(columns = lambda x : 'pay_policy_' + str(x))

print(pay_policy)

#meters_csv.set_index('G_SUBZONE', inplace=True)
#charlestown = meters_csv.loc[['0AG'], ['METER_ID', 'PAY_POLICY', 'VENDOR', 'METER_TYPE', 'INSTALLED_ON', 'PAY_POLICY','PRE_PAY','PARK_NO_PAY', 'TOW_AWAY','STREET_CLEANING']]
#print(charlestown)
#print(count('charlestown'))

#charlestown.to_csv('./charlestown_meters.csv')


# expand df.tags into its own dataframe
#tags = df['tags'].apply(pd.Series)




# Dataframe 1 contains: METER_ID, lat, long, (block #)?, VENDOR, METER_TYPE, INSTALLED_ON
# Dataframe 2 contains: METER_ID,PAY_POLICY,PRE_PAY,PARK_NO_PAY, TOW_AWAY,STREET_CLEANING
    # Add max park time, days hours?
    # #Remove HAS_SENSOR,G_DISTRICT,G_PASSPORT_ZONES,G_PM_ZONE,G_SUBZONE,G_ZONE,BASE_RATE,POLE_MOUNT,YOKE,HOUSING_TYPE,HOUSING_MANUFACTURER,SIDEWALKGE,COIN_SLOTLE,METER_CONDITION,PERMIT_RATE,INSTALLED_ON,PURCHASED_DATE,METER_STATE,SPACE_STATE

