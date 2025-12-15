SKILL_SET = [
    "python", "java", "machine learning", "deep learning",
    "sql", "flask", "django", "nlp", "tensorflow", "pytorch"
]

def extract_skills(text):
    found = []
    for skill in SKILL_SET:
        if skill in text:
            found.append(skill)
    return found
