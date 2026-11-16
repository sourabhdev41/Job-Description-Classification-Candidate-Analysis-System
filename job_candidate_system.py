import re
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# English stopwords set
STOPWORDS = set([
    "i", "me", "my", "we", "our", "you", "your", "he", "she", "it", "they", "them",
    "what", "which", "who", "this", "that", "these", "those", "am", "is", "are", "was",
    "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by",
    "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
    "under", "again", "then", "once", "here", "there", "when", "where", "why", "how", "all",
    "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just",
    "should", "now", "looking", "seeking", "wanted", "needed", "hiring", "experience",
    "years", "work", "must", "required", "role", "candidate"
])

# Minimalist illustrative styling configuration for plots
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.edgecolor'] = '#111111'
plt.rcParams['axes.linewidth'] = 1.2

def clean_text(text):
    """
    Cleans raw job descriptions or resume text:
    - Lowercase conversion
    - Replaces non-alphabet characters with spaces
    - Filters out stop words and short tokens
    """
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    words = text.split()
    cleaned = [w for w in words if w not in STOPWORDS and len(w) > 2]
    return " ".join(cleaned)

class JobCandidateSystem:
    def __init__(self, jobs_csv="job_descriptions.csv", candidates_csv="candidate_resumes.csv"):
        self.jobs_csv = jobs_csv
        self.candidates_csv = candidates_csv
        self.df_jobs = None
        self.df_candidates = None
        self.vectorizer = TfidfVectorizer(max_features=2500, ngram_range=(1, 2))
        self.classifier = LogisticRegression(max_iter=1000)
        self.kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
        self.categories = []

    def load_and_preprocess(self):
        print("[Step 1] Loading Job Descriptions & Candidate Resumes...")
        self.df_jobs = pd.read_csv(self.jobs_csv)
        self.df_candidates = pd.read_csv(self.candidates_csv)

        self.df_jobs["cleaned_jd"] = self.df_jobs["job_description"].apply(clean_text)
        self.df_candidates["cleaned_resume"] = self.df_candidates["resume_text"].apply(clean_text)
        self.categories = sorted(list(self.df_jobs["category"].unique()))

        print(f"Loaded {len(self.df_jobs)} Job Descriptions across {len(self.categories)} domains.")
        print(f"Loaded {len(self.df_candidates)} Candidate Resumes.")

    def train_job_classifier(self):
        print("\n[Step 2] Training Job Category Classifier (TF-IDF + Logistic Regression)...")
        X = self.vectorizer.fit_transform(self.df_jobs["cleaned_jd"])
        y = self.df_jobs["category"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.20, random_state=42, stratify=y
        )

        self.classifier.fit(X_train, y_train)
        predictions = self.classifier.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)

        print(f"Job Classification Accuracy: {accuracy * 100:.2f}%\n")
        print("Detailed Classification Report:")
        print(classification_report(y_test, predictions))

        # Minimal black and white confusion matrix with crisp line borders
        cm = confusion_matrix(y_test, predictions, labels=self.categories)
        plt.figure(figsize=(7.5, 5.5), facecolor='white')
        sns.heatmap(cm, annot=True, fmt='d', cmap='Greys', cbar=False,
                    xticklabels=self.categories, yticklabels=self.categories,
                    linewidths=1, linecolor='#111111')
        plt.title("Confusion Matrix - Job Category Classification", fontsize=12, fontweight='bold', pad=12, color='#111111')
        plt.xlabel("Predicted Category", fontsize=10, fontweight='bold', color='#111111')
        plt.ylabel("Actual Category", fontsize=10, fontweight='bold', color='#111111')
        plt.xticks(rotation=35, ha='right', color='#111111')
        plt.yticks(color='#111111')
        plt.tight_layout()
        plt.savefig("job_category_confusion_matrix.png", dpi=200, facecolor='white')
        plt.close()
        print("Saved: job_category_confusion_matrix.png")

    def cluster_jobs(self):
        print("\n[Step 3] Clustering Job Descriptions with K-Means...")
        X = self.vectorizer.transform(self.df_jobs["cleaned_jd"])
        self.df_jobs["cluster"] = self.kmeans.fit_predict(X)

        # 2D PCA Visualization with clean monochrome markers
        pca = PCA(n_components=2, random_state=42)
        reduced = pca.fit_transform(X.toarray())
        self.df_jobs["pca_x"] = reduced[:, 0]
        self.df_jobs["pca_y"] = reduced[:, 1]

        plt.figure(figsize=(8, 5.5), facecolor='white')
        markers = ['o', 's', '^', 'D', 'v']
        grays = ['#111111', '#444444', '#777777', '#aaaaaa', '#cccccc']
        for cluster_id in range(5):
            sub = self.df_jobs[self.df_jobs["cluster"] == cluster_id]
            plt.scatter(sub["pca_x"], sub["pca_y"], label=f"Cluster {cluster_id + 1}",
                        marker=markers[cluster_id], color=grays[cluster_id],
                        edgecolors='#111111', linewidth=0.8, alpha=0.85, s=45)

        plt.title("Job Description Clusters (K-Means with PCA 2D)", fontsize=12, fontweight='bold', color='#111111')
        plt.xlabel("PCA Component 1", fontsize=10, fontweight='bold', color='#111111')
        plt.ylabel("PCA Component 2", fontsize=10, fontweight='bold', color='#111111')
        plt.legend(loc="upper right", frameon=True, edgecolor='#111111')
        plt.grid(True, linestyle=':', alpha=0.5, color='#888888')
        plt.tight_layout()
        plt.savefig("job_role_clusters.png", dpi=200, facecolor='white')
        plt.close()
        print("Saved: job_role_clusters.png")

    def match_candidates_for_job(self, target_job_text, top_n=5, save_plot=True):
        cleaned_target = clean_text(target_job_text)
        target_vec = self.vectorizer.transform([cleaned_target])

        candidate_vecs = self.vectorizer.transform(self.df_candidates["cleaned_resume"])
        similarities = cosine_similarity(target_vec, candidate_vecs).flatten()

        results = self.df_candidates.copy()
        results["similarity_score"] = similarities * 100
        results = results.sort_values(by="similarity_score", ascending=False).reset_index(drop=True)

        top_candidates = results.head(top_n)

        pred_cat = self.classifier.predict(target_vec)[0]
        confidence = np.max(self.classifier.predict_proba(target_vec)) * 100

        if save_plot:
            plt.figure(figsize=(7.5, 4.2), facecolor='white')
            bars = plt.barh(top_candidates["name"], top_candidates["similarity_score"],
                            color='#111111', edgecolor='#111111', linewidth=1.2)
            plt.gca().invert_yaxis()
            plt.title(f"Top Candidate Match Scores ({pred_cat})", fontsize=12, fontweight='bold', color='#111111')
            plt.xlabel("Match Percentage (%)", fontsize=10, fontweight='bold', color='#111111')
            plt.xlim(0, 100)
            plt.grid(axis='x', linestyle=':', alpha=0.5, color='#888888')
            for idx, score in enumerate(top_candidates["similarity_score"]):
                plt.text(score + 1.2, idx, f"{score:.1f}%", va='center', fontweight='bold', color='#111111')
            plt.tight_layout()
            plt.savefig("candidate_match_ranking.png", dpi=200, facecolor='white')
            plt.close()
            print("Saved: candidate_match_ranking.png")

        return {
            "predicted_category": pred_cat,
            "category_confidence": f"{confidence:.1f}%",
            "ranked_candidates": top_candidates[[
                "candidate_id", "name", "primary_domain", "experience_years", "skills", "similarity_score"
            ]].to_dict(orient="records")
        }

if __name__ == "__main__":
    system = JobCandidateSystem()
    system.load_and_preprocess()
    system.train_job_classifier()
    system.cluster_jobs()

    sample_job = (
        "We are hiring a Senior DevOps Engineer to lead our AWS cloud infrastructure. "
        "The ideal candidate must have hands-on experience with Docker containerization, "
        "Kubernetes cluster administration, Linux scripting, Terraform, and setting up CI/CD pipelines with Jenkins. "
        "Knowledge of Prometheus monitoring and Git version control is essential."
    )

    result = system.match_candidates_for_job(sample_job, top_n=5)
    print(f"\nPredicted Category: {result['predicted_category']} ({result['category_confidence']})")
