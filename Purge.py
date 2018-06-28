import abc

class Purge(abc.ABC):
    @abc.abstractmethod
    def removen(self):
        pass
