f=open("hai.py","w")
f.write("print('hai')")
f.close()

with open("hai.py","r") as f:   #no need to close in WITH (already exists within the code)
    print(f.read())