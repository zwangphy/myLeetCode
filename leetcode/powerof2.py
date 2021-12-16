#!/usr/bin/env python
# coding: utf-8

# In[14]:


def isPower(n):
    if n == 1:
        return True
    
    else:
        while n > 1:
            if n%2 != 0:
                return False
            if n%2 == 0:
                n = n/2
            if n == 1:
                return True


# In[28]:


def isPowerRecursion(n):
    
    if n == 1:
        return True
    
    if n%2 != 0:
        return False
    
    return isPower(n/2)


# In[26]:


isPower(8)


# In[31]:


isPowerRecursion(8)


# In[ ]:




