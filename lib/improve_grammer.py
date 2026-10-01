def improve_grammer(string):
    if not isinstance(string, str):
        raise TypeError("input is not a string!")
    
    question_list = ["what", "how", "when", "where"]
    sentence = string.split()
    for word in sentence:
        if word in question_list:
            return string[0].upper()+string[1:len(string)] + "?"
    
    return "" if len(string) == 0 else string[0].upper()+string[1:len(string)] + "."