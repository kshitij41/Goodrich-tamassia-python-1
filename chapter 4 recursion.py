s = [5,9,2,8,7,6,3,2]

def find_max_recur(k,a,b):                                  #4.1
    if a != b:
     while 0 <= b < len(k) and 0 <= a < len(k):
       if k[a] >= k[b]:
        find_max_recur(s,a,b-1)
        break
       else:
        find_max_recur(s,a+1,b)
        break
    else:
        print(str(k[a]))

def find_min_recur(k,a,b):                                 #4.9
    if a != b:
     while 0 <= b < len(k) and 0 <= a < len(k):
       if k[a] <= k[b]:
         find_min_recur(s,a,b-1)
         break
       else:
         find_min_recur(s,a+1,b)
         break
    else:
        print(str(k[a]))



find_max_recur(s,0,6)
find_min_recur(s,0,6)

def log_n_int(n,k):                             #4.10
    if n//2 != 0:
        k += 1
        log_n_int(n//2,k)
        pass
    else:
        print(k)

log_n_int(15,0)

def elem_unique(s,k):                            #4.11
    if k == len(s) - 1:
        print('true')

    for j in range(k,len(s)):
        if s[k-1] == s[j]:
            print('false')
            break
        else:
            if j == len(s) - 1:
                elem_unique(s,k+1)
            else:
                continue


elem_unique(s,1)


def multiply_recur(m,n):                            #4.12
    if n == 0:
        return 0
    else:
        return m + multiply_recur(m,n-1)

print(multiply_recur(4,5))



import random


def Tower_of_hanoi(a,b,c):                                  #4.14  unsuccessful attempt,
    if a != [] and b != []:
     if a == [] and b != [] and c != []:
        if b[-1] > c[-1]:
            k = random.randrange(3)
            if k == 0:
                a.append(b.pop())


                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                a.append(c.pop())


                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                b.append(c.pop())

                return Tower_of_hanoi(a,b,c)

        elif b[-1] < c[-1]:
            k = random.randrange(3)
            if k == 0:
                a.append(c.pop())


                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                a.append(b.pop())


                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                c.append(b.pop())


                return Tower_of_hanoi(a,b,c)

     elif a != [] and b == [] and c != []:
        if a[-1] > c[-1]:
            k = random.randrange(3)
            if k == 0:
                b.append(a.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                b.append(c.pop())


                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                a.append(c.pop())

                return Tower_of_hanoi(a,b,c)

        elif a[-1] < c[-1]:
            k = random.randrange(3)
            if k == 0:
                b.append(c.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                b.append(a.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                c.append(a.pop())

                return Tower_of_hanoi(a,b,c)

     elif a != [] and b != [] and c == []:
        if a[-1] > b[-1]:
            k = random.randrange(3)
            if k == 0:
                c.append(a.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                c.append(b.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                a.append(b.pop())

                return Tower_of_hanoi(a,b,c)

        elif a[-1] < b[-1]:
            k = random.randrange(3)
            if k == 0:
                c.append(b.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                c.append(a.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                b.append(a.pop())

                return Tower_of_hanoi(a,b,c)
     elif a != [] and b != [] and c != []:
        if a[-1] > b[-1] > c[-1]:
            k = random.randrange(3)
            if k == 0:
                a.append(c.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                a.append(b.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                b.append(c.pop())

                return Tower_of_hanoi(a,b,c)

        elif a[-1] > c[-1] > b[-1]:
            k = random.randrange(3)
            if k == 0:
                a.append(b.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                a.append(c.pop())

                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                c.append(b.pop())

                return Tower_of_hanoi(a,b,c)

        elif c[-1] > a[-1] > b[-1]:
            k = random.randrange(3)
            if k == 0:
                c.append(b.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                c.append(a.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                a.append(b.pop())
                return Tower_of_hanoi(a,b,c)

        elif c[-1] > b[-1] > a[-1]:
            k = random.randrange(3)
            if k == 0:
                c.append(a.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                c.append(b.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                b.append(a.pop())
                return Tower_of_hanoi(a,b,c)

        elif b[-1] > c[-1] > a[-1]:
            k = random.randrange(3)
            if k == 0:
                b.append(a.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                b.append(c.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                c.append(a.pop())
                return Tower_of_hanoi(a,b,c)

        elif b[-1] > a[-1] > c[-1]:
            k = random.randrange(3)
            if k == 0:
                b.append(c.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                b.append(a.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 2:
                a.append(c.pop())
                return Tower_of_hanoi(a,b,c)

        elif a != [] and b == [] and c == []:
            k = random.randrange(2)
            if k == 0:
                b.append(a.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                c.append(a.pop())
                return Tower_of_hanoi(a,b,c)

        elif a == [] and b != [] and c == []:
            k = random.randrange(2)
            if k == 0:
                a.append(b.pop())
                return Tower_of_hanoi(a,b,c)

            elif k == 1:
                c.append(b.pop())
                return Tower_of_hanoi(a,b,c)
    return a,b,c


sample1 = [9,8,7,6,5,4,3,2,1]

print(Tower_of_hanoi(sample1,[],[]))


import itertools                                                       #4.15

def findsubsets(s,k):
    while k > 0:
     return set(itertools.combinations(s,k)),findsubsets(s,k-1)

print(findsubsets(sample1,9))

def symmetry(list,a,b):                                                #4.16
    if a < b:
        list[a],list[b] = list[b],list[a]
        symmetry(list,a+1,b-1)
        return list




sample2 = list("symmetry")
print(sample2)

print(symmetry(sample2,0,7))

def check_for_palindrome(list,a,b):                                    #4.17
    if a < b:
        if list[a] == list[b]:
            check_for_palindrome(list,a+1,b-1)
        else:
            return False
    return True

sample3 = ['a','i','e','e','i','g']

print(check_for_palindrome(sample3,0,5))


def vowel_consonent_count(s,v,c):                                         #4.18
    for j in range(len(s)):
        if s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u':
            v += 1
            continue
        else:
            c += 1
            continue
    return v,c

print(vowel_consonent_count(sample3,v=0,c=0))

def vowel_consonent_count_recur(s,j,v,c):

    if j < len(s):
      if s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u':
             v += 1

             return vowel_consonent_count_recur(s,j+1,v,c)

      else:
             c += 1

             return vowel_consonent_count_recur(s,j+1,v,c)


    return v,c


print(vowel_consonent_count_recur(sample3,j = 0,v = 0,c = 0))


def even_before_odd(s,a,b):                                                   #4.19
    if a < b :
        if s[a]%2 != 0 and s[b]%2 == 0:
            s[a],s[b] = s[b],s[a]
            even_before_odd(s,a+1,b-1)
        elif s[a]%2 != 0 and s[b]%2 != 0:
            even_before_odd(s,a,b-1)
        elif s[a]%2 == 0 and s[b]%2 == 0:
            even_before_odd(s,a+1,b)
        elif s[a]%2 == 0 and s[b]%2 != 0:
            even_before_odd(s,a+1,b-1)
        return s

sample4 = [5,9,2,7,6,3,8]
print(even_before_odd(sample4,0,6))

def before_less_than_k(s,k,a,b):                                               #4.20
    if a < b:
        if s[a] >= k and s[b] < k:
            s[a],s[b] = s[b],s[a]
            before_less_than_k(s,k,a+1,b-1)
        elif s[a] >= k and s[b] >= k:
            before_less_than_k(s,k,a,b-1)
        elif s[a] < k and s[b] < k:
            before_less_than_k(s,k,a+1,b)
        elif s[a] < k and s[b] >= k:
            before_less_than_k(s,k,a+1,b-1)
        return s


print(before_less_than_k(sample4,7,0,6))

def pair_sum_k(s,k,a,b):                                                  #4.21
    if a < b :
        if s[a] <= k/2 and s[b] >= k/2:
            if s[a] + s[b] == k:
                return a,b
            elif s[a] + s[b] > k:
                return pair_sum_k(s,k,a,b-1)
            elif s[a] + s[b] < k:
                return pair_sum_k(s,k,a+1,b)
    return False

sample5 = [4,5,6,11,34,65,76,123]

print(pair_sum_k(sample5,82,0,7))

def non_recursive_power(x,n):                                          #4.22

    s = []
    k = x
    while n != 0:
        s.append(n)
        n = n//2
    l = len(s)
    for j in range(l):
        pop = s.pop()
        if pop == 1:
            continue
        elif pop%2 == 0:
            x = x*x
        elif pop%2 != 0:
            x = x*x
            x *= k
    return x

print(non_recursive_power(4,15))


def iterative_scale(n):                                                    #4.25
    s = [1]
    p = 0
    if n == 0:
        raise ValueError
    else:
        while n-1 != 0:
            s.append(2*s[p]+1)
            n -=1
            p += 1
    spc = ' '
    for k in range(len(s)):
        print(str((spc*((2**(len(s)-k-1))-1)+"|")*s[k]))





iterative_scale(7)
















