import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def train_load_and_save_model(df, model_path, selected_features):
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            return pickle.load(f)

    X = df[selected_features]
    y = df["Personality"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.8, stratify=y, random_state=42
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("svm", SVC(gamma="scale", C=1.0, kernel="rbf", random_state=42))
    ])

    pipeline.fit(X_train, y_train)

    with open(model_path, "wb") as f:
        pickle.dump(pipeline, f)

    return pipeline
