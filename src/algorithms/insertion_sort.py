from src.algorithms.sort import Sort


class InsertionSort(Sort):
    '''
    ---------------------------------
    <InsertionSort>

        Stable:     True
        Inplace:    True

        Time Complexity
        ---------------
            Worst Case:     O(n\u00b2)
            Average Case:   O(n\u00b2)
            Best Case:      O(n)
    ----------------------------------
    '''
    def __init__(self, data=None):
        super().__init__('InsertionSort', data)

    def sort(self, data=None, display=None):
        if not data and not self.get_data():
            raise ValueError('data must be not None')
        if display:
            self.set_visualization(True)
        data=self.get_data()

        for i in range(1, len(data)):
            curr=data[i]
            j=i-1
            while j>=0 and curr < data[j]:
                data[j+1]=data[j]
                data[j]=curr
                j-=1
                if self.is_visualization_enabled():
                    display.update(first=data[i], second=curr)

        if self.is_visualization_enabled():
            display.update()
        if display:
            self.set_visualization(False)
