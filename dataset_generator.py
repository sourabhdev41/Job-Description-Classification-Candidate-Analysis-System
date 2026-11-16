import random
import pandas as pd

# 5 Major Categories
categories = [
    "Data Science & AI",
    "Software Development",
    "Cloud & DevOps",
    "Cybersecurity",
    "Product & Business Analysis"
]

jd_templates = {
    "Data Science & AI": [
        "Looking for a Data Scientist skilled in Python, machine learning, pandas, scikit-learn, and deep learning. Experience with SQL database queries, data visualization in Tableau or PowerBI, and model deployment.",
        "We need a Machine Learning Engineer to build predictive models, NLP pipelines, neural networks with PyTorch and TensorFlow. Strong knowledge of statistics, big data, and data cleaning required.",
        "Hiring an AI Analyst to work with statistical data, regression analysis, random forest, clustering algorithms, and data modeling. Must have solid Python, NumPy, and SQL skills.",
        "Seeking Senior Data Analyst to analyze business datasets, generate dashboards, perform A/B testing, and extract customer trends using SQL, Python, R, and Excel.",
        "Machine Learning Specialist wanted for computer vision, natural language processing, LLM fine-tuning, vector search, and feature engineering with high dimensional datasets."
    ],
    "Software Development": [
        "Seeking Full Stack Developer experienced in JavaScript, React.js, Node.js, Express, MongoDB, and REST APIs. Candidate must write clean code and build responsive user interfaces.",
        "Hiring Backend Software Engineer with strong Java, Spring Boot, microservices architecture, MySQL, and Redis. Knowledge of Git version control, unit testing, and API integration.",
        "Looking for a Frontend Engineer proficient in HTML, CSS, JavaScript, TypeScript, React, Next.js, and Tailwind CSS. Experience in website optimization and cross-browser support.",
        "We need a Python Software Developer skilled in Django, Flask, PostgreSQL, Celery, and building scalable backend systems with asynchronous tasks and automated testing.",
        "Mobile App Developer needed with Flutter, Dart, Android SDK, iOS development, state management with Bloc or Provider, and Firebase backend integration."
    ],
    "Cloud & DevOps": [
        "Hiring DevOps Engineer with strong expertise in Docker, Kubernetes, Linux system administration, CI/CD pipelines with Jenkins and GitHub Actions. Experience with AWS cloud infrastructure.",
        "Looking for a Cloud Solutions Architect with AWS, Azure, Terraform, Infrastructure as Code, VPC configuration, IAM security policies, and cloud cost management.",
        "Site Reliability Engineer (SRE) needed to manage production servers, monitoring with Prometheus and Grafana, incident handling, Bash scripting, and automated deployment.",
        "We need a Platform Engineer with Kubernetes cluster management, Helm charts, Ansible configuration, Docker containerization, and Google Cloud Platform (GCP).",
        "Cloud DevOps Specialist wanted to automate code delivery, manage microservices deployment on AWS ECS, write Terraform scripts, and ensure 99.9% uptime."
    ],
    "Cybersecurity": [
        "Hiring Cybersecurity Analyst for vulnerability assessment, penetration testing, network security monitoring, firewall configuration, and incident response handling.",
        "Looking for an Information Security Specialist experienced in ethical hacking, SIEM tools like Splunk, malware analysis, threat detection, and security compliance ISO 27001.",
        "We need a Security Engineer to perform code audits, secure API design, cryptography, zero trust architecture, OWASP top 10 remediation, and intrusion prevention.",
        "SOC Analyst needed for 24/7 security log monitoring, detecting phishing attacks, analyzing network packets with Wireshark, and handling security incident containment.",
        "Penetration Tester wanted with Kali Linux, Metasploit, Burp Suite, web application security testing, network scanning, and creating risk assessment reports."
    ],
    "Product & Business Analysis": [
        "Looking for a Technical Product Manager to define product roadmaps, write user stories, coordinate between engineering and design teams, and track Agile Scrum sprints.",
        "Hiring Business Analyst with experience in requirements gathering, process flow mapping, SQL data queries, stakeholder communication, and creating functional requirement documents.",
        "Product Owner needed to prioritize product backlog, conduct user research, analyze customer feedback, track KPI metrics, and run daily standup meetings in Jira.",
        "Seeking Senior Business Systems Analyst to bridge gap between business operations and IT, create wireframes, evaluate vendor tools, and document workflow diagrams.",
        "Product Operations Specialist to analyze feature adoption metrics, conduct competitor market research, run customer surveys, and assist development roadmap planning."
    ]
}

skills_bank = {
    "Data Science & AI": ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "SQL", "Pandas", "Scikit-Learn", "NLP", "Tableau", "PowerBI", "Statistics"],
    "Software Development": ["Java", "Spring Boot", "React", "Node.js", "JavaScript", "TypeScript", "Python", "Django", "REST API", "MongoDB", "PostgreSQL", "Git", "HTML/CSS"],
    "Cloud & DevOps": ["AWS", "Docker", "Kubernetes", "Linux", "Terraform", "CI/CD", "Jenkins", "Ansible", "Bash Scripting", "Prometheus", "Grafana", "Azure", "GCP"],
    "Cybersecurity": ["Network Security", "Ethical Hacking", "Penetration Testing", "SIEM", "Splunk", "Firewalls", "OWASP", "Wireshark", "Kali Linux", "Vulnerability Assessment", "Cryptography"],
    "Product & Business Analysis": ["Agile", "Scrum", "Jira", "Product Roadmap", "User Stories", "SQL", "Wireframing", "Market Research", "Business Requirements", "Data Analysis", "Communication"]
}

def generate_datasets():
    random.seed(42)
    jd_records = []

    # Generate 600 Job Descriptions (120 per category)
    for cat in categories:
        templates = jd_templates[cat]
        skill_list = skills_bank[cat]
        for i in range(120):
            base_text = random.choice(templates)
            extra_skills = random.sample(skill_list, k=4)
            full_text = f"{base_text} Key required tools and competencies: {', '.join(extra_skills)}. Minimum 2+ years practical industry experience required."
            jd_records.append({
                "job_id": f"JOB_{len(jd_records)+1:04d}",
                "category": cat,
                "job_description": full_text
            })

    df_jobs = pd.DataFrame(jd_records)
    df_jobs.to_csv("job_descriptions.csv", index=False)
    print(f"Created job_descriptions.csv with {len(df_jobs)} jobs.")

    # Generate 15 Realistic Candidate Profiles
    candidates = [
        ("Aarav Sharma", "Data Science & AI", "B.Tech Computer Science", 3, ["Python", "Machine Learning", "Pandas", "Scikit-Learn", "SQL", "Data Analysis", "Tableau"], "Experienced Data Scientist with 3 years building predictive models and data pipelines in Python and SQL."),
        ("Priya Patel", "Data Science & AI", "M.Tech Data Science", 2, ["Python", "Deep Learning", "PyTorch", "NLP", "TensorFlow", "Statistics"], "AI enthusiast specializing in NLP text processing and neural networks using PyTorch and Python."),
        ("Rohan Verma", "Software Development", "B.E. Information Technology", 4, ["Java", "Spring Boot", "Microservices", "MySQL", "REST API", "Git", "Docker"], "Backend Developer with 4 years building enterprise microservices using Java, Spring Boot, and MySQL."),
        ("Sneha Iyer", "Software Development", "BCA / MCA", 2, ["JavaScript", "React", "Node.js", "HTML/CSS", "MongoDB", "Express"], "Full Stack Web Developer with 2 years creating responsive single page web apps in React and Node.js."),
        ("Aditya Nair", "Cloud & DevOps", "B.Tech Electronics", 3, ["AWS", "Docker", "Kubernetes", "CI/CD", "Terraform", "Linux"], "Cloud Engineer specializing in AWS containerization with Docker and Kubernetes and CI/CD pipelines."),
        ("Ananya Rao", "Cloud & DevOps", "B.Tech Computer Science", 4, ["Linux", "Jenkins", "Ansible", "Kubernetes", "Prometheus", "Bash Scripting"], "DevOps Engineer focusing on Linux automation, CI/CD pipelines, and Kubernetes infrastructure monitoring."),
        ("Kavita Joshi", "Cybersecurity", "B.Tech Cyber Security", 3, ["Ethical Hacking", "Penetration Testing", "Kali Linux", "OWASP", "Burp Suite", "Network Security"], "Penetration Tester and security analyst with 3 years testing web apps and identifying vulnerabilities."),
        ("Manish Gupta", "Cybersecurity", "B.Sc Computer Science", 2, ["SIEM", "Splunk", "Network Security", "Wireshark", "Firewalls", "Incident Response"], "SOC Security Analyst skilled in log monitoring using Splunk, traffic analysis, and firewall configuration."),
        ("Pooja Deshmukh", "Product & Business Analysis", "B.Tech + MBA", 4, ["Agile", "Scrum", "Jira", "User Stories", "Product Roadmap", "Market Research"], "Product Manager with 4 years managing product backlogs, running Scrum sprints, and writing user stories."),
        ("Vikram Malhotra", "Product & Business Analysis", "B.Com + Business Analytics", 3, ["Business Requirements", "SQL", "Jira", "Wireframing", "Data Analysis", "Communication"], "Business Analyst with 3 years translating client business needs into functional requirements and SQL reports."),
        ("Harshit Srivastava", "Software Development", "B.Tech Computer Science", 1, ["Python", "Django", "PostgreSQL", "Git", "REST API"], "Junior Python developer with 1 year experience building REST APIs with Django and PostgreSQL."),
        ("Neha Saxena", "Data Science & AI", "M.Sc Statistics", 3, ["Python", "R", "Statistics", "Machine Learning", "PowerBI", "SQL"], "Statistical Data Analyst with 3 years experience in predictive regression and business intelligence reporting."),
        ("Siddharth Mehra", "Cloud & DevOps", "B.E. Information Technology", 2, ["Azure", "Docker", "Linux", "Terraform", "CI/CD"], "Cloud Specialist with 2 years deploying infrastructure on Microsoft Azure and automating pipelines."),
        ("Meera Chawla", "Cybersecurity", "B.Tech Information Security", 2, ["Vulnerability Assessment", "OWASP", "Cryptography", "Network Security", "Linux"], "Information Security Associate skilled in OWASP top 10 testing and vulnerability assessments."),
        ("Tarun Kapoor", "Product & Business Analysis", "BBA + MBA", 2, ["Agile", "Jira", "Communication", "Data Analysis", "User Stories"], "Associate Product Owner experienced in sprint planning and customer feedback analysis.")
    ]

    candidate_records = []
    for cid, (name, domain, edu, exp, skills, summary) in enumerate(candidates, 1):
        candidate_records.append({
            "candidate_id": f"CAN_{cid:03d}",
            "name": name,
            "primary_domain": domain,
            "education": edu,
            "experience_years": exp,
            "skills": ", ".join(skills),
            "resume_text": f"{summary} Education: {edu}. Skills: {', '.join(skills)}. Total Experience: {exp} years."
        })

    df_cand = pd.DataFrame(candidate_records)
    df_cand.to_csv("candidate_resumes.csv", index=False)
    print(f"Created candidate_resumes.csv with {len(df_cand)} candidate profiles.")

if __name__ == "__main__":
    generate_datasets()
