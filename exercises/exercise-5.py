# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.
seq = []
for num in range(0,51):
    if (num <= 1):
        seq.append(num)
    else:
        seq.append(seq[num-1] + seq[num-2]) 

print(f'{seq}')

print ([list((i, seq[i])) for i in range(len(seq))]) 

# Hint: The next number is found by adding the two numbers before it
