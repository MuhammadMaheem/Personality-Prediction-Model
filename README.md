# Personality-Prediction-Model
 Predicting if  a person is introvert of an extrovert


# 🧠 Personality Prediction App Using Machine Learning (OOP-Based)

This project is a machine learning-powered web application that predicts a user's personality (Introvert or Extrovert) based on their social behavior, using a Support Vector Machine (SVM) classifier and the Streamlit framework. The app also provides interactive data analysis and visualizations.

---

## 📌 Features

- Predicts personality as **Introvert** or **Extrovert**
- Interactive **data visualization** (heatmaps, pairplots, class distribution)
- Built using **OOP principles** for maintainability and scalability
- Developed with **Streamlit** for a modern and fast web interface
- Uses **SVM (Support Vector Machine)** for classification
- Caches data and model for fast user experience
- Simple form-based input for real-time prediction

---

## 📁 Dataset Used

The dataset is named `personality_dataset.csv` and contains social behavior metrics like:

- Time spent alone
- Stage fear (Yes/No)
- Social event attendance
- Enjoyment of going outside
- Drained after socializing (Yes/No)
- Friend circle size
- Social media post frequency
- Personality (Label)

---

## ⚙️ Technologies Used

| Category             | Tools/Technologies                                      |
|----------------------|---------------------------------------------------------|
| 🧠 Machine Learning   | `scikit-learn`, `SVM`, `StandardScaler`, `Pipeline`     |
| 🐍 Programming        | Python                                                  |
| 📊 Data Analysis      | `pandas`, `numpy`, `seaborn`, `matplotlib`             |
| 🌐 Web App Framework | Streamlit                                               |
| 💾 Serialization      | `pickle`                                                |
| 🏗️ OOP Design         | Python classes for modular design                      |

---


---

## 📄 `app.py` — Main Entry Point

### Purpose

Runs the Streamlit app, sets layout, and routes to data exploration or Personality prediction.




### Key Functions

- `st.set_page_config()`: Set page title, icon, layout
- Tabs: 
  - **📊 Data Exploration**
  - **🩺 Personality Prediction**
- Initializes `Personality` class
- Checks if dataset is loaded before proceeding

---

## 📄 `src/__init__.py`

### Purpose

Marks the `src/` directory as a Python module.

---












## 📄 `src/utils.py`

### Function: `load_model_and_scaler()`

**What it does**:
- Dataset loading
- Data cleaning

---

## 📄 `src/personality.py`

### Class: `Personality`

Main class that handles:
- Loads `Personality.pkl`
- Data exploration
- Form input & prediction With Streamlit integreted

---

## 📄 `src/train_model.py`

### Function: `train_load_and_save_model`
- Loads the processed Dataset
- uses SVM Model to train model `Personality.pkl`
- Trains the on 20/80
- saves the Model in a Pickel file


### `data_analysis()`

Provides multiple interactive analysis options:



1. **Show Data Table**
   - Displays first 5 rows


2. **Correlation Heatmap**
   - Show the Correlation

3. **Pair Ploting**
   - pair ploting is based on 6 colums ["TimeSpentAlone", "SocialEventAttendance", "FriendsCircleSize", "Personality"]
  
4. **Class Distribution**
   - Pie chart of Extroverts vs Introvert

---

### `form_inputs()`

Interactive patient form to collect 7 features:


- TimeSpentAlone
- StageFear
- SocialEventAttendance
- GoingOutside
- DrainedAfterSocializing
- FriendsCircleSize
- PostFrequency


### On submission:

- Scales inputs using loaded `StandardScaler`
- Predicts using `SVM pipeline`
- Shows result: Extrovert or Introvert


---

## 📄 `models/train_model.py`

### Purpose

Train and save the Personality prediction model and scaler.

---

### Steps Performed

1. **Load Data**
   - `pandas.read_csv()`

2. **Data Prepareing**
      - Rename-ing:
        "Time_spent_Alone": "TimeSpentAlone",
        "Stage_fear": "StageFear",
        "Social_event_attendance": "SocialEventAttendance",
        "Going_outside": "GoingOutside",
        "Drained_after_socializing": "DrainedAfterSocializing",
        "Friends_circle_size": "FriendsCircleSize",
        "Post_frequency": "PostFrequency",
        "Personality": "Personality"



3. **Select Features**
   ```
   [
      "TimeSpentAlone", "StageFear", "SocialEventAttendance",
      "GoingOutside", "DrainedAfterSocializing",
      "FriendsCircleSize", "PostFrequency"
   ]
   ```
       - Time_spent_Alone: Hours spent alone daily (0–11).
    - Stage_fear: Presence of stage fright (Yes/No).
    - Social_event_attendance: Frequency of social events (0–10).
    - Going_outside: Frequency of going outside (0–7).
    - Drained_after_socializing: Feeling drained after socializing (Yes/No).
    - Friends_circle_size: Number of close friends (0–15).
    - Post_frequency: Social media post frequency (0–10).
    - Personality: Target variable (Extrovert/Introvert).*

7. **Train-Test Split**
   - 80/20 split

8. **Standard Scaling**
   - StandardScaler transforms features to have:
    Mean = 0   
    Standard deviation = 1

Helps models learn better, especially when features vary in range.

1. **Train Model**
   - Pipeline and SVM Model combined 
  
2.  **Evaluate**
    - Accuracy and classification report

3.  **Save Artifacts**
    - `Personality.pkl`
   

---

## 📄 `data/personality_dataset.csv`

- Original personality dataset.
- Contains Personality features and Personality column.
- Preprocessed in `train_model.py`.


---

## ▶️ How to Run the App

```bash
streamlit run app.py
```

**Make sure:**
- `Personality.pkl` exist in `models/`
- Dataset exists in `data/`

---


## ✅ Summary

- Uses ML and Streamlit for an intuitive Personality prediction tool
- Modular codebase (train, utils, logic, UI)
- Real dataset-based training


