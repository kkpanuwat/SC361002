# sol1
def reverse_str(sentence):
    result = ""
    for i in range(len(sentence)-1,0,-1):
        result+=sentence[i-1]
    return result

sentence = "Structured Programming for Information Technology"
print("Reverse string:", reverse_str(sentence))