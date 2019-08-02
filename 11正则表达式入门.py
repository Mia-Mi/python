# 正则表达式
'''
re  模块
 用于处理字符串的强大工具
 Python的re模块拥有全部的正则表达式的功能
 python中的正则表达式是一个特殊的字符序列，
 检查一个字符串是否与某种模式匹配
'''

# 元字符 ：
#  .   ^   $   *   +   ?   {}  []   \   |   ()

'''
大多数字母和字符会匹配它们自身，
有少数特殊字符我们称为元字符，
它们不能匹配自身，它们定义了字符类、
子组匹配和模式重复次数等
。
'''
#例子：
'''
>>> re.search('a','iweojrfasdsdfjdi')
<_sre.SRE_Match object; span=(7, 8), match='a'>
>>> re.search('as','iweojrfasdsdfjdi')
<_sre.SRE_Match object; span=(7, 9), match='as'>
>>> re.search('as','iweojrfasdsdasfjdi')
<_sre.SRE_Match object; span=(7, 9), match='as'>
>>> re.search('python','iweojrfasdsdasfjdi')
>>> re.search(r'd.g','x dog dxgsldjlsjdig')
<_sre.SRE_Match object; span=(2, 5), match='dog'>
>>> re.findall(r'd.g','x dog dxgsldjlsjdig')
['dog', 'dxg', 'dig']
>>> x = re.search(r'd.g','x dog dxgsldjlsjdig')
>>> x
<_sre.SRE_Match object; span=(2, 5), match='dog'>
>>> x.group()
'dog'
>>> 
'''
# 元字符的使用
'''
    .    匹配除换行符之外的所有的字符 
  \d  匹配0~9的数字   
  \s   匹配任意的空白符，包括空格，制表符(Tab)，换行符等
  \w 匹配字母或数字或下划线或汉字等  
  \b  表示单词的边界
  ^    脱字符，匹配输入字符串的开始的位置
    $   匹配输入字符串的结束位置
  解除元字符的特殊功能例
    \.   表示匹配点号本身
   \D、\S、\W、\B是与小写的相反的作用
'''
#例子：
'''
>>> re.search(r'^d.g','x dog dxgsldjlsjdig')
>>> re.search(r'^d.g','dog dxgsldjlsjdig')
<_sre.SRE_Match object; span=(0, 3), match='dog'>
>>> re.search(r'd.g$','dog dxgsldjlsjdig')
<_sre.SRE_Match object; span=(14, 17), match='dig'>
>>> re.search(r'd.g$','dog dxgsldjlsjdigxx')
>>> re.search(r'\d','dog d1xgsldjl2sjdigxx')
<_sre.SRE_Match object; span=(5, 6), match='1'>
>>> re.search(r'\d','dog d12xgsldjl2sjdigxx')
<_sre.SRE_Match object; span=(5, 6), match='1'>
>>> re.search(r'\d\d','dog d12xgsldjl2sjdigxx')
<_sre.SRE_Match object; span=(5, 7), match='12'>
>>> re.search(r'is','this is a list')
<_sre.SRE_Match object; span=(2, 4), match='is'>
>>> re.search(r'\bis\b','this is a list')
<_sre.SRE_Match object; span=(5, 7), match='is'>
>>> re.search(r'\Bis\B','this is a list')
<_sre.SRE_Match object; span=(11, 13), match='is'>
'''
# 匹配次数
'''
 {M,N}   M和N 为非负整数，其中M<=N 表示前面的匹配M~N次
 {M，}   表示需要匹配M次
 {，N}    等价于{0~N}
 {N}          表示需要匹配N次
 *      匹配前面的子表达式零次或多次，等价于{0，}
 +      匹配前面的子表达式一次或多次，等价于{1，} 
 ？   匹配前面的子表达式零次或一次，等价于{0,1}
注：*？、+？、{n,m}?  贪婪与懒惰

'''
#例子
'''
>>> re.search(r'\d','this is a 1list')
<_sre.SRE_Match object; span=(10, 11), match='1'>
>>> re.search(r'\d','this is a 12list')
<_sre.SRE_Match object; span=(10, 11), match='1'>
>>> re.search(r'\d{2}','this is a 12list')
<_sre.SRE_Match object; span=(10, 12), match='12'>
>>> re.search(r'\d{2}','this is a 123456789list')
<_sre.SRE_Match object; span=(10, 12), match='12'>
>>> re.search(r'\d{5,11}','this is a 123456789list')
<_sre.SRE_Match object; span=(10, 19), match='123456789'>
>>> re.search(r'\d{5,}','this 123is a 123456789list')
<_sre.SRE_Match object; span=(13, 22), match='123456789'>
>>> re.search(r'\d{,5}','this 123is a 123456789list')
<_sre.SRE_Match object; span=(0, 0), match=''>
>>> re.search(r'\s\d{,5}','this 123is a 123456789list')
<_sre.SRE_Match object; span=(4, 8), match=' 123'>
>>> re.search(r'\d{,5}is','this 123is a 123456789list')
<_sre.SRE_Match object; span=(2, 4), match='is'>
>>> re.search(r'a*b','xxxaaaaabxxx')
<_sre.SRE_Match object; span=(3, 9), match='aaaaab'>
>>> re.search(r'a+b','xxxaaaaabxxx')
<_sre.SRE_Match object; span=(3, 9), match='aaaaab'>
>>> re.search(r'a*b','xxxbaaaaabxxx')
<_sre.SRE_Match object; span=(3, 4), match='b'>
>>> re.search(r'a+b','xxxbaaaaabxxx')
<_sre.SRE_Match object; span=(4, 10), match='aaaaab'>
>>> re.search(r'a.+b','xxxaabaaaaabxxx')
<_sre.SRE_Match object; span=(3, 12), match='aabaaaaab'>
>>> re.search(r'a.+?b','xxxaabaaaaabxxx')
<_sre.SRE_Match object; span=(3, 6), match='aab'>
>>> re.search(r'a.*?b','xxxaabaaaaabxxx')
<_sre.SRE_Match object; span=(3, 6), match='aab'>
>>> re.search(r'a.*b','xxxaabaaaaabxxx')
<_sre.SRE_Match object; span=(3, 12), match='aabaaaaab'>
>>> 
'''
# 子组匹配
'''
 [ ]   字符类，将要匹配的一类字符集放在[]里面
 例如:
 [ . ? * ( ) {} ]     匹配里面的这些符号
 [0-9]                 匹配0到9的数字相当于\d
 [^\d]                  匹配除数字以外的字符，相当于\D
 [a-z]                  匹配所有的小写字母
 [^a-z]                 匹配非小写字母
    |                       相当于或（or）分支条件
例如：
 A | B                 匹配字母A或者B 与[AB]是一样的
'''
# 例子：
'''
>>> re.search(r'[0-9]{2}','xxbxa12bababaaaabxxx')
<_sre.SRE_Match object; span=(5, 7), match='12'>
>>> re.search(r'[a-d]{2}','xxbxa12bababaaaabxxx')
<_sre.SRE_Match object; span=(7, 9), match='ba'>
>>> re.search(r'b[aeiou]a','xxbea12boabiabaxaaabxxx')
<_sre.SRE_Match object; span=(2, 5), match='bea'>
>>> re.findall(r'b[aeiou]a','xxbea12boabiabaxaaabxxx')
['bea', 'boa', 'bia']
>>> re.findall(r'[1-5]{2}b','xxbea12boabiabaxaaabxxx')
['12b']
>>> 
'''


# 分组
'''
 ()  分组，将要匹配的一类字符集放在()组成一个小组 
例如:
 (\d){3} 匹配一个三位数
 a(bc)*匹配一个a和0个或多个bc
 a(b|c) 匹配ab或者ac
'''
# re模块
'''
re.compile() 编译正则表达式为模式对象
re模块的常用方法
match()
判断一个正则表达式是否从开始处匹配字符串
search()   遍历字符串，找到正则表达式匹配的第一个位置
findall()     遍历字符串，找到正则表达式匹配的所有位置并
以列表的形式返回
查看匹配对象中的信息
group() 返回匹配到的字符串
star()返回匹配的开始位置
end()返回匹配的结束位置
span()  返回一个元组表示匹配位置（开始，结束）
'''
# 例子
'''
>>> m = re.search(r'http.+\.gif','http://jfdjsfijsdoifjsdaf.gif sdf http://sdfjjfoirew.gif')
>>> m.group()
'http://jfdjsfijsdoifjsdaf.gif sdf http://sdfjjfoirew.gif'
>>> m = re.search(r'http.+?\.gif','http://jfdjsfijsdoifjsdaf.gif sdf http://sdfjjfoirew.gif')
>>> m.group()
'http://jfdjsfijsdoifjsdaf.gif'
>>> m = re.findall(r'http.+?\.gif','http://jfdjsfijsdoifjsdaf.gif sdf http://sdfjjfoirew.gif')
>>> m
['http://jfdjsfijsdoifjsdaf.gif', 'http://sdfjjfoirew.gif']
>>> m = re.findall(r'http.+\.gif','http://jfdjsfijsdoifjsdaf.gif sdf http://sdfjjfoirew.gif')
>>> m
['http://jfdjsfijsdoifjsdaf.gif sdf http://sdfjjfoirew.gif']
'''

















