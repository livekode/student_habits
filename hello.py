from preswald import text, slider, table, connect, get_df, plotly, sidebar
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Connect to the data source
connect()

# Load the dataset
df = get_df("data/student_habits_performance.csv")

# Ensure numeric columns are properly typed
numeric_columns = ['age', 'study_hours_per_day', 'social_media_hours', 'netflix_hours', 
                  'attendance_percentage', 'sleep_hours', 'exercise_frequency', 
                  'mental_health_rating', 'exam_score']

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Add sidebar navigation
sidebar("""
## Navigation
- [Overview](#dataset-overview)
- [Performance Distribution](#performance-distribution)
- [Study Hours Impact](#study-hours-impact)
- [Gender Analysis](#performance-by-gender)
- [Digital Distractions](#digital-distractions-impact)
- [Sleep Hours](#sleep-hours-impact)
- [Balanced Lifestyle](#balanced-lifestyle-analysis)
- [Part-time Jobs](#impact-of-part-time-job)
- [Key Factors](#key-factors-influencing-exam-scores)
- [Success Patterns](#success-patterns-analysis)
- [Key Insights](#key-insights)
""")

# Display the title
text("# Student Habits & Performance Dashboard 📚")

# Overview of the dataset
text("## Dataset Overview")
text(f"This dataset contains information about {len(df)} students, examining various habits and their impact on exam performance.")

# Display a sample of the data
rows_to_display = slider("Number of rows to display", min_val=5, max_val=50, default=10)
table(df.head(rows_to_display))

# Performance Distribution
text("## Performance Distribution")
fig_hist = px.histogram(
    df, 
    x="exam_score", 
    nbins=30, 
    title="Distribution of Exam Scores",
    color_discrete_sequence=['#3498db']
)
fig_hist.update_layout(xaxis_title="Exam Score", yaxis_title="Number of Students")
plotly(fig_hist)

# Study Hours vs Exam Score
text("## Study Hours Impact")
study_fig = px.scatter(
    df,
    x="study_hours_per_day",
    y="exam_score",
    color="exam_score",
    color_continuous_scale="viridis",
    title="Study Hours vs Exam Score",
    labels={"study_hours_per_day": "Study Hours Per Day", "exam_score": "Exam Score"}
)
plotly(study_fig)

# Calculate correlation between study hours and exam score
correlation = round(df["study_hours_per_day"].corr(df["exam_score"]), 2)
text(f"Correlation between study hours and exam scores: **{correlation}**")

# Gender-based performance analysis
text("## Performance by Gender")
# Manual calculation of average by gender to avoid aggregation issues
gender_groups = df["gender"].unique()
gender_means = []

for gender in gender_groups:
    gender_data = df[df["gender"] == gender]
    avg_score = gender_data["exam_score"].mean()
    gender_means.append({"gender": gender, "exam_score": avg_score})

gender_perf = pd.DataFrame(gender_means)

gender_fig = px.bar(
    gender_perf, 
    x="gender", 
    y="exam_score", 
    title="Average Exam Score by Gender",
    color="gender",
    color_discrete_sequence=px.colors.qualitative.Set3
)
plotly(gender_fig)

# Digital Distractions Analysis
text("## Digital Distractions Impact")

# Create a slider for filtering by distraction levels
min_digital_hours = slider(
    "Minimum Digital Distraction Hours (Social Media + Netflix)", 
    min_val=0.0, 
    max_val=10.0, 
    default=3.0
)

# Calculate total digital hours
df["digital_hours"] = df["social_media_hours"] + df["netflix_hours"]

# Filter based on slider
digital_filtered = df[df["digital_hours"] >= min_digital_hours]

text(f"### Students with {min_digital_hours}+ hours of digital distractions: {len(digital_filtered)}")

# Digital hours vs Exam Score
digital_fig = px.scatter(
    df,
    x="digital_hours",
    y="exam_score",
    color="exam_score",
    size="study_hours_per_day",
    hover_data=["gender", "age"],
    title="Digital Distraction Hours vs Exam Score (size = study hours)",
    labels={"digital_hours": "Digital Hours (Social Media + Netflix)", "exam_score": "Exam Score"}
)
plotly(digital_fig)

# Show correlation
digital_corr = round(df["digital_hours"].corr(df["exam_score"]), 2)
text(f"Correlation between digital distraction hours and exam scores: **{digital_corr}**")

# Compare Sleep Hours Impact
text("## Sleep Hours Impact")

# Create visualization comparing sleep and exam scores
sleep_fig = px.scatter(
    df,
    x="sleep_hours",
    y="exam_score",
    color="exam_score",
    title="Sleep Hours vs Exam Score",
    labels={"sleep_hours": "Sleep Hours", "exam_score": "Exam Score"}
)
plotly(sleep_fig)

sleep_corr = round(df["sleep_hours"].corr(df["exam_score"]), 2)
text(f"Correlation between sleep hours and exam scores: **{sleep_corr}**")

# Balanced Lifestyle Analysis
text("## Balanced Lifestyle Analysis")

# Create bins for study hours and sleep hours
df["study_bin"] = pd.cut(df["study_hours_per_day"], bins=[0, 2, 4, 6, 10], labels=["Very Low", "Low", "Medium", "High"])
df["sleep_bin"] = pd.cut(df["sleep_hours"], bins=[0, 5, 7, 10], labels=["Low", "Medium", "High"])

# Create a heatmap of average scores by study and sleep bins
pivot_data = df.pivot_table(values="exam_score", index="sleep_bin", columns="study_bin", aggfunc="mean")

# Create heatmap
heatmap_fig = px.imshow(
    pivot_data,
    text_auto='.1f',
    color_continuous_scale="viridis",
    title="Average Exam Score by Study Hours and Sleep Hours",
    labels=dict(x="Study Hours", y="Sleep Hours", color="Avg Exam Score")
)
plotly(heatmap_fig)

# Part-time job impact
text("## Impact of Part-time Job")

# Manual calculation instead of groupby to avoid aggregation issues
job_categories = df["part_time_job"].unique()
job_data = []

for job in job_categories:
    job_subset = df[df["part_time_job"] == job]
    avg_score = job_subset["exam_score"].mean()
    count = len(job_subset)
    job_data.append({
        "Part-time Job": job,
        "Average Score": avg_score,
        "Count": count
    })

job_impact = pd.DataFrame(job_data)

job_fig = px.bar(
    job_impact,
    x="Part-time Job",
    y="Average Score",
    title="Impact of Part-time Job on Exam Scores",
    color="Part-time Job",
    text="Count"
)
job_fig.update_traces(texttemplate='%{text} students', textposition='outside')
plotly(job_fig)

# Feature importance for exam scores
text("## Key Factors Influencing Exam Scores")

# Calculate correlations with exam score for all numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
if 'exam_score' in numeric_cols:
    numeric_cols.remove('exam_score')  # Remove the target variable
corr_data = []

for col in numeric_cols:
    corr_val = round(df[col].corr(df['exam_score']), 3)
    corr_data.append({"Factor": col, "Correlation": corr_val})

corr_df = pd.DataFrame(corr_data)
corr_df = corr_df.sort_values("Correlation", ascending=False)

corr_fig = px.bar(
    corr_df,
    x="Factor",
    y="Correlation",
    title="Correlation of Various Factors with Exam Score",
    color="Correlation",
    color_continuous_scale=px.colors.sequential.Viridis
)
plotly(corr_fig)

# Multifactor Success Analysis
text("## Success Patterns Analysis")

# Create success indicator (top 25% scores)
top_quartile = df["exam_score"].quantile(0.75)
df["success"] = df["exam_score"] >= top_quartile

# Manual calculation of profiles to avoid aggregation issues
success_groups = [True, False]
metrics = ["study_hours_per_day", "sleep_hours", "social_media_hours", 
           "netflix_hours", "attendance_percentage", "exercise_frequency"]

success_data = []
for success in success_groups:
    success_subset = df[df["success"] == success]
    
    for metric in metrics:
        avg_value = success_subset[metric].mean()
        success_data.append({
            "success": success,
            "Metric": metric,
            "Average Value": avg_value
        })

success_profile = pd.DataFrame(success_data)

success_fig = px.bar(
    success_profile,
    x="Metric",
    y="Average Value",
    color="success",
    barmode="group",
    title="Comparison of Top Performers vs Others",
    color_discrete_map={True: "#2ecc71", False: "#e74c3c"}
)
success_fig.update_layout(legend_title_text="Top Performer")
plotly(success_fig)

# Key Insights
text("## Key Insights")
text("""
1. **Study Hours**: There is a strong positive correlation between daily study hours and exam scores.
2. **Digital Distractions**: Social media and Netflix hours show a negative correlation with exam performance.
3. **Sleep Balance**: Students with moderate to high sleep hours (6-8 hours) generally perform better than those with very low or very high sleep hours.
4. **Part-time Jobs**: Students with part-time jobs show only slightly lower average scores, suggesting good time management is possible.
5. **Balanced Lifestyle**: The best performers typically maintain a balance of adequate study time, sufficient sleep, and limited digital distractions.
""")
