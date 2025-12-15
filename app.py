from flask import Flask, render_template, request
import os
from resume_parser import parse_resume
from skill_extractor import extract_skills
from matcher import calculate_similarity
from bias_reduction import anonymize_text

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_desc = request.form["job_desc"]
        resume_files = request.files.getlist("resumes")

        results = []

        for file in resume_files:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)

            text = parse_resume(path)
            clean_text = anonymize_text(text)
            skills = extract_skills(clean_text)

            score = calculate_similarity(job_desc, clean_text)

            results.append({
                "name": file.filename,
                "skills": skills,
                "score": round(score * 100, 2)
            })

        results = sorted(results, key=lambda x: x["score"], reverse=True)
        return render_template("results.html", results=results)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
