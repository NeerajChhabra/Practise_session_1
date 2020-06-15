#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fractions import Fraction


# In[6]:


Fraction.greater_than_one = lambda self: self.numerator >= self.denominator


# In[7]:


f1 = Fraction(10,20)


# In[8]:


f2 = Fraction(100,20)


# In[16]:


f1.greater_than_one()


# In[17]:


f2.greater_than_one()


# In[ ]:





# In[ ]:





# In[ ]:




