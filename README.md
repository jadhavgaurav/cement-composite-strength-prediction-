# Cement Composite Strength Prediction

## Aim of the Project
To predict the ultimate compressive strength of cement composite mixtures using machine learning techniques, specifically leveraging **Random Forest** and **Artificial Neural Network (ANN)** models.

---

## Summary of the Project

This project aims to assist in the **design and optimization of cementitious composites** by predicting their **uniaxial compressive strength (UCS)** based on input variables such as proportions of materials, curing age, and other factors. By replacing the traditional costly and time-consuming experimental methods with a machine learning approach, this project contributes to advancing material science and construction industry practices.

Key Highlights:

- The dataset includes material proportions, curing age, and resulting UCS values.
- The models enable accurate predictions, reducing the need for extensive physical testing.
- Random Forest achieved an accuracy of **89%**, while ANN achieved **85%**.
=======
This project focuses on the development and optimization of **Electrically Conductive Cementitious Composites (ECCC)** using machine learning techniques. These composites are designed for **structural health monitoring** applications due to their high conductivity and strain sensitivity.

Key aspects of the study include:

1. **Material Composition**:
   - **Graphite Powder (GP)**: High conductivity but significantly reduces UCS.
   - **Waste Steel Slag (SS)**: Provides better UCS and conductivity compared to GGBS.
   - **Ground Granulated Blast-Furnace Slag (GGBS)**: Enhances conductivity but reduces UCS beyond a 20% replacement ratio.

2. **Experimental Dataset**:
   - **81 mixtures** tested for UCS.
   - **108 mixtures** tested for electrical resistivity.
   - Variables: filler content, cement proportions, and curing age.

3. **Machine Learning Model**:
   - A **Random Forest (RF)** model, optimized using the **Beetle Antennae Search (BAS)** algorithm, was developed to predict UCS and resistivity.
   - Achieved high prediction accuracy:
     - R² = **0.986** for UCS.
     - R² = **0.980** for resistivity.

4. **Key Findings**:
   - **GP** is most effective for conductivity but compromises UCS.
   - **SS** is a balanced filler, offering better conductivity and UCS than GGBS.
   - The BAS-RF model closely replicates experimental results, demonstrating its reliability for predictive simulations.

This project demonstrates the feasibility of using **waste materials** like slags to produce high-performance ECCCs, promoting sustainability and advancing intelligent construction technologies.

---

## Model Building Techniques


### 1. **Data Preprocessing**
- Addressed missing values.
- Standardized the features using **StandardScaler**.
=======
### 1. **Data Preprocessing**
- Addressed missing values.
- Scaled the features using **MinMaxScaler**.
- Performed train-test split for model evaluation.

### 2. **Feature Engineering**
- Derived features such as the **cement-to-water ratio** to enhance prediction accuracy.
=======
- Created a composite feature `Comps` to combine the effects of cement, blast furnace slag, superplasticizer, and water:
  ```python
  df['Comps'] = (df['cement'] + df['blast_furnace_slag'] + df['superplasticizer']) / df['water']
  ```

### 3. **Model Selection and Training**
- Used **Random Forest Regressor** for its ability to handle non-linear relationships and robustness to overfitting.
- Used **Artificial Neural Network (ANN)** for its capability to model complex relationships between features.
- Both models were trained with default parameters.
=======
- Both models were trained with default parameters (hyperparameter tuning was skipped to reduce execution time).
### 4. **Model Evaluation**
- Metrics used: **R-squared (R²)**, **Mean Absolute Error (MAE)**, and **Root Mean Squared Error (RMSE)**.
- **Random Forest**: Achieved **R² = 0.89** on the test set.
- **ANN**: Achieved **R² = 0.85** on the test set.

---

## Tools and Technologies Used
- **Python Libraries**: pandas, numpy, scikit-learn, tensorflow, matplotlib, seaborn
- **Machine Learning**: Random Forest, Artificial Neural Network (ANN)
- **Development Environment**: Jupyter Notebook

---

## Steps to Reproduce
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jadhavgaurav/cement-composite-strength-prediction.git
   cd cement-composite-strength-prediction
   ```

2. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:
   - Open the `cement_composite_strength_prediction.ipynb` file.
   - Follow the steps to preprocess the data, train the models, and evaluate their performance.

4. **Run the Flask App (Optional)**:
   - Use the Flask app provided to make predictions via a user-friendly web interface.
=======
   ```bash
   python app.py
   ```

---

## Conclusion
The project successfully predicts the ultimate compressive strength of cement composite mixtures using machine learning techniques. Random Forest achieved an accuracy of **89%**, while ANN achieved **85%**. This work demonstrates the potential of machine learning to optimize material design and reduce the dependency on physical testing.

Future enhancements include:
- Expanding the dataset to include additional features and samples.
- Exploring hyperparameter tuning for further optimization of both models.

---

For questions or collaborations, please reach out via [GitHub](https://github.com/jadhavgaurav).
=======
In this study, the influence of **Graphite Powder (GP)** and waste slags (**Steel Slag (SS)** and **Ground Granulated Blast-Furnace Slag (GGBS)**) on **Uniaxial Compressive Strength (UCS)** and **electrical resistivity** was analyzed through laboratory experiments. A **Random Forest (RF)** model, enhanced with the **Beetle Antennae Search (BAS)** algorithm, was employed to model UCS and resistivity. The following conclusions were drawn:

1. **Graphite Powder (GP)** significantly improves conductivity but reduces UCS due to its lubrication effect. A **4% GP ratio** is recommended for balanced performance.
2. **Steel Slag (SS)** is more effective than **GGBS**, as it has a lesser negative impact on UCS and provides higher conductivity.
3. **Slag-to-binder ratios (s/b)** below 20% slightly enhance UCS, but higher ratios lead to a significant decrease.
4. The Random Forest model and ANN model accurately predicts UCS , achieving **R² = 0.90** and **R² = 0.84**, respectively, on test sets.
5. Feature importance analysis indicates that **age** is the most significant factor for UCS.

This project highlights the potential of using waste materials for producing high-performance ECCCs, supporting sustainability and intelligent construction practices.

This project demonstrates the potential of leveraging waste materials and machine learning for sustainable, high-performance ECCC development, paving the way for intelligent construction technologies.

---
