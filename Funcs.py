from email.mime import base
import random

def snake_list_shuffle(x):
    funklist = []
    funklist.append(x[0])
    if len(x) >= 2:
        funklist.append(x[len(x)-1])
    if len(x) > 2:
        for i in range(2,len(x)):
            funklist.append(x[i-1])
    return funklist



def prime(x):
    if x < 0:
        return False
    else:
        for i in range(2,x):
            if x % i == 0:
                return False
        return True





def list_shuffle(x):
    func_list = []
  
    if type(x) == type(func_list):
        for i in range((len(x)-1),-1,-1):
            func_list.append(x[i])
        x = func_list
        return x
    else:
        print("invalid input")


def palindrome(x):
    test_word = ""
    for n in range(len(x)-1, -1, -1):
        test_word += x[n]
    if x == test_word:
        return True
    else:
        return False

def random_yt_url():
    bas64 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_'
    url_end =''
    for i in range(11):
        url_end += bas64[random.randint(0,63)]
    print("https://www.youtube.com/watch?v="+url_end)
    return "https://www.youtube.com/watch?v="+url_end
random_yt_url()