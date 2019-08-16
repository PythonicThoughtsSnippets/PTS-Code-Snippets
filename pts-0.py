# Python Thoughts Snippet #0
# Python 3.7
# 2019/07/28
# blog post: https://viviendomochileros.com/pythonic-thoughts-snippets-0/
# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE
# TO RAISE DISCUSSION

import inspect

from MySuperRrogram import ParameterValidationReport
from MySuperProgram.exceptions import ParameterNotValid


class ModuleBase:

    __init = False

    def __new__(cls, *args, testit=False, build=False, **kwargs):

        if testit or build:
            c = cls(*args, forceme=True, **kwargs)
            if testit:
                return c._initreport
            elif build:
                return c
        else:
            return super().__new__(cls)

    def __init__(self, frame, forceme=False, **kwargs):

        if not self.__init:
            self._forceme = forceme
            self.__init = True
            self._initreport = ParameterValidationReport()
            self.params, _, _, values = inspect.getargvalues(frame)
            self.params.remove('self')

            for param in self.params:
                try:
                    setattr(self, param, values[param])
                except ParameterNotValid as e:
                    if forceme:
                        self._initreport.append_msg(repr(e))
                        setattr(self, f'_{param}', values[param])
                    else:
                        raise e


class Module1(ModuleBase):
    def __init__(
            self,
            *,
            param1=-1,
            param2=4,
            **kwargs
            ):

        frame = inspect.currentframe()
        super().__init__(frame, **kwargs)
        return
    
    @property
    def param1(self):
        return self._param
    
    @param1.setter
    def param1(self, p):
        try:
            p = int(p)
        except (ValueError, TypeError):
            raise ParameterNotValid
        
        if p >= 0:
            raise ParameterNotValid
        else:
            self._param1 = p


if __name__ == '__main__':
    
    # Example
    m = Module1(param1=1)
    # this would rise error because param1 must be
    # negative int.
    
    m = Module1(param1=1, testit=True)
    # this would return a Report class with a representation
    # of the setter validation errors
    
    m = Module1(param1=1, build=True)
    # this would bypass the error and instantiate the
    # class nonetheless with attribute _param1 set to 1.
