#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install gingerit


# In[4]:


from gingerit.gingerit import GingerIt
text = input("Enter a sentence >>: ")
corrected_text = GingerIt().parse(text)
print(corrected_text['result'])


# In[ ]:





# In[ ]:




