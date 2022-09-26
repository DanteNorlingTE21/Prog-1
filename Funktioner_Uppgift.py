# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    print(f"{name} är bäst")
    


def square(number):
    return number*number
    


def sums(a,b):
    return (a + b)
    


# Nu blir det lite svårare


def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else: 
        return c


def palindrom(x):
    test_word = ""
    for n in range(len(x)-1, -1, -1):
        test_word += x[n]
    if x == test_word:
        return True
    else:
        return False


def prime(x):
    if x < 0:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True
