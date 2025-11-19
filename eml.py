# --- LINEAR REGRESSION ---

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
X, y = fetch_california_housing(return_X_y=True)

# Split train/test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression().fit(x_train, y_train)

# Evaluate
print("Linear Regression R² Score:", r2_score(y_test, model.predict(x_test)))




# --- LOGISTIC REGRESSION ---

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
X, y = load_breast_cancer(return_X_y=True)

# Split train/test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=3000).fit(x_train, y_train)

# Evaluate
print("Logistic Regression Accuracy:", accuracy_score(y_test, model.predict(x_test)))



# Exp : 2 -------

# --- IMPORTS ---
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# --- LOAD YOUR DATASET ---
df = pd.read_csv("class-dataset.csv")   # upload this file in Colab

# Features and labels
X = df[['f1', 'f2', 'f3']]
y = df['class']

# --- TRAIN TEST SPLIT ---
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# --- MODELS TO COMPARE ---
models = [
    LogisticRegression(max_iter=3000),
    SVC(),
    KNeighborsClassifier()
]

# --- TRAIN & EVALUATE EACH MODEL ---
for m in models:
    m.fit(x_train, y_train)
    y_pred = m.predict(x_test)
    print(m.__class__.__name__, "Accuracy:", accuracy_score(y_test, y_pred))


# Exp : 3 -----

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("tree-dataset.csv")

# Select features (X) and target (y)
X = df[['F1', 'F2', 'F3']]
y = df['output']

# Split dataset into training & testing set (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree model
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Train Random Forest model
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# Print test accuracy
print("Decision Tree Accuracy:", dt.score(X_test, y_test))
print("Random Forest Accuracy:", rf.score(X_test, y_test))
