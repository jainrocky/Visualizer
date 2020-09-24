from src.algorithms.sort import Sort


class SelectionSort(Sort):
    '''
    ---------------------------------
    <SelectionSort>

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
        super().__init__('SelectionSort', data)

    def sort(self, data=None, display=None):
        if not data and not self.get_data():
            raise ValueError('data must be not None')
        if display:
            self.set_visualization(True)
        if data:
            self.set_data(data)
        data=self.get_data()


        for i in range(len(data)):
            mn_index=i
            for j in range(i+1, len(data)):
                if data[mn_index] > data[j]:
                    mn_index=j
                if self.is_visualization_enabled():
                    display.update(first=data[j], second=data[mn_index])    
            data[i], data[mn_index]=data[mn_index], data[i]

        if self.is_visualization_enabled():
            display.update()

        if display:
            self.set_visualization(False)
