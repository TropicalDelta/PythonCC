with open('simple.txt') as fo: 
    text = fo.read()
    print("\nSimple one")
    print(text.rstrip())
    print("\nSecond one")
    for i in range(0,3):
        print(text.strip())
    print("Done")
    print("\nLast one")
    stringText = ''
    for line in text: 
        stringText += line.rstrip()
        if 'Python' in stringText:
            stringText.replace('Python', 'Only Python')
    
    print(stringText*3,sep=(" "))

