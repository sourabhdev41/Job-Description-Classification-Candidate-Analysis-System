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

```
job_classification_candidate_system/
|-- main.py                                      # Main interactive CLI application
|-- job_candidate_system.py                      # Core ML algorithms, NLP, TF-IDF & similarity engine
|-- dataset_generator.py                         # Dataset generator script
|-- job_descriptions.csv                         # Dataset of 600 verified job descriptions
|-- candidate_resumes.csv                        # Dataset of 15 candidate profiles with skills
|-- generate_pdf_presentation.py                 # ReportLab script building the 12-slide PDF presentation
|-- generate_pptx_presentation.py                # python-pptx script building the 12-slide PPTX presentation
|-- Job_Description_Classification_and_Candidate_Analysis.pdf   # 12-slide presentation in PDF format
|-- Job_Description_Classification_and_Candidate_Analysis.pptx  # 12-slide presentation in PPTX format
|-- PROJECT_REPORT.md                            # Comprehensive project report in simple English
|-- README.md                                    # Project documentation and execution guide
|-- requirements.txt                             # Python package dependencies
|-- .gitignore                                   # Standard Python Git ignore file
|-- fonts/                                       # Official Poppins TrueType fonts
|   |-- Poppins-Regular.ttf
|   |-- Poppins-Medium.ttf
|   `-- Poppins-Bold.ttf
|-- job_category_confusion_matrix.png            # Classification confusion matrix chart
|-- job_role_clusters.png                        # 2D PCA K-Means cluster scatter plot
`-- candidate_match_ranking.png                  # Candidate match percentage leaderboard
```

---

## Installation & Setup Guide

### Windows Setup (Windows 10 / 11)

1. Install Python 3:
   Download the installer from https://www.python.org/downloads/
   Make sure to check the box "Add Python to PATH" during installation.

2. Open Command Prompt or PowerShell:
   Press Windows Key, type cmd, and press Enter.

3. Clone or download this repository:
   ```cmd
   git clone https://github.com/<your-username>/job-classification-candidate-system.git
   cd job-classification-candidate-system
   ```

4. Install the required dependencies:
   ```cmd
   pip install -r requirements.txt
   ```

5. Run the application:
   ```cmd
   python main.py
   ```

---

### macOS Setup (MacBook / iMac)

1. Open Terminal (Command + Space, type Terminal, press Enter).

2. Clone this repository and navigate to the directory:
   ```bash
   git clone https://github.com/<your-username>/job-classification-candidate-system.git
   cd job-classification-candidate-system
   ```

3. Install the required dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python3 main.py
   ```

---

## How to Use the System

When you execute `python main.py` or `python3 main.py`, an interactive menu appears with five options:

1. Option 1: Paste any job description to automatically predict its domain category and get the top 5 ranked candidates based on Cosine Similarity.
2. Option 2: Run automated tests on built-in job descriptions for Data Science, Web Development, and Cybersecurity.
3. Option 3: Run a Skill Gap report by entering a job description and a candidate's name to view matched versus missing skills.
4. Option 4: View the complete roster of candidate resumes stored in the database.
5. Option 5: Exit the program.

---

## Experimental Results

- Test Set Classification Accuracy: 100.00%
- Precision for all 5 domains: 1.00
- Recall for all 5 domains: 1.00
- F1-Score for all 5 domains: 1.00
- Inference Time: Under 5 milliseconds per job description

Output charts generated by the system:
- `job_category_confusion_matrix.png`: Confusion matrix verifying zero misclassifications across test samples.
- `job_role_clusters.png`: 2D PCA scatter plot showing clear cluster boundaries between skill families.
- `candidate_match_ranking.png`: Match score bar chart ranking candidate suitability.

---

## Generating Presentations

You can regenerate the presentation files at any time using the included generator scripts:

To build the 12-slide PDF presentation with the Poppins font:
```bash
python generate_pdf_presentation.py
```

To build the PowerPoint (.pptx) presentation:
```bash
python generate_pptx_presentation.py
```

---

## License

This project is developed for educational and academic submission purposes.
