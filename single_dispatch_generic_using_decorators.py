#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


def singleDispatch(fn):
    registry ={}
    registry[object] = fn
    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    def registry_entry(type_):
        def inner(fn):
            registry[type_] = fn

            return fn
        return inner
    decorated.register = registry_entry
    return decorated


# In[2]:


@singleDispatch
def formatting(s):
    print('it is a string', s)


# In[3]:


formatting('hello')


# In[4]:


@formatting.register(int)
def its_int(a):
    print(' it is an int :', a)


# In[6]:


formatting(100
          )


# In[ ]:




