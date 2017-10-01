
import sys
data = []
for k in range(6):                                                           #5.2
    a = len(data)
    b = sys.getsizeof(data)
    if (k)%4 == 0:
     print('Length: {0:3d}; size in bytes: {1:4d}'.format(a,b))
    data.append(None)

data = [None,None,None,None,None,None,None,None]                               #5.3
for k in range(8):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; size in bytes: {1:4d}'.format(a,b))
    data.pop()


import ctypes

class DynamicArray:                                          #5.4   5.6
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def len(self):
        return self._n

    def __getitem__(self, k):
        if  k >= self._n:
            raise IndexError('invalid index')
        elif 0 <= k < self._n:
          return self._A[k]
        elif k < 0:
            if 0 <= -k < self._n:
                return self._A[self._n+k]

    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        return (c*ctypes.py_object)()


    def insert(self,k,value):
        if self._n == self._capacity:
            B = self._make_array(2*self._capacity)
            for j in range(k):
                B[j] = self._A[j]
            for l in range(k,self._n):
                B[l+1] = self._A[l]
            self._A = B
            self._capacity *= 2
            self._A[k] = value
            self._n += 1
        else:
         for j in range(self._n,k,-1):
            self._A[j] = self._A[j-1]
         self._A[k] = value
         self._n += 1

def repeated_integer(s):                                    #5.7
    n_consecutive_int = len(s) - 1
    sum = 0
    for j in range(len(s)):
        sum += s[j]
    return sum - (((n_consecutive_int)*(n_consecutive_int+1))/2)

sample1 = [1,2,3,4,5,6,7,8,9,10,7]

print(repeated_integer(sample1))


class CaesarCipher:

    def __init__(self,shift):
        encoder = [None]*26
        decoder = [None]*26
        for k in range(26):
            encoder[k] = chr((k+shift)%26 + ord('A'))
            decoder[k] = chr((k-shift)%26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self,message):
        return self._transform(message,self._forward)

    def decrypt(self,secret):
        return self._transform(secret,self._backward)

    def _transform(self,original,code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k])-ord('A')
                msg[k] = code[j]
        return ''.join(msg)

class CaesarCipher2:                                               #5.10

    def __init__(self,shift):

        self._forward = ''.join([chr((k+shift)%26 + ord('A')) for k in range(26)])
        self._backward = ''.join([chr((k-shift)%26 + ord('A')) for k in range(26)])

    def encrypt(self,message):
        return self._transform(message,self._forward)

    def decrypt(self,secret):
        return self._transform(secret,self._backward)

    def _transform(self,original,code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k])-ord('A')
                msg[k] = code[j]
        return ''.join(msg)

    def _forward(self):
        return self._forward


print(CaesarCipher2(3)._forward)


def multiple_list_sum(s):                                       #5.11
    sum = 0
    for a in range(len(s)):
        for b in range(len(s[a])):
            sum += s[a][b]
    return sum

sample2 = [[2,3,4],[11,23,45],[34,22,12]]

print(multiple_list_sum(sample2))


def multiple_list_sum_2(s):                             #5.12
    sum1 = 0
    for a in range(len(s)):
        sum1 += sum(s[a],0)
    return sum1

print(multiple_list_sum_2(sample2))

import random

def randomize_list(list):                                #5.14
    for k in range(2*len(list)):
        a = random.randrange(len(list))
        b = random.randrange(len(list))
        list[a],list[b] = list[b],list[a]
    return list

sample3 = [12,33,32,12,34,45,21,34,45]
print(randomize_list(sample3))


class DynamicArray:                                     #5.16
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def len(self):
        return self._n

    def __getitem__(self, k):
        if  k >= self._n:
            raise IndexError('invalid index')
        elif 0 <= k < self._n:
          return self._A[k]
        elif k < 0:
            if 0 <= -k < self._n:
                return self._A[self._n+k]

    def append(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def pop(self):
        self._A[self._n-1] = None
        self._n -= 1
        if self._n*4 <= self._capacity:
            B = self._make_array(self._n*2)
            for k in range(self._n):
                B[k] = self._A[k]
            self._A = B
            self._capacity = self._n*2


    def _resize(self,c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        return (c*ctypes.py_object)()


    def insert(self,k,value):
        if self._n == self._capacity:
            B = self._make_array(2*self._capacity)
            for j in range(k):
                B[j] = self._A[j]
            for l in range(k,self._n):
                B[l+1] = self._A[l]
            self._A = B
            self._capacity *= 2
            self._A[k] = value
            self._n += 1
        else:
         for j in range(self._n,k,-1):
            self._A[j] = self._A[j-1]
         self._A[k] = value
         self._n += 1

def remove_all(data,value):                       #5.25
    indexes_to_delete = []
    left_shift_negation = 0
    for k in range(len(data)):
        if data[k] == value:
            indexes_to_delete.append(k-left_shift_negation)
            left_shift_negation += 1
    for k in range(len(indexes_to_delete)):
        data.pop(indexes_to_delete[k])
    return data

sample4 = [2,3,4,2,5,6,7,8,9,2,2]

print(remove_all(sample4,2))

def six_repeated_integers(s):                                          #5.26
    sorted_s = []
    sorted_s.append(s.pop())
    for k in range(len(s)):
        sorted_s.append(s.pop())
        for j in range(len(sorted_s)-1,0,-1):
            if sorted_s[j] <= sorted_s[j-1]:
                sorted_s[j],sorted_s[j-1] = sorted_s[j-1],sorted_s[j]
    for l in range(len(sorted_s)):
        if sorted_s[l] == sorted_s[l+1]:
            return sorted_s[l]


sample5 = [1,2,3,4,4,4,4,4,4,5]

print(six_repeated_integers(sample5))

import math



def k_bit_number_missing(s):                                     #5.27
    sorted_s = []
    sorted_s.append(s.pop())
    for k in range(len(s)):
        sorted_s.append(s.pop())
        for j in range(len(sorted_s)-1,0,-1):
            if sorted_s[j] <= sorted_s[j-1]:
                sorted_s[j],sorted_s[j-1] = sorted_s[j-1],sorted_s[j]
    k_bit_not_there = []
    for l in range(len(sorted_s)-1):
        m = sorted_s[l+1] - sorted_s[l]
        if 2 <= m < len(sorted_s):
         for n in range(1,m):
            k_bit_not_there.append(sorted_s[l]+n)



    return k_bit_not_there


sample6 = [8,8,8,8,8,8,8,15]

print(k_bit_number_missing(sample6))


def natural_join(A,B):                                  #5.29
    result = []
    for k in range(len(A)):
        for l in range(len(B)):
            if A[k][1] == B[l][0]:
                result.append([A[k][0],A[k][1],B[l][1]])
    return result

sample7 = [[1,2],[9,4],[13,43],[1,33],[54,12]]
sample8 = [[2,5],[2,1],[43,11],[12,7],[2,17]]

print(natural_join(sample7,sample8))

def packet_sort(s):                                      #5.30
    sorted_s = []
    sorted_s.append(s.pop())
    for k in range(len(s)):
        sorted_s.append(s.pop())
        for j in range(len(sorted_s)-1,1,-1):
            if sorted_s[j] <= sorted_s[j-1]:
                sorted_s[j],sorted_s[j-1] = sorted_s[j-1],sorted_s[j]
    return sorted_s

def multiple_list_recursive_sum(s,k,sum1):                  #5.31
    if k == len(s):
        return sum1
    sum1 += sum(s[k],0)
    return multiple_list_recursive_sum(s,k+1,sum1)

sample9 = [[1,2,3],[2,32,12],[31,42,11]]
print(multiple_list_recursive_sum(sample9,0,sum1 = 0))


def three_D_Set_sum(A,B):                                      #5.32
    C = [[0]*3 for k in range(3)]
    for k in range(3):
        for l in range(3):
            C[k][l] += A[k][l] + B[k][l]
    return C

A_sum = [[1,2,3],[4,5,6],[7,8,9]]
B_sum = [[10,11,12],[13,14,15],[16,17,18]]
print(three_D_Set_sum(A_sum,B_sum))

def matrix_multiply(A,B):                                         #5.33
    if len(A[0]) != len(B):
        raise IndexError
    C = [[0]*len(B[0])for k in range(len(A))]
    for z in range(len(A)):
        for y in range(len(B[0])):
            for x in range(len(B)):
                C[z][y] += A[z][x]*B[x][y]
    return C

print(matrix_multiply(A_sum,B_sum))


class CaesarCipher:                                           #5.34

    def __init__(self,shift1,shift2):
        encoder = [None]*26
        decoder = [None]*26
        for k in range(26):
            encoder[k] = [chr((k+shift1)%26 + ord('A')),chr((k+shift2)%26 + ord('a'))]
            decoder[k] = [chr((k-shift1)%26 + ord('A')),chr((k-shift2)%26 + ord('a'))]
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self,message):
        return self._transform(message,self._forward)

    def decrypt(self,secret):
        return self._transform(secret,self._backward)

    def _transform(self,original,code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k])-ord('A')
                msg[k] = code[j][0]
            elif msg[k].islower():
                j = ord(msg[k])-ord('a')
                msg[k] = code[j][1]

        return ''.join(msg)


