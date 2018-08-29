#Q.1- Write a Python program to read n lines of a file.
f=open('file1.txt','r')
n=int(input("Enter number of lines you want to read: "))
try:
    for i in range(0,n):
        lines=f.readline()
        print(lines)
    f.close()
except FileNotFoundError:
    print("File not found.")


#Q.2- Write a Python program to count the frequency of words in a file.
f=open('file1.txt','r')
w=(f.read()).split()
count=1
i=0
checklist=[]
for j in range(0,len(w)):
    count=1
    word=w[i]
    if word in checklist:
            pass
    else:
        for l in range(0,len(w)):
            if (i==l):
                pass
            elif (word==w[l]):
                count+=1
        print("Frequency of",word,"is: ",count)
        checklist.append(word)     
    i+=1
f.close()


#Q.3- Write a Python program to copy the contents of a file to another file.
f1=open('file1.txt','r')
data=f1.read()
f2=open('file2.txt','w')
f2.write(data)
f1.close()
f2.close()


#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
f1=open('file1.txt','r')
f2=open('file2.txt','r')
for line1,line2 in zip(f1,f2):
    print(line1+line2)


#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
with open('file3.txt','w') as f:
    for i in range(10):
        number=int(input("Enter any number: "))
        f.write(' %d' % number)

with open('file3.txt', 'r') as f:
    lines=f.readlines()
    for l in lines:
        word=l.split()
    a= [int(i) for i in word]
    a.sort()
    str1 = '\n'.join(str(e) for e in a)
    fout = open('file4.txt','w')
    fout.write(str1)
    fout.close()


