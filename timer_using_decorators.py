#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[7]:


def outer(fn):
    from time import perf_counter
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        total_time = perf_counter() - start
        print(total_time)
        return result
    return inner


# In[12]:


@outer
def add(a, b):
    return a + b


# In[18]:


add(10, 20)


# In[ ]:





# In[ ]:




