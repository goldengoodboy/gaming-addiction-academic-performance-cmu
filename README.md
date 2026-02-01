# Gaming Behavior & Academic Performance at Chiang Mai University
*A Behavioral Economics Analysis of Game Addiction, Class Engagement, and GPA*

![STATA](https://img.shields.io/badge/STATA-17+-white?logo=stata&logoColor=blue)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5+-green?logo=matplotlib)

## 📊 Research Overview
Investigated the relationship between gaming behavior, game addiction, class engagement, and academic performance (GPA) among **465 undergraduate students** at Chiang Mai University using behavioral economics frameworks. Key insight: **Time allocation—not addiction intensity—negatively impacts GPA**, while academic engagement strongly predicts performance.

## 🔍 Key Findings
- ⏱️ **Hours spent gaming** negatively correlates with GPA (β = -0.035, p<0.10) when controlling for engagement
- 👥 **LGBTQ+ and male students** show significantly higher game addiction scores vs. female students (Tukey HSD, p<0.01)
- 🎮 **Competitive action games** (FPS, MMO) drive higher addiction vs. casual games (β = 0.454, p<0.05)
- 📈 **Class engagement mediates outcomes**: Timely assignment completion (+0.068 GPA) and peer collaboration (+0.109 GPA) strongly predict academic success
- ❌ **No direct negative relationship** between game addiction score and GPA when engagement is controlled

## 📌 Policy Implications
Findings support **engagement-based interventions** over restrictive gaming bans:
1. Time management workshops highlighting opportunity costs of gaming
2. Teacher-student interaction redesign to increase class relevance
3. Peer collaboration frameworks to offset gaming displacement effects

## 💼 Skills Demonstrated
| Category | Tools & Techniques |
|----------|-------------------|
| **Research Design** | Behavioral economics framework, opportunity cost analysis |
| **Data Collection** | Survey design (Wu et al. 2021 scale), Google Forms, 465 respondents |
| **Data Wrangling** | Excel cleansing, handling missing values, variable recoding |
| **Statistical Analysis** | OLS regression, ANOVA with Tukey HSD post-hoc tests, robust standard errors |
| **Programming** | STATA (do-files for regression/ANOVA), Python (pandas, matplotlib for visualization) |
| **Data Intepretation** | Intepret data base on the statistical result, statistical significan and mean different |
| **Provide Recommendation Solution** | Evidence-based recommendations for time management workshops |

## 📁 Repository Structure
├── data/cleaned/ # Anonymized survey responses (PII removed)
├── code/ # Reproducible analysis scripts
│ ├── analysis_regression.do # STATA regression models (Models 1-4)
│ └── visualization.py # Python matplotlib visualizations
├── results/figures/ # Publication-quality charts
├── results/tables/ # Regression output tables
└── report/executive_summary.pdf # 2-page summary for employers

## 🔒 Data Privacy
All personally identifiable information (PII) has been removed per Thai PDPA guidelines. Dataset contains only aggregated/anonymized variables used in published analysis.
