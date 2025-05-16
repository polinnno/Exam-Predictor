# Exam Outcome Predictor

<a href="https://exam-predictor-z4cw.onrender.com" target="_blank" style="text-decoration: none;">
  <div style="display: inline-flex; align-items: center; background-color: #28a745; color: white; padding: 10px 16px; border-radius: 8px; font-weight: bold; font-family: sans-serif;">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" style="margin-right: 8px;" viewBox="0 0 16 16">
      <path fill="currentColor" d="M4 2.01c0-.848.98-1.32 1.64-.79l7.48 5.99c.506.405.506 1.17 0 1.58l-7.48 5.99A1.01 1.01 0 0 1 4 13.99v-12z"/>
    </svg>
    Play
  </div>
</a>

This project is a web application designed to predict how well a student might perform on an exam based on personal study habits, mental health indicators, and subjective experiences. Built using Python and Flask, it shows a practical use-case of machine learning models in everyday tools.
![index](model/results/exam.png)

## What Does It Do?

The application helps students estimate their potential exam scores using various lifestyle and study-related factors. Students enter personal data, and the app calculates and visually presents a predicted score.

## Input Parameters

| Parameter                    | Type          | Description                                     |
|------------------------------|---------------|-------------------------------------------------|
| Hours of Sleep               | Integer       | Hours of sleep before the exam                  |
| Anxiety Level                | Integer (1-10)| Self-reported anxiety level                     |
| Burnout Feeling              | Boolean       | Presence of mental/physical exhaustion          |
| Attendance Rate              | Percentage    | Class attendance percentage                     |
| Homework Completion Rate     | Percentage    | Percentage of completed homework assignments    |
| Hours Studied                | Integer       | Total hours spent studying                      |
| Perceived Course Complexity  | Integer (1-10)| Subjective rating of course difficulty          |

### Type of Model
This project utilizes **Multiple Linear Regression** by establishing a linear relationship between the dependent variable (exam scores) and independent variables (sleep, anxiety, attendance, etc.).

### Model Training and Performance

The model was trained on synthetically generated data. Data was split into training (80%) and testing (20%) subsets.

#### Evaluation metrics values

- **Mean Absolute Error (MAE)**: 4.18 (predictions typically deviate by approximately 4 points).
- **R² score**: 0.82 (about 82% of variability in exam scores is explained by the model).
<div style="display: flex; gap: 20px;">
  <img src="model/results/scatter_real_vs_predicted.png" alt="Scatter Plot: Actual vs. Predicted Scores" width="48%">
  <img src="model/results/error_distribution.png" alt="Histogram: Distribution of Prediction Errors" width="48%">
</div>
