def set_title(text):
    text = text.lower()
    text = text.replace(text[0],text[0].upper(),1)
    return text

def set_start(text):
    text = text.lower()
    text = text.split(" ")
    result = str()
    for i in range(0,len(text)):
        text[i] = text[i].replace(text[i][0],text[i][0].upper(),1)
        result+=text[i]+" "
    return result