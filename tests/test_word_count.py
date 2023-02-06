from src.word_count.core import WordCountCore
from src.utils.exceptions import NoTextException


def test_should_count_words():
    """
        Testing a valid input
    """
    assert WordCountCore({"text": "word word"}).count_words() == 2

def test_should_ignore_empty_spaces():
    """
        Empty spaces don't count as words
    """
    assert WordCountCore({"text": "    word     word     "}).count_words() == 2

def test_should_raise_no_text_exception():
    """
        This input should raise an 'NoTextException' else this test should fail
    """
    try:
        WordCountCore({"text": ""}).count_words()
        assert False
    
    except NoTextException:
        assert True

    except Exception:
        assert False