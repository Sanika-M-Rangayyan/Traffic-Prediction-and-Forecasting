import streamlit as st

from predict import predict


def main():
    st.title("TRAFFIC PREDICTION")
    predict()
    
if __name__ == '__main__':
    main()
