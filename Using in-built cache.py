#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functools import lru_cache


# In[10]:


@lru_cache(maxsize = 8)
def fact(n):
    print('calculation {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)


# In[ ]:





# In[ ]:





# In[ ]:




