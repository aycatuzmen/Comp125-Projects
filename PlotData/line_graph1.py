import matplotlib.pyplot as plt
def main():
    #create a list with x and y coordinated
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    #build the line graph
    plt.plot(x_coords, y_coords)

    #add a title
    plt.title('Sample Data')

    #add labels to the axes
    plt.xlabel('Year')
    plt.ylabel('Spending')

    #limit values
    plt.xlim(xmin=1, xmax=10)
    plt.ylim(ymin=-1, ymax=6)

    # customize ticks
    plt.xticks([0, 1,2,3,4], ['2016','2017','2018','2019','2020'])
    plt.yticks([1, 2, 3, 4, 5], ['0m', '10m', '20m', '30m', '40m'])

    #add grid
    plt.grid(True)

    #display the graph
    plt.show()

if __name__ == '__main__':
    main()