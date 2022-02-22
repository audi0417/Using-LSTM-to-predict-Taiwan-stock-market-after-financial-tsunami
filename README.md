# Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami


## 摘要

被視為景氣領先指標(Leading indicator)之一的股價指數，容易受多方因素影響，公司營運、資金流向、市場消息、國際趨勢乃至於預期心理，金融危機的發生，更提升各國股市間的相關性，過多因素使得人工預測股市顯得困難，為了提升預測的效度以獲得更高的投資收益，利用人工智慧預測股市便成為目前金融科技發展的一大方向。
因此本研究旨在透過LSTM長短期記憶網路模型挖掘2007-2008金融海嘯事件後台灣股市市場隱藏趨勢，分析人力不易處理的股市動態影響因素與相互因果關係，剖析台股發行量加權股價指數之遞延效果及影響程度，並採用均方根誤差評比預測模型績效，與過去的人工神經網路比較其預測精準度，提升預測的精準度與投資者績效及獲利，作為投資者分散風險的參考。

關鍵詞：台股發行量加權指數、長期短期記憶網路、人工神經網路。


## Abstract

The stock price index, which is regarded as one of the leading indicators, is easily affected by many factors, including company operations, capital flows, market news, international trends and even psychological expectations, and the occurrence of the financial crisis has increased the correlation between stock markets in various countries. The use of artificial intelligence to predict the stock market has become a major direction in the development of financial technology.
Therefore, this study aims to explore the hidden trend of Taiwan stock market after the 2007-2008 financial tsunami by using LSTM. We analyze the dynamic factors and mutual causality of the stock market that cannot be easily handled by human, analyze the deferred effect and the degree of influence of the weighted stock price index of Taiwan stock issuance, and evaluate the performance of the prediction model by using root mean square error to compare with artificial neural network. The RMSE is used to compare the prediction accuracy with the past artificial neural network, to improve the prediction accuracy, investor performance and profitability, and as a reference for investors to diversify risk.

## 研究目的

一、透過 LSTM 模型進行金融海嘯後台股加權指數的深度學習與走勢預測
二、探究不同參數對台股加權指數預測模型的影響，調整並優化出最佳參數 組合
三、利用人工智慧尋找金融海嘯後台股加權指數之遞延效果及影響程度


## 研究流程

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/%E5%9C%96%E7%89%87%201.png)


## 研究方法
-開發語言：Python 3.6  
-演算法套件：Keras 2.2.0

旨在以長短期記憶網路模型(LSTM)建立長期趨勢分析模型進行預測;透過反覆測試、調整並優化模型參數，獲得最佳參數組合，提升 LSTM 預測結果之準確率。最後，分別透過 LSTM 與 ANN 比較我國股市加權指數長期趨勢之模型預測能力

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/1645531533168.jpg)


## 研究結果


-預測模型：ANN

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/1645531906204.jpg)

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/1645532921495.jpg)

-預測模型：LSTM

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/1645531916677.jpg)

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/1645532930756.jpg)

本研究針對兩種模型分別進行 5 次實驗，並取得平均準確值，從中可發現，本研究的建模有效提升 ANN 與 LSTM 的 R2 模型解釋度，而 LSTM 模型的 R2 平均解釋度大於 ANN 人工神經網路模型的平均解釋度，具有較優良的表現， 展現出 LSTM 模型穩定且精準度較高的特性。

![image](https://github.com/audi0417/Using-LSTM-to-predict-Taiwan-stock-market-after-financial-tsunami/blob/main/photo/1645533008492.jpg)


  
## Reference

1. Chimmula, V., & Zhang, L. (2020). Time series forecasting of COVID-19 transmission in Canada using LSTM networks. Chaos, solitons, and fractals, 135, 109864.  
2. Gurav, U. & Sidnal, N. (2018). Predict Stock Market Behavior: Role of Machine Learning Algorithms. 10.1007/978-981-10-7245-1_38.  
3. Lee, S.I.&Yoo, S.J. Multimodal deep learning for finance: integrating and forecasting international stock markets. J Supercomput 76, 8294–8312 (2020).  
4. Lien, D., Lee, G.,Yang, L. & Zhang, Y. (2018). "Volatility spillovers among the U.S. and Asian stock markets: A comparison between the periods of Asian currency crisis and subprime credit crisis," The North American Journal of Economics and Finance, Elsevier, vol. 46(C), pages 187-201.  
5. Mehtab, S., Dutta, A.& Sen, J. (2020). Robust Predictive Models for the Indian IT Sector Using Machine Learning and Deep Learning.  
6. Moghaddam, A.H., Moghaddam, M. H., & Esfandyari, M. (2016). Stock market index prediction using artificial neural network. Journal of Economics, Finance750and Administrative Science,21, 89–93.  
7. Moghar, A. & Hamiche, M. (2020). Stock Market Prediction Using LSTM Recurrent Neural Network. Procedia Computer Science. 170. 1168-1173. 10.1016/j.procs.2020.03.049.  
8. Selvin, S., Vinayakumar, R., Gopalakrishnan, E., Menon, V., & Soman, K.P. (2017). Stock price prediction using LSTM, RNN and CNN-sliding window model. 2017 International Conference on Advances in Computing, Communications and Informatics (ICACCI), 1643-1647.  
9. Wang,G.J., Xie, C. & Stanley, H.E. (2018).Correlation Structure and Evolution of World Stock Markets: Evidence from Pearson and Partial Correlation-Based       Networks. Comput Econ 51, 607–635.  


