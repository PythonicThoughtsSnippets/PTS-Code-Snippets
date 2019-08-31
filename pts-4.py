# Python Thoughts Snippet #4 - Factory Method - Creational Pattern
# Python 3.7
# 2019/08/31
# blog post: https://viviendomochileros.com/pythonic-thoughts-snippets-4/
# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept

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
            # this actually calls object.__new__(match_d[True])
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
