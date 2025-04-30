
# 🎧 Podcast Listening Time Prediction

This project aims to predict the **listening time (in minutes)** for podcast episodes based on a variety of episode-related features such as title, genre, sentiment, episode length, host popularity, and more. The dataset was provided as part of a machine learning competition (e.g., on Kaggle), and models were trained and evaluated using Scikit-learn pipelines and regression algorithms.

---

## 📂 Project Structure

```
├── data/
│   ├── train.csv
│   ├── test.csv
├── notebook.ipynb
├── submission.csv
├── README.md
```

---

## 📊 Features Used

- **Numerical Features:**
  - Episode_Length_minutes
  - Host_Popularity_percentage
  - Guest_Popularity_percentage
  - Number_of_Ads

- **Categorical (Nominal) Features:**
  - Podcast_Name
  - Episode_Title
  - Genre
  - Publication_Day
  - Publication_Time

- **Ordinal Features:**
  - Episode_Sentiment (Negative < Neutral < Positive)

- **Target Variable:**
  - Listening_Time_minutes

---

## ⚙️ Preprocessing

Preprocessing was handled using a `ColumnTransformer` inside a Scikit-learn pipeline. This included:
- **Numerical Features:** Imputation with mean and standard scaling.
- **Nominal Features:** One-hot encoding.
- **Ordinal Features:** Custom ordinal encoding.

---

## 🧠 Models

The following regression models were trained and compared:
- Linear Regression
- ElasticNet Regression with GridSearchCV

Performance was evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 📈 Results

| Model           | MAE     | RMSE    | R² Score |
|----------------|---------|---------|----------|
| Linear Regression | X.XX    | X.XX    | X.XX      |
| ElasticNet       | X.XX    | X.XX    | X.XX      |

> Replace the X.XX values with your actual metrics.

---

## 📤 Submission

The final model was used to generate predictions on the test set. The predictions were saved to a `submission.csv` file in the following format:

```
ID, Listening_Time_minutes
0, 27.52
1, 32.18
2, 14.76
...
```

---

## 🛠️ Libraries Used

- Python 3.10+
- pandas
- numpy
- scikit-learn
- matplotlib / seaborn (for visualization, if used)

---

## 🚀 How to Run

1. Clone the repo
2. Install dependencies
3. Run the notebook or Python script

---

## 📌 TODOs / Improvements

- Try more complex models like Random Forest or XGBoost
- Perform feature selection or dimensionality reduction
- Tune hyperparameters more extensively
- Analyze feature importances
