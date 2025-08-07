# Part 1: Theoretical Analysis (30%)

## Q1: How AI-driven code generation tools (e.g., GitHub Copilot) reduce development time. What are their limitations?

**Answer:**  
GitHub Copilot reduces development time by providing real-time code suggestions, auto-completions, and boilerplate code generation. It helps developers focus more on logic and problem-solving rather than repetitive syntax. This boosts productivity and minimizes coding errors.

**Limitations include:**

- Lack of context understanding: Suggestions may be irrelevant or incorrect for complex logic.
- Security concerns: May suggest vulnerable code patterns.
- Over-reliance: Developers may stop understanding the underlying code.
- Licensing: Some Copilot outputs may resemble copyrighted code.

---

## Q2: Compare supervised and unsupervised learning in the context of automated bug detection.

**Answer:**  

- **Supervised Learning:** Uses labeled datasets (bug/no bug) to train models like Random Forest or SVM. It's effective in detecting known bug patterns and predicting future ones.

- **Unsupervised Learning:** No labeled data. It detects anomalies or unusual code patterns using clustering or outlier detection, helpful for unknown or zero-day bugs.

**Conclusion:** Supervised learning is accurate for common bugs; unsupervised learning helps discover new or rare bugs.

---

## Q3: Why is bias mitigation critical when using AI for user experience personalization?

**Answer:**  
Bias mitigation ensures that personalization algorithms don't unfairly favor or exclude users based on race, gender, age, etc. Unchecked AI can reinforce stereotypes or lead to unequal user treatment. Ethical AI must provide inclusive and fair personalization, which builds trust and prevents discrimination.

---

## Case Study: AIOps in Deployment Pipelines

**Answer:**  

AIOps enhances deployment efficiency by automating anomaly detection, log analysis, and failure prediction in CI/CD pipelines.

**Example 1:**  
AIOps tools detect slow API response during deployment and reroute traffic while auto-scaling resources.

**Example 2:**  
By analyzing historical logs, AIOps predicts failed builds and notifies teams to act preemptively.
