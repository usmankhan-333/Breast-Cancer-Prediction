import streamlit as st
import joblib as jb
import numpy as np
model = jb.load('model.pkl')
st.title('Breast Cancer Predict Model')
st.image('Breast.jpeg')
x=input_text = (-0.23717436, 0.97747327, -0.9703657, 0.95153273, 0.84817356,
              0.19600497, 0.23049103, 0.12410924, 0.82197482, -0.26217937,
              -0.17589656, 0.70102346, -0.7025513, 0.86844184, 0.4456708,
              -0.44607383, 0.25258133, 0.03881402, 0.26181173, -0.16213617,
              -0.0281802, 0.78545873, -0.99294417, 0.83379043, 0.61725382,
              -0.26161682, 0.18378643, -0.12284186, 0.48146709, -0.23623611,
              -0.26238354)
#x=st.number_input('INPUT DATA')
st.write('Prediction Input Data:',x)
if st.button('Predict'):
    np_df=np.asarray(x)
    prediction = model.predict(np_df.reshape(1, -1))
    if prediction[0]==1:
        st.write('CANCER...')
    else:
        st.write('Not Cancer')