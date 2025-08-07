## Part 1: Theoretical Understanding

### Q1: Compare TensorFlow and PyTorch

| Feature      | TensorFlow                             | PyTorch                          |
|--------------|----------------------------------------|----------------------------------|
| Ecosystem    | Large ecosystem with TensorBoard, TFX, TF Lite | Simpler ecosystem, deep research support |
| Computation  | Static computation graph (TF 1.x), now supports dynamic (TF 2.x) | Dynamic computation graph        |
| Syntax       | Verbose, but more production-ready     | Pythonic, easier for beginners   |
| Deployment   | TensorFlow Serving, TF Lite            | TorchServe, ONNX                 |
| When to Use  | Scalable production models, mobile apps| Rapid prototyping, research      |

**Use TensorFlow** when you want better deployment pipelines.  
**Use PyTorch** for flexibility during development and experimentation.

---

### Q2: Two Use Cases for Jupyter Notebooks

1. **Exploratory Data Analysis (EDA):**  
   Allows visualization and inline data manipulation (e.g., using `pandas`, `matplotlib`).

2. **Prototyping AI Models:**  
   Step-by-step testing and debugging of ML models with outputs at each cell.

---

### Q3: spaCy vs Basic String Operations

spaCy offers:
- Pre-trained models for tokenization, NER, POS tagging, etc.
- Rule-based matching with linguistic awareness.
- Faster and more accurate than regex or manual parsing.

**Example:** Instead of splitting strings manually to find names, spaCy identifies `ORG`, `PRODUCT`, etc., automatically using context.

---

### Comparative Analysis: Scikit-learn vs TensorFlow

| Feature        | Scikit-learn                            | TensorFlow                         |
|----------------|-----------------------------------------|------------------------------------|
| Application    | Classical ML (SVM, decision trees, k-NN) | Deep learning (CNNs, RNNs, Transformers) |
| Beginner Friendly | Yes, easy syntax                      | Steeper learning curve             |
| Community      | Strong, used in education and research   | Very large and supported by Google |
| Deployment     | Not ideal for production                | Built-in tools for deployment (e.g., TF Serving, Lite) |
