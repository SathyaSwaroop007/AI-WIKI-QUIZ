# WikiQuiz AI
AI-Powered Wikipedia Quiz Generator

A full-stack application that transforms Wikipedia articles into structured, high-quality quizzes using Generative AI, RESTful APIs, and persistent storage.

This project is designed to demonstrate backend engineering skills, AI integration, API design, and database modeling in a production-oriented manner.

---

## Problem Statement

Wikipedia is a powerful knowledge source, but learning from it is mostly passive.

WikiQuiz AI converts encyclopedic content into interactive quizzes, enabling active learning and knowledge validation.

---

## Solution Overview

- Scrapes and cleans Wikipedia article content
- Uses Google Gemini to generate contextual quiz questions
- Enforces deterministic quiz rules (count, difficulty, explanations)
- Persists quizzes and questions in MySQL
- Exposes a clean FastAPI-based REST API

---

## Key Features

- AI-generated quizzes with explanations
- Difficulty levels: Easy, Medium, Hard
- Quiz history with timestamps
- Related topics suggested by AI
- RESTful API with validation and CORS
- Persistent storage using MySQL

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
│   ├── main.py          # FastAPI application
│   ├── requirements.txt
│   ├── myenv/           # Virtual environment
│   └── test_gemini.py   # Gemini API testing
├── frontend/
│   └── src/
└── README.md

---

## Installation and Setup

### 1. Clone and Navigate
cd backend

### 2. Create Virtual Environment
python -m venv myenv

### 3. Activate Environment (Windows)
.\myenv\Scripts\Activate

### 4. Install Dependencies
pip install -r requirements.txt

---

## Database Setup

Ensure MySQL is running, then execute:

CREATE USER 'quiz_user'@'localhost' IDENTIFIED BY 'quiz_password_123';
CREATE DATABASE wiki_quiz_db;
GRANT ALL PRIVILEGES ON wiki_quiz_db.* TO 'quiz_user'@'localhost';
FLUSH PRIVILEGES;

Update credentials before production use.

---

## Gemini API Configuration

In main.py, set:

GEMINI_API_KEY = "YOUR_API_KEY"

Get the API key from Google AI Studio.

---

## Running the Application

python -m uvicorn main:app --reload

Server runs at:

http://127.0.0.1:8000

### API Documentation
- Swagger UI: /docs
- ReDoc: /redoc

---

## API Endpoints

### Health Check
GET /

### Generate Quiz
POST /generate-quiz

Request body:
{
  "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
}

### Get All Quizzes
GET /quizzes

### Get Quiz by ID
GET /quiz/{quiz_id}

---

## Quiz Generation Rules

The AI is constrained to ensure consistency:

- Exactly 7 questions
- 4 options per question (A–D)
- Difficulty distribution:
  - 2–3 Easy
  - 3–4 Medium
  - 1–2 Hard
- Short explanations for each answer
- 5 related topics

---

## Database Schema

### quizzes Table
- Article URL
- Title and summary
- Related topics (JSON)
- Creation timestamp

### questions Table
- Question text
- Options (JSON)
- Correct answer
- Explanation
- Difficulty level

Foreign key constraints enforce relational integrity.

---

## Common Errors

Invalid Wikipedia URL: URL must use https://en.wikipedia.org/wiki/...
Short article: Article content too small
Internal error: Gemini API or database failure

---

## Engineering Highlights

- Deterministic AI outputs via strict prompting
- Clean separation of concerns
- Scalable REST API design
- Proper relational data modeling
- Defensive error handling

---

## Future Enhancements

- User authentication and personalization
- Multi-language quiz generation
- Custom quiz length
- Difficulty-based filtering
- Shareable quiz links
- Analytics dashboard
- PDF and CSV export
- Live quiz mode with scoring

---

## Why This Project

This project demonstrates the ability to integrate Generative AI into real systems, design production-ready APIs, handle unstructured data, and build scalable backend architectures.
---

## Screenshots

FastAPI Swagger UI – WikiQuiz AI
<img width="1920" height="1080" alt="Screenshot 2026-01-27 093832" src="https://github.com/user-attachments/assets/f2196e11-60d9-4807-8045-47aad1fc43f1" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 093730" src="https://github.com/user-attachments/assets/ec4dfb15-c6e9-4480-93a2-920f079ad2de" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 093716" src="https://github.com/user-attachments/assets/74811385-aa20-46e9-a11b-cf393369b89a" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 094128" src="https://github.com/user-attachments/assets/436d057f-c1aa-4e46-94e0-92c6978a07a4" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 094055" src="https://github.com/user-attachments/assets/35d64211-c02c-4598-8659-ce05467853e8" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 094033" src="https://github.com/user-attachments/assets/d67de1da-0002-411a-bb25-c8c709ba821f" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 094015" src="https://github.com/user-attachments/assets/501031c2-1886-43f9-944f-d1ce16b4d47f" />
<img width="1920" height="1080" alt="Screenshot 2026-01-27 093913" src="https://github.com/user-attachments/assets/2d6faa00-498b-4fd6-9f35-a87465a015e3" />

