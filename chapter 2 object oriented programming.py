class Flower():                                           #2.4
    def __init__(self,name,n_petals,price):
        self._name = name
        self._n_petals = int(n_petals)
        self._price = price

    def price(self):
         return self._price

    def n_petals(self):

         return self._n_petals

    def name(self):

         return self._name

    def break_petal(self,x):
        if int(x) != x:
            raise ValueError
        if x > self._n_petals:
            raise ValueError
        self._n_petals -= x
        return self._n_petals

    def grow_petal(self,x):
        self._n_petals += x
        return self._n_petals

    def change_name(self, eman):
        self._name = eman
        return self._name

    def change_price(self,new):
        self._price = new
        return self._price


blossom = Flower('blossom',7,3.68)

blossom.change_price(4)
print(str(blossom.price()))

blossom.break_petal(4)
print(blossom._n_petals)


class Vector():                            #2.9 , 2.10 , 2.11 , 2.12
    def __init__(self,d):
        self._coords = [0]*d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] + self[j]
        return result



    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return   str(self._coords)[1:-1]

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        for j in range(len(self)):
            self._coords[j] *= -1
        return self._coords

    def __mul__(self, x):
        for j in range(len(self)):
            self._coords[j] *= x
        return self._coords

    def __rmul__(self,x):
        for j in range(len(self)):
            self._coords[j] = x*self._coords[j]

    def __mulv__(self,other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j]*self[j]
        return result

    def __rmulv__(self,other):
        if len(self) != len(other):
            raise  ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]*other[j]
        return result

u = Vector(4)


u.__setitem__(0,12)
u.__setitem__(1,23)
u.__setitem__(2,19)
u.__setitem__(3,8)

v = [12,34,12,42] + u

print(v)


v*3

print(v)

3*v

print(v)

print(u.__mulv__(v))


class Vector():                                      #2.13 2.14 2.15
    def __init__(self,d):
        if type(d) is int:
           self._coords = [0]*d
        elif len(d) > 1:
            self._coords = [0]*len(d)
            for j in range(len(d)):
                self._coords[j] = d[j]


    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] + self[j]
        return result



    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return   str(self._coords)[1:-1]

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        for j in range(len(self)):
            self._coords[j] *= -1
        return self._coords

    def __mul__(self, x):
        for j in range(len(self)):
            self._coords[j] *= x
        return self._coords

    def __rmul__(self,x):
        for j in range(len(self)):
            self._coords[j] = x*self._coords[j]

    def __mulv__(self,other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j]*self[j]
        return result

    def __rmulv__(self,other):
        if len(self) != len(other):
            raise  ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]*other[j]
        return result




j = Vector([12,34,12,33])
k = Vector(7)

print(j)
print(k)

class Progression:

    def  __init__(self,start = 0):
        self._current = start

    def _current(self):
        return self._current

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):

        print(''.join(str(next(self)) for j in range(n)))


class FibonacciProgression(Progression):                     #2.18

    def __init__(self,first = 0 ,second = 1):

        super().__init__(first)
        self._prev = second - first

    def _advance(self):

        self._prev,self._current = self._current,self._prev + self._current
        return self._current



k = FibonacciProgression(2,2)
k._advance()
k._advance()
k._advance()
k._advance()
k._advance()
k._advance()
print(k._advance())

class ArithmeticProgression(Progression):

    def __init__(self,increment = 1,start = 0):

        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment



ap = ArithmeticProgression(128,0)

def two_point_one_nine(x,y,k):                           #2.19
    while x < y:
        x += 128
        k += 1
    return k

ans = two_point_one_nine(0,10000000,0)
print(ans)

from abc import ABCMeta,abstractmethod

class Sequence(metaclass=ABCMeta):                     #2.22

    @abstractmethod
    def __len__(self):

     @abstractmethod

     def __getitem__(self, item):


      def __contains__(self, value):
        for j in range(len(self)):
            if self[j] == value:
                return True
        return False

    def index(self,val):
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')

    def count(self,val):
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError
        for j in range(len(self)):
            if self[j] == other[j]:
                continue
            else:
                return False
        return True

    def __lt__(self, other):
        if len(self) != len(other):
            raise ValueError
        for j in range(len(self)):
            if self[j] < other[j]:
                continue
            else:
                return False
        return True




class Vector():                                         #2.25
    def __init__(self,d):
        self._coords = [0]*d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] + self[j]
        return result



    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return   str(self._coords)[1:-1]

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        for j in range(len(self)):
            self._coords[j] *= -1
        return self._coords

    def __mul__(self, x):
        if isinstance(x,int):
            for j in range(len(self)):
                self._coords[j] *= x
            return self
        elif isinstance(x,Vector):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*x[j]
            return result


class SequenceIterator:                 #2.26

    def __init__(self,sequence):
        self._seq = sequence
        self._k = 0

    def __next__(self):
        self._k -= 1
        if self._k*-1 < len(self):
            return(self._seq[self._k])
        else:
            raise StopIteration()



class Range:                                            #2.27

    def __init__(self,start,stop = None,step = 1):

        if step == 0:
           raise ValueError('step cannot be 0')

        if stop is None:
            start,stop = 0,start

        self._lenght = max(0,(stop - start + step - 1)//step)
        self._start = start
        self._step = step

    def __len__(self):
        return self._lenght

    def __getitem__(self, k):
         if k < 0:
             k += len(self)

         if not 0 <= k < self._lenght:
             raise IndexError('index out of range')

         return self._start + k*self._step

    def __contains__(self, pop):
        k = 0
        j = self._start + k*self._step
        while j < pop:
            k += 1
            j = self._start + k*self._step
        if j == pop:
            print('True')
        else:
            print('False')

pop = Range(2,1000,5)

pop.__contains__(77)


class CreditCard:                                           # 2.28   2.29  2.30

    def __init__(self,customer,bank,acnt,limit,total_p):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
        self._total_p = total_p

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def _set_balance(self,b):
        self._balance = b
        return self._balance

    def charge(self,price):

        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self,amount):
        self._balance -= amount
        self._total_p += amount

class PredatoryCreditCard(CreditCard):

    def __init__(self,customer,bank,acnt,limit,apr,charges,minpay):

        super().__init__(customer,bank,acnt,limit)
        self._apr = apr
        self._charges = charges
        self._minpay = (minpay/100)*self._balance

    def charge(self,price):
        self._charges += 1
        success = super().charge(price)
        if not success:
            self._balance += 5
        if self._charges > 10:
            self._balance -= 1
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr,1/12)
            self._balance *= monthly_factor
        self._charges = 0
        if self._total_p < self._minpay:
            self._balance -= 100
        self._total_p = 0

class Progression:

    def  __init__(self,start = 0):
        self._current = start

    def _current(self):
        return self._current

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self,n):

        print(''.join(str(next(self)) for j in range(n)))


class Difference_progression(Progression):               #2.31

    def __init__(self,first = 2,second = 200):
        super().__init__(first)
        self._prev = first + second

    def _advance(self):
        if self._prev > self._current:
           self._prev,self._current = self._current,self._prev - self._current
        elif self._prev < self._current:
            self._prev,self._current = self._current,self.current - self._prev



class Root_progression(Progression):                    #2.32

     def __init__(self,first = 65536):
         super().__init__(first)
         self._prev = first*first

     def _advance(self):
         self._prev,self._current = self._current,self._current**(1/2)
         return self._current


k = Root_progression()
k._advance()
k._advance()
print(k._advance())




def Polynomial_derivative(Coeff,Power):                   #2.33
    newCoeff = []
    newPower = []
    if len(Coeff) != len(Power):
        raise IndexError
    for j in range(len(Coeff)):
        if Power[j] == 0:
            newCoeff.append(0)
        else:
           newCoeff.append(Coeff[j]*Power[j])
        newPower.append(Power[j]-1)
        continue

    print(newCoeff)
    print(newPower)

one = [2,3,2,3]
two = [5,2,1,0]

Polynomial_derivative(one,two)

def Alphabet_frequency(document):                                           #2.34
    array = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    wordlist = list(document)
    for k in range(len(wordlist)):
        if wordlist[k] == '':
            continue
        else:
              num = ord(wordlist[k]) - 97
              if 0 < num < len(array):
                array[num] += 1
                continue

    print(array)
    print(alpha)



words = 'hey there how are you'
Alphabet_frequency(words)


class Alice_create_packet:                               #2.35 attempt
    def __init__(self,packets):
        self._packets = packets

    def fill_packet_set(self,packet):
        self._packets.append(packet)
        return self._packets

    def _packets(self):
        return self._packets

class Bob_recieves:

    def __init__(self,storage):
        self._storage = storage

    def _storage(self):
         return self._storage

    def _check_and_delete(self):
        for l in range(len(self._storage)):
            self._storage[l] = 'None'

class Internet_process(Alice_create_packet,Bob_recieves):

     def __init__(self,packets,storage):
         super().__init__(packets)
         super().__init__(storage)

     def check_n_send(self):
         for l in range(len(self._packets)):
             self._storage.append(self._packets[l])
         return self._storage


import random                                               #2.36

def river(lenght):
    objects = ['bear','fish','None']
    k = ['']*(lenght)
    for l in range(len(k)):
        k[l] = objects[random.randrange(3)]
    return k

def none_filler(list,object):
    r = random.randrange(len(list))
    if list[r] == 'None':
        list[r] = object
    else:
        none_filler(list,object)

def movement(river):
    object = ['bear','fish','None']
    for l in range(len(river)):
       x = random.randrange(3)
       if x == 0:
         if l == 0:
           river[l] = 'None'
         else:
            if river[l-1] == river[l]:
                if river[l] != 'None':
                    none_filler(river,river[l])
                    continue
                else:
                    continue
            elif river[l] != 'None' and river[l-1] != river[l] != 'None':
                if river[l-1] == 'bear':
                    river[l] = 'None'
                    continue
                elif river[l-1] == 'None':
                    river[l-1] = river[l]
                    river[l] = 'None'
                else:
                    river[l-1] = 'bear'
                    river[l] = 'None'
                    continue
            else:
                continue
       elif x == 1:
           if l == len(river) - 1:
               river[l] = 'None'
           else:
               if river[l+1] == river[l]:
                   if river[l] != 'None':
                       none_filler(river,river[1])
                       continue
                   else:
                       continue
               elif river[l] != 'None' and river[l+1] != river[l] != 'None' :
                   if river[l+1] == 'bear':
                      river[l] = 'None'
                      continue
                   else:
                       river[l+1] == 'bear'
                       river[l] = 'None'
                       continue
               else:
                   continue

       elif x == 2:
           continue

    return river

river1 = ['bear','fish','fish','None','None','fish','bear','None','None','None']
print(movement(river1))


from time import sleep

from threading import Timer

def timeout():
    print(movement(river1))

t = Timer(50000.0,timeout())
t.start()

class Animal:                                                      #2.37
    def __init__(self,type,gender,strength):
        self._type = type
        self._gender = gender
        self._strength = strength

    def _type(self):
        return self._type

    def _gender(self):
        return self._gender

    def _strength(self):
        return self._strength

    def __repr__(self):
        return '%s %s %s'%(self._type,self._gender,self._strength)



def none_filler(list,object):
    r = random.randrange(len(list))
    if list[r] == 'None':
        list[r] = object
    else:
        none_filler(list,object)

def movement_2(river):

    for l in range(len(river)):
       x = random.randrange(3)
       if x == 0:
         if l == 0:
           river[l] = 'None'
           continue
         else:
            if river[l-1] == river[l] == 'None':
                continue
            elif river[l-1] == 'None':
                river[l-1] = river[l]
                river[l] = 'None'
                continue
            elif river[l] == 'None':
                continue


            elif river[l-1]._type == 'bear' and river[l]._type == 'fish':
                river[l] = 'None'
                continue
            elif river[l-1]._type == 'fish' and river[l]._type == 'bear':
                river[l-1] = 'None'
                continue

            elif river[l-1]._type == river[l]._type:
                if river[l-1]._gender == river[l]._gender:
                    if river[l-1]._strength > river[l]._strength:
                        river[l] = 'None'
                        continue

                    else:
                        river[l-1] = 'None'
                        continue
                else:
                    if river[l-1]._strength > river[l]._strength:
                        k = (river[l-1]._strength + river[l]._strength)//2
                        object = Animal(river[l]._type,river[l-1]._gender,k)
                        none_filler(river,object)
                        continue
                    else:
                        k = (river[l-1]._strength + river[l]._strength)//2
                        object = Animal(river[l]._type,river[l]._gender,k)
                        none_filler(river,object)
                        continue




       elif x == 1:
           if l == len(river) - 1:
               river[l] = 'None'
               continue
           else:
               if river[l+1] == river[l] == 'None':
                   continue
               elif river[l] == 'None':
                   continue
               elif river[l+1] == 'None':
                   river[l+1] = river[l]
                   river[l] = 'None'
                   continue

               elif river[l+1]._type == 'bear' and river[l]._type == 'fish':
                    river[l] = 'None'
                    continue
               elif river[l+1]._type == 'fish' and river[l]._type == 'bear':
                    river[l+1] = 'None'
                    continue

               elif river[l+1]._type == river[l]._type:
                   if river[l+1]._gender == river[l]._gender:
                       if river[l+1]._strength > river[l]._strength:
                           river[l] = 'None'
                           continue
                       else:
                           river[l+1] = river[l]
                           river[l] = 'None'
                           continue
                   else:
                       if river[l+1]._strength > river[l]._strength:
                           k = (river[l+1]._strength + river[l]._strength)//2
                           object = Animal(river[l]._type,river[l+1]._gender,k)
                           none_filler(river,object)
                           continue
                       elif river[l+1]._strength <= river[l]._strength:
                           k = (river[l+1]._strength + river[l]._strength)//2
                           if river[l]._type == 'bear':
                              object = Animal('bear',river[l]._gender,k)
                              none_filler(river,object)
                              continue
                           else:
                               object = Animal('fish',river[l]._gender,k)
                               none_filler(river,object)
                               continue

                       else:
                           continue
               else:
                   continue

       elif x == 2:
           continue

    return river

ab = Animal('bear','m',76)
bc = Animal('fish','f',130)
cd = Animal('bear','f',23)
de = Animal('bear','f',217)
ef = Animal('fish','m',176)
fg = Animal('bear','f',237)

river_3 = [ab,bc,cd,'None',de,ef,'None','None',fg,ab,cd,ab,cd]
print(movement_2(river_3))


class E_book_reader:                                          #2.38
    def __init__(self,Inventory,Collection):
        self._Inventory = Inventory
        self._Collection = Collection

    def Buy_Book(self,x):
        self._Collection.append(self._Inventory[x])
        return self._Collection

    def read_book(self,y):
        fw = open("sample.txt",'w')
        fw.write(self._Collection[y])
        fw.close()
        fr = open("sample.txt",'r')
        fr.read()

    def Purchased_book(self):
        return self._Collection

class Polygon:                                              #2.39

    def __init__(self,*coords):
        self._list = []
        li = self._list
        for c in coords:
            li.append(c)
        self._sides = len(li)

    def _triangle_area(self,t1,t2,t3):
        k = (1/2)*((t1[0]*(t2[1]-t3[1]))-(t2[0]*(t1[1]-t3[1]))+(t3[0]*(t1[1]-t2[1])))
        if k < 0 :
            return -k
        else:
            return k

    def _area_polygon(self):
        li = self._list
        area = 0
        for k in range(1,len(li)-1):
            area += self._triangle_area(li[0],li[k],li[k+1])
        return area

    def _side_length(self,s1,s2):
        return (((s2[0]-s1[0])**2) + ((s2[1]-s1[1])**2))**(1/2)

    def _perimeter(self):
        li = self._list
        p = 0
        for l in range(len(li)-1):
            p += self._side_length(li[l],li[l+1])
        p += self._side_length(li[-1],li[0])

        return p

square = Polygon([0,0],[0,2],[2,2],[2,0],[1,-1])               #only work when coordinated are entered in circular order
print(square._area_polygon())
print(square._perimeter())
