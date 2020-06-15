#!/usr/bin/env python
# coding: utf-8

# In[7]:


class calc:
    def __init__(self):
        self.count = 0
        
    def __call__(self, fun ):
        def inner(*args, **kwargs):
            self.count += 1
            print(self.count)
            return fun(*args, **kwargs)
        return inner
        


# In[8]:


@calc()
def add(a, b):
    return a+b


# In[10]:


add(10,20)


# In[ ]:




