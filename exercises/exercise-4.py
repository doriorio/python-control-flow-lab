# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
tri_status = None
a_input = input('Enter the lengths of three side of a triangle: a:')
b_input = input('Enter the lengths of three side of a triangle: b:')
c_input = input('Enter the lengths of three side of a triangle: c:')
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in lengthb
#      isosceles - two sides are the same length
if (a_input == b_input and b_input == c_input):
    tri_status = 'equalateral'
elif (a_input != b_input) and (a_input != c_input) and (b_input != c_input):
    tri_status = 'scalene'
else:
    tri_status = 'isoceles'


# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
print(f'A triangle with sides of {a_input}, {b_input}, {c_input} is a {tri_status} triangle')