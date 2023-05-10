import math

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

# print(train_setosa, train_versicolor, train_virginica)

total1 = 0
total2 = 0
total3 = 0

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


# Calcular distância euclidiana

def euclidean_distance(value1, value2):
    sum = 0

    for i in range(len(value1) - 1):
        sum += math.pow(float(value1[i]) - float(value2[i]), 2)
    
    return math.sqrt(sum)


# KNN

def knn(train, sample, k):
    dist = {}

    for i in range(len(train)):
        d = euclidean_distance(train[i], sample)
        dist[i] = d
    
    k_neighbors = sorted(dist, key= dist.get)[:k]

    amout_setosa = 0
    amout_versicolor = 0
    amount_virginica = 0

    for i in k_neighbors:
        # print(train[i])
        if train[i][-1] == 'Iris-setosa':
            amout_setosa += 1
        elif train[i][-1] == 'Iris-versicolor':
            amout_versicolor += 1
        else:
            amount_virginica += 1
    
    a = [amout_setosa, amout_versicolor, amount_virginica]

    if(a.index(max(a) == 0)):
        return 'Iris-setosa'
    elif(a.index(max(a)) == 1):
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'


k = 3

def statistics(k, klass):
    ft = 0
    fn = 0
    tp = 0
    tn = 0

    for sample in test:
        iris_class = knn(train, sample, k)
        hit = False

        if(klass == sample[-1] and klass == iris_class):
            hit = True
        if(klass != sample[-1] and klass != iris_class):
            hit = True

        if hit:
            if(iris_class == klass):
                tp += 1
            else:
                tn += 1
        else:
            if(iris_class == klass):
                fn += 1
            else:
                ft += 1

    hit_rate = ((tp + tn)/(tp + tn + ft + fn))*100 
    sensitivity = (tp / (tp + fn))*100
    specificity = (tn / (tn + ft))*100

    print(klass, end=':\n')
    print('Hit rate:   ', round(hit_rate, 2), end='%\n')
    print('Sensivity:  ', round(sensitivity,2), end='%\n')
    print('Specificity:', round(specificity, 2), end='%\n\n')


statistics(k, 'Iris-setosa')
statistics(k, 'Iris-versicolor')
statistics(k, 'Iris-virginica')