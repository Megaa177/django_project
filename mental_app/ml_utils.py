# mental_app/ml_utils.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from .models import Patient

def train_and_save_model():
    # Pull data from DB
    qs = Patient.objects.all().values()
    df = pd.DataFrame(qs)
    
    # --- Step 1: Clean target ---
    # Remove rows where target is None or empty
    df = df[df['mental_health_condition'].notnull()]
    df = df[df['mental_health_condition'].str.strip() != '']
    
    # Target as string
    y = df['mental_health_condition'].astype(str)
    
    # --- Step 2: Preprocess features ---
    X = df.drop(['id', 'mental_health_condition'], axis=1)
    
    # Fill NaNs in features with default value
    X = X.fillna('Unknown')
    
    # Convert categorical features to numeric 0/1
    X = pd.get_dummies(X, drop_first=True)
    
    # --- Step 3: check ---
    if X.isnull().any().any():
        raise ValueError("There are still NaNs in features after preprocessing!")
    
    print("Features (X) and target (y) ready for training.")
    print("X shape:", X.shape)
    print("Target classes:", y.unique())
    
    # --- Step 4: Train Random Forest Classifier ---
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)
    
    # --- Step 5: Save model and feature columns ---
    joblib.dump(rf, 'mental_app/rf_model.pkl')
    joblib.dump(X.columns.tolist(), 'mental_app/model_columns.pkl')
    
    print("Model training complete. rf_model.pkl and model_columns.pkl saved.")
