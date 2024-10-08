
# Python Basic to End

Python is a programming language that is interpreted, object-oriented, and high-level too.

- Python executes line by line code.
- If it satisfies by the rule then only it ececutes the line of code.

### Python Logo
![App Screenshot](https://gss-technology.com/wp-content/uploads/2021/07/04.png)

## Python Data_Types

- Integer
- Float
- String
- List
- Tuple
- Set
- Dictionary

#### Examples

Integer : 45

Float : 55.56

String : 'Python','123','python123'

List : [10,20,30,40,50]

Tuple : (10,20,30,40,50)

Sets : {10,20,30,40,50}

Dictionary : {Key_value}->{'apple':100}

## Python Variable

The variable is stored in temporary memory called RAM.

Ex: a = 90

When we call 'a' ,it gives 98 as output.

- int - uses 4 bytes of memory 
- float - uses 4 bytes of memory 
- string - uses 1 byte of memory

## Rules to create a variable
 
There are 4 different rules to create a variable

- Variable should not start with a number if needed
  we want to start with the underscore(_).

  EX:  

       _9a=100
- Variable should be single word or single character but not       multiple words if needed we have to use underscore(_).

  Ex: 
       
       Sai_Ram = 100

- Python variables are completely case sensitive.

  Ex: 

      name ='sai'

      print(NAME) #here call name because it is case sensitive

output: error

- Punctuations are not used as a variable 

  Ex:  

        $=100 
        print($) 

output: Invalid 

## Relation between print and variable :
- Using , (comma) inside the print we can add one data type with other data type and comma gives one tab space.
- Using + we can add string data type along with given variables but we need to make sure that given variables are also string and the + operator won't give any tab space.
- Using Identifiers like
                        
                         %d -> int

                         %f -> float

                         %s -> str

- Using { } and f function.
  if f see anything in the flower braces, it prints which is in {}flower braces

## Operators
- Addition -> +
- Substraction -> -
- Multiplication -> *
- Division -> /
- FLoor Division->//
- Mod function-> %
- Power->** 
- Built_in_Function->pow()
- Greaterthan-> >
- Lessthan-> <
- Greaterthan or equal to-> >=
- Lessthan or equal to-> <=
- Equal to-> =
- Double equal to->==
- Not equal to->!=
- and 
- or

# Python String Concept:
String is represented in the quotes - ' '

Ex: 

    a = 'python'

1. Memory Allocation

2. Indexing

3. Slicing

4. Skipping

5. Mutable or Immutable

6. Built_in_functions

**Memory Allocation** : Memory allocation can be defined as allocating a block of space in the computer memory to a program.

Ex: 
    
    a = 'sai'

**Indexing** : 2 types

- forward indexing 
- backward indexing
Ex: 

      a = 'data'

      print(a[2])

output: t

**Slicing** : To access group of characters at a time.

Ex: 
   
     a ='data science'

     print(a[2:6])

output : ta s

**Skipping** : To skip how many values we use skipping.

Ex: 

       a = 'data science'

       print(a[::2])

output : dt cec 

**Mutable or Immutable**:

Mutable - if user can increase or decrese memory.
Immutable - if user cannot increase or decrease memory.

- String is **Immutable**

String - It is used to find ASCII number, memory address.
       - String is Immutable
       - String does indexing, slicing and skipping.
#### Built_in_functions:
- capitalize
- title
- lower
- upper
- islower
- isupper
- startswith
- endswith
- isalpha
- isnumeric
- isalnum
- count
- index
- split
- join

**capitalize** : It will capital the starting letter.

Ex: 
     
    a='sai baba'
    a.capitalize()
    print(a)

output: 

    Sai baba

**title** : It will capital each word starting letter into capital.

Ex: 
    
    a='sai baba'
    a.title()
    print(a)

output: 
    
    Sai Baba

**lower** : All the capital letters are converted into small letters.

Ex: 
    
    a='AmeriCA'
    print(a.lower())

output: 
    
    america

**upper** : All the small letters are converted into capital letters.

Ex: 
    
    a='AmeriCA'
    print(a.upper())

output: 
    
    AMERICA

**islower** : It checks whether all are small letters or not , if it is small that says True , if not False.

Ex: 

    a='AmeriCA'
    print(a.islower())

output: 
    
    False

**isupper** : It checks whether all are capital letters or not , if it is capital that says True , if not False.

Ex: 

    a='AmeriCA'
    print(a.isupper())

output: 
    
    False

**isalpha** : It will check all are alphabets or not.

Ex: 

    a='america123'
    print(a.isalpha())

output: 
    
    False

**isnumeric** : It will check all are numbers or not.

Ex: 
    
    a='1223'
    print(a.isnumeric())

output: 
    
    True

**isalnum** : It contains both the numbers and alphabets, but not the space.

Ex: 

    a='python123'
    print(a.isalnum())

output: 
    
    True

**startswith** : It takes input from user and checks whether the starting letter matches with the given letter and if matches it prints as True , or else False.

Ex: 
    
    a= 'deep learning'
    print(a.startswith('p'))

output: 
    
    False

**endswith** : It takes input from user and checks whether the ending letter matches with the given letter and if matches it prints as True , or else False.

Ex: 
    
    a='deep learning'
    print(a.endswith('g'))

output: 
    
    True

**replace** : It will replace a string.

Ex: 
    
    a='joy'
    print(a.replace('j','r'))

output: 
    
    roy

**count** : It is used to count the number of times a given character is repeating.

Ex: 

    a='data science'
    print(a.count('a'))

output: 
    
    2

**index** : It is used to find the index of a given character.

Ex: 

    a='data science'
    print(a.index('e'))

output: 
     
    8

- len function : It is used to find length of a string.

Ex: 
     
    len('sai')
   
output: 
     
    3

#### string and substring
Ex: 
    
    a='python is very simple language'
    print('is' in a)

output: 
    
    True

## Operators in strings
Ex:

    python = 'ab' #9506
    java   = 'CD' #4556
    print(python > java) #9506>4556

output: 
    
    True

Based on the ASCII(American Standard Code for Information Interchange) values it gives the output.

Explanation: 

    A-65            a-97

    B-66            b-98

    C-67            c-99

    D-68            d-100


a-97 b-98 --> a * b = 9506

C-67 D-68 --> C * D = 4556

python > java --> ab > CD --> 9506 > 4556 = True

### To find **ascii** values of a given character.
ord('F') - 70

ord('a') - 97

ord('z') - 122

### To find character from a given ascii value.
chr(70) - 'F'

chr(100) - 'd'

chr(97) - 'a'

# Python List Concept 

List is represented in the square braces - []

Ex: 
    
    a = [10,20.55,'data']

1. Memory Allocation

2. Indexing

3. Slicing

4. Skipping

5. Mutable or Immutable

6. Built_in_functions

**Memory Allocation** : Memory allocation can be defined as allocating a block of space in the computer memory to a program.

Ex: 

    a = [10,50,'python']

**Indexing** : 

Ex:
     
    a = [10,55.55,'data']

    print(a[1])

output: 
    
    55.55

**Slicing**:

Ex:

    a = [10,15,19,3,7,32,17]

    print(a[2:5])
  
output: 

    19,3,7

**Skipping**:

Ex:

    a = [10,15,19,3,7,32,17]

    print(a[::2])

output: 
    
    [10,19,7,17]

**Mutable or Immutable**:
 - List is **Mutable**
 - Using index it is not possible to do adding or deleting in the memory for list concept , in that case use **built_in_functions**.

### Built_in_Functions:
**addition** 

- append
- extend
- insert

**deletion**

- pop
- remove

**other**

- count
- index
- copy
- clear
- sort
- reverse

### for adding

**append** : It will take single value from the user and will add to the exixting list only at the end.

Ex: 

    a = [10,50,3,13]

    a.append(500)

    print(a)

output: 
    
    [10,50,3,13,500]

- Note : we can't append two values a.append(200,300) # error

**extend** : It will take many value multiple values from the user and will add to the existing list only at the end.

Ex: 

    a=[10,50,3,13]
    a.extend([1,2])
    print(a)

output: 
    
    [10,50,3,13,1,2]

**insert** : we can add values where ever we ant it need index number where we wanted to add.

Ex: 

    a=[10,50,3,13]
    a.insert(2,300)
    print(a)

output: 
    
    [10,50,300,3,13]

### for deleting

**pop** : pop will remove last value defaultly but if we pass a number it will treat like index.

Ex:
   
    a=[10,50,3,13]
    a.pop()
    print(a)

output: 

    [10,50,3]
Ex: 

    a=[10,50,3,13]
    a.pop(2)#giving index value and removing
    print(a)

output: 

     [10,50,13]

**remove** : It will value directly and remove the value.

Ex: 
   
    a=[10,50,3,13]
    a.remove(50)
    print(a)

output: 
    
    [10,3,13]

**replace** : It replaces the value.

Ex: 

    a=[10,50,3,13]
    a[1]=5
    print(a)

output: 
    
    [10,5,3,13]

**count** : used to count the values. 

Ex: 
    
    a=[1,2,4,5,1,3,19,30,1]
    print(a.count(1))

output: 
    
    3

**index** : used to find the index of a given value.

Ex: 

    a=[1,2,4,5,1,3,19,30,1]
    print(a.index(19))

output: 
    
    6

**clear** : It is used to clear the data from the variable but variable will be alive in the memory. 

Ex: 

    a=[1,2,4,5]
    a.clear()
    print(a)

output:
    
     []

**copy** : There are 2 types of copy techniques

- deep copy
- shallow copy

**deep copy** : It has same address.

Ex:  
    
    a=[10,20,50]
    b=a
    print(a)
    print(b)
    print(id(a))
    print(id(a))
output: 

    [10,20,50]
    [10,20,50]
    13363760886528 
    13363760886528

**shallow copy** : It has different address and if we add value to a it won't copy in b.

Ex:
   
    a=[10,20,50]
    b=a.copy()
    print(a)
    print(b)
    print(id(a))
    print(id(b))
    a.append(100)
    print(a)
    print(b)

output:
  
    [10,20,50]
    [10,20,50]
    12345567856
    12342346578
    [10,20,50,100]
    [10,20,50]

**reverse** : [::-1] It reverses the given input.

Ex:
   
    a=[10,20,30,40,50]
    a.reverse()
    print(a)

output:
    
    [50,40,30,20,10]

**sort** : ascending and descending orders.

Ex: 

    a=[9,1,5,7,11,13,6,2,8]
    a.sort() #default ascending order
    print(a)

output: 

    [1,2,5,6,7,8,9,11,13]

Ex: 

    descending order
    a=[9,1,5,7,11,13,6,2,8]
    a.sort(reverse=True)
    print(a)

output: 

    [13,11,9,8,7,6,5,2,1]

# Python Tuple Concept
- Python tuple is represented  in parenthesis -> ()

Ex: 

    a = (10,55.55,'data')

1. Memory Allocation

2. Indexing

3. Slicing

4. Skipping

5. Mutable or Immutable

6. Built_in_functions

**Memory Allocation** : Memory allocation can be defined as allocating a block of space in the computer memory to a program.

Ex:
    
    a = (10,20.66,'python)

- user can pass anything inside the tuple like int | float | string | boolean.
- memory allocation, indexing, slicing, skipping are same as string and list only.

**Indexing** :

Ex:  

    a=(10,4,17,9,21,36)
    print(a[2])

output: 

    17

**Slicing** :

Ex:
   
    a=(10,4,17,9,21,36)
    print(a[1:4])

output: 
    
    (4,17,9)

**Skipping** :

Ex: 

    a=(10,4,17,9,21,36)
    print(a[::3])

output: 
    
    (10,9)

**Mutable or Immutable** :
- Tuple is **Immutable**

**Built_in_Functions** :

- It has 2 built_in_functions only

       - count
       - index

**count** : 

Ex:

    a=(10,4,17,9,21,36)
    a.count(4)
    print(a)

output: 

    1

**index** : 

Ex: 

    a=(10,4,17,9,21,36)
    print(a.index(36))

output: 
    
    5

# Python Sets Concept
- Python sets are represented in flower braces -> **{}**

Ex:

     a = {10,20,30,40}

- Memory Allocation

- Mutable or Immutable

- Built_in_functions

**Memory Allocation** : Memory allocation can be defined as allocating a block of space in the computer memory to a program.

Ex:
   
    a = {10,30,40,60,70}

- Allocation of memory is unordered in sets.

- Python sets are unordered pairs, which means there will be no index concept,if there is no index means no slicing and skipping.

- Python sets don't allow **duplicates values**.

Ex:

    a = {10,20,30,50,10,100,20,10}
    print(a)

output:

    {50,100,20,10,30}

**Mutable or Immutable** : 

- Python sets are **Mutable**.
- Python sets are mutable but they **don't allow mutable types** inside the set.

Ex: 

    a = {10,55.55,'data',[1,2,3]}#here list is mutable 
    print(a)

output: 
    error
     
    unhashable type:'list'

- Manually we can't prove that set is mutable but by using built_in_functions we can prove it as mutable.

**Built_in_Functions** :

- add
- update
- pop
- discard
- remove
- clear
- copy
- union
- intersection

**add** : It will take only one input from the user and will add to the existing set **randomly**.

Ex: 

    a = {10,5,6,20,98,45}
    a.add(600)
    print(a)

output: 
    
    {98,20,5,6,600,10,45}

**update** : It takes multiple values from the user and will add  to the existing set randomly.

Ex:
    
    a = {10,5,6,20,98,45}
    a.update([100,200,300])
    print(a)

output:
    
    {5,6,200,10,20,98,100,300,45}

**pop** : It will remove any one value randomly.

Ex:
    
    a = {10,5,6,20,98,45}
    a.pop()
    print(a)

output: 

    {20,5,6,10,45}

**discard** : It will take only one input from the user and if the input is available in the set, it will remove or else it will remain silent.

Ex: 
  
    a = {10,5,6,20,98,45}
    a.discard(98)
    print(a)

output:
     
    {20,5,6,10,45}

**remove** : It will take only one input from the user and if the input is available in the set, it will remove or else it will throw an error.

Ex: 

    a = {10,5,6,20,98,45}
    a.remove(900)
    print(a)

output: 
     
    error
    not found value 900
    
**copy** : 2 types
- deep copy
- shallow copy

**deep copy** : same address and it copies values in a to b are same.

Ex: 

    a = {10,5,6,30,98,45}
    b=a
    print(a)
    print(b)
    print(id(a))
    print(id(b))

output:

    {20, 5, 39, 10, 45}
    {20, 5, 39, 10, 45}
    133192238102144
    133192238102144

**shallow copy** : It has different address and if we add value to a it won't copy in b.
 
Ex:
    
    a={10,20,39,45,5}
    b=a.copy()
    print(a)
    print(b)
    a.add(1000)
    print(id(a))
    print(id(b))
    print(a)
    print(b)

output:
     
    {20, 5, 39, 10, 45}
    {20, 5, 39, 10, 45}
    133192238101696
    133192238103488
    {20, 5, 39, 1000, 10, 45}
    {20, 5, 39, 10, 45}

**union** : 

Ex: 

    a={1,2,3,4,5,6}
    b={5,6,7,8,9,10}
    print(a.union(b))

output: 

    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

**intersection** : 

Ex:

    a={1,2,3,4,5,6}
    b={5,6,7,8,9,10}
    print(a.intersection(b))

output: 

    {5,6}

**clear** : 
- Empty set representation -> set()

Ex:

    a = {1,10,15,19,25}
    a.clear()
    print(a)

output: 

    set()

# Python Dictionary Concept
- Python Dictionary are represented in flower braces -> **{Key_Value}**

- Dictionary is used to prepare the structured data but not to show the data. Dictionary will be represented with ->{Key_Value} sets are also represented with {}, but dictionary is represented with Key-Value pair where key is the column name and value is the column value.

EX:

    a = {'Age':30,'Loc':'Chennai','Salary':1200}
    print(a)
    print(type(a))

output:
 
    {'Age':30,'Loc':'Chennai','Salary':1200}

- In dictionary values can be anything 
Ex: 
   
    a = {'Age':30,'Salary':55.55,'Loc':'Hyd','Pincode':(500085),'State':['Telangana'],'data':{1,2,3}}
    print(a)
    
output:
  {'Age':30,'Salary':55.55,'Loc':'Hyd','Pincode':(500085),'State':['Telangana'],'data':{1,2,3}}

- Mutable types are not allowed in dictionary as a **key**
Ex: 
    a = {1:500,2.2:800,'loc':'hyd',['pincode']:(500085)}
    print(a)
output:
    error
    Unhashable the list

#### To call multiple values
Ex:
    a = {'Age':[0,40,50],'Loc':['Chennai','Banglore','Hyderabad'],'Salary':[1200,1800,2200]}
    print(a)
    print(a['Loc'])
output:
    ['Chennai','Banglore','Hyderabad']
### Dictionary is Mutabl or Immutable
Ex: adding to dictionary

    fruits = {'apple':500 ,'carrot':100}
    print(f'Before adding :{fruits})
    fruits['banana'] = 1000
    print(f'After adding :{fruits})
output: 

    Before adding :{'apple':500,'carrot':100}
    After adding :{'apple':500,'carrot':100,'banana':1000}

Ex: deleting from dictionary

    fruits = {'apple':500 ,'carrot':100,'banana':1000}
    print(f'Before deleting :{fruits})
    del fruits['carrot']
    print(f'After deleting :{fruits})
output: 

    Before adding :{'apple':500,'carrot':100,'banana':1000}
    After adding :{'apple':500,'banana':1000}
- From these operations we can say that dictionary is **Mutable**

## Dictionary Built_in_Functions:
- get 
- update 
- pop 
- popitem
- key 
- value
- items
- clear
- copy

**get** : It is used to call required data from the existing dictionary.

Ex: 

    b = {'apple':500,'carrot':100,'banana':1000}
    print(b.get('carrot'))

output:

    100

**update** : It is used to add key_value to the existing dictionary.

Ex:

    b = {'apple':500,'carrot':100,'banana':1000}
    b.update({'grapes':200})
    print(b)

output:

    {'apple':500,'carrot':100,'banana':1000,'grapes':200}

**pop** : It will take key from the user and will remove that key_value.

Ex:
  
    b = {'apple':500,'carrot':100,'banana':1000}
    b.pop('carrot')
    print(b)

output:
 
    b = {'apple':500,'banana':1000}

**popitem** : It will remove last key_value.

Ex:
  
    b = {'apple':500,'carrot':100,'banana':1000}
    b.popitem()
    print(b)

output:
 
    b = {'apple':500,'carrot':100}

**keys** : It will print all the keys in the dictionary.

Ex:

    b = {'apple':500,'carrot':100,'banana':1000}
    print(b.keys())

output:
    
    dict_keys([apple,carrot,banana])

**values** : It will print all the values in the dictionary.

Ex:

    b = {'apple':500,'carrot':100,'banana':1000}
    print(b.values())

output:
    
    dict_values([500,100,1000])

**items** : It will print both keys and values in the dictionary.

Ex:

    b = {'apple':500,'carrot':100,'banana':1000}
    print(b.items())

output:
    
    dict_keys([(apple,500),(carrot,100),(banana,1000)])

**clear** : It is used to clear the data from the variable but variable will be alive in the memory.

Ex:

    b = {'apple':500,'carrot':100,'banana':1000}
    b.clear()
    print(b)

output:
    
    {}

**copy** : There are 2 types of copy techniques

- deep copy
- shallow copy

**deep copy** : It has same address.

Ex:

    b={'apple':500,'carrot':100,'banana':1000}
    a=b
    print(a)
    print(b)
    print(id(a))
    print(id(b))
output:
    
    {'apple': 500, 'carrot': 100, 'banana': 1000}
    {'apple': 500, 'carrot': 100, 'banana': 1000}
    138914830239936
    138914830239936

**shallow copy** : It has different address and if we add value to a it won't copy in b.

Ex:

    b={'apple':500,'carrot':100,'banana':1000}
    a=b.copy()
    print(a)
    print(b)
    print(id(a))
    print(id(b))

output:

    {'apple': 500, 'carrot': 100, 'banana': 1000}
    {'apple': 500, 'carrot': 100, 'banana': 1000}
    138914831763712
    138914831764480


# Control Statements
Control statements in Python are used to control the flow of execution of a program based on certain conditions or loops.
### Looping Statements

    - for loop
    - while loop

### Conditional Statements

    - if
    - else
    - elif
    
### Control Flow Altering Statements
 
    - break
    - continue

**for loop** : Executes a block of code a specified number of times, typically iterating over a range of values.

Ex:
    for i in range(11,21):
    print(i+10)

output: 
      
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30

**while loop** : Executes a block of code as long as a specified condition is true.

Ex:
   
    a=1
    while a<=20:
    print(a)
    a=a+1

output: 

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20

**if** : The if statement evaluates a condition and executes the block of code if the condition is True.

Ex:

    money=20000
    iphone=50000
    if money>iphone:
    print('I will buy iphone')
  
    #it won't print anything it will be silent

**else** : The else block executes when the if condition is False.

Ex:

    money=20000
    iphone=50000
    if money>iphone:
    print('I will buy iphone')
    else:
    print('I will not buy an iphone')

output:

    I will not buy an iphone

**elif** : The elif statement allows you to check multiple conditions.

Ex:
    money=20000
    iphone=50000
    samsung=25000
    vivo=15000
    if money>iphone:
    print('I will buy iphone')
    elif money>samsung:
    print('i will buy samsung')
    elif money>vivo:
    print('i will buy vivo')
    else:
    print('i wont buy any phone')

output: 

    i will buy vivo

**break** : The break statement is used to exit the loop prematurely when a certain condition is met.

Ex:
 
    for i in range(11,21):
    print(i)
    if i==13:
    break

output:
 
    11
    12
    13

**continue** : The continue statement skips the current iteration and proceeds with the next iteration.

Ex:

    for i in range(11,21):
    if i==16:
    continue
    print(i)

output:

    11
    12
    13
    14
    15
    17
    18
    19
    20

**pass** : The pass statement is a placeholder for future code. It does nothing when executed but is used to define an empty block.

Ex:

    if x > 5:
    pass  # placeholder for future implementation

# Functions

Function is used for **reusability** - Writing the logic one time and using them many times.

### Syntax:
          
    def <[function_name]> ():
     - logic here

Ex: 
   
    def sharuk():
      print('good morning')
    sharuk()

output:

    good morning

There are **two** types in the Functions

1. Non - Parameter Functions

Ex:
 
    def sharuk():
       print('good morning')
    sharuk()

output: 

    good morning

2. Parameter Functions

Ex: 

    def sai(a,b):
      print(a+b)
    sai(10,20)

output: 
   
    30

## Local Variable and Global Variable

**Local variable** : The variable in the function is called Local.

Ex:

    #local variable
    def fun():
      p=100  #local variable
      print(f'i am using inside the function:{p}')
    fun()
    print(f'i am using outside the function:{p}')

output:

    error, it can't call outside fun because it is local variable

**Global variable** : we call from anywhere we access it in inside and outside of the function.

Ex: 

    k=60 #global variable
    def fun():
       print(f'i am using inside the function:{k}')
    fun()
    print(f'i am using outside the function:{k}')

outputt: 

    i am using inside the function:60
    i am using outside the function:60

## Conversion of local to global 

Ex:

    def fun():
      global p
      p=100
      print(f'i am using inside the fun:{p}')
    fun()
    print(f'i am using outside the fun:{p}')

output:

    i am using inside the fun:100
    i am using outside the fun:100

### Return key word :
return gives the values/variables which present in return 

Ex:
 
    def fun(a,b):
       c=[]
       for i in range(a,b):
         if i%2==0:
           c.append(i)
       return c

    sol=fun(11,21)
    print(sol)
 
output:

    [12, 14, 16, 18, 20]

# Lambda functions:
 

