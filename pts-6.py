# Python Thoughts Snippet #6 - Test Driven Development
# Python 3.7
# 2019/12/02
# post: https://pythonicthoughtssnippets.github.io/#6-test-driven-development

# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept.

def random_fragment(iterable, fragsize=None):
    """
    Generate a slice object that reflects a random fragment from iterable.
    
    (iterable, int -> slice object)
    
    Parameters
    ----------
    iterable : iterable-type
        An interable: string, list, tuple, etc.

    fragsize : int or NoneType
        The size of the fragment to generate.

    Returns
    -------
    slice object
        A slice object reflecting a random fragment of the `iterable`
        of size `fragsize`.
        If `fragsize` is ``None``, returns a full range slice object.
    """
    # this is separate from the try: block to account input of for types
    # that are now iterable and have not to do with the usage
    # of fragsize=None
    len_ = len(iterable)

    try:
        start = random.randint(0, len_ - fragsize)
    except TypeError:  # fragsize is None
        return slice(None, None, None)
    else:
        return slice(start, start + fragsize, None)

# And these are the tests I wrote.

"""Test libutil."""
import pytest

# I know libutil is a very bad name. What does that mean? That other
# libs are not *util* ? :-P

from project.libs import libutil as UTIL


def test_random_fragment_return():
    """Test return type is slice object."""
    result = UTIL.random_fragment([1, 2])
    assert isinstance(result, slice)


@pytest.mark.parametrize(
    'in1,fragsize,expected',
    [
        (list(range(1000)), 7, 7),
        (list(range(1000)), 0, 0),
        (list(range(1000)), None, 1000),
        ([], None, 0),
        ([], 0, 0),
        ('abcdefgh', 3, 3),
        ((1,2,3,4), 1, 1),
        ],
    )
def test_random_fragment(in1, fragsize, expected):
    """
    Test fragment has expected length.

    Parametrize
    -----------
    1: list with fragsize < len(list)
    2: list with fragsize == 0, should return empty list
    3: list with fragsize is None, should return whole list
    4: empty list with fragsize is None, should return empty list
    5: empty list with fragsize is None, should return empty list
    6: functionality for strings
    7: functionality for tuples
    """
    result = UTIL.random_fragment(in1, fragsize)
    assert len(in1[result]) == expected


@pytest.mark.parametrize(
    'in1,fragsize,error',
    [
        ([], 7, ValueError),
        (list(range(100)), 700, ValueError),
        (9, 2, TypeError),
        (9.0, 2, TypeError),
        ],
    )
def test_random_fragment_errors(in1, fragsize, error):
    """
    Test errors raised with input.

    Parametrize
    -----------
    1: Empty list with fragsize > 0
    2: list with fragsize > len(list)
    3: int
    4: float
    """
    with pytest.raises(error):
        UTIL.random_fragment(in1, fragsize)

