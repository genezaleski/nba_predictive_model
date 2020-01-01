import time
import math
from csv import reader

#convert string values of stats dataset
#to floats (only columns containing numeric
#values)
def preProcessNums(data, col):
    for row in data:
        row = filter(bool,row)
        row[col] = float(row[col].strip())

#convert classes of player 
def preProcessClasses(data, col):
    temp = [row[col] for row in data]
    vals = set(temp)
    curr = dict()
    for i,j in enumerate(vals):
        curr[j] = i
        print('[%s] = %d' % (j,i))
    for row in data:
        x = curr[row[col]]
        row[col] = x
    return curr 

#calculate euclidean distance between two points
#through the square root of the summation of the
#pythagorean distance between two points.
def euclideanDist(r1,r2):
    distance = 0.0
    for i in range(len(r1)-1):
        r1 = filter(bool,r1)
        r2 = filter(bool,r2)
        r2[i] = float(r2[i])
        distance += (r1[i] - r2[i])**2
    return math.sqrt(distance)

#get the k nearest neighbors for the values 
#passed in the train and test rows.
def getNeighbors(train,testRow, numNeighbors):
    dist = list()
    for trainRow in train:
        euclid = euclideanDist(testRow,trainRow)
        dist.append((trainRow,euclid))
    dist.sort(key = lambda tup: tup[1])
    knn = list()
    for i in range(numNeighbors):
        knn.append(dist[i][0])
    return knn

#use results of the knn and subsequently the euclidean distance
#to predict the class of a sample row of data.
def predict(train,testRow,numNeighbors):
    neighbors = getNeighbors(train,testRow,numNeighbors)
    temp = [row[-1] for row in neighbors]
    predict = max(set(temp),key=temp.count)
    return predict

#use the prediction on dataset to find the predicted class.
def knn(train,test,numNeighbors):
    prediction = list()
    for row in test:
        temp = predict(train,row,numNeighbors)
        prediction.append(temp)
    return prediction

#open stats file as python object
stats = list()
with open("playerStatsCopy.csv",'r') as file:
    fileReader = reader(file)
    for row in fileReader:
        if not row:
            continue
        stats.append(row)

for i in range(len(stats[0])-1):
    preProcessNums(stats,i)

preProcessClasses(stats,len(stats[0])-1)

k = 5
row = [9,1,1]
start = time.time()
res = predict(stats,row,k)
end = time.time()
print('Data=%s, Predicted: %s' % (row,res))
if res==1:
    print("The statistics entered should belong to an all-star player.")
elif res==0:
    print("The statistics entered should belong to an above average scorer.")
elif res==2:
    print("The statistics entered should belong to an above average playmaker.")
elif res==3:
    print("The statistics entered should belong to an above average rebounder.")
elif res==4:
    print("The statistics entered should belong to an average nba player.")
print("Completed execution in ",end-start," seconds.")

def error_percentage(actual,predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100

predicted1 = []
row=[2,2,2]
predicted1.append(predict(stats,row,k))
row=[2,6,6]
predicted1.append(predict(stats,row,k))
row=[10,2,2]
predicted1.append(predict(stats,row,k))
row=[13,8,9]
predicted1.append(predict(stats,row,k))
row=[28,14,3]
predicted1.append(predict(stats,row,k))
row=[15,1,2]
predicted1.append(predict(stats,row,k))
row=[8,2,8]
predicted1.append(predict(stats,row,k))
row=[17,1,1]
predicted1.append(predict(stats,row,k))
row=[30,10,10]
predicted1.append(predict(stats,row,k))
row=[14,2,4]
predicted1.append(predict(stats,row,k))
actual1 = [1,2,1,2,3,4,2,4,3,4]
print("Error Rate: ",100-error_percentage(actual1,predicted1))

