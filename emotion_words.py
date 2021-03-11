#We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
#Find the total number of words in the file and assign this value to the variable num_words.

f=open("emotion_words.txt","r")
num_words=0
x=[]
for i in f:
    x=i.split()
    num_words+=len(x)
print(num_words)
