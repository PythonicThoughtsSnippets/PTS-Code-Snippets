# example of a Factory Method Pattern for object creation
# blog post to be written.

from abc import ABC, abstractmethod


class Interface(ABC):
    
    def __new__(cls, arg1):
        
        match_d = {
            # evalutes arguments based on conditions to decide which
            # subclass to instantiate
            is_for_subclass1(arg1): SubClass1,
            is_for_subclass2(arg1): SubClass2,
            # etc...
            }
    
        try:
            # this actually class object.__new__(match_d[True])
            # dont know if it is better to super(Interface) or object.
            return super(Interface, cls).__new__(match_d[True])
        except KeyError:
            raise NotImplementedError from None

    @abstractmethod
    def run(self):
        return


class SubClass1(Interface):
    
    def __init__(self, arg1):
        # do init magic
        
    def run(self):
        #run magic
        
        self._private_meth_1()
        self._private_meth_2()
        
        return
    
    def _private_meth_1(self):
        return    
    
    def _private_meth_2(self):
        return

class SubClass2(Interface):
    
    def __init__(self, arg1):
        # do init magic
        
    def run(self):
        #run magic
        
        self._private_meth_1()
        self._private_meth_2()
        
        return
    
    def _private_meth_1(self):
        return    
    
    def _private_meth_2(self):
        return
    
    def _private_meth_3(self):
        return