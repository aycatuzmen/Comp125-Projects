import matplotlib.pyplot as plt

def main():
    values = [20, 60, 80, 20]
    slice_labels=['1st', '2nd', '3rd', '4th']
    plt.pie(values, labels=slice_labels, colors=('r', 'g', 'b', 'm'))
    plt.show()

if __name__ == '__main__':
    main()
