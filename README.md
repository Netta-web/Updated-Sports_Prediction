⚽ Player Rating Prediction using Machine Learning

This project is a Machine Learning-based web application that predicts a football player’s overall rating based on key performance metrics.
It was built using Python (v1.2.1) and Flask for deployment, with a Random Forest Regressor as the underlying model.

🧠 Project Overview

The goal of this project was to predict a player’s overall rating using selected attributes from a large dataset of male football players.
The model helps identify how various features—such as Reactions, Potential, Short Passing, Vision, and International Reputation—influence the player’s performance score.

After testing different feature combinations, the final model was optimized to use the top 5 most important features, balancing accuracy and computational efficiency.

Model Performance

Using the top 5 selected features, the Random Forest model achieved the following metrics:

R² Score: 0.84
MAE (Mean Absolute Error): 1.99
RMSE (Root Mean Square Error): 2.81
These results indicate that the model performs reliably in predicting a player’s rating based on their stats.

Requirements

This project was built and tested using Python 1.2.1.
Make sure you have this version (or a compatible one) installed.

Core Dependencies

Install the required packages with:

pip install -r requirements.txt


If you don’t have the file, you can generate one with:

pip freeze > requirements.txt


Main Libraries Used:

Flask — for creating the web interface

scikit-learn — for building and training the Random Forest model

pandas — for data cleaning and preprocessing

numpy — for numerical computation

matplotlib — for visualizations (optional)


⚙️ How to Run the App Locally

Clone the repository

git clone https://github.com/Netta-web/Updated-Sports_Prediction.git
cd Updated-Sports_Prediction


Install the dependencies

pip install -r requirements.txt


Run the Flask application

python app.py


Open your browser and visit:

http://127.0.0.1:5000/


Enter player stats in the form fields and get the predicted Overall Rating instantly.

🧩 Features

Interactive Web Interface: Clean and simple input form built with HTML and CSS.

Top-5 Feature Model: Uses only the most influential features to improve efficiency.

Instant Predictions: Quickly returns the player’s predicted rating.

Error Handling: Prompts users if invalid inputs are entered.

Scalable: Can be extended to include more features or other models.
<img width="1596" height="785" alt="image" src="https://github.com/user-attachments/assets/707967e3-92e1-458c-a9ac-4ce0968056e1" />


⚠️ Model and Dataset Notice

Due to GitHub’s file size restrictions, the following files could not be uploaded to this repository:

random_forest_model.pkl — 402 MB

top5_model.pkl — 667 MB

male_players (legacy).csv — 86 MB

You can, however, access the dataset on Kaggle using the link below:
https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset 

Access Dataset on Kaggle
To retrain the model, download the dataset and run the included training script.
Both models can also be re-created from the code in this repository.

🧮 Top 5 Features Used
Feature	Description	Data Type
Reactions	How quickly the player responds to events in the game.	Integer (0–100)
Potential	The player’s predicted maximum overall rating.	Integer (0–100)
Short Passing	Player’s ability to accurately pass over short distances.	Integer (0–100)
Vision	Ability to see passing options and make creative plays.	Integer (0–100)
International Reputation	A measure of global recognition (1–5 scale).	Integer (1–5)

These were determined as the most influential features in predicting a player’s rating.

🌐 Deployment

The app is to be deployed using Render for public access.
Render provides a free and simple way to host Flask applications with integrated build and runtime environments.

👩🏽‍💻 Author
Bennetta Avaga

🎓 Senior at Ashesi University, Ghana
💻 Majoring in Computer Science
🔍 Interests: Software Development, Data Science, and Artificial Intelligence
