# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix,
)

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Drop rows with missing values
penguins_clean = penguins.dropna()

print('The penguin dataset:')
print(penguins_clean.head())

# Features and target
X = penguins_clean.drop("sex", axis=1)
y = penguins_clean["sex"]

# Select numerical and categorical features
numerical_features = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
categorical_features = ["island", "species"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_features),
        ("cat", OneHotEncoder(drop="first"), categorical_features)
    ]
)

# Create pipeline with classifier
clf_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the model
clf_pipeline.fit(X_train, y_train)

# Predict
y_pred = clf_pipeline.predict(X_test)

# Evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Optional visualization: true vs predicted
results_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

# %%
# Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=clf_pipeline.classes_)
cm_df = pd.DataFrame(cm, index=clf_pipeline.classes_, columns=clf_pipeline.classes_)

plt.figure(figsize=(6, 4))
sns.heatmap(cm_df, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix: Sex Classification")
plt.tight_layout()
plt.show()

# %%
