# SWYNEX-Model-or-API-Integration

## Project Title
AI-based Student Performance Risk Classification using Model Integration

## Objective
This project uses Artificial Intelligence to classify students into **At Risk** or **Not At Risk** based on their academic performance and engagement-related data.

## Input Features
The model uses the following student data:
- Study Hours
- Attendance
- Previous Mark
- Assignment Score

## Model Used
A **Decision Tree Classifier** is used to train the model and classify student performance risk.

## Dataset
The dataset contains student performance information with input features and a target column named `result`.

## Working Process
1. Load the student performance dataset.
2. Select the required input features.
3. Split the dataset into training and testing data.
4. Train the Decision Tree model.
5. Predict the student risk category.
6. Evaluate the model using accuracy.

## Example Input
Study Hours: 3  
Attendance: 65  
Previous Mark: 55  
Assignment Score: 60

## Output
The model predicts whether the student is **At Risk** or **Not At Risk**.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Decision Tree Classifier

## Evaluation
Model performance is evaluated using **Accuracy Score** on the test dataset.

## Internship
This project is completed as part of **SWYNEX Technologies Internship – Task 2**.
