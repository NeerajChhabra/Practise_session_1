#!/usr/bin/env python
# coding: utf-8

# In[2]:


from functools import singledispatch


# In[9]:


@singledispatch
def htmll_int(arg):
    print('this is an int', arg)


# In[10]:


htmll_int(10)


# In[ ]:





# In[14]:


@singledispatch
def htmlize(arg):
    return(arg)


# In[18]:


@htmlize.register(int)
def html_int(arg):
    print('int', arg)


# In[19]:


htmlize(10)


# In[22]:


@htmlize.register(str)
def html_str(arg):
    print('string', arg)


# In[23]:


htmlize('abr')


# In[ ]:




