# Student Habits & Performance Analysis

![Student Habits](./images/student.jpg)

## Overview

This project analyzes the relationship between student habits and academic performance. Using a dataset of 1000 students, this interactive dashboard presents insights into how various behaviors and lifestyle factors impact exam scores.

## Data Description

The dataset includes the following variables for each student:

- **Demographics**: student_id, age, gender
- **Study Habits**: study_hours_per_day, attendance_percentage
- **Digital Activities**: social_media_hours, netflix_hours
- **Lifestyle Factors**: sleep_hours, diet_quality, exercise_frequency
- **Work Status**: part_time_job
- **Background**: parental_education_level, internet_quality
- **Well-being**: mental_health_rating
- **Engagement**: extracurricular_participation
- **Outcome**: exam_score

## Key Findings

1. **Study Hours**: Strong positive correlation with exam scores
2. **Digital Distractions**: Negative correlation between social media/Netflix hours and performance
3. **Sleep Balance**: Optimal performance observed with moderate sleep hours (6-8 hours)
4. **Part-time Jobs**: Minimal impact on academic performance, suggesting effective time management
5. **Balanced Lifestyle**: Top performers maintain a balance of study time, sufficient sleep, and limited digital distractions

## Dashboard Features

The interactive dashboard includes:

- Performance distribution visualization
- Impact analysis of study hours
- Gender-based performance comparison
- Digital distraction analysis with filtering options
- Sleep impact visualization
- Balanced lifestyle heatmap
- Part-time job impact assessment
- Feature importance visualization
- Comparison of top performers versus others

## Getting Started

### Prerequisites

- Python 3.9+
- Preswald framework
- Required packages: pandas, numpy, plotly

### Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python run.py
   ```

## Customization

The dashboard branding can be customized by editing the `preswald.toml` file:

- Change the application title and name
- Update the favicon and logo
- Modify the color scheme

## Project Structure

```
student_habits/
├── data/
│   └── student_habits_performance.csv
├── images/
│   ├── student.jpg
│   └── student_favicon.ico
├── hello.py                # Main dashboard code
├── run.py                  # Server runner
├── preswald.toml           # Configuration file
└── README.md               # This file
```

## Analysis Methodology

This project follows a data-driven approach to understand student success factors:

1. **Exploratory Data Analysis**: Visualizing distributions and relationships
2. **Correlation Analysis**: Measuring associations between habits and performance
3. **Segmentation**: Comparing profiles of top performers vs. others
4. **Feature Importance**: Identifying key predictors of academic success

## Conclusions

The analysis reveals that academic success is primarily determined by dedicated study time, but is also significantly influenced by maintaining a balanced lifestyle. Digital distractions show a notable negative impact, while factors like part-time employment have minimal effect when properly managed.

Students aiming to improve their academic performance should focus on:

- Increasing dedicated study hours
- Limiting digital distractions
- Maintaining healthy sleep patterns
- Finding balance across all lifestyle factors

## License

This project is for educational purposes only.

---

Created with Preswald
