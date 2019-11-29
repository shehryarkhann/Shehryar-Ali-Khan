#!/usr/bin/env python
# coding: utf-8

# In[1]:


a='shehryar khattar'
dir(a)


# In[2]:


a = "Shehryar khattar"
print(a.upper())
print(a)


# In[3]:


name ='Shehryar khattar'
print(name)
print(name.capitalize()) #Only capitalize 1 character of string


# In[4]:


name='Shehryar khattar'
print(name.center(30)) #taking space of 40 character and pring name in the middle


# In[5]:


name='Shehryar khattar'
print(name.count('a')) #print total number of a character like 'a'


# In[6]:


name='Shehryar khattar'
print(name.encode()) #encode the string


# In[7]:


name='Shehryar khattar'
print(name.endswith('l')) #compare with end character of string and reture true or false


# In[8]:


name ='S\shehryar khattar'
print(name.expandtabs(4)) #space between the character


# In[9]:


name='Shehryar khattar'
print(name.find('t')) #return the index of find character


# In[12]:


name='My Name is {fname} {lname}'
print(name.format(fname='Muhammad ',lname='Shehryar khattar')) #Insert the fname and lname inside the placeholder{}, the fname and lname should be in fixed point


# In[13]:


name={'fname':'Muhammad iqbal', 'lname':'Shehryar khattar'}
print('{fname} {lname}'.format_map(name))


# In[14]:


name={'fname':'Muhammad', 'lname':'Shehryar khan'}
print('{fname} {lname}'.format_map(name))


# In[15]:


name='Shehryar khan' 
print(name.index('y'))  #return the index of specific character


# In[17]:


name='Shehryar998' 
print(name.isalnum()) #return if string is alphanumeic or not e.g character and number


# In[18]:


name='Shehryar khan' 
print(name.isascii())


# In[19]:


name='Shehryar khan' 
print(name.isdecimal()) #return if string have any decimal value


# In[20]:


name='Shehryar Kahn' 
print(name.isdigit()) #return if string have any digits


# In[21]:


name='Shehryar khan' 
print(name.isidentifier()) #return true or false if string have some identifier like start with _,or no space between word


# In[22]:


name='ShehryarKhan' 
print(name.isidentifier()) #return true or false if string have some identifier like start with _,or no space between word


# In[23]:


name='Shehryar kahn'
print(name.islower()) #return true or false if string have all characters are lower case'


# In[24]:


name='shehryar khan'
print(name.islower()) #return true or false if string have all characters are lower case'


# In[25]:


name='shehryar Khan'
print(name.isnumeric())
number='25'
print(number.isnumeric()) #return true or false if string have all characters are numeric


# In[26]:


name='Shehryar Kahn'
print(name.isprintable()) #return true or false if string have all characters are printable


# In[27]:


name='Shehryar khattar'
print(name.isspace())
name='  '
print(name.isspace())  #returns True if all the characters in a string are whitespaces, otherwise False


# In[30]:


name='Shehryar Khattar'
print(name.istitle()) #return true or false if each word start with an upper case letter


# In[31]:


name='shehryar khattar'
print(name.isupper())
name='SHEHRYAR KHATTAR'
print(name.isupper())  #return true or false if whole string will have upper case letter


# In[35]:


name={'Shehyar','Khattar'}
print('  '.join(name)) #method takes all items in an iterable and joins them into one string.A string must be specified as the separator.name='Kayani '


# In[36]:


name='Khattar '
name1=name.ljust(30)
print(name1,"Shehryar khan")  #return 20 character space from left justified


# In[37]:


name='ShehRyaR KHattAr'
print(name.lower())  #return all character in lower case


# In[38]:


name=' Shehryar khan '
print(name)
name=' Shehryar khattar   '
print(name.lstrip())   #remove space for letf side


# In[39]:


name='Shehryar Khattar'
print(name.partition('Shehryar khan'))  #return a tuple


# In[40]:


name='Shehryar khattar'
print(name.replace('Shehryar','sherri'))  #replace the word to another word


# In[41]:


name='Shehrya khattar'
print(name.rfind('t')) #return the index almost rindex(),if value not found return -1


# In[42]:


name='Shehryar khattar'
print(name.rindex('a')) #return the index almost rindex(),if value not found return error


# In[43]:


name='Shehryar khattar'
print(name.rjust(40)) #return a justified version of string


# In[44]:


name='Shehryar khattar'
print(name.rpartition('Khan'))


# In[45]:


name='Shehryar khattar'
print(name.rsplit()) #return in list


# In[46]:


name='Shehryar khattar'
print(name.rstrip())


# In[47]:


name='Shehryar khattar'
print(name.split())


# In[48]:


name='Shehryar khattar'
print(name.splitlines()) #return a single work list


# In[50]:


name='Shehryar Khattar'
print(name.startswith('t'))
name='Muhammad iqbal khan'
print(name.startswith('M')) #return true or false if the given character are starting character of whole string


# In[51]:


name='Shehryar Khattar'
print(name.startswith('t'))
name='Muhammad iqbal khan'
print(name.startswith('i')) #return true or false if the given character are starting character of whole string


# In[52]:


name='Shehryar Khattar'
print(name.startswith('S'))
name='Muhammad iqbal khan'
print(name.startswith('M')) #return true or false if the given character are starting character of whole string


# In[53]:


name='Shehryar khattar'
print(name.strip())


# In[54]:


name='Shehryar khattar'
print(name.swapcase())  #return first character of every work in lower and other whole string will be UPPER case


# In[55]:


help(str)


# In[59]:


string= 'abcd'
paper1= {"a":"68","b":"56"}
t= string.maketrans(paper1)
t


# In[61]:


ord("a")


# In[62]:


string= "hello world"
paper1= {"a":"1","b":"2","c":"3","d":"4"}
table= string.maketrans(paper1)
table


# In[63]:


chr(99)


# In[64]:


string="hello world"
dic1="abcde"
dic2="12345"
t= string.maketrans(dic1,dic2)
t


# In[65]:


chr(101)


# In[69]:


string="hello World"
dic1="abcde"
dic2="12345"
dic3="@#$%"
t= string.maketrans(dic1,dic2,dic3)
t


# In[70]:


string.translate(t)


# In[71]:


name='Shehryar Khan'
print(name.title()) #convert the first character of every word in UPPER Case


# In[72]:


name='Shehryar Khattar'
print(name.upper()) #return the whole string in upper case


# In[73]:


name= 'Shehryar Khattar'
print(name.zfill(0))  #add zero ofter the total character of string with include space


# In[74]:


name='shehryar khattar'
print(name.zfill(50)) #add zero ofter the total character of string with include space


# In[ ]:




