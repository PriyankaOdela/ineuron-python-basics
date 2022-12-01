#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
* 
'hello'
-87.8
- 
()


6 


Values : 'hello',-87.8,6
Expressions :*,-,/


# In[ ]:


get_ipython().set_next_input('2. What is the difference between string and variable');get_ipython().run_line_magic('pinfo', 'variable')

String : A string is a sequence of characters enclosed in a single('') or double(" ") quotes.

Variable : A variable is a label for storing values and accessing when needed.


# In[ ]:


3. Describe three different data types.

The most common data types used in python for numbers -INTEGER,FLOAT and for words we use STRING.

#integer - 12
#float - 23.45
#string - "Fred" or 'Fred' or '23'

Precisely in Python,type() is used for getting type of the object.

Integers can positive or negative numbers.
 Ex : -4,-3,3,4,0

Floats are real numbers but also includes decimals.
 Ex : 2.3344,3.145
 
String is a sequence of characters enclosed in ' ' or " " but not the mixed ' ".
 Ex : "Fred"
 
Boolean - Boolean is one of the most used data type.It can take only one of two values either True or False.

 


# In[ ]:


get_ipython().set_next_input('4. What is an expression made up of? What do all expressions do');get_ipython().run_line_magic('pinfo', 'do')

An expression is made of operations like simple arithemetic operations(+,-,*,/).
 Ex : 4+3+2+1,4-3,5*6

An expression evaluates the task given.


# In[ ]:


get_ipython().set_next_input('5. This assignment statements, like spam = 10. What is the difference between an expression and a statement');get_ipython().run_line_magic('pinfo', 'statement')

A statement is a complete line of code that performs some action, while an expression is any section of the code that evaluates to a value.

Ex for expression :
min(2,3)
'Foo'
2+3+4
2*3

Ex for statement:
print()
if condition:
for value in variable:


# In[ ]:


get_ipython().set_next_input('6. After running the following code, what does the variable bacon contain');get_ipython().run_line_magic('pinfo', 'contain')
bacon = 22
bacon + 1


23


# In[ ]:


get_ipython().set_next_input('7. What should the values of the following two terms be');get_ipython().run_line_magic('pinfo', 'be')
'spam' + 'spamspam'
'spam' * 3


'spamspamspam'


# In[ ]:


get_ipython().set_next_input('8. Why is eggs a valid variable name while 100 is invalid');get_ipython().run_line_magic('pinfo', 'invalid')

Variable name should start with letter or an underscore.
So 'eggs' is valid variable name while 100 isn't.
The first letter of variable name must be alphabet or underscore.

