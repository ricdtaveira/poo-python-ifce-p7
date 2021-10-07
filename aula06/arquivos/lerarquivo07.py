f = open("demofile3.txt", "a")
f.write("EITA! I have deleted the content!\n")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
