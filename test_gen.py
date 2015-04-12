from random import randint
T = int(raw_input())
Smax = int(raw_input())

print(T)

def randomString():
    string =""
    for i in range(Smax):
        string += str(randint(0,3))
    return string

for i in range(T):
    print(str(Smax) + " "+randomString()+"1")