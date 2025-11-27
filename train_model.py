"""import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("kidney_disease.csv")

# Clean missing values
df = df.replace("?", np.nan)
df = df.dropna()

# Encode categorical columns
label_cols = ['rbc','pc','pcc','ba','htn','dm','cad','appet','pe','ane','classification']
for col in label_cols:
    if col in df.columns:
        df[col] = LabelEncoder().fit_transform(df[col])

# Select 10 features
features = ['sc','bu','al','sg','sod','pot','hemo','htn','dm','ane']
X = df[features]
y = df['classification']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "ckd_model.pkl")

print("Model trained and saved as ckd_model.pkl")"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("kidney_disease.csv")

# Drop ID column
df = df.drop(columns=["id"])

# Encode target column
label = LabelEncoder()
df["classification"] = label.fit_transform(df["classification"])

# Split features & target
X = df.drop(columns=["classification"])
y = df["classification"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ckd_model.pkl")

print("Model trained and saved successfully!")
print(f"Trained on {X.shape[1]} features")
