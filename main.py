from NaiveBayes import  Pool
import os

DClasses = ["dunya",  "ekonomi",  "magazin",  "saglik",  "siyaset",'spor','teknoloji']

base = "news/"


p = Pool()
for i in DClasses:
    print(i)
    p.learn(base + i, i)


base = "test/"
#base = "cleanData/"
total=0
right=0
for i in DClasses:
    dir = os.listdir(base + i)
    for file in dir:
        total+=1
        #print('22 Cat', i)
        res = p.Probability(base + i + "/" + file)
        a,b=res[0]
        #print(i + ": " + file + ": " + str(res))
        if i==a:
            right+=1




accuracy=right/total
print('accuracy = ',accuracy) # accuracy =  0.98


