from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
import shutil
from utils import extract_text_from_pdf
from model import get_similarity

app = FastAPI()

JOB_DESCRIPTION = """
Looking for Automation mobile tester with java,
selenium, appium, testng, cucumber, rest assured, git"""

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Resume Screening</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body{
                background: linear-gradient(120deg,#1e3c72,#2a5298);
                height:100vh;
                display:flex;
                align-items:center;
                justify-content:center;
                font-family: Arial, sans-serif;
            }
            .card{
                border-radius:20px;
                box-shadow:0 10px 30px rgba(0,0,0,0.2);
            }
            h2{
                font-weight:bold;
                color:#2a5298;
            }
            .btn-custom{
                background:#2a5298;
                color:white;
                font-weight:bold;
                border-radius:10px;
            }
            .btn-custom:hover{
                background:#1e3c72;
            }
        </style>
    </head>

    <body>
        <div class="card p-5 text-center" style="width:420px;">
            <h2>AI Resume Screening</h2>
            <p class="text-muted">Upload resume & check job match score</p>

            <form action="/upload" method="post" enctype="multipart/form-data">
                <input class="form-control mb-3" type="file" name="file" required>
                <button class="btn btn-custom w-100" type="submit">
                    Check Resume Score
                </button>
            </form>

            <hr>
            <small class="text-muted">Powered by AI | KloudKonnekt Technologies</small>
        </div>
    </body>
    </html>
    """

@app.post("/upload", response_class=HTMLResponse)
async def upload_resume(file: UploadFile = File(...)):
    file_path = f"resumes/{file.filename}"
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)
    score = get_similarity(resume_text, JOB_DESCRIPTION)

    score_percent = round(score*100,2)

    return f"""
    <html>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
    body {{
        background: linear-gradient(120deg,#1e3c72,#2a5298);
        color:white;
        display:flex;
        justify-content:center;
        align-items:center;
        height:100vh;
    }}
    .card {{
        padding:40px;
        border-radius:20px;
        text-align:center;
        background:white;
        color:black;
        width:450px;
    }}
    </style>
    </head>

    <body>
    <div class="card">
        <h2>Resume Score Result</h2>
        <h1 style="color:green;">{score_percent}% Match</h1>
        <p>with job description</p>

        <a href="/" class="btn btn-primary">⬅ Upload Another Resume</a>
    </div>
    </body>
    </html>
    """