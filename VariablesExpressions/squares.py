# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

import math

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.
for i in range (1,11):
    print(i, '\t\t', int(math.pow(i, 2)))



