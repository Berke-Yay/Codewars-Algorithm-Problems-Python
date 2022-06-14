def is_isogram(string):
    #This function checks if the given string consists of distinctive characters.

    string = string.lower()
    for i in string:
        if string.count(i)>1:
            return False
    return True
