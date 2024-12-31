from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Example data
data = pandas.read_csv('datasets/StudentPerformanceFactors.csv')

# Prepare data
X = df[["Hours_Studied", "Attendance"]]
y = df["Exam_Score"]
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
dt_model = DecisionTreeRegressor(random_state=42, max_depth=5)
dt_model.fit(X_train, y_train)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Prediction function
def get_model_prediction(request):
    if request.model_type == "decision_tree":
        input_data = [[request.hours_studied, request.attendance]]
        prediction = dt_model.predict(input_data)[0]
    elif request.model_type == "linear_regression":
        input_data = [[request.hours_studied, request.attendance]]
        prediction = lr_model.predict(input_data)[0]
    else:
        return {"error": "Invalid model_type. Choose 'decision_tree' or 'linear_regression'."}
    return {"predicted_score": prediction}