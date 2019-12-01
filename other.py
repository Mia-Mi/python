Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> print("wewre")
wewre
>>> a =10
>>> a*3
30
>>> c=b
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c=b
NameError: name 'b' is not defined
>>> b=a*3
>>> c=b
>>> print(c)
30
>>> a=20
>>> print(c)
30
>>> pint(b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pint(b)
NameError: name 'pint' is not defined
>>> print(b)
30
>>> print(a)
20
>>> print(b)
30
>>> print(c)
30
>>> b=a
>>> print(b)
20
>>> print(a)
20
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>>  import cmath
SyntaxError: unexpected indent
>>>  import cmath
SyntaxError: unexpected indent
>>> cos(5)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    cos(5)
NameError: name 'cos' is not defined
>>> s=list[]
SyntaxError: invalid syntax
>>> s=[1,2,3]
>>> s.apeend(4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.apeend(4)
AttributeError: 'list' object has no attribute 'apeend'
>>> s.append(4)
>>> a
20
>>> s
[1, 2, 3, 4]
>>> s[3]
4
>>> s.append["asd","sadsa","sadsad"]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.append["asd","sadsa","sadsad"]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> s[4]=2
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s[4]=2
IndexError: list assignment index out of range
>>> s(4)=2
SyntaxError: can't assign to function call
>>> s.append("sd")
>>> s
[1, 2, 3, 4, 'sd']
>>> s(2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s(2)
TypeError: 'list' object is not callable
>>> s[2】
      
SyntaxError: invalid character in identifier
>>> s[2]
      
3
>>> s[2]=345
      
>>> s
      
[1, 2, 345, 4, 'sd']
>>> s.remove(2)
      
>>> s
      
[1, 345, 4, 'sd']
>>> s.pop()
      
'sd'
>>> s
      
[1, 345, 4]
>>> s.pop()
      
4
>>> s
      
[1, 345]
>>> s.pop()
      
345
>>> s.pop()
      
1
>>> s.pop()
      
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.pop()
IndexError: pop from empty list
>>> s.append("是多少啊")
      
>>> s
      
['是多少啊']
>>> s
      
['是多少啊']
>>> s[1]
      
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    s[1]
IndexError: list index out of range
>>> s[0]
      
'是多少啊'
>>> s.append("是多少啊")
      
>>> s.append("是多少啊")
      
>>> s
      
['是多少啊', '是多少啊', '是多少啊']
>>> s.append("是多少啊")
      
>>> s
      
['是多少啊', '是多少啊', '是多少啊', '是多少啊']
>>> s.append("sadsadsadsadadsa")
      
>>> s
      
['是多少啊', '是多少啊', '是多少啊', '是多少啊', 'sadsadsadsadadsa']
>>> append(1)
      
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    append(1)
NameError: name 'append' is not defined
>>> s.append(1,2)
      
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    s.append(1,2)
TypeError: append() takes exactly one argument (2 given)
>>> s.append(1)
      
>>> s.append(2）
	     
SyntaxError: invalid character in identifier
>>> s.append(2)
	     
>>> s
	     
['是多少啊', '是多少啊', '是多少啊', '是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s[2]=1
	     
>>> s
	     
['是多少啊', '是多少啊', 1, '是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s(2)
	     
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    s(2)
TypeError: 'list' object is not callable
>>> s[2]
	     
1
>>> 
	     
>>> s[1:4]
	     
['是多少啊', 1, '是多少啊']
>>> s.remove[4]
	     
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    s.remove[4]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> s
	     
['是多少啊', '是多少啊', 1, '是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s.remove(1)
	     
>>> s
	     
['是多少啊', '是多少啊', '是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s
	     
['是多少啊', '是多少啊', '是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s.remove(0)
	     
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s.remove(0)
ValueError: list.remove(x): x not in list
>>> s.remove(s[0])
	     
>>> s
	     
['是多少啊', '是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s.remove('是多少啊')
	     
>>> s
	     
['是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> s
	     
['是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> type(s)
	     
<class 'list'>
>>> d={}
	     
>>> type()type(s)
	     
SyntaxError: invalid syntax
>>> type(d)
	     
<class 'dict'>
>>> d={name:luopeng,age:18}
	     
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    d={name:luopeng,age:18}
NameError: name 'name' is not defined
>>> {'name':luopeng,'age':18}
	     
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    {'name':luopeng,'age':18}
NameError: name 'luopeng' is not defined
>>>  d={"name":"luopeng","age":18}
	     
SyntaxError: unexpected indent
>>> d={name:"luopeng",age:18}
	     
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d={name:"luopeng",age:18}
NameError: name 'name' is not defined
>>> s
	     
['是多少啊', 'sadsadsadsadadsa', 1, 2]
>>> ={"name":"luopeng","age":18}
	     
SyntaxError: invalid syntax
>>> d=={"name":"luopeng","age":18}
	     
False
>>> d={"name":"luopeng","age":18}
	     
>>> d
	     
{'name': 'luopeng', 'age': 18}
>>> d[name]=luopeng1
	     
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    d[name]=luopeng1
NameError: name 'luopeng1' is not defined
>>>  d[name]="luopeng1"
	     
SyntaxError: unexpected indent
>>> d["name"]="luopeng1"
	     
>>> d
	     
{'name': 'luopeng1', 'age': 18}
>>> d["age"]=21
	     
>>> d
	     
{'name': 'luopeng1', 'age': 21}
>>> d.pop("age")
	     
21
>>> d
	     
{'name': 'luopeng1'}
>>> d["age"]=31
	     
>>> d
	     
{'name': 'luopeng1', 'age': 31}
>>> d["age"]=34
	     
>>> d
	     
{'name': 'luopeng1', 'age': 34}
>>> d["age1"]=21
	     
>>> d
	     
{'name': 'luopeng1', 'age': 34, 'age1': 21}
>>> d["name1']="luopeng1"
      
SyntaxError: invalid syntax
>>> d["name1"]="luopeng1"
      
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1'}
>>> d[""]="luo asdsa"
      
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'luo asdsa'}
>>> d[""]="luo asdsadfds"
      
>>> d[" "]="luo asdsadfds"
      
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'luo asdsadfds', ' ': 'luo asdsadfds'}
>>> d["  "]="luo asdsadfds"
      
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'luo asdsadfds', ' ': 'luo asdsadfds', '  ': 'luo asdsadfds'}
>>> d[]
      
SyntaxError: invalid syntax
>>> d[""]
      
'luo asdsadfds'
>>> d[" "]
      
'luo asdsadfds'
>>> d[" "]='luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds'
      
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'luo asdsadfds', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'luo asdsadfds', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> 
      
>>> d1=d
      
>>> d1
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'luo asdsadfds', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> d[""]="yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
      
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> d1
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> d1[""]="zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
      
>>> d1
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> d
      
{'name': 'luopeng1', 'age': 34, 'age1': 21, 'name1': 'luopeng1', '': 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', ' ': 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', '  ': 'luo asdsadfds'}
>>> d.keys()
      
dict_keys(['name', 'age', 'age1', 'name1', '', ' ', '  '])
>>> d.values()
      
dict_values(['luopeng1', 34, 21, 'luopeng1', 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz', 'luozzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz asdsadfds', 'luo asdsadfds'])
>>> s={1,2,3}
      
>>> type(s)
      
<class 'set'>
>>> type（d1)
	     
SyntaxError: invalid character in identifier
>>> type(d1)
	     
<class 'dict'>
>>> set1={"zhaosi","guangkun","dajiao","liuneng"}
	     
>>> set2={"zhaosi1","guangkun","dajiao1","liuneng"}
	     
>>> set1&set2
	     
{'liuneng', 'guangkun'}
>>> set1|set2
	     
{'guangkun', 'dajiao1', 'dajiao', 'liuneng', 'zhaosi1', 'zhaosi'}
>>> list1=[1,2,3,4,5,6,7,8,9,0,1,22]
	     
>>> setnew=set(list1)
	     
>>> setnew
	     
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22}
>>> listtwo=list(setnew)
	     
>>> listtwo
	     
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22]
>>> set1&set2|set2
	     
{'guangkun', 'dajiao1', 'liuneng', 'zhaosi1'}
>>> set1&set2|set2&set1
	     
{'liuneng', 'guangkun'}
>>> tuple1=(1,"dsfds","dsfds")
	     
>>> type(tuple)
	     
<class 'type'>
>>> type(tuple1)
	     
<class 'tuple'>
>>> tuple1(1)
	     
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    tuple1(1)
TypeError: 'tuple' object is not callable
>>> tuple[1]
	     
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    tuple[1]
TypeError: 'type' object is not subscriptable
>>> tuple1[1]
	     
'dsfds'
>>> tuple2=(1)
	     
>>> type(tuple2)
	     
<class 'int'>
>>> sssss=inout("dsadsadadas")
	     
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    sssss=inout("dsadsadadas")
NameError: name 'inout' is not defined
>>>  sssss=input("sfddssdfsd")
	     
SyntaxError: unexpected indent
>>> ssss=input("sdfdsfdsfss")
	     
sdfdsfdsfssf
>>> inta=input("input a")
	     
input a6
>>> intb=input(" input b")
	     
 input b8
>>> print(inta+intb)
	     
68
>>> s=-1
	     
>>> s
	     
-1
>>> s*s
	     
1
>>> str(10)
	     
'10'
>>> type(str(10))
	     
<class 'str'>
>>> g=type(str(10))
	     
>>> g
	     
<class 'str'>
>>> print g
	     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(g)?
>>> print(g)
	     
<class 'str'>
>>> print(g,"")
	     
<class 'str'> 
>>> g=str（100）
	     
SyntaxError: invalid character in identifier
>>> g=str(100)
	     
>>> g
	     
'100'
>>> fuhao=-1
	     
>>> power(fuhao,2)
	     
Traceback (most recent call last):
  File "<pyshell#182>", line 1, in <module>
    power(fuhao,2)
NameError: name 'power' is not defined
>>> import math
	     
>>> power(fuhao,2)
	     
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    power(fuhao,2)
NameError: name 'power' is not defined
>>> pow(fuhao,2)
	     
1
>>> pow(fuhao,3)
	     
-1
>>> (-1)*1*pow(-1,1)
	     
1
>>> 1+(-1）*3*pow(-1,(3-2))
       
SyntaxError: invalid character in identifier
>>> 1+（-1)*3*pow(-1,(3-2))
	     
SyntaxError: invalid character in identifier
>>> 1+(-1)*3*pow(-1,3)
	     
4
>>> 2**3
	     
8
>>> 10//4
	     
2
>>> 10/4
	     
2.5
>>> (10) % 2
	     
0
>>> （10） %4
	     
SyntaxError: invalid character in identifier
>>> (10)  %  4
	     
2
>>> "123" in ("asdsada12345")
	     
True
>>> "123" in ("asdsada12")
	     
False
>>> 


>>> s2=("1","2","3")
	
>>> s2=("1","2","3","4","5")
	
>>> "&".join(s2)
	
'1&2&3&4&5'
>>> s2=("1","2","3","4',"6")
	
SyntaxError: invalid syntax
>>> s2=("1","2","3","4',"")
	
SyntaxError: EOL while scanning string literal
>>> s2=("1","2","3","4","5","6")
	
>>> s3={1,2,3,4,5,6,7,8,9}
	
>>> "&".join(s3)
	
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    "&".join(s3)
TypeError: sequence item 0: expected str instance, int found
>>> s4=(1,2,3,4,5,6,7,8,9)
	
>>> "&".join(s4)
	
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    "&".join(s4)
TypeError: sequence item 0: expected str instance, int found
>>> s5=[1,2,3,4,5,6,7,8,9]
	
>>> "&".join(s5)
	
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    "&".join(s5)
TypeError: sequence item 0: expected str instance, int found
>>> s6=("1","2","3","4","5","6")
	
>>> "&".join(s6)
	
'1&2&3&4&5&6'
>>> 
