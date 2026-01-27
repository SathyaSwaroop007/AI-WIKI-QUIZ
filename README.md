# WikiQuiz AI 🧠  
**Turn Wikipedia into interactive learning — instantly**

WikiQuiz AI is a full-stack application that converts Wikipedia articles into structured, high-quality quizzes using Generative AI.

Instead of passively reading long articles, users can actively test their understanding through automatically generated questions, explanations, and difficulty levels — all powered by a production-ready backend.

This project is built to showcase **real-world backend engineering**, **AI integration**, and **API-first design**.

---

## Why WikiQuiz AI?

Wikipedia is one of the richest knowledge bases in the world — but learning from it is mostly passive.

WikiQuiz AI changes that by:
- Turning articles into quizzes  
- Encouraging active recall  
- Helping users validate what they’ve actually learned  

---

## What It Does

1. Takes a Wikipedia article URL  
2. Scrapes and cleans the article content  
3. Uses Google Gemini to generate quiz questions  
4. Applies strict rules to ensure consistency and quality  
5. Stores quizzes and questions in a relational database  
6. Exposes everything through a clean REST API  

---

## Key Features

- AI-generated quizzes with clear explanations  
- Difficulty levels: **Easy, Medium, Hard**  
- Fixed, deterministic quiz structure  
- Quiz history with timestamps  
- AI-suggested related topics  
- RESTful FastAPI backend  
- Persistent storage with MySQL  

---

## System Architecture

React Frontend
↓
FastAPI Backend
↓
Wikipedia Scraper (BeautifulSoup)
↓
Google Gemini API
↓
MySQL Database


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

AI_WIKI/
├── backend/
│ ├── main.py # FastAPI application
│ ├── requirements.txt
│ ├── myenv/ # Virtual environment
│ └── test_gemini.py # Gemini API testing
├── frontend/
│ └── src/
└── README.md


---

## Installation & Setup

### 1. Navigate to Backend
```bash
cd backend
2. Create Virtual Environment
python -m venv myenv
3. Activate Environment (Windows)
.\myenv\Scripts\Activate
4. Install Dependencies
pip install -r requirements.txt
Database Setup
Ensure MySQL is running, then execute:

CREATE USER 'quiz_user'@'localhost' IDENTIFIED BY 'quiz_password_123';
CREATE DATABASE wiki_quiz_db;
GRANT ALL PRIVILEGES ON wiki_quiz_db.* TO 'quiz_user'@'localhost';
FLUSH PRIVILEGES;
⚠️ Update credentials before production use.

Gemini API Configuration
In main.py, set:

GEMINI_API_KEY = "YOUR_API_KEY"
Get your API key from Google AI Studio.

Running the Application
python -m uvicorn main:app --reload
Server runs at:

http://127.0.0.1:8000
API Documentation
Swagger UI: /docs

ReDoc: /redoc

API Endpoints
Health Check
GET /
Generate Quiz
POST /generate-quiz
Request Body

{
  "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
}
Get All Quizzes
GET /quizzes
Get Quiz by ID
GET /quiz/{quiz_id}
Quiz Generation Rules
To ensure consistent AI output, strict constraints are enforced:

Exactly 7 questions

4 options per question (A–D)

Difficulty distribution:

2–3 Easy

3–4 Medium

1–2 Hard

Short explanation for every answer

5 related topics per quiz

Database Design
quizzes Table
Article URL

Title

Summary

Related topics (JSON)

Created timestamp

questions Table
Question text

Options (JSON)

Correct answer

Explanation

Difficulty level

Foreign key constraints ensure relational integrity.

Common Errors Handled
Invalid Wikipedia URL

Article too short to generate a quiz

Gemini API failures

Database connection issues

All handled defensively with meaningful API responses.

Engineering Highlights
Deterministic AI behavior via strict prompting

Clean separation of concerns

Production-style REST API design

Relational database modeling

Robust error handling

Future Enhancements
User authentication & personalization

Multi-language quiz generation

Custom quiz length

Difficulty-based filtering

Shareable quiz links

Analytics dashboard

PDF / CSV export

Live quiz mode with scoring

Screenshots
Quiz Generation Page
<img width="1920" height="1080" alt="Quiz Generation Page" src="https://github.com/user-attachments/assets/74811385-aa20-46e9-a11b-cf393369b89a" />
History View
<img width="1920" height="1080" alt="History View" src="https://github.com/user-attachments/assets/ec4dfb15-c6e9-4480-93a2-920f079ad2de" />
Quiz Details Modal
<img width="1920" height="1080" alt="Quiz Details Modal" src="https://github.com/user-attachments/assets/2d6faa00-498b-4fd6-9f35-a87465a015e3" />
Tested URLs
<img width="1920" height="1080" alt="Tested URLs" src="https://github.com/user-attachments/assets/f2196e11-60d9-4807-8045-47aad1fc43f1" /> <img width="1920" height="1080" alt="More Tested URLs" src="https://github.com/user-attachments/assets/501031c2-1886-43f9-944f-d1ce16b4d47f" />
JSON API Output
<img width="1920" height="1080" alt="JSON API Output" src="https://github.com/user-attachments/assets/436d057f-c1aa-4e46-94e0-92c6978a07a4" />
