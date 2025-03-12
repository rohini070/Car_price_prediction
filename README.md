Car Price Prediction

This project focuses on predicting the prices of used cars based on various features using machine learning techniques. The goal is to provide an accurate estimation of a car's market value to assist buyers and sellers in making informed decisions.

## Table of Contents
- Overview
- Dataset
- Features
- Installation
- Usage
- Model Performance
- Contributing

## Overview
In the used car market, determining the appropriate selling price can be challenging due to numerous factors influencing a vehicle's value. This project aims to simplify this process by leveraging machine learning algorithms to predict car prices based on historical data.

## Dataset
The dataset used for this project contains information about various cars and their corresponding prices. Key attributes include:

- **Car Name**: The brand and model of the car.
- **Year**: The year the car was manufactured.
- **Selling Price**: The price at which the car is being sold (target variable).
- **Present Price**: The current ex-showroom price of the car.
- **Kms Driven**: The total kilometers driven by the car.
- **Fuel Type**: The type of fuel used by the car (e.g., Petrol, Diesel, CNG).
- **Seller Type**: Indicates if the seller is a dealer or an individual.
- **Transmission**: The transmission type of the car (Manual or Automatic).
- **Owner**: The number of previous owners.

## Features
- **Data Cleaning and Preprocessing**: Handling missing values, encoding categorical variables, and scaling numerical features.
- **Exploratory Data Analysis (EDA)**: Visualizing data distributions and relationships between variables.
- **Model Building**: Implementing machine learning models such as Linear Regression, Decision Trees, and Random Forest Regressors.
- **Model Evaluation**: Assessing model performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared score.
- **Web Application**: A user-friendly interface built with Flask to input car details and get price predictions.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/rohini070/Car_price_prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Car_price_prediction
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Ensure your virtual environment is activated.
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your browser and go to `http://localhost:5000` to use the car price prediction tool.

## Model Performance
The project implements multiple models for comparison. Performance metrics include:

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **R-squared Score**

## Contributing
Contributions are welcome! If you find any bugs or want to add features, feel free to fork the repository and create a pull request.
