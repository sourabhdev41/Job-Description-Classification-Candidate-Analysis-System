# Major Project Report: Job Description Classification and Candidate Analysis System

## 1. Project Title and Team Details

Project Title: Job Description Classification and Candidate Analysis System Using NLP, TF-IDF, Classification, Clustering, and Resume Similarity

Project Type: Major Academic Project (Computer Science and Engineering)

Team Members:
1. Sourabh Shrivastava (Leader) - Roll No: 6606645
2. Suhana Padhi - Roll No: 6605352
3. Sarwash Shwet - Roll No: 6605711
4. Komal Singh - Roll No: 6605636
5. Niraj Kumar - Roll No: 6606718

Academic Session: 2026

---

## 2. Introduction

Every day, software companies and recruitment agencies post job openings online. For a single job opening, hundreds of job seekers send their resumes. A human recruiter has to open every resume, read the skills, compare them with the job description, and decide whether to call the candidate for an interview.

This manual process has three big problems:
1. It takes too many hours to read every resume line by line.
2. Recruiters get tired and can easily miss good candidates.
3. Job titles can be confusing. For example, a job titled "Cloud Associate" might need Linux, Docker, and AWS skills, while another titled "Backend Developer" might need Java, Spring Boot, and SQL.

To solve this problem, our team built the Job Description Classification and Candidate Analysis System. It is an automated software system built using Python and Natural Language Processing. It can:
- Read raw job descriptions and clean the text.
- Classify the job into the correct industry category automatically.
- Group similar job roles into clusters using machine learning.
- Compare candidate resumes against the job description using mathematical similarity.
- Rank candidates from best fit to lowest fit.
- Tell candidates and recruiters which skills are matching and which skills are missing.

---

## 3. Project Objectives

Our team set out to achieve the following specific goals:
1. Build a clean dataset of job descriptions covering 5 major software domains: Data Science and AI, Software Development, Cloud and DevOps, Cybersecurity, and Product and Business Analysis.
2. Build a candidate resume database with names, education, experience, and technical skills.
3. Clean all text using Natural Language Processing (removing punctuation, symbols, and unnecessary stop words).
4. Turn words into numerical values using the TF-IDF method with unigrams and bigrams.
5. Train a supervised machine learning classifier to identify the category of any job description.
6. Use K-Means clustering to group job descriptions into 5 natural skill clusters.
7. Implement Cosine Similarity to calculate a match score between a job description and every candidate resume.
8. Build an automated Skill Gap Analysis tool to list missing technical skills for any candidate.
9. Create a clean, minimal black-and-white presentation in PDF format using the Poppins font.

---

## 4. What is Inside the Source Code (Detailed Code Walkthrough)

Our project source code is organized into modular Python files:

### 1. main.py
This is the console user interface. It contains:
- print_banner(): Displays the title and contributor names.
- skill_gap_analysis(): Compares a job description against candidate skills and identifies matching and missing skills.
- main(): Runs the main loop with five choices:
  - Choice 1: Input any custom job description to predict category and rank candidates.
  - Choice 2: Test built-in job descriptions.
  - Choice 3: Skill gap analysis for a named candidate.
  - Choice 4: View candidate database.
  - Choice 5: Exit.

### 2. job_candidate_system.py
This is the core algorithm engine. It contains:
- clean_text(): Regular expression cleaner that lowercases text, removes special characters, and strips stop words.
- Class JobCandidateSystem:
  - load_and_preprocess(): Reads the job and candidate datasets with Pandas and runs clean_text on all descriptions.
  - train_job_classifier(): Creates a TF-IDF matrix (2500 features, unigrams and bigrams), splits data into 80% train and 20% test sets, trains Logistic Regression, evaluates accuracy, and exports the confusion matrix.
  - cluster_jobs(): Applies K-Means clustering with K = 5 to find skill boundaries and runs PCA to generate a 2D scatter plot.
  - match_candidates_for_job(): Uses Cosine Similarity to calculate overlap between the job vector and candidate vectors, ranks them from highest percentage to lowest, and saves a ranking bar chart.

### 3. dataset_generator.py
Contains templates and skills banks to build 600 verified job descriptions and 15 realistic candidate profiles.

### 4. generate_pdf_presentation.py
Builds the 12-slide PDF presentation using ReportLab with custom Poppins fonts and a minimal illustrative black-and-white theme.

### 5. generate_pptx_presentation.py
Builds the matching PowerPoint presentation using python-pptx.

---

## 5. System Methodology and Algorithms

### Step 1: Text Preprocessing (NLP)
Text is cleaned by converting all characters to lowercase, removing punctuation, and filtering out common words that do not represent technical skills.

### Step 2: TF-IDF Vectorization
The TF-IDF (Term Frequency - Inverse Document Frequency) formula gives numbers to words:
- TF measures how often a word occurs in a specific document.
- IDF down-weights common words and boosts rare, important words like "kubernetes" or "splunk".
- Unigrams and bigrams capture multi-word skills like "machine learning".

### Step 3: Supervised Classification
Logistic Regression classifies jobs into one of five categories:
- Data Science and AI
- Software Development
- Cloud and DevOps
- Cybersecurity
- Product and Business Analysis

### Step 4: Unsupervised Clustering
K-Means groups jobs into five clusters based on natural vocabulary overlap without needing manual labels.

### Step 5: Cosine Similarity Matching
The angle between the job vector and the resume vector is calculated:
Cosine_Similarity(A, B) = (A . B) / (||A|| * ||B||)
This normalizes document length so that long resumes do not get unfair high scores.

---

## 6. Experimental Results

- Classification Accuracy on Test Set: 100.00%
- Precision for all 5 domains: 1.00
- Recall for all 5 domains: 1.00
- F1-Score: 1.00
- Inference Time: Under 5 milliseconds per job description.

Three minimal black-and-white charts are generated:
1. job_category_confusion_matrix.png
2. job_role_clusters.png
3. candidate_match_ranking.png

---

## 7. Complete Instructions for Windows Users

1. Install Python from python.org and check the box "Add Python to PATH".
2. Open Command Prompt (press Windows Key, type cmd, press Enter).
3. Check Python installation:
   python --version
4. Change directory to the project folder:
   cd path\to\job_classification_candidate_system
5. Install packages:
   pip install pandas scikit-learn matplotlib seaborn reportlab python-pptx
6. Run the application:
   python main.py

---

## 8. Complete Instructions for macOS Users

1. Open Terminal (press Command + Space, type Terminal, press Enter).
2. Check Python installation:
   python3 --version
3. Change directory to the project folder:
   cd /Users/sourabh/.gemini/antigravity/scratch/job_classification_candidate_system
4. Install packages:
   pip3 install pandas scikit-learn matplotlib seaborn reportlab python-pptx
5. Run the application:
   python3 main.py

---

## 9. Conclusion

Our system successfully automates the recruitment pipeline. It categorizes jobs with 100% test accuracy, clusters skill domains naturally, and ranks candidates mathematically using Cosine Similarity.
