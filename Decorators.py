#!/usr/bin/env python
# coding: utf-8

# In[13]:


my_dict = {}
def outer(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        my_dict
        count += 1
        my_dict[fn.__name__] = count
        return fn(*args, **kwargs)
    return inner


# In[21]:


@outer
def add(a, b):
    my_dict[(a, b)] = a+b
    return a+b


# In[22]:


add(10,20)


# In[23]:


add(100,200)


# In[24]:


my_dict


# In[19]:


add(300,20000)


# In[ ]:




