# WikiQuiz AI 🧠  
**Turn Wikipedia into interactive learning — instantly**

WikiQuiz AI is a full-stack application that converts Wikipedia articles into structured, high-quality quizzes using Generative AI.

Instead of passively reading long articles, users can actively test their understanding through automatically generated questions, explanations, and difficulty levels — all powered by a production-ready backend.

This project demonstrates **backend engineering**, **AI integration**, and **API-first system design**.

---

## Why WikiQuiz AI?

Wikipedia is one of the richest knowledge bases in the world, but learning from it is mostly passive.

WikiQuiz AI transforms reading into **active learning** by generating quizzes directly from Wikipedia articles.

---

## What It Does

1. Accepts a Wikipedia article URL  
2. Scrapes and cleans article content  
3. Generates quiz questions using Google Gemini  
4. Applies strict rules for consistency  
5. Stores quizzes and questions in MySQL  
6. Exposes everything via a REST API  

---

## Key Features

- AI-generated quizzes with explanations  
- Difficulty levels: Easy, Medium, Hard  
- Deterministic quiz structure  
- Quiz history with timestamps  
- AI-suggested related topics  
- RESTful FastAPI backend  
- Persistent MySQL storage  

---

## System Architecture

```
React Frontend
      ↓
FastAPI Backend
      ↓
Wikipedia Scraper (BeautifulSoup)
      ↓
Google Gemini API
      ↓
MySQL Database
```

---

## Tech Stack

### Backend
- FastAPI
- Uvicorn
- Google Gemini API
- MySQL
- BeautifulSoup
- Requests
- Pydantic

### Frontend
- React

---

## Project Structure

```
AI_WIKI/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── myenv/
│   └── test_gemini.py
├── frontend/
│   └── src/
└── README.md
```

---

## Installation & Setup

### 1. Navigate to Backend
```bash
cd backend
```

### 2. Create Virtual Environment
```bash
python -m venv myenv
```

### 3. Activate Environment (Windows)
```bash
.\myenv\Scripts\Activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Database Setup

Ensure MySQL is running, then execute:

```sql
CREATE USER 'quiz_user'@'localhost' IDENTIFIED BY 'quiz_password_123';
CREATE DATABASE wiki_quiz_db;
GRANT ALL PRIVILEGES ON wiki_quiz_db.* TO 'quiz_user'@'localhost';
FLUSH PRIVILEGES;
```

⚠️ Update credentials before production use.

---

## Gemini API Configuration

In `main.py`:

```python
GEMINI_API_KEY = "YOUR_API_KEY"
```

Get your API key from Google AI Studio.

---

## Running the Application

```bash
python -m uvicorn main:app --reload
```

Server URL:
```
http://127.0.0.1:8000
```

### API Docs
- Swagger UI: `/docs`
- ReDoc: `/redoc`

---

## API Endpoints

### Health Check
```
GET /
```

### Generate Quiz
```
POST /generate-quiz
```

Request Body:
```json
{
  "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
}
```

### Get All Quizzes
```
GET /quizzes
```

### Get Quiz by ID
```
GET /quiz/{quiz_id}
```

---

## Quiz Generation Rules

- Exactly 7 questions  
- 4 options per question (A–D)  
- Difficulty distribution:
  - 2–3 Easy  
  - 3–4 Medium  
  - 1–2 Hard  
- Short explanation for every answer  
- 5 related topics  

---

## Database Design

### quizzes Table
- Article URL  
- Title  
- Summary  
- Related topics (JSON)  
- Created timestamp  

---

## Common Errors Handled

- Invalid Wikipedia URL  
- Article too short  
- Gemini API failure  
- Database connection issues  

---

## Future Enhancements

- User authentication  
- Multi-language support  
- Custom quiz length  
- Difficulty-based filtering  
- Shareable quiz links  
- Analytics dashboard  
- PDF / CSV export  
- Live quiz mode  

---

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

This is not a demo project — it is a complete system.
