# Wikipedia Quiz Generator

An AI-powered web application that generates quizzes from Wikipedia articles. Scrapes article content, processes it with Google Gemini API, and stores quizzes in a MySQL database.

---

## Features

* **Wikipedia Article Scraping:** Automatically extract content from Wikipedia articles.
* **AI-Powered Quiz Generation:** Uses Google Gemini for contextual quiz questions.
* **MySQL Database:** Persistent storage for quizzes, questions, and history.
* **RESTful API:** FastAPI backend with full CORS support.
* **Quiz History:** Track all generated quizzes with timestamps.
* **Related Topics:** AI-generated list of related topics.
* **Difficulty Levels:** Questions categorized as easy, medium, or hard.
* **Detailed Explanations:** Each question includes an explanation for the correct answer.

---

---

## Tech Stack

### Frontend
- React (Create React App)
- Vercel

### Backend
- FastAPI  
- Uvicorn  
- Google Gemini API  
- MySQL  
- BeautifulSoup  
- Requests  
- Pydantic  

---

## Project Structure

```
AI_WIKI/
├── backend/
│   ├── main.py                 # FastAPI backend
│   ├── requirements.txt         # Python dependencies
│   ├── myenv/                   # Virtual environment
│   └── test_gemini.py           # Gemini API testing
├── frontend/src                 # React frontend
└── README.md                    # Project documentation
```

## Installation

1. **Clone Project & Navigate:**

```bash
cd backend
```

2. **Create Virtual Environment:**

```bash
python -m venv myenv
```

3. **Activate Virtual Environment:**

* Windows CMD:

```bash
myenv\Scripts\activate
```

* PowerShell:

```bash
.\myenv\Scripts\Activate.ps1
```

4. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

5. **Configure MySQL Database:**

```sql
CREATE USER 'quiz_user'@'localhost' IDENTIFIED BY 'quiz_password_123';
CREATE DATABASE wiki_quiz_db;
GRANT ALL PRIVILEGES ON wiki_quiz_db.* TO 'quiz_user'@'localhost';
FLUSH PRIVILEGES;
```

> ⚠️ Change the password in `main.py` before production.

6. **Configure Gemini API:**

```python
GEMINI_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"
```

Get API key from Google AI Studio.

---

## Running the Application

**Start Backend Server:**

```bash
# Activate venv first (if not already)
.\myenv\Scripts\Activate.ps1

# Run FastAPI server
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Access:**

* API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* Health Check: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**Expose to LAN/External:**

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Access via `http://YOUR_IP:8000`.

---

## API Endpoints

### 1. Health Check

**GET /**

```bash
curl http://127.0.0.1:8000/
```

**Response:**

```json
{
  "message": "Wikipedia Quiz Generator API",
  "status": "active"
}
```

### 2. Generate Quiz

**POST /generate-quiz**

```json
{
  "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
}
```

**Response:** Full quiz object including questions, options, explanations, and related topics.

### 3. Get All Quizzes

**GET /quizzes**
**Response:**

```json
[
  {
    "id": 1,
    "url": "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "article_title": "Artificial intelligence",
    "question_count": 7,
    "created_at": "2025-11-15T10:30:00.123456"
  }
]
```

### 4. Get Specific Quiz

**GET /quiz/{quiz_id}**
**Example:**

```bash
curl http://127.0.0.1:8000/quiz/1
```

**Response:** Returns complete quiz with all questions.

---

## Database Schema

**quizzes Table:**

```sql
CREATE TABLE quizzes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(500) NOT NULL,
    article_title VARCHAR(500) NOT NULL,
    article_summary TEXT,
    related_topics JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**questions Table:**

```sql
CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quiz_id INT NOT NULL,
    question_text TEXT NOT NULL,
    options JSON NOT NULL,
    correct_answer VARCHAR(10) NOT NULL,
    explanation TEXT,
    difficulty VARCHAR(20),
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
);
```

---

## Quiz Generation Logic

1. Scrape Wikipedia: Title, summary, main content
2. Clean content: Remove citations, normalize whitespace
3. Prompt Gemini: Generate quiz JSON
4. Parse response: Validate structure
5. Save to DB
6. Return quiz to client

**Quiz Requirements:**

* 7 questions per quiz
* 4 options per question (A, B, C, D)
* Difficulty: 2-3 easy, 3-4 medium, 1-2 hard
* 1-2 sentence explanations
* 5 related topics

---

## Configuration (main.py)

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'quiz_user',
    'password': 'quiz_password_123', # change before production
    'database': 'wiki_quiz_db'
}
```

## Common Error

**Invalid Wikipedia URL**

* Correct: `https://en.wikipedia.org/wiki/Artificial_intelligence`
* Incorrect: `https://wikipedia.org/wiki/Artificial_intelligence`
* Incorrect: `https://en.wikipedia.org/w/index.php?title=Artificial_intelligence`


## Screenshots

### Quiz Generation Page
<img src="https://github.com/user-attachments/assets/74811385-aa20-46e9-a11b-cf393369b89a" width="100%" />

### History View
<img src="https://github.com/user-attachments/assets/ec4dfb15-c6e9-4480-93a2-920f079ad2de" width="100%" />

### Quiz Details Modal
<img src="https://github.com/user-attachments/assets/2d6faa00-498b-4fd6-9f35-a87465a015e3" width="100%" />

### Tested URLs
<img src="https://github.com/user-attachments/assets/f2196e11-60d9-4807-8045-47aad1fc43f1" width="100%" />
<img src="https://github.com/user-attachments/assets/501031c2-1886-43f9-944f-d1ce16b4d47f" width="100%" />

### JSON API Output
<img src="https://github.com/user-attachments/assets/436d057f-c1aa-4e46-94e0-92c6978a07a4" width="100%" />

---
