# Part 2: Case Study Analysis (40%)

## Case 1: Biased Hiring Tool (Amazon)

### Source of Bias
- Training data derived from male-dominated tech resumes, leading to gender bias in hiring decisions.

### Proposed Fixes
- **Debias Training Data**: Oversample resumes from female candidates to balance representation.
- **Adversarial Fairness**: Use adversarial networks to detect and remove gender signals from inputs.
- **Human-in-the-Loop**: Incorporate HR professionals to review and approve AI-generated shortlists.

### Fairness Metrics
- **Disparate Impact Ratio**: Should be greater than 0.8 between gender groups.
- **Equal Opportunity Difference**: Should be less than 0.1 to ensure fairness in true positive rates.

---

## Case 2: Facial Recognition in Policing

### Ethical Risks
- **Wrongful Arrests**: Increased risk of misidentification, especially among minority groups.
- **Privacy Violations**: Deployment of mass surveillance systems without public consent.

### Policy Recommendations
- **Ban Real-Time Surveillance**: Allow usage only for retrospective analysis with legal warrants.
- **Mandate Accuracy Thresholds**: Require <1% false positives across all demographic groups to ensure equitable performance.
