# Part 2: Practical Implementation

## Task 1: Edge AI Prototype

- **Tools:** TensorFlow Lite, Colab (simulate Raspberry Pi environment)  
- **Goal:** Train a lightweight model to classify recyclable materials (plastic, paper, metal).  

**Steps:**  
1. Collect/prepare a small labeled dataset of recyclable items.  
2. Train a compact CNN model in TensorFlow.  
3. Convert model to TensorFlow Lite format.  
4. Test inference speed and accuracy on sample data.  

**Explain:** Edge AI reduces latency and network dependency, critical for field applications like waste sorting robots.

---

## Task 2: AI-Driven IoT Concept for Smart Agriculture

- **Sensors:** Soil moisture, temperature, humidity, light intensity, nutrient sensors  
- **AI Model:** Regression model (e.g., Random Forest) predicting crop yield based on sensor data and weather forecasts.  

**Data Flow Diagram:**  
Sensors → Edge AI preprocess → Cloud AI model → Farmer’s dashboard with yield predictions and alerts

---

## Task 3: Ethics in Personalized Medicine

- **Potential Biases:**  
  - Underrepresentation of ethnic minorities in cancer genomic datasets leads to less accurate treatment recommendations.  

- **Fairness Strategies:**  
  - Include diverse, balanced datasets.  
  - Use bias detection frameworks and adjust models for equitable treatment across groups.
