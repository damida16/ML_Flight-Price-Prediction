# ✈️ Flight Price Prediction

A machine learning web application that predicts flight ticket prices based on historical booking data. This project demonstrates the complete ML pipeline from data preprocessing to model deployment.

---

## 📋 Project Overview

This is my first end-to-end machine learning project, built to learn and demonstrate the complete development cycle:
- Data cleaning and preprocessing
- Exploratory data analysis
- Feature engineering
- Model training and evaluation
- Web application deployment

### Problem Statement
Flight ticket prices fluctuate based on multiple factors like airline, route, timing, and number of stops. This project aims to predict ticket prices using historical data to help travelers understand pricing patterns.

### Solution
A Random Forest regression model trained on 10,683 historical Indian domestic flight records, deployed as an interactive web application using Streamlit.

---

## 🎯 Key Features

- **Interactive UI**: User-friendly interface for inputting flight details
- **Real-time Predictions**: Instant price estimates based on user input
- **Transparent Model**: 81% prediction accuracy (R² score)
- **Deployed Application**: Accessible via web browser, no installation needed

---

## 🛠️ Tech Stack

- **Language**: Python 3.13
- **ML Framework**: scikit-learn
- **Web Framework**: Streamlit
- **Data Processing**: pandas, numpy
- **Model**: Random Forest Regressor
- **Deployment**: Streamlit Community Cloud

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| **R² Score** | 81.35% |
| **Mean Absolute Error (MAE)** | ₹1,167.58 |
| **Training Data** | 10,683 flight records |
| **Features** | 17 engineered features |

**Interpretation**: The model explains 81% of variance in flight prices, with an average prediction error of ₹1,167. For flights ranging ₹3,000-₹40,000, this represents acceptable accuracy for a learning project.

---

## 🗂️ Dataset Information

- **Source**: Historical Indian domestic flight data (2019)
- **Size**: 10,683 records
- **Features**: 11 original columns
- **Routes**: 5 source cities, 6 destination cities
- **Airlines**: 12 different carriers

### Original Features:
- Airline
- Date of Journey
- Source & Destination
- Route
- Departure & Arrival Time
- Duration
- Total Stops
- Additional Info
- Price (target variable)

---

## ⚙️ Technical Implementation

### 1. Data Preprocessing
- Parsed duration strings ("2h 50m") into numeric features
- Extracted temporal features (day, month) from journey dates
- Extracted time features (hour, minute) from departure/arrival times
- Handled missing values through strategic imputation

### 2. Feature Engineering
- **One-Hot Encoding**: Source cities (5 binary columns)
- **Label Encoding**: Airlines (0-11) and Destinations (0-5)
- **Numerical Mapping**: Total stops (0-4)
- **Time Features**: Journey day/month, departure/arrival hour/minute
- **Duration Features**: Hours, minutes, and total minutes

**Final Feature Set**: 17 features used for model training

### 3. Model Selection
Chose **Random Forest Regressor** because:
- Handles non-linear relationships well
- Robust to outliers
- No need for feature scaling
- Provides feature importance metrics
- Good performance with tabular data

### 4. Model Training
```python
RandomForestRegressor(
    n_estimators=100,  # Number of trees
    random_state=42     # Reproducibility
)
```

### 5. Evaluation
- Train-test split: 80-20
- Metrics: R², MAE, RMSE
- No hyperparameter tuning needed (default params performed well)

---

## 🚀 Deployment Architecture

```
User Browser
    ↓
Streamlit Cloud Server
    ↓
app.py (Web Application)
    ↓
Load Model (rf_random.pkl)
    ↓
Preprocess User Input
    ↓
Model Prediction
    ↓
Return Result to User
```

**Deployment Platform**: Streamlit Community Cloud
- Auto-deployed from GitHub repository
- Serverless architecture
- Free hosting
- HTTPS enabled
- Automatic redeployment on git push

---

## 📝 Project Structure

```
Flight-Price-Prediction/
│
├── app.py                  # Streamlit web application
├── rf_random.pkl          # Trained Random Forest model
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore rules
```

---

## 🎓 What I Learned

### Technical Skills
- End-to-end ML pipeline implementation
- Data preprocessing techniques for real-world messy data
- Feature engineering for categorical and temporal data
- Model evaluation and interpretation
- Web application development with Streamlit
- Git version control and GitHub collaboration
- Cloud deployment workflows

### Key Takeaways
1. **Data quality matters**: Spent 40% of project time on cleaning and preprocessing
2. **Feature engineering is crucial**: Proper encoding improved model performance significantly
3. **Simplicity works**: Default Random Forest params performed well without extensive tuning
4. **Deployment is essential**: A model in a notebook isn't as valuable as a usable application

### Challenges Overcome
- Parsing inconsistent duration formats (mix of "2h 50m", "5h", "45m")
- Handling temporal features (dates and times)
- Understanding encoding strategies (when to use one-hot vs label encoding)
- Learning model evaluation metrics (R², MAE, RMSE)
- Deploying ML model with proper dependency management

---

## 🔮 Future Enhancements

### Short-term
- [ ] Add data visualization (price trends, feature importance charts)
- [ ] Implement confidence intervals for predictions
- [ ] Add model explanation (why this price was predicted)
- [ ] Support for round-trip pricing

### Long-term
- [ ] Integrate real-time flight data APIs
- [ ] Expand to international routes
- [ ] Add price alert notifications
- [ ] Implement "best time to book" recommendations
- [ ] Multi-route comparison feature
- [ ] Mobile app version

---

## ⚠️ Limitations & Disclaimers

### Current Limitations
- **Historical data only**: Based on 2019 data, not real-time prices
- **Geographic scope**: Limited to Indian domestic routes
- **Missing factors**: Does not account for:
  - Seasonal demand patterns
  - Public holidays and events
  - Fuel price fluctuations
  - Dynamic airline pricing strategies
  - COVID-19 impact on pricing
- **Model accuracy**: 81% means ~1 in 5 predictions may be less accurate

### Important Notes
⚠️ **This is an educational project** demonstrating ML concepts and deployment workflows.

⚠️ **Not intended for actual booking decisions.** Real flight prices depend on many factors beyond this model's scope.

⚠️ **Data is outdated.** Trained on 2019 data; current prices will differ significantly.

---

## 🏃‍♂️ Running Locally

### Prerequisites
- Python 3.11+
- pip package manager

### Installation

1. **Clone repository**
```bash
git clone https://github.com/damida16/Flight-Price-Prediction.git
cd Flight-Price-Prediction
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run application**
```bash
streamlit run app.py
```

4. **Open browser**
Navigate to `http://localhost:8501`

---

## 📦 Dependencies

```
streamlit==1.51.0
pandas==2.2.3
scikit-learn==1.5.2
```

All dependencies are specified in `requirements.txt` for reproducibility.

---

## 🤝 Contributing

This is a personal learning project, but feedback and suggestions are welcome!

Feel free to:
- Open issues for bugs or suggestions
- Fork the repository and experiment
- Share improvements or alternative approaches

---

## 🙏 Acknowledgments

- Dataset source: Kaggle flight price dataset
- Learning resources: Udemy ML courses, YouTube tutorials, documentation
- Framework: Streamlit for rapid prototyping
- Community: Stack Overflow, GitHub, ChatGPT for troubleshooting

---

## 📄 License

This project is open source and available for educational purposes.

---

**Damida Shu Mudita | Built with ❤️ as a learning project | 2026**
