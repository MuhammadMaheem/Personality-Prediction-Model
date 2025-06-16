import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from models.train_model import train_load_and_save_model
from utils.data_utils import data_loading


class Personality:
    def __init__(self):
        self.model_path = "Personality.pkl"
        self.selected_features = [
            "TimeSpentAlone", "StageFear", "SocialEventAttendance",
            "GoingOutside", "DrainedAfterSocializing",
            "FriendsCircleSize", "PostFrequency"
        ]
        self.df = data_loading()
        self.model = train_load_and_save_model(self.df, self.model_path, self.selected_features)

    def data_analysis(self):
        st.sidebar.header("Understanding the Data")
        if st.sidebar.checkbox("Show the Data Table"):
            st.header("Show Data Table")
            st.dataframe(self.df.head())

        if st.sidebar.checkbox("Show Correlation Heatmap"):
            st.subheader("Correlation Heatmap")
            plt.figure(figsize=(26, 22))
            sns.heatmap(self.df.select_dtypes(include=[np.number]).corr(), annot=True, cmap="coolwarm")
            st.pyplot(plt.gcf())
            plt.clf()

        if st.sidebar.checkbox("Show Pair Plot"):
            st.header("Pair Plot")
            pair_df = self.df[["TimeSpentAlone", "SocialEventAttendance", "FriendsCircleSize", "Personality"]]
            sns.pairplot(pair_df, hue="Personality")
            st.pyplot(plt.gcf())
            plt.clf()

        if st.sidebar.checkbox("Show Class Distribution"):
            st.subheader("Personality Distribution")
            sns.countplot(x="Personality", data=self.df)
            st.pyplot(plt.gcf())
            plt.clf()

    def input_form(self):
        st.header("Input Values")
        st.write("Answer the questions below to find out your personality")
        with st.form("Input form"):
            time_spent_alone = st.slider("Time Spent alone (Hours/Day)", 0.0, 11.0, 0.0, step=0.5)
            stage_fear = st.selectbox("Do you have Stage Fear?", ["Yes", "No"])
            social_event_attendance = st.slider("Social Event Attendance (Events/Month)", 0, 10, 0)
            going_outside = st.slider("Do you like to go outside? (1 = Not at all, 10 = Love it)", 1, 10, 0)
            drained_after_socializing = st.selectbox("Do you feel drained after socializing?", ["Yes", "No"])
            friends_circle = st.slider("How many friends do you have?", 0, 15, 0)
            post_frequency = st.slider("Social Media Post Frequency (Posts/Month)", 0, 10, 0)

            submitted = st.form_submit_button("Predict Personality")

            if submitted:
                input_data = {
                    "TimeSpentAlone": time_spent_alone,
                    "StageFear": 1 if stage_fear == "Yes" else 0,
                    "SocialEventAttendance": social_event_attendance,
                    "GoingOutside": going_outside,
                    "DrainedAfterSocializing": 1 if drained_after_socializing == "Yes" else 0,
                    "FriendsCircleSize": friends_circle,
                    "PostFrequency": post_frequency
                }

                input_df = pd.DataFrame([input_data])
                prediction = self.model.predict(input_df)[0]
                st.success(f"Your Personality is: {prediction}")
                

