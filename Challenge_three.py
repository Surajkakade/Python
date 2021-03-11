#Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

three=[]
f=open("school_prompt.txt","r")

for i in f:
    x=i.split()
    three.append(x[2])
    
