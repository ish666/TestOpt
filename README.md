# 🧪 TestOpt - Test Optimization Library

**TestOpt** is a Python library for optimizing test cases using multiple AI/ML-based and heuristic techniques.  
It helps reduce testing time, increase fault coverage, and improve software reliability.
Python library that automatically optimizes software test suites using machine learning, mutation testing, and heuristic methods. It helps prioritize and reduce test cases to improve efficiency and fault coverage.


---

## 🚀 Features

- ✅ Test Suite Reduction (Greedy Algorithm)
- 📊 Test Case Prioritization (Coverage-Based & Fault-Based)
- 🤖 Machine Learning-Based Defect Prediction
- 🧬 Mutation Testing Optimization
- 🏆 CLI to compare all and select the best approach

---

## 🛠 Installation

```bash
git clone https://github.com/your-username/TestOpt.git
cd TestOpt
pip install -r requirements.txt
 .
Sample test data is available in `sample_data.csv`. To try the tool, run:

```bash
python run_testopt.py --data sample_data.csv

---

### ✅ 6. **Usage**
```md
## 🧪 Usage

### Option 1: With Custom CSV
```bash
python run_testopt.py --data data/my_test_data.csv
## 📄 Sample `test_data.csv` Format

| test_case | mutants   | lines_of_code | cyclomatic_complexity | code_churn | prior_defects | defective |
|-----------|-----------|----------------|------------------------|-------------|----------------|-----------|
| TC1       | M1 M2     | 80             | 8                      | 2           | 0              | 0         |
| TC2       | M3        | 100            | 12                     | 5           | 1              | 1         |
## 🤝 Contributing

Contributions are welcome! Please fork the repo, create a feature branch, and submit a PR. For major changes, open an issue first.
## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
Contribution by Niti Sharma
