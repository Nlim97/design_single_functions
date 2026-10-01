1. Describe the problem.
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Fucntion signature.

def improve_grammer(sentence: str) => formatted_sentence : str


3. Tests

def improve_grammer("") => ""

def improve_grammer("hello my name is Bob") => "Hello my name is Bob."

def improve_grammer("what is your name") => "What is your name?"
