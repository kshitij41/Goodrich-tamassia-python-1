def is_multiple(n,m):
    if n < m:
        print('False')
    elif n == m:
        print('True')
    else:
        k = 1
        while m*k < n:
            k = k+1
        if m*k == n:
            print('True')
        else:
            print('False')

is_multiple(586,293)


def is_even(k):
    n = 2

    while n < k:
        n += 2
    if n == k:
       print('True')
    else:
       print('False')

is_even(28)



def minmax(data):
    i = 0
    j = 0
    max = 0
    while i < len(data):
        for n in range(i):
            if data[n] > max:
               max = data[n]
        i += 1
    min = 100
    while j < len(data):
        for k in range(j):
            if data[k] < min:
                min = data[k]
        j += 1
    result = [min, max]
    return result



def funk(n):
    S = 0
    while n > 0:
        S += (n-1)*(n-1)
        n -= 1
    print(str(S))

funk(5)

def funk1(n):
    s = 0
    k = 1
    while k <= n:
        s += k**2
        k += 2
    print(str(s))

funk1(11)

for k in range(50,100,10):
    print(str(k))


def some(j):
    s = []
    n = 0
    while n != j:
       k = 2**n
       s.append(k)
       n += 1
    print(str(s))

some(9)

import random

kuku = [8 ,9 ,7 ,3 ,2 ,5 ,4 ,3 ,11 ,15]

print(str(kuku[random.randrange(len(kuku)-1)]))



def listrev(data):
 new = [0]*len(data)
 for k in range(0,len(data)):
     new[k - len(data)] = data[len(data) - k - 1]
 print(str(new))


listrev(kuku)



def oddproduct(data):
    for a in range(0, len(data)):
        for b in range(a+1, len(data)):
            if (data[a]*data[b])%2 == 1:
                print(str(a),str(b))

oddproduct(kuku)

def notequal(data):
    for a in range(0, len(data)):
        for b in range(a+1, len(data)):
            if data[a] == data[b]:
                print(str(a),str(b))

notequal(kuku)


def scale(data,factor):
    for j in range(len(data)):
        data[j] *= factor
    print(str(data))

scale(kuku,8)
j = []
for n in range(26):
   j.append( chr(ord('a') + n))
print(j)


op = [2, 4, 5, 3 , 22 , 14 , 65, 32]
s = list(op)
random.shuffle(s)
print(str(s))


k = []
def shuffle(a,n,s):        # using randint in a binary manner to come up with a function similar to shuffle

    if n <= 0 :
        s.append(a)
    elif n == a:
        s.append(n)
    else:
       k = random.randint(a,n)
       s.append(k)
       if a <= k-1 :
          shuffle(a,k-1,s)
       if k+1 <= n:
          shuffle(k+1,n,s)
    return s



print(str(shuffle(0,7,k)))

fe = open('sample.txt','w')        # write sequence of lines and print those lines in reverse order
fe.write('hey there\n')
fe.write('what\'s goinf on\n')
fe.write('are you free tomorrow\n')

k = []
fe.close()
fname = open('sample.txt', 'r')
with fname as f:
   content = f.readlines()
content = [x.strip() for x in content]
for n in content:
  k.append(n)
for j in range(len(k)-1,-1,-1):
  print(k[j])

a = [5,5,2,4,5,3,7] #
b = [4,5,6,7,8,6,4]
c = [None]*7
for n in range(len(c)):
  c[n] = a[n]*b[n]
print(str(c))

j = [None]*8
try:
  number = random.randint(0,20)
  j[number] = 7
except IndexError:
  print('on’t try buffer overflow attacks in Python!')

def vowelcount(string):
   p = ['a','e','i','o','u']
   t = 0
   for n in range(len(string)):
    for k in p:
       if string[n] == k:
          t += 1
   print(str(t))

words = 'sunshine'
vowelcount(words)

def RemovePunctuation(string):
 b = []
 j = list(string)
 k = [',','"','(',')','!',':',';']
 for n in range(len(j)):
  for m in range(len(k)):
    if j[n] == k[m]:
       b.append(n)
 for f in range(len(b)):
   j[b[f]] = ""
 print(''.join(l for l in j))

words1 = "asd : weewr;sdk ad'asdjbd:::,,,("
RemovePunctuation(words1)

def ThreeInputEquation(a,b,c):
    if (a+b) == c:
       print('true')
    elif (b+c) == a:
       print('true')
    elif (c+a) == b:
       print('true')
    else:
       print('false')

ThreeInputEquation(4,1,3)




k = 2
for l in range(6):
    if l == k:
        continue
    print(str(l))


d = ['']*4   #catdog permutation mini solution
for k in range(4):
    d[k] = 'c'
    for l in range(4):
        if l == k:
            continue
        d[l] = 'a'
        for m in range(4):
            if m == k:
                continue
            elif m == l:
                continue
            d[m] = 't'
            for n in range(4):
                if n == k:
                    continue
                elif n == l:
                    continue
                elif n == m :
                    continue
                d[n] = 'd'
                print(d)

def calculator():             # 1.33 and 1.34...don't know what exactly is meant by button push...i think we are not supposed to use gui for now
    a = float(input('first number: '))
    d = input('expression:')
    b = float(input('second number: '))
    c = ['-','+','/','*']
    for n in range(len(c)):
     if c[n] == d and n == 0:
            print(str(a-b))
            k = input('do you want to continure y or n:')
            if k == 'y':
                calculator()
            else:
                break

     elif c[n] == d and n == 1:
            print(str(a+b))
            k = input('do you want to continue y or n:')
            if k == 'y':
                calculator()
            else:
                break
     elif c[n]== d and n == 2:
            if b == 0:
                if a==0:
                    print('not defined')
                    k = input('do you want to continue y or n:')
                    if k == 'y':
                        calculator()
                    else:
                        break
                else:
                    print('infinity')
                    k = input('do you want to continue y or n:')
                    if k == 'y':
                        calculator()
                    else:
                        break
            else:
              print(str(a/b))
              k = input('do you want to continure y ro n:')
              if k == 'y':
                  calculator()
              else:
                  break

     elif c[n] == d and n == 3:

             print(str(a*b))
             k = input('do you want to continure y or n:')
             if k == 'y':
                 calculator()
             else:
                break
     else:
         continue

def punishment_simulator(string):
    j = 1
    d = [3,10,11,14,23,25,27,30,31]  # since it is a stand-alone programme d array is chosen for this particular case at random by me
    k = list(string)
    while j <= 100:
      n = random.randint(0,len(d)-1)

      if d[n] == 3:
            k[d[n]] =  ""
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 10:
            k[d[n]] = ""
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 11:
            k[d[n]] = 't'
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 14:
            k[d[n]] = '['
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 23:
            k[d[n]] = 'u'
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 25:
            k[d[n]] = ""
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 27:
            k[d[n]] = ""
            print("".join(x for x in k),j)
            k = list(string)
            j += 1
            continue
      elif d[n] == 30:
            k[d[n]],k[d[n+1]] = k[d[n+1]],k[d[n]]
            print("".join(x for x in k),j)
            j += 1
            continue


string = "I will never spam my friends again"

punishment_simulator(string)


def same_birthday_probability(n):
    probability = 1-(364/365)**((n*(n-1))/2)
    print(str(probability*100))


same_birthday_probability(75)




def filler(k,x,j):  #word count problem starts

    if x < len(j):
      for b in range(len(j)):
        if j[b] == 0:
         x = 1
         for n in range(b,len(k)):
             if k[n] == k[b]:
                 j[n] = x,k[b]
                 x += 1

def word_count(string):
    k = string.split()
    x = 0
    j = [0]*(len(k))
    filler(k,x,j)
    print(j)

word_count("babu ka sabu dana babu ka sabu dana dana sabu ka hai babu")

