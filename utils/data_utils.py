import pandas as pd
import streamlit as st

@st.cache_data
def data_loading():
    df = pd.read_csv("data/personality_dataset.csv")
    df.rename(columns={
        "Time_spent_Alone": "TimeSpentAlone",
        "Stage_fear": "StageFear",
        "Social_event_attendance": "SocialEventAttendance",
        "Going_outside": "GoingOutside",
        "Drained_after_socializing": "DrainedAfterSocializing",
        "Friends_circle_size": "FriendsCircleSize",
        "Post_frequency": "PostFrequency",
        "Personality": "Personality"
    }, inplace=True)
    df.dropna(inplace=True)
    return df
