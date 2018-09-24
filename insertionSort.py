import random
def randomPerm(n):
    v=[]
    for i in range(n):
        v.append(i+1)
    for i in range(len(v)-1):
        j = random.randint(i, len(v)-1)
        aux = v[i]
        v[i] = v[j]
        v[j] = aux
    return v

def isortSteps(a):
    compar = 0
    swaps = 0
    whileq = 2
    v = []
    for i in range(len(a)):
        v.append(a[i])        
    steps = 0
    for i in range(1,len(v)):
        x = v[i]
        j = i-1
        while (j > -1) and (v[j] > x):
            whileq = whileq + 2
            if v[j] > x:
                compar = compar + 1
            v[j+1] = v[j]
            swaps = swaps + 1
            j = j -1
            steps = steps + 3
        steps = steps + 1
        v[j+1] = x
        swaps = swaps + 1
        steps = steps + 4
    steps = steps + 1
    print 'Steps: ' + str(steps)
    print 'Comparisons: ' + str(compar)
    print 'Swaps: ' + str(swaps)
    print 'While Questions: ' + str(whileq)
    return steps


n = 50
runs = 100

sum = 0
min = n**3
max = 0
for i in range(runs):
    x = randomPerm(n)
    t = isortSteps(x)
    if t < min :
       min = t
    if t > max :
       max = t
    sum = sum + t
