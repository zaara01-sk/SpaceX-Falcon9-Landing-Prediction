# SpaceX Falcon 9 First Stage Landing Prediction

## Project Overview
This project predicts the success of SpaceX Falcon 9 first-stage landings. By accurately predicting landing outcomes, we can estimate the cost of a launch, as the first stage's reusability is the primary factor in SpaceX's cost advantage over competitors.

## Project Phases
1. **Data Collection:** Used SpaceX REST API and Web Scraping (BeautifulSoup) from Wikipedia.
2. **Data Wrangling:** Cleaned data and engineered a binary "Class" variable (1 for success, 0 for failure).
3. **Exploratory Data Analysis (EDA):** Performed analysis using SQL and Visualizations (Seaborn/Matplotlib).
4. **Interactive Analytics:** Created geospatial maps with Folium and dashboards with Plotly Dash.
5. **Predictive Modeling:** Built and tuned classification models (Logistic Regression, SVM, Decision Tree, KNN).

## Key Results
- Best Model: All models achieved approximately 83.33% accuracy on the test set.
- Strategic Insights: Launch success rates improved significantly over time (flight number) and vary by orbit type.

## Technologies Used
- Python (Pandas, NumPy, Scikit-Learn)
- BeautifulSoup (Web Scraping)
- SQLite (SQL Analysis)
- Folium (Geospatial Analysis)
- Plotly Dash (Interactive Dashboard)

Author: Zaara Akbar Shaikh
Date: 18/01/26
