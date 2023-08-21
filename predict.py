import streamlit as st
from model_rf import predict_result
from model_svm import predict_result_svm
def predict():
	col1,col2=st.columns(2)
	with col1:
		CodedDay=st.text_input("Coded day")
		Zone=st.text_input("Zone")
	with col2:
		Weather =st.text_input("Weather")
		Temperature=st.text_input("Temp")
	if st.button("Predict from Random Forest"):
		p=predict_result(CodedDay,Zone,Weather,Temperature)
		st.success(str(p))
	if st.button("Predict from SVM"):
		p=predict_result_svm(CodedDay,Zone,Weather,Temperature)
		st.success(str(p))
    

