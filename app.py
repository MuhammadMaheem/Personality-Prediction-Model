import streamlit as st
from core.personality import Personality

def main():
    st.title("Personality Predictor")
    st.markdown("Enter your details to check if you're an Introvert or an Extrovert")

    app = Personality()
    app.data_analysis()
    app.input_form()

if __name__ == "__main__":
    main()
