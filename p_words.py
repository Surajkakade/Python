#Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

f=open("school_prompt.txt","r")
p_words=[]
for i in f:
    x=i.split()
    for j in x:
        if 'p' in j:
            p_words.append(j)
