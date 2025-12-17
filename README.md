# 💬 Gemini-Powered Chat Application 🤖

This project is a Django-based chat application that leverages the power of the Gemini API to provide intelligent and engaging conversations. It allows users to register, log in, and interact with different Gemini models, storing chat history for future reference.

## 🚀 Key Features

- **User Authentication:** Secure user registration, login, and logout functionality. 🔐
- **Multiple Gemini Models:** Supports selection of different Gemini models for varied conversational experiences. 🧠
- **Real-time Chat Interface:** A dynamic chat interface for seamless interaction. 🗣️
- **Markdown Support:** Formats Gemini API responses using Markdown for enhanced readability. ✨
- **Chat History:** Stores chat messages in a database, allowing users to review past conversations. 💾
- **Download Chat History:** Users can download their chat history in text format. ⬇️
- **Health Check Endpoint:** Provides a health check endpoint for monitoring application status. 🩺

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Django
- **Database:** SQLite3 (default, configurable)
- **AI Model:** Google Gemini API
- **API Requests:** `requests` library
- **Markdown Formatting:** `markdown` library
- **Environment Management:** `os`
- **Utilities:** `sys`, `pathlib`

## 📦 Getting Started

### Prerequisites

- Python 3.8+
- Django 4.0+
- A Google Gemini API key

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure settings:**

    - Set the `SECRET_KEY` in `gemini_project/settings.py`. **Do not use the example key in production!** Generate a strong, random key.
    - Obtain a Gemini API key from Google AI Studio and set it as an environment variable or directly in `chat/views.py` (not recommended for production).

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

### Running Locally

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**

    Open your web browser and navigate to `http://localhost:8000/`.

## 📂 Project Structure

```
gemini_project/
├── chat/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       ├── chat/
│       │   ├── chat.html
│       │   ├── login.html
│       │   └── register.html
│   └── forms.py
├── gemini_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── db.sqlite3
└── requirements.txt
```

## 📸 Screenshots

<img width="362" height="354" alt="image" src="https://github.com/user-attachments/assets/bd3e9ef1-9eee-4e21-b9dd-27c656e16ba3" />

<img width="361" height="328" alt="image" src="https://github.com/user-attachments/assets/865cdab9-e2c9-4882-bc8f-fa54b2915902" />

<img width="923" height="590" alt="image" src="https://github.com/user-attachments/assets/e6f51a3e-fd95-4694-8395-aaa1449620ab" />
