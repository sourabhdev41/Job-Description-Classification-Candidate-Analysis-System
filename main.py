import os
import sys
from job_candidate_system import JobCandidateSystem, clean_text
from sklearn.metrics.pairwise import cosine_similarity

def print_banner():
    print("=" * 70)
    print("   JOB DESCRIPTION CLASSIFICATION & CANDIDATE ANALYSIS SYSTEM")
    print("=" * 70)
    print("Project Contributors:")
    print(" - Sourabh Shrivastava (Leader) - 6606645")
    print(" - Suhana Padhi - 6605352")
    print(" - Sarwash Shwet - 6605711")
    print(" - Komal Singh - 6605636")
    print(" - Niraj Kumar - 6606718")
    print("=" * 70)

def skill_gap_analysis(system, target_text, candidate_name):
    # Match candidate in df
    matches = system.df_candidates[system.df_candidates["name"].str.lower() == candidate_name.lower()]
    if matches.empty:
        print(f"Candidate '{candidate_name}' not found.")
        return

    cand_row = matches.iloc[0]
    cand_skills = [s.strip().lower() for s in cand_row["skills"].split(",")]
    
    # Common tech words in JD
    jd_words = set(clean_text(target_text).split())
    
    matched = [s for s in cand_skills if any(w in s for w in jd_words)]
    missing_in_candidate = [w for w in ["docker", "kubernetes", "aws", "python", "sql", "react", "java", "jira", "linux", "siem", "terraform", "ci/cd"] if w in jd_words and not any(w in s for s in cand_skills)]
    
    print("\n--- Skill Gap Analysis ---")
    print(f"Candidate: {cand_row['name']} ({cand_row['primary_domain']})")
    print(f"Candidate's Registered Skills: {cand_row['skills']}")
    print(f"Matched Skills with JD: {', '.join(matched) if matched else 'None detected'}")
    print(f"Missing Key Skills to Learn for this Job: {', '.join(missing_in_candidate) if missing_in_candidate else 'No major gaps found'}")

def main():
    print_banner()

    if not os.path.exists("job_descriptions.csv") or not os.path.exists("candidate_resumes.csv"):
        print("Generating required datasets first...")
        from dataset_generator import generate_datasets
        generate_datasets()

    system = JobCandidateSystem()
    system.load_and_preprocess()
    system.train_job_classifier()
    system.cluster_jobs()

    print("\nSystem initialization complete. All machine learning models ready.")

    while True:
        print("\n" + "-" * 50)
        print("Main Menu:")
        print("1. Enter a Job Description (Classify & Rank Candidates)")
        print("2. Test with Built-in Sample Job Descriptions")
        print("3. Check Skill Gap for a Candidate against a Job")
        print("4. View All Candidates in Database")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\nEnter or paste the Job Description text below:")
            jd_input = input("> ").strip()
            if not jd_input:
                print("Input is empty. Returning to menu.")
                continue

            res = system.match_candidates_for_job(jd_input, top_n=5)
            print("\n" + "=" * 50)
            print(f"Predicted Job Category : {res['predicted_category']}")
            print(f"Classification Confidence: {res['category_confidence']}")
            print("=" * 50)
            print("Top Matched Candidates (Ranked by Cosine Similarity):")
            for idx, cand in enumerate(res["ranked_candidates"], 1):
                print(f" {idx}. {cand['name']}")
                print(f"    Domain: {cand['primary_domain']} | Experience: {cand['experience_years']} yrs")
                print(f"    Match Score: {cand['similarity_score']:.1f}%")
                print(f"    Skills: {cand['skills']}")
        elif choice == "2":
            samples = [
                ("Machine Learning Engineer", "Hiring a Data Scientist experienced in Python, scikit-learn, PyTorch, pandas, machine learning, and deep learning algorithms with SQL database."),
                ("Full Stack Web Developer", "Looking for React developer with JavaScript, Node.js, Express, HTML/CSS, REST API, MongoDB, and frontend optimization."),
                ("SOC Cybersecurity Specialist", "Need Information Security Analyst for SIEM monitoring using Splunk, firewall management, threat incident response, and Wireshark.")
            ]
            print("\nRunning Sample Job Tests:")
            for title, desc in samples:
                print("\n" + "=" * 50)
                print(f"Testing Job: {title}")
                res = system.match_candidates_for_job(desc, top_n=3, save_plot=False)
                print(f"Predicted Category: {res['predicted_category']} ({res['category_confidence']})")
                print("Top Matched Candidate:")
                top1 = res["ranked_candidates"][0]
                print(f" -> {top1['name']} ({top1['primary_domain']}) - Match: {top1['similarity_score']:.1f}%")
        elif choice == "3":
            print("\nEnter Job Description:")
            jd_text = input("> ").strip()
            print("Enter Candidate Name (e.g. Aarav Sharma, Ananya Rao, Sneha Iyer):")
            cand_name = input("> ").strip()
            if jd_text and cand_name:
                skill_gap_analysis(system, jd_text, cand_name)
        elif choice == "4":
            print("\nRegistered Candidates in System:")
            for idx, row in system.df_candidates.iterrows():
                print(f"{idx+1:2d}. {row['name']} | {row['primary_domain']} | Exp: {row['experience_years']} yrs | Skills: {row['skills']}")
        elif choice == "5":
            print("\nExiting system. Thank you!")
            break
        else:
            print("Invalid option. Please choose 1 to 5.")

if __name__ == "__main__":
    main()
