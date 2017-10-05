class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return  len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self._data.pop()

    def Stack(self):
        return self._data


a = ArrayStack()
b = ArrayStack()
a.push(3)
a.push(4)
a.push(5)
a.push(6)
print(a.Stack())
b.push(a.pop())
b.push(a.pop())
b.push(a.pop())
b.push(a.pop())
print(b.Stack())

def Recursive_pop_stack(a):
    if a.is_empty():                                #6.4
        return a.Stack()
    a.pop()
    return Recursive_pop_stack(a)

print(Recursive_pop_stack(b))

def Reversing_A_list(a):                            #6.5
    pops = len(a)
    empty_stack = ArrayStack()
    for k in range(pops):
        empty_stack.push(a.pop(0))
    for l in range(pops):
        a.append(empty_stack.pop())
    return a
sample1 = [3,3,2,4,5,5,7]
print(Reversing_A_list(sample1))

class ArrayQueue:
    DEFAULT_CAPACITY = 20

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise ValueError('queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front+1)%len(self._data)
        self._size -= 1
        return answer

    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size)%len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None]*cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front = 0


from collections import deque

class ArrayQueue_Deque:                             #6.11

    def __init__(self):
        self._data = deque()
        self._size = len(self._data)
        self._first = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError('Empty')
        return self._first

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Empty')
        answer = self._data[0]
        self._data.popleft()
        return answer

    def enqueue(self,e):
        self._data.append(e)


class ArrayStack_Capped:                                  #6.16
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None]*self._maxlen
        self._maxlen = ArrayStack_Capped.DEFAULT_CAPACITY
        self._top  = 0


    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return  len(self._data) == 0

    def push(self,e):
        if self._top+1 == self._maxlen:
            raise ValueError('Full')
        self._data[self._top+1] = e
        self._top += 1

    def top(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        answer = self._data[self._top]
        self._data[self._top] = None
        self._top -= 1
        return answer

    def Stack(self):
        return self._data

def Reverse_Stack(s):                             #6.18
    l = len(s)
    empty1 = ArrayStack()
    empty2 = ArrayStack()
    for k in range(l):
        empty1.push(s.pop())
    for k in range(l):
        empty2.push(empty1.pop())
    for k in range(l):
        s.push(empty2.pop())
    return s.Stack()


sample2 = ArrayStack()
sample2.push(2)
sample2.push(4)
sample2.push(7)
sample2.push(9)
print(sample2.Stack())

print(Reverse_Stack(sample2))


def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.is_empty()

def is_matched_html(raw):                           #6.19
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>',j+1)
        if k == -1:
            return False
        p = raw.find(' ',j+1)
        tag = raw[j+1:p]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<',k+1)
    return S.is_empty()


def Postfix_notation(expression):                          #6.22
    list1 = list(expression)
    stack1 = []
    len1 = len(list1)
    for k in range(len(list1)):
        if list1[k] == ')':
            if list1[k-1] != ')':
                list1[k-2],list1[k-1] = list1[k-1],list1[k-2]
    if list1[-1] != ')':
        list1[-1],list1[-2] = list1[-2],list1[-1]
    for k in range(len(list1)):
        if list1[k] == '(':
            if list1[k-1] != '(':
                sign = list1[k-1]
                stack1.append(')')
                for j in range(k+1,len(list1)):
                    if list1[j] == ')':
                      if stack1 != []:
                        stack1.pop()
                        if stack1 == []:
                            list1[k-1],list1[j] = list1[j],list1[k-1]
                            continue
                    elif list1[j] == '(':
                        stack1.append(')')
    j = 0
    for k in range(len1):
        if list1[j] == '(' or list1[j] == ')':
            list1.pop(j)
        else:
            j += 1

    return ''.join(k for k in list1)

sample3 = "((5*3)/(4*2))*(5-7)"
print(Postfix_notation(sample3))



def Capital_Gain(Stock_Activity):
  Bought = ArrayQueue()                                     #6.36
  Sold = ArrayQueue()

  for k in range(len(Stock_Activity)):
    if Stock_Activity[k][0] == 'Bought':
       Bought.enqueue(Stock_Activity[k][1])
    elif Stock_Activity[k][0] == 'Sold':
        Sold.enqueue(Stock_Activity[k][1])
  No_Sold = 0
  Sold_for = 0
  while not Sold.is_empty():
    x = Sold.dequeue()
    No_Sold += x[0]
    Sold_for += x[0]*x[1]
  No_Bought = 0
  Bought_for = 0
  while not Bought.is_empty():
      k = Bought.dequeue()
      if k[0] + No_Bought >= No_Sold:
          return (Sold_for-Bought_for)-((No_Sold-No_Bought)*k[1])
      Bought_for += k[0]*k[1]
      No_Bought += k[0]

Stock_Activity = [['Bought',[100,20]],['Bought',[20,24]],['Bought',[200,36]],['Sold',[150,30]]]

print(Capital_Gain(Stock_Activity))





