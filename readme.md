# Insurance Premium Prediction API

A robust REST API built with **FastAPI** that predicts insurance premiums based on user demographics and health data. This project serves a machine learning model to provide real-time predictions.

## 🚀 Features

* **FastAPI Backend:** High-performance, asynchronous API framework.
* **ML Integration:** Loads a pre-trained scikit-learn model for predictions.
* **Data Validation:** Uses Pydantic schemas for strict input/output validation.
* **Health Checks:** dedicated endpoint to verify model loading status.

## 📂 Project Structure

```bash
├── config/             # Configuration files
├── model/              # ML model and prediction logic
├── schema/             # Pydantic data models (Input/Output)
├── app.py              # Main application entry point
├── requirements.txt    # Project dependencies
└── README.md           # Documentation