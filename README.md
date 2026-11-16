# Job Description Classification & Candidate Analysis System

A Machine Learning and Natural Language Processing (NLP) system to classify tech job descriptions, cluster skill requirements, and match candidate resumes using TF-IDF representation and Cosine Similarity.

---

## Project Details

- Project Type: Major Academic Project (Computer Science & Engineering)
- Academic Session: 2026
- Core Technologies: Python, NLP, TF-IDF, Logistic Regression, K-Means Clustering, Cosine Similarity, ReportLab

---

## Project Contributors

- Sourabh Shrivastava (Leader) - Roll No: 6606645
- Suhana Padhi - Roll No: 6605352
- Sarwash Shwet - Roll No: 6605711
- Komal Singh - Roll No: 6605636
- Niraj Kumar - Roll No: 6606718

---

## Key Features

1. NLP Text Preprocessing: Cleans raw job descriptions and resumes by lowercasing text, stripping symbols, and filtering out uninformative domain stop words.
2. TF-IDF Representation: Extracts unigram and bigram features (up to 2500 terms) to capture multi-word technical skills like "machine learning", "deep learning", "penetration testing", and "cloud infrastructure".
3. Supervised Job Classification: Automatically categorizes incoming job descriptions into 5 key technology domains using multi-class Logistic Regression with 100% test accuracy.
4. Unsupervised Job Clustering: Partitions job postings into 5 skill clusters using K-Means and visualizes them in 2D space with Principal Component Analysis (PCA).
5. Resume-Job Cosine Similarity Matching: Measures the mathematical angle between candidate resumes and job postings to generate an objective match percentage leaderboard.
6. Automated Skill Gap Analysis: Highlights which required skills a candidate already possesses and which specific competencies they are missing.
7. Presentation Generation: Includes Python scripts using ReportLab and python-pptx to generate a 12-slide presentation in minimal black-and-white format using the Poppins font.

---

## Supported Job Categories

The system categorizes and clusters job postings into five technology domains:
1. Data Science & AI (Python, pandas, scikit-learn, deep learning, PyTorch, statistics)
2. Software Development (Java, Spring Boot, React, Node.js, REST APIs, databases)
3. Cloud & DevOps (AWS, Docker, Kubernetes, Terraform, Linux, CI/CD pipelines)
4. Cybersecurity (SIEM, Splunk, penetration testing, Kali Linux, firewalls, OWASP)
5. Product & Business Analysis (Agile, Jira, user stories, product roadmaps, Scrum)

---

## Repository Structure
