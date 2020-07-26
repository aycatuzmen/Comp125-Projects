#@author: Buket

"""Pie chart of fruit sales"""

from matplotlib import pyplot as plt

filename = 'fruit_sales_data.csv'
firstrow = True
months=[]
apples = []
bananas = []
mangos = []
grapes = []
avocados = []
strawberries = []
with open(filename) as f:
    for line in f:
        if firstrow:
            firstrow = False
        else:
            split_line = line.split(',')
            # Get the necessary columns as lists

            months.append(int(split_line[0]))
            apples.append(int(split_line[1]))
            bananas.append(int(split_line[2]))
            mangos.append(int(split_line[3]))
            grapes.append(int(split_line[4]))
            avocados.append(int(split_line[5]))
            strawberries.append(int(split_line[6]))

#plot the chart
labels = ['Apple','Banana', 'Mango', 'Grape', 'Avocado', 'Strawberry']
salesData   = [sum(apples), sum(bananas), sum(mangos), 
         sum(grapes), sum(avocados), sum(strawberries)]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='upper left')
plt.title('Fruit sales data')
plt.show()