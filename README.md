# 🩺 Healthcare Symptom Checker AI

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green?logo=fastapi&logoColor=white)
![Generative AI](https://img.shields.io/badge/Generative_AI-LLM-purple.svg)

A web application that takes user-reported symptoms and leverages a Large Language Model (LLM) to suggest potential conditions and recommended next steps for educational purposes.

---

## ✨ Demo

This is a demonstration of the final application in action. The user enters their symptoms, and the AI provides a formatted, helpful response.

https://drive.google.com/file/d/1cElpLwbxnNdwe4e8ySgTe6NDcdWtFsA4/view?usp=sharing

---

## 📖 About The Project

This project is a full-stack web application built with a Python FastAPI backend and a vanilla HTML, CSS, and JavaScript frontend. It serves as an educational tool to demonstrate the power of LLMs in processing natural language to provide structured, informational responses. User queries and AI responses are logged in an SQLite database.

**This application is for informational and educational purposes only and is not a substitute for professional medical advice.**

---

## 🚀 Features

- **Intuitive Web Interface:** A clean and simple UI for users to enter their symptoms.
- **AI-Powered Analysis:** Utilizes a powerful LLM to understand symptoms and provide relevant information.
- **Structured Responses:** The AI is prompted to return potential conditions with explanations, severity tags, and safe next steps.
- **Dynamic Frontend:** The UI handles loading states, errors, and formats the AI's response beautifully.
- **Query Logging:** All interactions are saved to an SQLite database for potential future analysis.

---

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI, Uvicorn, Gunicorn
- **Database:** SQLAlchemy, SQLite
- **AI Model:** Generative AI (LLM)
- **Frontend:** HTML5, CSS3, JavaScript (ES6)
- **Deployment:** Render

---

## ⚙️ Setup and Installation

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/YOUR_USERNAME/symptom-checker-project.git](https://github.com/YOUR_USERNAME/symptom-checker-project.git)
    cd symptom-checker-project
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    - Create a file named `.env` in the root of the project.
    - Add your secret API key to this file:
      ```
      GOOGLE_API_KEY="YOUR_API_KEY_HERE"
      ```

---

## 🏃‍♀️ Usage

To run the application locally, use the following command in your terminal:

```sh
uvicorn main:app --reload
