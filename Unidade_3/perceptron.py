import numpy as np
import random


list=[]
f = open('iris.data', 'r')
for row in f.readlines():
    a=row.replace('\n','').split(',')
    list.append(a) 

# Resizing:
sepalLength = []
sepalWidth = []
petalLength = []
petalWidth = []

for i in list:
    sepalLength.append(float(i[0]))
    sepalWidth.append(float(i[1]))
    petalLength.append(float(i[2]))
    petalWidth.append(float(i[3]))

rlist = [] # it will contain the resized elements


def resize(x, i):
    return round(2*(x[i] - min(x))/(max(x) - min(x)) - 1, 4)


for i in range(len(list)):
    aux = []
    aux.append(resize(sepalLength, i))
    aux.append(resize(sepalWidth, i))
    aux.append(resize(petalLength, i))
    aux.append(resize(petalWidth, i))
    aux.append(list[i][-1])
    rlist.append(aux)


def countclasses(rlist):
    setosa = 0
    versicolor = 0
    virginica = 0

    for i in range(len(rlist)):
        if list[i][4] == 'Iris-setosa':
            setosa += 1
        if list[i][4] == 'Iris-versicolor':
            versicolor += 1
        if list[i][4] == 'Iris-virginica':
            virginica += 1
    
    return [setosa,versicolor,virginica]


# Reserve p% for training
p = 0.3
setosa, versicolor, virginica = countclasses(rlist)

train = []
test = []
train_setosa = int(setosa*p)
train_versicolor = int(versicolor*p)
train_virginica = int(virginica*p)

total1, total2, total3 = 0, 0, 0
for i in rlist:
    if i[-1] == 'Iris-setosa' and total1 < train_setosa:
        train.append(i)
        total1 += 1
    elif i[-1] == 'Iris-versicolor' and total2 < train_versicolor:
        train.append(i)
        total2 += 1
    elif i[-1] == 'Iris-virginica' and total3 < train_virginica:
        train.append(i)
        total3 += 1
    else:
        test.append(i)


t = [] 
out = []
out_setosa1 = []
out_versicolor1 = []
out_virginica1 = []


def separator(list):
    new_list = []
    o1 = []
    o2 = []
    o3 = []

    for r in list:
        # Get the training sample set
        new_list.append(r[:4])
    
        # Associate the desired output to each sample obtained
        if r[-1] == 'Iris-setosa':
            o1.append(1)
        else:
            o1.append(0)
        
        if r[-1] == 'Iris-versicolor':
            o2.append(1)
        else:
            o2.append(0)
        
        if r[-1] == 'Iris-virginica':
            o3.append(1)
        else:
            o3.append(0)
    
    for i in new_list:
        i.append(1)

    return new_list, o1, o2, o3



# Get the training sample set
# Associate the desired output to each sample obtained
t, out_setosa1, out_versicolor1, out_virginica1 = separator(train)

# Get the test sample set
test_, o1, o2, o3 = separator(test)

x_train = np.asanyarray(t)
y_output_setosa1 = np.asanyarray(out_setosa1)
y_output_versicolor1 = np.asanyarray(out_versicolor1)
y_output_virginica1 = np.asanyarray(out_virginica1)

x_test = np.asanyarray(test_)
y_output_setosa2 = np.asarray(o1)
y_output_versicolor2 = np.asarray(o2)
y_output_virginica2 = np.asarray(o3)


def perceptron(train, output, learning_rate, epochs):
    # starts the weight list with small random values
    weights = np.zeros(len(x_train[0]))
    for i in range(len(weights)):
        weights[i] = random.uniform(-0.01, 0.01)

    for _ in range(epochs):
        error = 0
        for xi, yi in zip(train, output):
            u = np.dot(xi, weights)
            s = np.where(u >= 0.0, 1, 0)
            if s != yi:
                error = yi - s
                weights += learning_rate*error*xi
    
    return weights


def perceptron_validate(test, output, w):
    ft, fn, tp, tn = 0, 0, 0, 0

    for xi, yi in zip(test, output):
        u = np.dot(xi, w)
        s = np.where(u >= 0, 1, 0)
        if s == 1:
            if s == yi:
                tp += 1
            else:
                ft += 1
        else:
            if s == yi:
                tn += 1
            else:
                fn += 1

    hit_rate = ((tp + tn)/(tp + tn + ft + fn))*100 
    sensitivity = (tp / (tp + fn))*100
    specificity = (tn / (tn + ft))*100

    print('Hit rate:   ', round(hit_rate, 2), end='%\n')
    print('Sensivity:  ', round(sensitivity,2), end='%\n')
    print('Specificity:', round(specificity, 2), end='%\n\n')


alpha = 0.1 # learning rate
epochs = 10

w1 = perceptron(x_train, y_output_setosa1, alpha, epochs)
w2 = perceptron(x_train, y_output_versicolor1, alpha, epochs)
w3 = perceptron(x_train, y_output_virginica1, alpha, epochs)

print('Iris-setosa', end=':\n')
perceptron_validate(x_test, y_output_setosa2, w1)

print('Iris-versicolor', end=':\n')
perceptron_validate(x_test, y_output_versicolor2, w2)

print('Iris-virginica', end=':\n')
perceptron_validate(x_test, y_output_virginica2, w3)