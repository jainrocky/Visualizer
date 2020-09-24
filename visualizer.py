from colorama import Fore, Style, Back
from src.utils.display import Display
from src.algorithms.bubble_sort import BubbleSort
from src.algorithms.selection_sort import SelectionSort
from src.algorithms.insertion_sort import InsertionSort
import random

algos=[
    ('Bubble Sort', BubbleSort),
    ('Selection Sort', SelectionSort),
    ('Insertion Sort', InsertionSort),
    ('Quick Sort', None),
    ('Merge Sort', None),
    ('Heap Sort', None),
    ('Shell Sort', None),
]


def print_header():
    header='''
     _________________________________________________________________________________________________________
    |    __      __    _     _______     _     _     _____    ___       _    _______     _____    ______      |  
    |    \ \\    / /   |_|   |  _____|   | |   | |   |  _  |   | |      |_|  |_____  |   |  __|   |  _  |      |  
    |     \ \\  / /     _    | |_____    | |   | |   | |_| |   | |       _        / /    | |__    | |_| |      |  
    |      \ \\/ /     | |   |______ |   | |   | |   |  _  |   | |      | |      / /     |  __|   | _  _|      |
    |       \  /      | |    _____| |   | |___| |   | | | |   | |___   | |     / /___   | |__    | |\\ \\       |  
    |        \/       |_|   |_______|   |_______|   |_| |_|   |_____|  |_|    /______|  |____|   |_| \\_\\      |
    |_________________________________________________________________________________________________________|

    '''
    print(Fore.GREEN, end='')
    print(header)
    print(Style.RESET_ALL, end='')

def main():
    print(Fore.BLUE+'Thank you for using Visualizer!\n')
    print(Style.RESET_ALL, end='')
    print('     ------')
    print('    | Menu |')
    print('     ------')
    for i, algo in enumerate(algos):
        print('\t|')
        print('\t|___[{}] {}'.format(i, algo[0]))
    print('\t|')
    print('\t|___[{}] {}\n'.format('q', 'Quit'))
    print('Select an option to continue')
    run=True
    while run:
        option=input('>>> '+Fore.RED)
        print(Style.RESET_ALL, end='')
        if option=='q' or option=='Q':
            run=False
        elif option.isdigit() and 0<=int(option)<=len(algos)-1:
            # try:
            if not algos[int(option)][1]:
                print(Fore.RED+algos[int(option)][0]+' is not Implemented yet'+Style.RESET_ALL)
                continue
            print(Fore.CYAN+algos[int(option)][1].__doc__+Style.RESET_ALL)
            data=random.sample(range(1, 700), 50)
            Display(
                algos[int(option)][1](data=data),
                height=800,
                width=1200,
                # data_color=(255, 255, 255),
                data_color=(0,0,0),
                text_color=(255, 255, 255),
                first_color=(0, 0, 255),
            )
            # except:
            #     print('Some Error occurred!')
        else:
            print(Fore.RED+'Please choose a correct option!'+Style.RESET_ALL)

if __name__=='__main__':
    print_header()
    main()
    # data=random.sample(range(20), 5)
    # bs=InsertionSort(data=data)
    # print(bs.get_data())
    # bs.sort()
    # print(bs.get_data())
    