#@author: Buket

"""Read Total profit of all months and show it using a line plot"""

import csv
from matplotlib import pyplot as plt


filename = 'fruit_sales_data.csv'
firstrow = True
total_profits = []
months=[]
with open(filename) as f:
    for line in f:
        if firstrow:
            firstrow = False
        else:
            split_line = line.split(',')
            total_profit = int(split_line[8])   # get the total profit data for each month
            total_profits.append(total_profit)

            month = int(split_line[0])  # get the months as a list
            months.append(month)

print(months)
print(total_profits)
#plot the chart
plt.plot(months, total_profits, label = 'Profit of each month',)
plt.xlabel('Months')
plt.ylabel('Profit in dollars')
plt.xticks(months)
plt.title('Profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()