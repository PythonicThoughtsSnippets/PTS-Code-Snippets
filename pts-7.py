# Python Thoughts Snippet #7 - Pytest Fixture
# Python 3.7
# 2019/12/09
# post: https://pythonicthoughtssnippets.github.io/#7-tdd---pytest-fixtures

# THIS CODE IS NOT MEANT TO BE FUNCTIONAL OR EXECUTABLE,
# IT IS A REPRESENTATION OF AN IDEA AND AN EXAMPLE TO RAISE DISCUSSION.

# As a common practice in my Pythonic Thoughts Snippets,
# I am not going into the details of the minor implementations,
# on doubts please search elsewhere on the web, there are countless of
# amazing explanations; here, we focus on the broader concept.

# pseudo code
@pytest.mark.parametrize(
    'fname',
    [
        (Path('file1')),
        (Path('file2')),
        ],
    )
def test_my_file_parser(fname):
    parser = MyFileParser(fname)
    data1 = parser.data_foo()
    assert isinstance(data1, list)
    assert len(data1) == 50


# bellow the fixture approach
@pytest.fixture(
    params=[
        Path('file1'),
        Path('file2'),
        ],
    )
def parser_data1(request):
    parser = MyFileParser(request.param)
    data1 = parser.data_foo()
    return data1


def test_parser_data1_type(parser_data1):
    assert isinstance(parser_data1, list)


def test_parser_data1_len(parser_data1):
    assert len(parse_data1) == 50
