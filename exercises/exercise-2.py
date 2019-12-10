# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:

#Please enter a word or phrase: 
user_input=input(' Please enter a word or phrase:').lower()

# 2. Print the following message:
print(f'What you entered is {len(user_input)} characters long')



#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
if (user_input != quit):
    user_input=input(' Please enter a word or phrase:').lower()
if (user_input == quit):
    break

