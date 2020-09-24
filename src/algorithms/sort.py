from abc import ABCMeta, abstractmethod


class Sort(metaclass=ABCMeta):

    def __init__(self, name, data):
        self.__name=name
        self.set_data(data)
        self.__visualization=False

    @abstractmethod
    def sort(self, data=None, display=None):
        pass
    
    def set_data(self, data):
        self.__data=data

    def get_data(self):
        return self.__data
        
    def get_name(self):
        return self.__name
    
    def set_visualization(self, state):
        if type(state) != bool:
            raise ValueError('Argument must be of type bool')
        self.__visualization=state

    def is_visualization_enabled(self, ):
        return self.__visualization
