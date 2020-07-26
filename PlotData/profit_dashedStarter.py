#@author: Buket

"""
Get total profits of fruits for all months to show line plot with the following properties:
    
Line style must be dotted and line-color should be yellow
You should show legend at the lower left location.
X label name = Month Number
Y label name = Total sales
Marker should be circle
Line marker should be green
Line width should be 5

"""
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
        
plt.plot(months, total_profits, label = 'Profit of each month', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Months')
plt.ylabel('Profit in dollars')
plt.legend(loc='lower left')
plt.title('Fruit Sales data of the year')
plt.xticks(months)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()
