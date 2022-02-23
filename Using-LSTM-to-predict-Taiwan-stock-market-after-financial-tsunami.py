#!/usr/bin/env python
# coding: utf-8

# In[1]:


#加入需運用的套件
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import LSTM
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime


get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


start = datetime.datetime(2009,1,1)
end = datetime.datetime(2020,12,31)
df_tw = web.DataReader("^TWII", "yahoo", start, end)
df_tw


# In[20]:


df_tw.drop(['Close', 'High', 'Low', 'Close', 'Volume','Adj Close'], axis=1, inplace=True)
df_tw.tail(10)


# In[21]:


#資料歸一化
scaler = MinMaxScaler(feature_range=(-1, 1))

#需將資料做reshape的動作，使其shape為(資料長度,1) 
x_set= df_tw.values.reshape(-1,1)
TW = scaler.fit_transform(x_set)
TW_df = pd.DataFrame(TW)


# In[22]:


split_point = int(len(TW_df)*0.9)
train = TW_df.iloc[:split_point].copy()
test = TW_df.iloc[split_point:-1].copy() #因為預測一天後的結果，最後一天預測並無解答，所以-1


# In[23]:


predict_days = 1
X_train = train[:-predict_days]
y_train = train[predict_days:]
X_test = test[:-predict_days]
y_test = test[predict_days:]


# In[24]:


X_train = X_train.values
y_train = y_train.values
X_test = X_test.values
y_test = y_test.values


# In[25]:


X_train = X_train.reshape((X_train.shape[0],1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0],1, X_test.shape[1]))
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)


# # Long Short-Term Memory 

# In[26]:


lstm_model = Sequential()
lstm_model.add(LSTM(units=400, return_sequences=False, input_shape=(X_train.shape[1],1)))
lstm_model.add(Dropout(0.2))
lstm_model.add(Dense(1))
lstm_model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='loss', patience=2, verbose=1)
history_lstm_model = lstm_model.fit(X_train, y_train, epochs=20, batch_size=1, verbose=1, shuffle=True, callbacks=[early_stop])


# In[27]:


y_train_pred_lstm = lstm_model.predict(X_train)
y_train_test_lstm = lstm_model.predict(X_test)
plt.figure(figsize=(10, 6))
plt.plot(y_test[:,0], label='TW_Open')
plt.plot(y_pred_test_lstm, label='LSTM')
plt.title("LSTM's Prediction")
plt.xlabel('Observation')
plt.ylabel('Open')
plt.legend()
plt.show();


# In[28]:


print("The R2 score on the Train set is:\t{:0.3f}".format(r2_score(y_train, y_train_pred_lstm)))
print("The R2 score on the Test set is:\t{:0.3f}".format(r2_score(y_test, y_pred_test_lstm)))


# # Artificial Neural Network

# In[47]:


nn_model = Sequential()
nn_model.add(Dense(400, input_dim=1, activation='relu'))
nn_model.add(Dropout(0.2))
nn_model.add(Dense(1))
nn_model.compile(loss='mean_squared_error', optimizer='adam')
early_stop = EarlyStopping(monitor='loss', patience=2, verbose=1)
history = nn_model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=1, callbacks=[early_stop], shuffle=False)


# In[48]:


y_train_pred_nn = nn_model.predict(X_train)
y_test_pred_nn = nn_model.predict(X_test)
plt.figure(figsize=(10, 6))
plt.plot(y_test, label='True')
plt.plot(y_pred_test_nn, label='NN')
plt.title("ANN's Prediction")
plt.xlabel('Observation')
plt.ylabel('Open Price')
plt.legend()
plt.show();


# In[49]:


print("The R2 score on the Train set is:\t{:0.3f}".format(r2_score(y_train, y_train_pred_nn)))
print("The R2 score on the Test set is:\t{:0.3f}".format(r2_score(y_test, y_pred_test_nn)))


# In[ ]:




