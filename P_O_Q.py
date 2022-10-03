
from Funcs import prime

P_O_Q = []


for p in range (1,2000):
    for q in range(1,2000):
        if prime(p) and prime(q):
            if prime((p**q + q**p)):
                P_O_Q.append(f"{p} och {q}")
                print(f"{p} och {q}")
        
    

print(P_O_Q)