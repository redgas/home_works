#!/usr/bin/env python

# coding: utf-8

# In[55]:


import re 

pattern = '.*/[0-9]{8}'
prog = re.compile(pattern)


# In[56]:


new_list = []
import collections
with open ('URLs.txt' , 'r') as str:
    for line in str:
        line = line.strip()
        if prog.match(line):
            line = line.split('/')
            new_list.append(line[1])
print (collections.Counter(new_list))      


# In[ ]:




