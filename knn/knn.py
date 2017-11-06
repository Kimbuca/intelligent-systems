import math
import operator
import random

data = open('pima-indians-diabetes.data.txt')
data_matrix = []

train_percentage = int(math.floor(100 * random.random()));

HAS_DIABETES = '1'
k = 10

#parse info
for line in data:
    parsed_line = line.splitlines()[0].split(',')
    data_matrix.append(parsed_line)

train_sample = int(math.ceil( len(data_matrix) * (train_percentage / float(100)) ))
test_sample = len(data_matrix) - train_sample

## data split
train_data = data_matrix[:int(train_sample)]
test_data = data_matrix[-int(test_sample):]

def euclideanDistante(x, xi):
    distance = 0.0
    
    for i in range(len(x)-1):
        distance += pow( ( float(x[i]) - float(xi[i]) ), 2)
    distance = math.sqrt(distance)

    return distance


def compareInstances(positive, negative):
    if positive != negative:
        return 'pos' if positive > negative else 'neg'
    else:
        return 'NaN'

def knn_predict(test_data, train_data, k_value):
    for i in test_data:
      
        eu_Distance =[]
        knn = []
        positive = 0
        negative = 0
        
        for j in train_data:
            eu_dist = euclideanDistante(i, j)
            
            ## storing class value and eu_dist as an object
            eu_Distance.append((j[8], eu_dist))
            
            ## sort by eu_dis which is key[1] on the obj
            eu_Distance.sort(key = operator.itemgetter(1))
            
            ## get the first k values elements which once sorted are the nearest
            knn = eu_Distance[:k_value]
            
            for k in knn:
                if k[0] == HAS_DIABETES:
                    positive += 1
                else:
                    negative +=1
    
        i.append(compareInstances(positive, negative));

knn_predict(test_data, train_data, k)

#output result
for d in test_data:
    print d

print 'train percentage ', train_percentage, '%'
print 'train sample of ', train_sample, ' instances '
print 'test sample of ', test_sample, 'instances '
print 'K value :', k
