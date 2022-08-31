n = int(input("num"))
p_list = [2,3]
i = 1

for i in range(1,n):
    n1 = 6*i -1
    n2 = 6*i +1
    for l in range(len( p_list)):
        if n1 % p_list[l] == 0:
            break
        elif l + 1 == len(p_list):
            p_list.append(n1)
            
    for k in range(len( p_list)):
        if n2 % p_list[k] == 0:
            break
        elif k + 1 == len(p_list):
            p_list.append(n2)
            

for f in range(n):
    print(p_list[f])
    