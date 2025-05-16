from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/predictor5.pkl")

def safe_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        sleep = safe_int(request.form.get("sleep_hours"))
        anxiety = safe_int(request.form.get("anxiety_level"))
        burnout = safe_int(request.form.get("burnout_feeling", 0))


        if request.form.get("attended_percent"):
            attended = safe_float(request.form.get("attended_percent"))
        else:
            attended_count = safe_int(request.form.get("attended_count"))
            attended_total = safe_int(request.form.get("attended_total"), 1)
            attended = (attended_count / attended_total) * 100

        if request.form.get("homework_percent"):
            homework = safe_float(request.form.get("homework_percent"))
        else:
            hw_done = safe_int(request.form.get("hw_done"))
            hw_total = safe_int(request.form.get("hw_total"), 1)
            homework = (hw_done / hw_total) * 100

        hours_studied = safe_int(request.form.get("hours_studied"))
        complexity = safe_int(request.form.get("course_complexity"))

        if any([
            sleep <= 0 and request.form.get("sleep_hours") == "",
            anxiety <= 0 and request.form.get("anxiety_level") == "",
            hours_studied <= 0 and request.form.get("hours_studied") == "",
            complexity <= 0 and request.form.get("course_complexity") == ""
        ]):
            raise ValueError("Missing or invalid input.")

        input_data = np.array([[sleep, anxiety, burnout, attended, homework, hours_studied, complexity]])
        prediction = model.predict(input_data)[0]

        return render_template("index.html", prediction_text=f"Predicted exam score: {prediction:.2f}%")

    except Exception:
        return render_template("index.html", form_error="Please fill in all fields correctly.")

if __name__ == "__main__":
    app.run(debug=True)
