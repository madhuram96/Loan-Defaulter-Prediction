#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import pickle
print ('Ran')


# In[2]:


app_train=pd.read_csv("C:\\Users\\DELL\\Desktop\\CDAC\\DBDA_Feb2019\\Project\\home-credit-default-risk\\application_train.csv")
app_test=pd.read_csv("C:\\Users\\DELL\\Desktop\\CDAC\\DBDA_Feb2019\\Project\\home-credit-default-risk\\application_test.csv")

print("Shape of training data: {}".format(app_train.shape))
print("Shape of test data: {}".format(app_test.shape))


# In[3]:


app_train.head()


# In[4]:



train_labels = app_train['TARGET']
train_sk_id_curr = app_train['SK_ID_CURR']
test_sk_id_curr = app_test['SK_ID_CURR']

app_train.drop('SK_ID_CURR', inplace=True, axis=1)
app_test.drop('SK_ID_CURR', inplace=True, axis=1)

app_train, app_test = app_train.align(app_test, join = 'inner', axis = 1)
print('Training Features shape: ', app_train.shape)
print('Testing Features shape: ', app_test.shape)


# In[5]:


cat_features = [f for f in app_train.columns if app_train[f].dtype == 'object']


# In[6]:


def column_index(df, query_cols):
    cols = df.columns.values
    sidx = np.argsort(cols)
    return sidx[np.searchsorted(cols, query_cols, sorter=sidx)]


# In[7]:


cat_features_inds = column_index(app_train, cat_features)    
print("Cat features are: %s" % [f for f in cat_features])
print(cat_features_inds)


# In[8]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
for col in cat_features:
    app_train[col] = le.fit_transform(app_train[col].astype(str))
    app_test[col] = le.fit_transform(app_test[col].astype(str))


# In[9]:


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy = 'median')
imputer.fit(app_train)
app_train = imputer.transform(app_train)
app_test = imputer.transform(app_test)


# In[10]:


app_train


# In[11]:


from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(app_train, train_labels, 
                                                    test_size = 0.3, 
                                        
                                                    stratify=train_labels)


# In[14]:


gaussian = GaussianNB()
gaussian.fit(X_train, y_train)


# In[40]:


y_pred = gaussian.predict(X_test)


# In[41]:


y_pred


# In[42]:


predictions=gaussian.predict(app_test)


# In[43]:


from sklearn.metrics import roc_curve, roc_auc_score


print('AUC:', roc_auc_score(y_test, gaussian.predict_proba(X_test)[:,1]))
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
y_pred = gaussian.predict(X_test)
print('Accuracy score ',accuracy_score(y_test, y_pred))


# In[37]:


y_pred_prob


# In[44]:


submission = pd.DataFrame({'SK_ID_CURR': test_sk_id_curr, 'TARGET': predictions})


# In[47]:


submission.head()


# In[49]:


submission.to_csv('C:\\Users\\DELL\\Desktop\\CDAC\\DBDA_Feb2019\\Project\\result_excel_file\\baseline_gaussian_imputed_median.csv', index = False)

