
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
- Using Identifiers like %d -> int
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

Ex: a = 'pyton'

1. Memory Allocation

2. Indexing

3. Slicing

4. Skipping

5. Mutable or Immutable

6. Built_in_functions

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
output: Sai baba

**title** : It will capital each word starting letter into capital.

Ex: 
    
    a='sai baba'
    a.title()
    print(a)

output: Sai Baba

**lower** : All the capital letters are converted into small letters.

Ex: 
    
    a='AmeriCA'
    print(a.lower())

output: america

**upper** : All the small letters are converted into capital letters.

Ex: 
    
    a='AmeriCA'
    print(a.upper())

output: AMERICA

**islower** : It checks whether all are small letters or not , if it is small that says True , if not False.

Ex: 

    a='AmeriCA'
    print(a.islower())

output: False

**isupper** : It checks whether all are capital letters or not , if it is capital that says True , if not False.

Ex: 

    a='AmeriCA'
    print(a.isupper())

output: False

**isalpha** : It will check all are alphabets or not.

Ex: 

    a='america123'
    print(a.isalpha())

output: False

**isnumeric** : It will check all are numbers or not.

Ex: 
    
    a='1223'
    print(a.isnumeric())

output: True

**isalnum** : It contains both the numbers and alphabets, but not the space.

Ex: 

    a='python123'
    print(a.isalnum())

output: True

**startswith** : It takes input from user and checks whether the starting letter matches with the given letter and if matches it prints as True , or else False.

Ex: 
    
    a= 'deep learning'
    print(a.startswith('p'))

output: False

**endswith** : It takes input from user and checks whether the ending letter matches with the given letter and if matches it prints as True , or else False.

Ex: 
    
    a='deep learning'
    print(a.endswith('g'))

output: True

**replace** : It will replace a string.

Ex: 
    
    a='joy'
    print(a.replace('j','r'))

output: roy

**count** : It is used to count the number of times a given character is repeating.

Ex: 

    a='data science'
    print(a.count('a'))

output: 2

**index** : It is used to find the index of a given character.

Ex: 

    a='data science'
    print(a.index('e'))

output: 8

- len function : It is used to find length of a string.

Ex: 
     
     len('sai')
   
output: 3

#### string and substring
Ex: 
    
    a='python is very simple language'
    print('is' in a)

output: True

## Operators in strings
Ex:

    python = 'ab' #9506
    java   = 'CD' #4556
    print(python > java) #9506>4556

output: True

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

**Indexing** : 

Ex:
     
     a = [10,55.55,'data']

     print(a[1])

output: 55.55

**Slicing**:

Ex:

    a = [10,15,19,3,7,32,17]

    print(a[2:5])
  
output: 19,3,7

**Skipping**:

Ex:

    a = [10,15,19,3,7,32,17]

    print(a[::2])

output: [10,19,7,17]

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

output: [10,50,3,13,500]

- Note : we can't append two values a.append(200,300) # error

**extend** : It will take many value multiple values from the user and will add to the existing list only at the end.

Ex: 

    a=[10,50,3,13]
    a.extend([1,2])
    print(a)

output: [10,50,3,13,1,2]

**insert** : we can add values where ever we ant it need index number where we wanted to add.

Ex: 

    a=[10,50,3,13]
    a.insert(2,300)
    print(a)

output: [10,50,300,3,13]

### for deleting

**pop** : pop will remove last value defaultly but if we pass a number it will treat like index.

Ex:
   
    a=[10,50,3,13]
    a.pop()
    print(a)

output: [10,50,3]

    a=[10,50,3,13]
    a.pop(2)#giving index value and removing
    print(a)

output: [10,50,13]

**remove** : It will value directly and remove the value.

Ex: 
   
    a=[10,50,3,13]
    a.remove(50)
    print(a)

output: [10,3,13]

**replace** : It replaces the value.

Ex: 

    a=[10,50,3,13]
    a[1]=5
    print(a)

output: [10,5,3,13]

**count** : used to count the values. 

Ex: 
    
    a=[1,2,4,5,1,3,19,30,1]
    print(a.count(1))

output: 3

**index** : used to find the index of a given value.

Ex: 

    a=[1,2,4,5,1,3,19,30,1]
    print(a.index(19))

output: 6

**clear** : It is used to clear the data from the variable but variable will be alive in the memory. 

Ex: 

    a=[1,2,4,5]
    a.clear()
    print(a)

output: []

**copy** : There are 2 types of copy techniques

- deep copy
-shallow copy

**deep copy** :

Ex:  
    
    a=[10,20,50]
    b=a
    print(a)
    print(b)

output: 

        [10,20,50]

        [10,20,50]

    print(id(a))
    print(id(a))

output:
        
        13363760886528
     
        13363760886528

**shallow copy** :

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

**reverse** : [::-1]

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

    a=(10,55.55,'data')

- user can pass anything inside the tuple like int | float | string | boolean.
- memory allocation, indexing, slicing, skipping are same as string and list only.

**Slicing** :

Ex:
    
    a=(10,4,17,9,21,36)
    print(a[2])

output: 17

**Slicing** :

Ex:
   
    a=(10,4,17,9,21,36)
    print(a[1:4])

output: (4,17,9)

**Skipping** :

Ex: 

    a=(10,4,17,9,21,36)
    print(a[::3])

output: (10,9)

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

output: 1

**index** : 

Ex: 

    a=(10,4,17,9,21,36)
    print(a.index(36))

output: 5
