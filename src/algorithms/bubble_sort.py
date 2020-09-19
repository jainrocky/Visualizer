from src.algorithms.sort import Sort


class BubbleSort(Sort):
    '''
    ---------------------------------
    <Bubble Sort>

        Stable:     False
        Inplace:    True

        Time Complexity
        ---------------
            Worst Case:     O(n\u00b2)
            Average Case:   O(n\u00b2)
            Best Case:      O(n\u00b2)
    ----------------------------------
    '''
    
    def __init__(self, data=None):
        super().__init__('BubbleSort', data)

    def sort(self, data=None, display=None):
        if not data and not self.get_data():
            raise ValueError('data must be not None')
        if display:
            self.set_visualization(True)
        data=self.get_data()
        for i in range(len(data)):
            for j in range(len(data)-i-1):
                if data[j]>data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                if self.is_visualization_enabled():
                    display.update(first=data[j], second=data[j+1])
        if self.is_visualization_enabled():
            display.update()

        if display:
            self.set_visualization(False)
