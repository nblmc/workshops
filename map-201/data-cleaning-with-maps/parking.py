from geopy.geocoders import Nominatim # Nominatim is a free geocoder pulling from OpenStreetMap data
import pandas as pd

# Keep in mind that the code that is run will not automatically display results.  If you want the program to report back to you, you will need to wrap the command (or the variable it is saved to) in a print funtion

#MD
##### Let's take a look at the data available in the csv by printing the column headings.  The data structure is identical for the Charlestown and Boston dataframes.
# pd.dataframe.columns

print(boston_meters.columns)

#MD
# Dataframe 1 tells us which vendors service the meters in the "VENDOR" column. How many vendors service the boston area meters?
print(meters_csv.VENDOR.unique())

# What are the distinct types of pay policies for meters? 
## ANSWER: #print(meters_csv.PAY_POLICY.unique())



# Now lets try to find the spots that are free on saturdays
#df[df['column'].str.contains('string we are looking for')]
free_saturdays = meters_csv[~ meters_csv['PAY_POLICY'].str.contains('SAT', na=False)]
print(free_saturdays)

# Do any of the meters require payment on Sunday?



#MD
##### Merging Dataframes
# Insert merge types picture


# We have a dataframe listing parking meters for Charlestown and another dataframe listing parking meters for Boston
# Try combining these two into one dataframe
# The syntax is dataframe.merge(dataframe_2, how = "")   Default is inner merge


