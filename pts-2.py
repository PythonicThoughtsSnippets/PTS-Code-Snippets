# Python Thoughts Snippet #2
# Python 3.7
# 2019/08/16
# post: https://pythonicthoughtssnippets.github.io/#2-unpacking-conditional-expressions
# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE
# TO RAISE DISCUSSION

# pretty clear code that makes use of list and zip
# to unpack a list of tuples to two separated lists of tuples
# or in this case just a tuple because there is only one element
a = [("1", "2"), ("", "")]
b, c = list(zip(*a))
print(b)
print(c)
# >>> ('1', '')
# >>> ('2', '')

# here I would expect the same as before, however...
a = [("1", "2"), ("", "")]
# notice that the if True is just an example of 
# a conditional that I was expecting to evaluate to True in
# most cases.
b, c = list(zip(*a)) if True else [""], [""]
print(b)
print(c)
# ¡unexpected output!
# >>> [('1', ''), ('2', '')]
# >>> ['']

a = [("1", "2"), ("", "")]
b, c = list(zip(*a)) if True else ([""], [""])
print(b)
print(c)
# >>> ('1', '')
# >>>  ('2', '')
