#!/usr/bin/env python
# coding: utf-8

# In[33]:


def timed(n):
    def dec(fn):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_time = 0
            for i in range(1,n+1):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_time += perf_counter() - start
            avg_time = total_time / n
            print(avg_time)
#             print('{0}, {1}'.format(total_time, n))
            return result
        return inner
    return dec
        


# In[34]:


@timed(100000)
def add(a, b):
    return a+b


# 

# In[ ]:





# In[ ]:




