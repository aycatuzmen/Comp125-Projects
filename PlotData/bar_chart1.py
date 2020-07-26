import matplotlib.pyplot as plt
def main():
    #create a list with x and y coordinated
    left_edges = [0, 10, 20, 30 ,40]
    height_edges = [100, 200, 300, 400, 500]

    #bar width
    bar_width = 5

    #build the line graph
    plt.bar(left_edges, height_edges, bar_width, color=('r', 'g', 'b', 'k', 'm'))

    #add a title
    plt.title('Sample Data')

    ##customize tick marks
    plt.xticks([5, 15, 20, 25, 30], ['2016', '2017', '2018'])

    #add labels to the axes
    plt.xlabel('X axis')
    plt.ylabel('Y axis')



    #display the graph
    plt.show()

if __name__ == '__main__':
    main()