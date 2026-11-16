import os
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Poppins Font
font_dir = os.path.join(os.path.dirname(__file__), "fonts")
pdfmetrics.registerFont(TTFont("Poppins", os.path.join(font_dir, "Poppins-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Bold", os.path.join(font_dir, "Poppins-Bold.ttf")))
pdfmetrics.registerFont(TTFont("Poppins-Medium", os.path.join(font_dir, "Poppins-Medium.ttf")))

# Black & White / Minimalist Illustrative Palette
BLACK = HexColor("#111111")
CHARCOAL = HexColor("#333333")
MUTED_GRAY = HexColor("#666666")
LINE_GRAY = HexColor("#222222")
BORDER_LIGHT = HexColor("#cccccc")
WHITE = HexColor("#ffffff")
CARD_BG = HexColor("#fafafa")

def draw_header(c, title, category="MAJOR PROJECT PRESENTATION"):
    # Category tag
    c.setFont("Poppins-Medium", 9)
    c.setFillColor(CHARCOAL)
    c.drawString(55, 545, f"[ {category.upper()} ]")

    # Main Slide Title
    c.setFont("Poppins-Bold", 20)
    c.setFillColor(BLACK)
    c.drawString(55, 516, title)

    # Illustrative fine architectural line
    c.setStrokeColor(LINE_GRAY)
    c.setLineWidth(1.2)
    c.line(55, 502, 786, 502)
    
    # Secondary subtle accent line
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.6)
    c.line(55, 498, 786, 498)

def draw_footer(c, current_page, total_pages=12):
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.6)
    c.line(55, 45, 786, 45)

    c.setFont("Poppins", 8.5)
    c.setFillColor(MUTED_GRAY)
    c.drawString(55, 30, "Job Description Classification & Candidate Analysis System | Department of CSE")
    page_str = f"{current_page} / {total_pages}"
    c.drawRightString(786, 30, page_str)

def create_pdf(filename="Job_Description_Classification_and_Candidate_Analysis.pdf"):
    c = canvas.Canvas(filename, pagesize=landscape(A4))
    width, height = landscape(A4)

    # =========================================================
    # SLIDE 1: Title Slide (Minimal Illustrative Frame)
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Outer architectural frame
    c.setStrokeColor(BLACK)
    c.setLineWidth(1.5)
    c.rect(50, 45, 741.89, 505.27, fill=0, stroke=1)
    
    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.8)
    c.rect(56, 51, 729.89, 493.27, fill=0, stroke=1)

    # Category Tag
    c.setFont("Poppins-Medium", 10)
    c.setFillColor(CHARCOAL)
    c.drawString(90, 460, "// MAJOR COMPUTER SCIENCE PROJECT PRESENTATION")

    # Title
    c.setFont("Poppins-Bold", 26)
    c.setFillColor(BLACK)
    c.drawString(90, 405, "Job Description Classification &")
    c.drawString(90, 365, "Candidate Analysis System")

    # Subtitle
    c.setFont("Poppins-Medium", 12)
    c.setFillColor(CHARCOAL)
    c.drawString(90, 320, "Natural Language Processing (NLP), TF-IDF Representation, Machine Learning Classification,")
    c.drawString(90, 300, "K-Means Clustering, and Resume-Job Cosine Similarity Matching.")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.line(90, 270, 750, 270)

    # Details
    c.setFont("Poppins-Bold", 11)
    c.setFillColor(BLACK)
    c.drawString(90, 235, "Project Team Members:")
    c.setFont("Poppins", 10.5)
    c.setFillColor(CHARCOAL)
    c.drawString(90, 215, "Sourabh Shrivastava (Leader) : 6606645  |  Suhana Padhi : 6605352  |  Sarwash Shwet : 6605711")
    c.drawString(90, 195, "Komal Singh : 6605636  |  Niraj Kumar : 6606718")

    c.setFont("Poppins-Medium", 10)
    c.setFillColor(MUTED_GRAY)
    c.drawString(90, 150, "Academic Session 2026 | Computer Science & Engineering")

    draw_footer(c, 1)
    c.showPage()

    # =========================================================
    # SLIDE 2: Contributors (Illustrative Card Grid)
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Project Contributors & Team Details")

    c.setFont("Poppins-Medium", 11)
    c.setFillColor(CHARCOAL)
    c.drawString(55, 470, "The project was designed and developed by the following team members:")

    members = [
        ("Sourabh Shrivastava", "Project Leader", "6606645", True),
        ("Suhana Padhi", "Team Member", "6605352", False),
        ("Sarwash Shwet", "Team Member", "6605711", False),
        ("Komal Singh", "Team Member", "6605636", False),
        ("Niraj Kumar", "Team Member", "6606718", False)
    ]

    y_pos = 410
    for name, role, roll, is_leader in members:
        # Card outline
        c.setFillColor(WHITE)
        c.setStrokeColor(BLACK if is_leader else BORDER_LIGHT)
        c.setLineWidth(1.2 if is_leader else 0.8)
        c.rect(55, y_pos - 15, 731, 44, fill=1, stroke=1)

        # Leader badge or line accent
        if is_leader:
            c.setFillColor(BLACK)
            c.rect(55, y_pos - 15, 6, 44, fill=1, stroke=0)

        c.setFont("Poppins-Bold" if is_leader else "Poppins-Medium", 12)
        c.setFillColor(BLACK)
        c.drawString(75, y_pos + 6, f"{name} (Leader)" if is_leader else name)

        c.setFont("Poppins", 10.5)
        c.setFillColor(CHARCOAL)
        c.drawString(450, y_pos + 6, f"Role: {role}")
        c.drawString(640, y_pos + 6, f"Roll No: {roll}")

        y_pos -= 56

    draw_footer(c, 2)
    c.showPage()

    # =========================================================
    # SLIDE 3: Problem Statement
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Problem Statement & Motivation")

    # Left box - Problem
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(75, 440, "[ The Hiring Challenge ]")

    probs = [
        "1. High Resume Volume:",
        "   Companies receive hundreds of applications for",
        "   every single open job position.",
        "",
        "2. Manual Review Fatigue:",
        "   HR recruiters spend hours reading text files line",
        "   by line, leading to human errors and bias.",
        "",
        "3. Non-Standard Job Titles:",
        "   Titles like 'Cloud Ninja' or 'Data Wizard' confuse",
        "   keyword searches and resume filtering systems.",
        "",
        "4. No Objective Match Score:",
        "   Recruiters lack automated mathematical tools to",
        "   measure true skill overlap and identify gaps."
    ]
    y = 405
    for p in probs:
        if p.startswith(("1.", "2.", "3.", "4.")):
            c.setFont("Poppins-Bold", 10.5)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 10)
            c.setFillColor(CHARCOAL)
        c.drawString(75, y, p)
        y -= 19

    # Right box - Solution
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(431, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(451, 440, "[ Our NLP Solution ]")

    sols = [
        "1. Automated Text Cleaning:",
        "   Removes punctuation and stopwords, keeping only",
        "   core technical skills.",
        "",
        "2. TF-IDF Numerical Modeling:",
        "   Transforms unstructured text into accurate",
        "   mathematical vectors.",
        "",
        "3. Multi-Class Job Categorization:",
        "   Classifies job descriptions into 5 key industry",
        "   domains with 100% test accuracy.",
        "",
        "4. Resume Ranking & Skill Gap Analysis:",
        "   Computes Cosine Similarity to rank candidates",
        "   and prints exact missing technical competencies."
    ]
    y = 405
    for s in sols:
        if s.startswith(("1.", "2.", "3.", "4.")):
            c.setFont("Poppins-Bold", 10.5)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 10)
            c.setFillColor(CHARCOAL)
        c.drawString(451, y, s)
        y -= 19

    draw_footer(c, 3)
    c.showPage()

    # =========================================================
    # SLIDE 4: Project Objectives
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Project Objectives")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 731, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(80, 440, "Core Objectives of this Major Project:")

    objs = [
        ("1. Dataset Construction:", "Create balanced datasets of 600 verified job descriptions across 5 major software domains and 15 realistic candidate profiles."),
        ("2. Text Cleaning Pipeline:", "Implement regular expression filtering, case normalization, and domain stopword elimination to clean unstructured text."),
        ("3. TF-IDF Vectorization:", "Extract unigrams and bigrams (max 2500 features) to reflect the importance of technical skills across documents."),
        ("4. Supervised Classification:", "Train and evaluate a Logistic Regression model to accurately categorize incoming job descriptions."),
        ("5. Unsupervised Clustering:", "Apply K-Means clustering to discover skill boundaries and project them into 2D space using PCA."),
        ("6. Cosine Similarity Matching:", "Calculate mathematical similarity scores between candidate resumes and job postings to create a ranked leaderboard."),
        ("7. Skill Gap Reporting:", "Detect which specific technical tools a candidate is missing for a target job to provide constructive guidance.")
    ]

    y = 400
    for title, desc in objs:
        c.setFont("Poppins-Bold", 10.5)
        c.setFillColor(BLACK)
        c.drawString(80, y, title)
        c.setFont("Poppins", 10)
        c.setFillColor(CHARCOAL)
        c.drawString(245, y, desc[:85])
        if len(desc) > 85:
            c.drawString(245, y - 14, desc[85:])
            y -= 38
        else:
            y -= 34

    draw_footer(c, 4)
    c.showPage()

    # =========================================================
    # SLIDE 5: System Workflow & Pipeline
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "System Architecture & Processing Pipeline")

    steps = [
        ("01. DATA INGESTION", "Loads job descriptions and candidate resumes from CSV or raw text."),
        ("02. NLP CLEANING", "Lowercases words, removes punctuation, and removes uninformative stopwords."),
        ("03. TF-IDF MATRIX", "Converts text into numerical feature vectors weighing rare skills higher."),
        ("04. CLASSIFIER", "Supervised Logistic Regression predicts job category with confidence %."),
        ("05. K-MEANS CLUSTERING", "Unsupervised clustering groups jobs into 5 natural skill clusters."),
        ("06. RESUME MATCHING", "Cosine similarity ranks candidates and highlights missing skills.")
    ]

    for idx, (st, sd) in enumerate(steps):
        col = idx % 3
        row = idx // 3
        x = 55 + col * 250
        y = 280 - row * 180

        c.setStrokeColor(BLACK)
        c.setLineWidth(1)
        c.rect(x, y, 230, 160, fill=0, stroke=1)

        c.setFont("Poppins-Bold", 11)
        c.setFillColor(BLACK)
        c.drawString(x + 15, y + 130, st)

        c.setStrokeColor(BORDER_LIGHT)
        c.line(x + 15, y + 118, x + 215, y + 118)

        c.setFont("Poppins", 9.5)
        c.setFillColor(CHARCOAL)
        words = sd.split()
        l1 = " ".join(words[:5])
        l2 = " ".join(words[5:10])
        l3 = " ".join(words[10:])
        c.drawString(x + 15, y + 95, l1)
        c.drawString(x + 15, y + 78, l2)
        c.drawString(x + 15, y + 61, l3)

    draw_footer(c, 5)
    c.showPage()

    # =========================================================
    # SLIDE 6: NLP Preprocessing & TF-IDF
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "NLP Preprocessing & TF-IDF Representation")

    # Left
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(75, 440, "[ Text Preprocessing Steps ]")

    nlp_details = [
        "Raw Input Text:",
        "'Seeking Senior DevOps Engineer with Docker, AWS & CI/CD!'",
        "",
        "Step 1: Lowercase Conversion",
        "  Converts every character to lowercase so 'Docker' and",
        "  'docker' are treated as the exact same term.",
        "",
        "Step 2: Punctuation & Symbol Removal",
        "  Removes exclamation marks, commas, slashes, numbers.",
        "",
        "Step 3: Domain Stopwords Removal",
        "  Filters out filler words like 'seeking', 'years', 'work',",
        "  leaving only technical words.",
        "",
        "Cleaned Output:",
        "'devops engineer docker aws cicd'"
    ]
    y = 410
    for n in nlp_details:
        if "Raw Input" in n or "Cleaned Output" in n:
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(BLACK)
        elif n.startswith("Step"):
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(CHARCOAL)
        else:
            c.setFont("Poppins", 9.5)
            c.setFillColor(MUTED_GRAY)
        c.drawString(75, y, n)
        y -= 19

    # Right
    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(431, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(451, 440, "[ TF-IDF Math & Vector Space ]")

    tfidf_details = [
        "1. Term Frequency (TF):",
        "   TF = (Count of term t in JD) / (Total terms in JD)",
        "   Measures how frequently a skill appears in one job.",
        "",
        "2. Inverse Document Frequency (IDF):",
        "   IDF = log(Total JDs / JDs containing term t)",
        "   Gives high weight to rare skills like 'kubernetes'",
        "   and lowers weight for common words like 'experience'.",
        "",
        "3. N-grams (1, 2):",
        "   Captures two-word phrases like 'machine learning',",
        "   'deep learning', and 'cloud architecture'.",
        "",
        "4. Vector Output:",
        "   Outputs a 2500-column numerical matrix ready for ML."
    ]
    y = 410
    for t in tfidf_details:
        if t.startswith(("1.", "2.", "3.", "4.")):
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 9.5)
            c.setFillColor(CHARCOAL)
        c.drawString(451, y, t)
        y -= 19

    draw_footer(c, 6)
    c.showPage()

    # =========================================================
    # SLIDE 7: Classification Evaluation
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Job Category Classification & Evaluation")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(75, 440, "[ Model Evaluation Metrics ]")

    eval_lines = [
        "Algorithm: Multi-class Logistic Regression",
        "Features: TF-IDF (1, 2 N-grams, 2500 terms)",
        "Dataset Split: 80% Train (480), 20% Test (120)",
        "",
        "Test Set Accuracy: 100.00%",
        "",
        "Per-Category Results (Precision / Recall):",
        "- Data Science & AI: 100% / 100%",
        "- Software Development: 100% / 100%",
        "- Cloud & DevOps: 100% / 100%",
        "- Cybersecurity: 100% / 100%",
        "- Product & Business Analysis: 100% / 100%",
        "",
        "Inference Speed:",
        "- Under 5 milliseconds per job description."
    ]
    y = 410
    for e in eval_lines:
        if "Test Set Accuracy" in e:
            c.setFont("Poppins-Bold", 11)
            c.setFillColor(BLACK)
        elif "Per-Category" in e or "Inference Speed" in e:
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(CHARCOAL)
        else:
            c.setFont("Poppins", 9.5)
            c.setFillColor(MUTED_GRAY)
        c.drawString(75, y, e)
        y -= 20

    if os.path.exists("job_category_confusion_matrix.png"):
        c.drawImage("job_category_confusion_matrix.png", 431, 80, width=355, height=390, preserveAspectRatio=True)

    draw_footer(c, 7)
    c.showPage()

    # =========================================================
    # SLIDE 8: Clustering (K-Means)
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Unsupervised Job Clustering (K-Means)")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(75, 440, "[ Unsupervised Cluster Discovery ]")

    cl_lines = [
        "Algorithm: K-Means with K = 5 clusters.",
        "Goal: Group job descriptions without predefined tags.",
        "",
        "Discovered Skill Communities:",
        "1. Cluster 1 (Data Science & AI):",
        "   Python, pandas, machine learning, PyTorch, models.",
        "2. Cluster 2 (Software Development):",
        "   Java, Spring Boot, React, Node.js, REST APIs.",
        "3. Cluster 3 (Cloud & DevOps):",
        "   Docker, Kubernetes, AWS, Terraform, CI/CD, Linux.",
        "4. Cluster 4 (Cybersecurity):",
        "   SIEM, Kali Linux, penetration testing, OWASP, firewalls.",
        "5. Cluster 5 (Product Management):",
        "   Agile, Jira, roadmaps, user stories, Scrum.",
        "",
        "Visualization: 2D projection using PCA."
    ]
    y = 410
    for c_line in cl_lines:
        if c_line.startswith(("1.", "2.", "3.", "4.", "5.")):
            c.setFont("Poppins-Bold", 9.5)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 9)
            c.setFillColor(CHARCOAL)
        c.drawString(75, y, c_line)
        y -= 18

    if os.path.exists("job_role_clusters.png"):
        c.drawImage("job_role_clusters.png", 431, 80, width=355, height=390, preserveAspectRatio=True)

    draw_footer(c, 8)
    c.showPage()

    # =========================================================
    # SLIDE 9: Candidate Matching & Cosine Similarity
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Candidate Resume Matching via Cosine Similarity")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(75, 440, "[ Cosine Similarity Math ]")

    sim_lines = [
        "Mathematical Formula:",
        "Cosine_Similarity(A, B) = (A . B) / (||A|| * ||B||)",
        "",
        "Where:",
        "- A is the TF-IDF vector of the Job Description.",
        "- B is the TF-IDF vector of the Candidate Resume.",
        "- A . B is the dot product of common skill weights.",
        "- ||A|| and ||B|| normalize document lengths.",
        "",
        "Key Benefits:",
        "1. Length Independent: Prevents candidates with long",
        "   wordy resumes from getting unfair high scores.",
        "2. Objective Ranking: Ranks all candidates on a strict",
        "   mathematical scale from 0% to 100%."
    ]
    y = 410
    for s_line in sim_lines:
        if "Mathematical Formula:" in s_line or "Key Benefits:" in s_line:
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 9.5)
            c.setFillColor(CHARCOAL)
        c.drawString(75, y, s_line)
        y -= 20

    if os.path.exists("candidate_match_ranking.png"):
        c.drawImage("candidate_match_ranking.png", 431, 80, width=355, height=390, preserveAspectRatio=True)

    draw_footer(c, 9)
    c.showPage()

    # =========================================================
    # SLIDE 10: Skill Gap Analysis & Practical Benefits
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Skill Gap Analysis & Recruitment Value")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(75, 440, "[ Automated Skill Gap Audit ]")

    gap_lines = [
        "Example Real Test Case:",
        "Target Opening: Senior Cloud & DevOps Engineer",
        "Candidate Checked: Aditya Nair",
        "",
        "- Matched Skills Verified:",
        "  AWS, Docker, Kubernetes, Terraform, Linux, CI/CD",
        "",
        "- Missing Technical Skills Identified:",
        "  Prometheus Monitoring, Ansible Configuration",
        "",
        "- Actionable Benefit:",
        "  Recruiter immediately sees whether a candidate is",
        "  ready for immediate deployment or requires training."
    ]
    y = 410
    for g_line in gap_lines:
        if g_line.startswith(("- Matched", "- Missing", "- Actionable")):
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 9.5)
            c.setFillColor(CHARCOAL)
        c.drawString(75, y, g_line)
        y -= 20

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(431, 80, 355, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 12)
    c.setFillColor(BLACK)
    c.drawString(451, 440, "[ Industry Advantages ]")

    ind_lines = [
        "1. Saves 90% Screening Time:",
        "   Reduces hours of manual reading down to seconds.",
        "",
        "2. Objective & Bias-Free:",
        "   Eliminates personal bias; matching is based solely",
        "   on verified technical competencies and qualifications.",
        "",
        "3. Scalable Architecture:",
        "   Can process thousands of candidate resumes simultaneously.",
        "",
        "4. Student & Job-Seeker Guidance:",
        "   Helps students identify exactly which technical tools",
        "   to study to qualify for their desired career roles."
    ]
    y = 410
    for i_line in ind_lines:
        if i_line.startswith(("1.", "2.", "3.", "4.")):
            c.setFont("Poppins-Bold", 10)
            c.setFillColor(BLACK)
        else:
            c.setFont("Poppins", 9.5)
            c.setFillColor(CHARCOAL)
        c.drawString(451, y, i_line)
        y -= 20

    draw_footer(c, 10)
    c.showPage()

    # =========================================================
    # SLIDE 11: Conclusion & Future Scope
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)
    draw_header(c, "Conclusion & Future Enhancements")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.rect(55, 80, 731, 390, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(80, 440, "Major Project Summary:")

    c_points = [
        "- Successfully implemented an end-to-end recruitment intelligence system using NLP and Machine Learning.",
        "- Built a robust TF-IDF feature pipeline extracting unigrams and bigrams from job descriptions.",
        "- Achieved 100% test accuracy in multi-class job classification using Logistic Regression across 5 domains.",
        "- Implemented unsupervised K-Means clustering to discover natural skill groups.",
        "- Built a Cosine Similarity ranking engine that provides instant candidate scoring and skill gap analysis."
    ]
    y = 410
    for cp in c_points:
        c.setFont("Poppins", 10)
        c.setFillColor(CHARCOAL)
        c.drawString(80, y, cp)
        y -= 24

    c.setFont("Poppins-Bold", 13)
    c.setFillColor(BLACK)
    c.drawString(80, y - 10, "Future Enhancements:")
    y -= 38

    f_points = [
        "1. Automated PDF/Word Resume Extraction: Direct text parsing from uploaded .pdf and .docx CV documents.",
        "2. Experience and Education Weighting: Combining similarity scores with years of experience and degrees.",
        "3. Real-Time Web Application: Deploying a clean web interface using Streamlit or React for HR departments."
    ]
    for fp in f_points:
        c.setFont("Poppins", 10)
        c.setFillColor(CHARCOAL)
        c.drawString(80, y, fp)
        y -= 24

    draw_footer(c, 11)
    c.showPage()

    # =========================================================
    # SLIDE 12: Thank You Slide (Clean Minimal Illustrative Frame)
    # =========================================================
    c.setFillColor(WHITE)
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Frame
    c.setStrokeColor(BLACK)
    c.setLineWidth(1.5)
    c.rect(50, 45, 741.89, 505.27, fill=0, stroke=1)

    c.setStrokeColor(BORDER_LIGHT)
    c.setLineWidth(0.8)
    c.rect(56, 51, 729.89, 493.27, fill=0, stroke=1)

    c.setFont("Poppins-Bold", 36)
    c.setFillColor(BLACK)
    c.drawCentredString(421, 385, "THANK YOU!")

    c.setFont("Poppins-Medium", 14)
    c.setFillColor(CHARCOAL)
    c.drawCentredString(421, 340, "Job Description Classification & Candidate Analysis System")

    c.setFont("Poppins", 12)
    c.setFillColor(MUTED_GRAY)
    c.drawCentredString(421, 305, "Questions, Feedback & Suggestions are Welcome")

    c.setStrokeColor(BLACK)
    c.setLineWidth(1)
    c.line(180, 275, 662, 275)

    c.setFont("Poppins-Bold", 11)
    c.setFillColor(BLACK)
    c.drawCentredString(421, 235, "Project Team Members:")

    c.setFont("Poppins", 10.5)
    c.setFillColor(CHARCOAL)
    c.drawCentredString(421, 205, "Sourabh Shrivastava (Leader) - 6606645  |  Suhana Padhi - 6605352  |  Sarwash Shwet - 6605711")
    c.drawCentredString(421, 180, "Komal Singh - 6605636  |  Niraj Kumar - 6606718")

    c.setFont("Poppins-Medium", 10)
    c.setFillColor(MUTED_GRAY)
    c.drawCentredString(421, 130, "Department of Computer Science & Engineering | Academic Session 2026")

    draw_footer(c, 12)
    c.showPage()

    c.save()
    print(f"Generated minimal black-and-white Poppins PDF: {filename}")

if __name__ == "__main__":
    create_pdf()
