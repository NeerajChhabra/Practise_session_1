#!/usr/bin/env python
# coding: utf-8

# In[2]:


cache ={1:1, 2:1}


# In[27]:


def outer(fn):
    def inner(n):
        if n not in cache:
            print('calculating {0}'.format(n))
            result = fn(n)
            cache[n] = result
            return result
        else:
            return cache[n]
    return inner
        
        


# In[28]:


@outer
def fib(n):
    if n > 2:
        
        return fib(n-1) + fib(n-2)
    else:
        return 1


# In[29]:


fib(1)


# In[30]:


fib(4)


# In[31]:


cache


# In[32]:


fib(100)


# In[33]:


cache


# In[34]:


fib(100)


# In[35]:


fib(99)


# In[ ]:




