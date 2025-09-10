import pandas as pd
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
        self.model = train_load_and_save_model(
            self.df, self.model_path, self.selected_features)

    def predict(self, input_data: dict):
        """Predict personality from input dictionary"""
        input_df = pd.DataFrame([input_data])
        prediction = self.model.predict(input_df)[0]
        return prediction
