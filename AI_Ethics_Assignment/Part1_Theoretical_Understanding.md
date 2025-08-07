# Q1: Algorithmic Bias

**Definition:**  
Algorithmic bias occurs when an AI system produces systematically unfair outcomes due to prejudices in training data, model assumptions, or design.

**Examples:**
1. **Hiring Tools** – Discriminating against female resumes based on historical male-dominated data.
2. **Loan Approval** – Higher rejection rates for minority groups due to biased credit scoring models.

# Ethical Principles Matching

| Principle         | Definition                                               |
|------------------|----------------------------------------------------------|
| A) Justice        | Fair distribution of AI benefits and risks              |
| B) Non-maleficence| Ensuring AI does not harm individuals or society        |
| C) Autonomy       | Respecting users’ right to control data and decisions   |
| D) Sustainability | Designing AI to be environmentally friendly             |

# Case Study: Amazon’s Biased Hiring Tool

**Source of Bias:**  
- Historical data favored male candidates.
- Model learned from biased hiring patterns.

**Three Fixes:**
1. Remove gender-based features from input.
2. Use fairness-aware learning algorithms (e.g., reweighing).
3. Regular audits using fairness metrics (e.g., disparate impact).

**Metrics for Fairness:**
- Equal Opportunity Difference
- Disparate Impact Ratio
- False Positive/Negative Rate Differences

# Audit Summary – COMPAS Dataset

**Objective:**  
To audit racial bias in risk scores using AI Fairness 360.

**Findings:**
- African-American individuals had a higher false positive rate.
- Disparate Impact Ratio: 0.6 (< 0.8 indicates bias)
- Equal Opportunity Difference: -0.15

**Remediation Steps:**
1. Apply reweighing or bias mitigation algorithms.
2. Train separate models with fairness constraints.
3. Incorporate demographic fairness metrics into evaluation pipeline.

# Ethical AI Guidelines for Healthcare 🏥

## 1. Patient Consent Protocols
- AI systems must collect **informed consent**.
- Patients should know how their data is used and by whom.

## 2. Bias Mitigation Strategies
- Ensure **diverse training datasets** (ethnicity, gender, age).
- Perform regular **fairness audits** and retrain as needed.

## 3. Transparency Requirements
- Use explainable models (e.g., SHAP, LIME).
- Medical staff must be able to understand and question AI decisions.
