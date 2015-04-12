from random import randint
T = int(raw_input())
D = int(raw_input())
max = int(raw_input())

print(T)

def randomString():
    string =""
    for i in range(D):
        string += str(randint(1,max)) + " "
    return string[:-1]

for i in range(T):
    print(D)
    print(randomString())