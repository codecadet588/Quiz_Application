# Quiz App using Flask and Open Trivia API 🎉

Welcome to my **Quiz App**!  
This project lets you take a quiz, track your score, and view previous quiz results. It's powered by **Flask**, **SQLite**, and the **Open Trivia API**.

---

## 🌟 Features

- **Generate Questions**: Get quiz questions based on your choice of category, difficulty, and number of questions.
- **Answer Multiple-Choice Questions**: Select answers and get your score at the end.
- **Save Your Results**: Your name and score are saved in the database so you can see your progress.
- **Simple and Clean UI**: A smooth, easy-to-use interface for a great experience on both desktop and mobile.

---

## 🚀 How to Use


## **How the Quiz Works** 🧑‍💻

1. **Start Page**: You enter your name, choose your quiz settings (category, difficulty, and number of questions).
2. **Quiz Page**: Answer the questions! You’ll see your progress as you go.
3. **Results Page**: After finishing the quiz, you’ll see your score and it will be saved in the database.
4. **View Past Results**: You can always go back to check your previous scores.

---

## **Technologies Used** ⚙️

- **Flask**: The backend for handling requests and quizzes.
- **HTML/CSS**: Used to build and style the web pages.
- **JavaScript**: Makes the quiz interactive and fun.
- **SQLite**: Stores your quiz results (your name and score).


---

## **Database** 📊

The app saves quiz results in a simple **SQLite** database. The database has a table called `Records` with:

| Field        | Type     | Description                      |
|--------------|----------|----------------------------------|
| `id`         | INTEGER  | A unique identifier for each result |
| `name`       | TEXT     | User’s name                      |
| `percentage` | INTEGER  | User’s score as a percentage     |

---

## **Conclusion** 🎉

This is a fun, easy-to-use quiz app that lets you challenge yourself and track your progress. It’s built with **Flask**, **HTML**, **CSS**, **JavaScript**, and **SQLite**, making it a great beginner project.


