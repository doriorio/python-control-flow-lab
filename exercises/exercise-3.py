# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 

dog_age = input('Input a dog''s age in human years')
dog_age = int(dog_age)
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
dog_years = None
if (dog_age == 1 or dog_age == 2):
    dog_years = dog_age*10
    
else:
    dog_years = (((dog_age - 2 )* 7) + 20)


# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx
print(f'The dogs age in dog years is {dog_years}')

# Hint:  Use the int() function to convert the string returned from input() into an integer