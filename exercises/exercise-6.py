# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):

month_year = input('Enter the month of the season (Jan - Dec):').lower()

# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
day_month = input('Enter the day of the month:')
day_month = int(day_month)

# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall

if (month_year) in ("jan", "feb", "mar"):
    if (month_year == "mar" and day_month > 19):
        print(f'{month_year} {day_month} is in spring')
    else:
        print(f'{month_year} {day_month} is in winter')
if (month_year) in ("apr", "may", "jun"):
    if (month_year == "jun" and day_month > 21):
        print(f'{month_year} {day_month} is in summer')
    else:
        print(f'{month_year} {day_month} is in spring')
if (month_year) in ("jul", "aug", "sep"):
    if (month_year == "sep" and day_month > 21):
        print(f'{month_year} {day_month} is in fall')
    else:
        print(f'{month_year} {day_month} is in summer')
if (month_year) in ("oct", "nov", "dec"):
    if (month_year == "dec" and day_month > 20):
        print(f'{month_year} {day_month} is in winter')
    else:
        print(f'{month_year} {day_month} is in fall')



# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.