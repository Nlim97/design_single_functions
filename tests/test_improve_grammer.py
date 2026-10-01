from lib.improve_grammer import *
import pytest

"Test for empty string"

def test_empty_string():
    assert improve_grammer("") == ""

"capitalize and full stop to normal sentence"

def test_normal_sentence():
    assert improve_grammer("hello my name is Bob") == "Hello my name is Bob."

"handles question sentences"
def test_question_string():
    assert improve_grammer("what is your name") == "What is your name?"

"handle invalid inputs"
def test_invalid_input():
    with pytest.raises(TypeError, match="input is not a string!"):
        improve_grammer(5)