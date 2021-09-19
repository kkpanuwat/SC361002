inp = "Structured Programming for Information Technology"
inp = inp.lower()
inp = inp.replace(" ","")

alredy = ""
for i in sorted(inp):
    if(not i in alredy):
        print(i,':',inp.count(i))
        alredy+=i
    else:
        continue

    