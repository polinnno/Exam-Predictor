import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

data_path = os.path.join('..', 'assets', 'exam_data6.csv')
df = pd.read_csv(data_path)

X = df[[
    'sleep_hours',
    'anxiety_level',
    'burnout_feeling',
    'attended_lectures',
    'homework_completion_rate',
    'hours_studied',
    'course_complexity'
]]
y = df['exam_score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


with open("results/metrics.txt", "w") as f:
    f.write(f"MAE: {mae:.2f}\n")
    f.write(f"R² Score: {r2:.2f}\n")


model_path = os.path.join('predictor6.pkl')
joblib.dump(model, model_path)

print("Saved at:", model_path)


# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='skyblue', edgecolor='black')
plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs. Predicted Scores")
plt.grid(True)
plt.savefig("results/scatter_real_vs_predicted.png")
plt.close()

# Error Distribution
errors = y_test - y_pred
plt.figure(figsize=(8, 6))
plt.hist(errors, bins=20, color='salmon', edgecolor='black')
plt.title("Error Distribution")
plt.xlabel("Error (Actual - Predicted)")
plt.ylabel("Number of Instances")
plt.grid(True)
plt.savefig("results/error_distribution.png")
plt.close()
