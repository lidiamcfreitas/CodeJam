global res


def multiply(a,b):
    global res
    res = ""
    invert = 0
    if a[0]=="-" and b[0]=="-":
        a = a[1]
        b = b[1]
        
    if( a[0]=="-" and b[0]!="-" ):
        invert = 1
        a = a[1]
    if ( b[0]=="-" and a[0]!="-" ):
        invert = 1
        b = b[1]
        
    if a=="1":
        res = b
    if b == "1":
        res = a       
    if a==b and a!= "1":
        res = "-1"
    if a=="i" and b =="j":
        res =  "k"
    if a=="j" and b == "i":
        res = "-k"
    if a=="i" and b=="k":
        res = "-j"
    if a=="k" and b=="i":
        res = "j"
    if a=="j" and b=="k":
        res = "i"
    if a=="k" and b=="j":
        res = "-i"
    if (invert==1):
        if res[0]=="-":
            res = res[1]
        else:
            res = "-" + res
    return res






#MAIN
T = int(raw_input())
for test in range(1,T+1):
    L, X = tuple(map(int, raw_input().split(" ")))
    S = str(raw_input())
    
    string = S*X
    i = []
    j = []
    k = []

    i_mult = "1"
    for i_n in range(len(string)):
        ext = 0
        i_mult = multiply(i_mult, string[i_n])
        if i_mult == "i":
            j_mult = "1"
            for j_n in range(i_n+1,len(string)):
                j_mult = multiply(j_mult, string[j_n])
                if j_mult == "j":                 
                    k_mult = "1"
                    for k_n in range(j_n+1, len(string)):
                        k_mult = multiply(k_mult, string[k_n])
                        if k_mult == "k" and k_n==len(string)-1: 
                            ext = 1
                            print ("Case #%d: YES" % test)
                            break
                if(ext==1):
                    break
        if(ext==1):
            break
    if (ext==0):
        print ("Case #%d: NO" % test)
    
    #print(i)
    """
    for posi in range(len(i)):
        mult = "1"
        newString = string[posi+1:]
        #print(newString)
        for n in range(len(newString)):
                mult = multiply(mult, newString[n])
                #print(newString[n], mult)
                if mult == "j":
                    j += [n+i[posi]+1]
        
    
    #print(j)
    
    for posi in range(len(j)):
        ex = 0
        mult = "1"
        newString = string[j[posi]+1:]
        #print(newString)
        for n in range(len(newString)):
                mult = multiply(mult, newString[n])
                #print(newString[n], mult)
                if mult == "k":
                    #k += [n+j[posi]+1]
                    if n+j[posi]+1==len(string)-1:
                        ex = 1
                        break
        if ex==1:
            break
        
    if k!=[]:
        if max(k)==len(string)-1:
            print ("Case #%d: YES" % test)
        else:
            print ("Case #%d: NO" % test)
    
    else:
        print ("Case #%d: NO" % test)
    
    """



