# Resume AI Project

This is a simple AI-based resume screening web application built using Python and FastAPI.

The purpose of this project is to understand how Natural Language Processing (NLP) can be used to compare resumes with a given job description and calculate a similarity score.

## Live Demo (Deployed on Cloud)

Access the live application here:
**https://resume-ai-project-gunl.onrender.com/**

## What this project does

* Accepts resume upload (PDF)
* Extracts text from the resume
* Converts text into vector embeddings
* Compares it with a job description
* Calculates a similarity score
* Displays the result in a web interface

## Technologies Used

* Python
* FastAPI
* Sentence Transformers
* FAISS
* HTML/CSS
* Docker
* Render (Cloud Deployment)

## How to Run Locally

Install dependencies:
pip install -r requirements.txt

Run the application:
uvicorn app:app --reload

Open in browser:
http://127.0.0.1:8000

## Run with Docker

Build image:
docker build -t resumeai .

Run container:
docker run -p 10000:10000 resumeai

Open:
http://localhost:10000

---

This project was created as part of my learning journey in AI and backend development.
