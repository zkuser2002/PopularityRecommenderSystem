#!/usr/bin/env python
# coding: utf-8

# In[18]:


#import libraries
import pandas as pd
import numpy as np
frame=pd.read_csv('rating_final.csv')
cuisine=pd.read_csv('chefmozcuisine.csv')
frame.head()

cuisine.head()


# In[7]:


#Recommendation based on counts
rating_count=pd.DataFrame(frame.groupby('placeID')['rating'].count())
rating_count.sort_values('rating',ascending=False).head()


# In[10]:


most_rated_places=pd.DataFrame([135085,132825,135032,135052,132834],index=np.arange(5),columns=['placeID'])
summery=pd.merge(most_rated_places,cuisine,on='placeID')
summery


# In[11]:


cuisine['Rcuisine'].describe()


# In[ ]:




