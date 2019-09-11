# Python Thoughts Snippet #5 - Separate Logics
# Python 3.7
# 2019/09/11
# post: https://pythonicthoughtssnippets.github.io/#5-separate-logics

# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept

# example 1
def check_folder_exists(func):
    """
    Decorator for class property setters
    """
    @wraps(func)
    def wrapper(self, folder):
        
        if not Path(folder).exists():
            raise FileNotFoundError(f'Path not found: {folder}')
        
        else:
            return func(self, folder)
    return wrapper


class Parameters:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
    
    @property
    def db_folder(self):
        return self._db_folder
    
    @db_folder.setter
    @check_folder_exists
    def db_folder(self, folder):
        self._db_folder = folder

# example 2
for step in config_reader.steps:
                
    with GCTXT.abort_if_exception(), \
            GCTXT.query_upon_error(XCPTNS.ConfigReadingException), \
            GCTXT.abort_if_critical_exceptions(CONFREADER.critical_errors):
            
        step()
