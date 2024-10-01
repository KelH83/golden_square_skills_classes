from lib.class_challenge import *
import pytest

check_grammar = GrammarStats()

def test_instance_created():
    assert isinstance(check_grammar, GrammarStats)

def test_check():
    assert check_grammar.check('This is an acceptable sentence.') == True
    assert check_grammar.check('this is a sentence missing a capital.') == False
    assert check_grammar.check('This sentence is missing ending punctuation') == False
    assert check_grammar.check('this sentence is missing a starting capital and does not end with punctuation') == False
    
def test_check_for_errors():  
    with pytest.raises(Exception) as e:
        check_grammar.check(123)
    error_message = str(e.value)
    assert error_message == "Only strings are allowed!"

def test_percentage_good():
    assert check_grammar.percentage_good() == '1%'
    