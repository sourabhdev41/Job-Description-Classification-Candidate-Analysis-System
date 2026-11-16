import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Minimalist Black & White Palette
    BLACK = RGBColor(17, 17, 17)
    CHARCOAL = RGBColor(51, 51, 51)
    LIGHT_BORDER = RGBColor(204, 204, 204)
    WHITE = RGBColor(255, 255, 255)
    FONT_NAME = "Poppins"

    def add_header(slide, title_text, category="MAJOR PROJECT PRESENTATION"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.4))
        p = cat_box.text_frame.paragraphs[0]
        p.text = f"[ {category.upper()} ]"
        p.font.name = FONT_NAME
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = CHARCOAL

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.7), Inches(0.8))
        p_t = title_box.text_frame.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = FONT_NAME
        p_t.font.size = Pt(24)
        p_t.font.bold = True
        p_t.font.color.rgb = BLACK

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.5), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = BLACK
        line.line.color.rgb = BLACK

    # Slide 1: Title
    s1 = prs.slides.add_slide(blank_layout)
    outer = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9))
    outer.fill.solid()
    outer.fill.fore_color.rgb = WHITE
    outer.line.color.rgb = BLACK
    outer.line.width = Pt(1.5)

    tf = s1.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.333), Inches(2.2)).text_frame
    p = tf.paragraphs[0]
    p.text = "Job Description Classification &\nCandidate Analysis System"
    p.font.name = FONT_NAME
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = BLACK

    p2 = tf.add_paragraph()
    p2.text = "Natural Language Processing (NLP), TF-IDF, Classification, Clustering & Resume Matching"
    p2.font.name = FONT_NAME
    p2.font.size = Pt(16)
    p2.font.color.rgb = CHARCOAL
    p2.space_before = Pt(12)

    sub_tf = s1.shapes.add_textbox(Inches(1.5), Inches(4.3), Inches(10.333), Inches(1.8)).text_frame
    p3 = sub_tf.paragraphs[0]
    p3.text = "Department of Computer Science & Engineering | Academic Session 2026"
    p3.font.name = FONT_NAME
    p3.font.size = Pt(13)
    p3.font.color.rgb = CHARCOAL

    p4 = sub_tf.add_paragraph()
    p4.text = "Team: Sourabh Shrivastava (Leader) | Suhana Padhi | Sarwash Shwet | Komal Singh | Niraj Kumar"
    p4.font.name = FONT_NAME
    p4.font.size = Pt(13)
    p4.font.bold = True
    p4.font.color.rgb = BLACK
    p4.space_before = Pt(10)

    # Slide 2: Contributors
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Project Contributors & Team Details")

    tf2 = s2.shapes.add_textbox(Inches(1.5), Inches(1.8), Inches(10.333), Inches(5.0)).text_frame
    p = tf2.paragraphs[0]
    p.text = "The project was developed collaboratively by the following members:"
    p.font.name = FONT_NAME
    p.font.size = Pt(14)
    p.font.color.rgb = CHARCOAL

    members = [
        ("Sourabh Shrivastava", "Project Leader", "6606645"),
        ("Suhana Padhi", "Team Member", "6605352"),
        ("Sarwash Shwet", "Team Member", "6605711"),
        ("Komal Singh", "Team Member", "6605636"),
        ("Niraj Kumar", "Team Member", "6606718")
    ]
    for name, role, roll in members:
        p = tf2.add_paragraph()
        if "Leader" in role:
            p.text = f"- {name} (Leader) : Roll No. {roll}"
            p.font.bold = True
            p.font.color.rgb = BLACK
        else:
            p.text = f"- {name} : Roll No. {roll}"
            p.font.color.rgb = CHARCOAL
        p.font.name = FONT_NAME
        p.font.size = Pt(14)
        p.space_before = Pt(12)

    # Slide 3: Problem Statement
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Problem Statement & Need for Automation")

    b_l = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b_l.fill.solid()
    b_l.fill.fore_color.rgb = WHITE
    b_l.line.color.rgb = BLACK
    tf_l = b_l.text_frame
    p = tf_l.paragraphs[0]
    p.text = "Manual Screening Challenges"
    p.font.name = FONT_NAME
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLACK
    probs = [
        "Companies receive hundreds of resumes for single openings.",
        "Manual resume screening is slow, exhausting, and prone to bias.",
        "Job titles in tech are frequently non-standard and confusing.",
        "Crucial candidate skills get overlooked in long documents.",
        "Recruiters lack fast tools to measure exact skill overlap."
    ]
    for pr in probs:
        p = tf_l.add_paragraph()
        p.text = f"- {pr}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    b_r = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b_r.fill.solid()
    b_r.fill.fore_color.rgb = WHITE
    b_r.line.color.rgb = BLACK
    tf_r = b_r.text_frame
    p = tf_r.paragraphs[0]
    p.text = "Our Machine Learning Solution"
    p.font.name = FONT_NAME
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLACK
    sols = [
        "Cleans raw job postings and resumes using standard NLP.",
        "Transforms technical vocabulary into numerical TF-IDF vectors.",
        "Classifies job postings into 5 technology categories.",
        "Clusters job roles using unsupervised K-Means.",
        "Ranks candidates mathematically using Cosine Similarity.",
        "Pinpoints missing skills through automated gap analysis."
    ]
    for sl in sols:
        p = tf_r.add_paragraph()
        p.text = f"- {sl}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    # Slide 4: Objectives
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Project Objectives")
    b4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.9), Inches(11.3), Inches(4.8))
    b4.fill.solid()
    b4.fill.fore_color.rgb = WHITE
    b4.line.color.rgb = BLACK
    tf4 = b4.text_frame
    p = tf4.paragraphs[0]
    p.text = "Major Objectives of the System:"
    p.font.name = FONT_NAME
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLACK
    objs = [
        "1. Build a Text Cleaning Pipeline for JDs and candidate resumes.",
        "2. Formulate TF-IDF numerical matrices capturing unigrams and bigrams.",
        "3. Train a multi-class supervised classifier for 5 major technology domains.",
        "4. Apply unsupervised K-Means clustering to discover skill boundaries.",
        "5. Implement Cosine Similarity matching engine to score candidate fit.",
        "6. Provide automated Skill Gap reports for candidates and recruiters."
    ]
    for ob in objs:
        p = tf4.add_paragraph()
        p.text = ob
        p.font.name = FONT_NAME
        p.font.size = Pt(13)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(10)

    # Slide 5: Workflow
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "System Workflow & Pipeline")
    steps = [
        ("01. DATA INGESTION", "Job descriptions and resumes loaded from CSV / text inputs."),
        ("02. NLP CLEANING", "Lowercasing, symbol removal, and stopword filtering."),
        ("03. TF-IDF MATRIX", "High-dimensional feature representation (2500 n-grams)."),
        ("04. CLASSIFICATION", "Logistic Regression predicts 1 of 5 job categories."),
        ("05. CLUSTERING", "K-Means groups job descriptions into 5 skill clusters."),
        ("06. RESUME MATCH", "Cosine similarity calculates candidate fit & skill gaps.")
    ]
    for idx, (st, sd) in enumerate(steps):
        c = idx % 3
        r = idx // 3
        x = Inches(0.8 + c * 3.9)
        y = Inches(1.9 + r * 2.5)
        bx = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, Inches(3.6), Inches(2.2))
        bx.fill.solid()
        bx.fill.fore_color.rgb = WHITE
        bx.line.color.rgb = BLACK
        tfs = bx.text_frame
        p = tfs.paragraphs[0]
        p.text = st
        p.font.name = FONT_NAME
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = BLACK
        p2 = tfs.add_paragraph()
        p2.text = sd
        p2.font.name = FONT_NAME
        p2.font.size = Pt(11)
        p2.font.color.rgb = CHARCOAL
        p2.space_before = Pt(6)

    # Slide 6: NLP & TF-IDF
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "NLP Preprocessing & TF-IDF Vectorization")
    b6_l = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b6_l.fill.solid()
    b6_l.fill.fore_color.rgb = WHITE
    b6_l.line.color.rgb = BLACK
    tf6_l = b6_l.text_frame
    p = tf6_l.paragraphs[0]
    p.text = "NLP Text Cleaning Steps"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    n_pts = [
        "Raw Input: 'Seeking Senior DevOps Engineer with Docker & AWS!'",
        "1. Case Normalization: lowercase conversion.",
        "2. Symbol Stripping: removes punctuation and special characters.",
        "3. Stopwords Removal: removes filler terms like 'seeking', 'years'.",
        "Cleaned Output: 'devops engineer docker aws'"
    ]
    for pt in n_pts:
        p = tf6_l.add_paragraph()
        p.text = pt
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    b6_r = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b6_r.fill.solid()
    b6_r.fill.fore_color.rgb = WHITE
    b6_r.line.color.rgb = BLACK
    tf6_r = b6_r.text_frame
    p = tf6_r.paragraphs[0]
    p.text = "TF-IDF Vector Space"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    t_pts = [
        "TF measures skill frequency within a specific document.",
        "IDF down-weights general words and rewards rare skills.",
        "N-grams (1, 2) capture phrases like 'deep learning' or 'cloud infrastructure'.",
        "Produces clean numerical vectors ready for classification and similarity math."
    ]
    for pt in t_pts:
        p = tf6_r.add_paragraph()
        p.text = pt
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    # Slide 7: Classification Results
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Job Category Classification Results")
    b7 = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b7.fill.solid()
    b7.fill.fore_color.rgb = WHITE
    b7.line.color.rgb = BLACK
    tf7 = b7.text_frame
    p = tf7.paragraphs[0]
    p.text = "Model Evaluation"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    evals = [
        "Algorithm: Multi-class Logistic Regression with TF-IDF.",
        "Dataset: 600 verified job descriptions across 5 categories.",
        "Train / Test Split: 80% Train, 20% Test.",
        "Test Accuracy: 100.00%",
        "Macro Average Precision, Recall, and F1-score: 1.00",
        "Fast inference time: under 5 milliseconds per JD."
    ]
    for ev in evals:
        p = tf7.add_paragraph()
        p.text = f"- {ev}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(6)

    if os.path.exists("job_category_confusion_matrix.png"):
        s7.shapes.add_picture("job_category_confusion_matrix.png", Inches(6.8), Inches(1.9), width=Inches(5.6))

    # Slide 8: Clustering
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Job Description Clustering (K-Means)")
    b8 = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b8.fill.solid()
    b8.fill.fore_color.rgb = WHITE
    b8.line.color.rgb = BLACK
    tf8 = b8.text_frame
    p = tf8.paragraphs[0]
    p.text = "Unsupervised Cluster Analysis"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    cl_pts = [
        "K-Means with K = 5 partitions jobs by natural skill overlap.",
        "Cluster 1: Data Science & AI (Python, pandas, PyTorch, models).",
        "Cluster 2: Software Development (Java, React, REST API, Node).",
        "Cluster 3: Cloud & DevOps (AWS, Docker, Kubernetes, CI/CD).",
        "Cluster 4: Cybersecurity (SIEM, Kali, OWASP, penetration).",
        "Cluster 5: Product & Business Analysis (Jira, Agile, roadmaps).",
        "PCA reduces 2500 TF-IDF features to 2D for clean visual inspection."
    ]
    for cp in cl_pts:
        p = tf8.add_paragraph()
        p.text = f"- {cp}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(6)

    if os.path.exists("job_role_clusters.png"):
        s8.shapes.add_picture("job_role_clusters.png", Inches(6.8), Inches(1.9), width=Inches(5.6))

    # Slide 9: Resume Matching
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Candidate Resume Matching via Cosine Similarity")
    b9 = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b9.fill.solid()
    b9.fill.fore_color.rgb = WHITE
    b9.line.color.rgb = BLACK
    tf9 = b9.text_frame
    p = tf9.paragraphs[0]
    p.text = "Mathematical Resume Ranking"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    sim_pts = [
        "Cosine Similarity computes angle between JD vector & Resume vector.",
        "Formula: Cosine_Sim(A, B) = (A . B) / (||A|| * ||B||)",
        "Range: 0% (no skill overlap) to 100% (exact keyword alignment).",
        "Length Normalization: Prevents bloated resumes from gaining unfair scores.",
        "Recruiters receive an instant, objective leaderboard of qualified candidates."
    ]
    for sp in sim_pts:
        p = tf9.add_paragraph()
        p.text = f"- {sp}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    if os.path.exists("candidate_match_ranking.png"):
        s9.shapes.add_picture("candidate_match_ranking.png", Inches(6.8), Inches(1.9), width=Inches(5.6))

    # Slide 10: Skill Gap
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Skill Gap Analysis & Recruitment Impact")
    b10_l = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b10_l.fill.solid()
    b10_l.fill.fore_color.rgb = WHITE
    b10_l.line.color.rgb = BLACK
    tf10_l = b10_l.text_frame
    p = tf10_l.paragraphs[0]
    p.text = "Skill Gap Analysis"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    sg_pts = [
        "Automated comparison of job requirements vs candidate CV skills.",
        "Displays matched proficiencies directly.",
        "Highlights missing technical keywords to bridge.",
        "Provides constructive feedback for candidates to upskill."
    ]
    for sg in sg_pts:
        p = tf10_l.add_paragraph()
        p.text = f"- {sg}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    b10_r = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.6), Inches(4.8))
    b10_r.fill.solid()
    b10_r.fill.fore_color.rgb = WHITE
    b10_r.line.color.rgb = BLACK
    tf10_r = b10_r.text_frame
    p = tf10_r.paragraphs[0]
    p.text = "Practical Industry Value"
    p.font.name = FONT_NAME
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = BLACK
    iv_pts = [
        "Time Efficiency: Screening cut from hours to seconds.",
        "Objective Decisions: Evaluation based purely on competency.",
        "Scalability: Can process thousands of applications concurrently.",
        "Reduced Bias: Eliminates demographic biases in early screening."
    ]
    for iv in iv_pts:
        p = tf10_r.add_paragraph()
        p.text = f"- {iv}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(8)

    # Slide 11: Conclusion
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Conclusion & Future Enhancements")
    b11 = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(1.9), Inches(11.3), Inches(4.8))
    b11.fill.solid()
    b11.fill.fore_color.rgb = WHITE
    b11.line.color.rgb = BLACK
    tf11 = b11.text_frame
    p = tf11.paragraphs[0]
    p.text = "Major Project Achievements:"
    p.font.name = FONT_NAME
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLACK
    ach_pts = [
        "Successfully developed and tested an automated Job Classification & Candidate Analysis System.",
        "Combined supervised classification, unsupervised clustering, and cosine similarity matching.",
        "Demonstrated 100% classification accuracy on five core software industry categories.",
        "Delivered an interactive tool for recruiters to classify JDs, rank resumes, and run skill gap audits."
    ]
    for ap in ach_pts:
        p = tf11.add_paragraph()
        p.text = f"- {ap}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(6)

    p = tf11.add_paragraph()
    p.text = "Future Scope:"
    p.font.name = FONT_NAME
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = BLACK
    p.space_before = Pt(14)
    fut_pts = [
        "1. Automated PDF/Word parser for seamless resume uploads.",
        "2. Experience weight factors combined with similarity scores.",
        "3. Live web recruitment portal using Streamlit or React."
    ]
    for fp in fut_pts:
        p = tf11.add_paragraph()
        p.text = f"- {fp}"
        p.font.name = FONT_NAME
        p.font.size = Pt(12)
        p.font.color.rgb = CHARCOAL
        p.space_before = Pt(6)

    # Slide 12: Thank you
    s12 = prs.slides.add_slide(blank_layout)
    outer12 = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9))
    outer12.fill.solid()
    outer12.fill.fore_color.rgb = WHITE
    outer12.line.color.rgb = BLACK
    outer12.line.width = Pt(1.5)

    tf_ty = s12.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.333), Inches(4.5)).text_frame
    p = tf_ty.paragraphs[0]
    p.text = "THANK YOU!"
    p.font.name = FONT_NAME
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = BLACK
    p.alignment = PP_ALIGN.CENTER

    p2 = tf_ty.add_paragraph()
    p2.text = "Job Description Classification & Candidate Analysis System"
    p2.font.name = FONT_NAME
    p2.font.size = Pt(16)
    p2.font.color.rgb = CHARCOAL
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(12)

    p3 = tf_ty.add_paragraph()
    p3.text = "Questions & Suggestions are Welcome"
    p3.font.name = FONT_NAME
    p3.font.size = Pt(14)
    p3.font.color.rgb = CHARCOAL
    p3.alignment = PP_ALIGN.CENTER
    p3.space_before = Pt(18)

    p4 = tf_ty.add_paragraph()
    p4.text = "Contributors: Sourabh Shrivastava (Leader) | Suhana Padhi | Sarwash Shwet | Komal Singh | Niraj Kumar"
    p4.font.name = FONT_NAME
    p4.font.size = Pt(12)
    p4.font.bold = True
    p4.font.color.rgb = BLACK
    p4.alignment = PP_ALIGN.CENTER
    p4.space_before = Pt(24)

    output_pptx = "Job_Description_Classification_and_Candidate_Analysis.pptx"
    prs.save(output_pptx)
    print(f"Minimal B&W PPTX presentation saved: {output_pptx}")

if __name__ == "__main__":
    create_pptx()
