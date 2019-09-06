# Python Thoughts Snippet #4 - Factory Method - Creational Pattern
# Python 3.7
# 2019/08/31
# post: https://pythonicthoughtssnippets.github.io/#4-factory-method-creational-pattern
# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept


# EDIT 2019/09/05
# There's a very interesting fault in the design shown in the original example
# of this post, I came to understand it when I was actually using the pattern.
# Can you spot it before hand? Bellow is the original example from this post,
# and, at the end, an updated explanation.


# The original example:
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

# An updated discussion:
from abc import ABC, abstractmethod


class Interface:
    
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


class ClassBase(ABC):
    
    @abstractmethod
    def run(self):
        return


class SubClass1(ClassBase):
    
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


class SubClass2(ClassBase):
    
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
