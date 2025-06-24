# Spam Message Classifier - Web App

A web-based application built using **Flask**, **scikit-learn**, and **HTML/CSS/JS** that classifies text messages as **Spam** or **Not Spam (Ham)** using a trained machine learning model.

---

## Features

- Enter any message and classify it instantly.
- Trained on real-world labeled SMS spam dataset.
- Clean dark-themed UI for modern aesthetic.
- Fully responsive frontend (HTML/CSS/JavaScript).
- Simple Flask backend integrated with ML model.

---

## Model Info

- Model: **Multinomial Naive Bayes**
- Vectorization: **CountVectorizer**
- Trained using: [Kaggle - SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Saved using: `joblib`

---

## Tech Stack

| Frontend | Backend | ML |
|----------|---------|----|
| HTML5, CSS3 (Dark Theme), JS | Flask (Python) | scikit-learn, pandas, joblib |

---

## Preview

> ![Screenshot 2025-06-24 155448](https://github.com/user-attachments/assets/155bf676-0874-4c72-bd1d-36c0b90a9e25)
> ![Screenshot 2025-06-24 155204](https://github.com/user-attachments/assets/3b8c0e49-fc48-4f6d-9af1-c5d08e832c9c)
> ![Screenshot 2025-06-24 155358](https://github.com/user-attachments/assets/0f087457-8c57-486f-b5c8-a8e085ad8328)

---

## How to Run Locally

### 1. Clone the repository 

```bash
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run and save the model

```bash
python train_model.py
```

### 4. Run the app

```bash
python app.py
```

---



