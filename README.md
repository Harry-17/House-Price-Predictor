
---

# 🏠 House Price Predictor

A simple machine learning application built with Streamlit to predict house prices based on user-provided features. This project demonstrates the integration of a trained regression model into an interactive web interface for real-time predictions.

## 🚀 Features

* Interactive web interface using Streamlit.
* User inputs for various house features.
* Real-time price prediction based on input features.
* Clean and intuitive user experience.

## 🧠 Model Overview

The application utilizes a regression model trained on a dataset containing various features influencing house prices. The model predicts the price of a house based on the input features provided by the user.

## 📁 Project Structure

```

├── house_price_predictor.ipynb  # Jupyter notebook with data analysis and model training
├── app.py                       # Streamlit application script
├── model.pkl                    # Serialized trained model
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```



## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Harry-17/House-Price-Predictor.git
   cd House-Price-Predictor
   ```



2. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```



3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



## ▶️ Running the Application

After installing the dependencies, start the Streamlit application with the following command:

```bash
streamlit run app.py
```



This will launch the application in your default web browser, allowing you to input house features and receive price predictions.

## 📊 Usage

1. Open the application in your web browser.
2. Enter the required features of the house (e.g., number of bedrooms, square footage, location).
3. Click the "Predict" button to view the estimated price of the house.([www.slideshare.net][1])

## 📚 Dataset

The model was trained on a dataset containing various features influencing house prices. The dataset includes information such as the number of bedrooms, bathrooms, square footage, and location.([www.slideshare.net][1])

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Acknowledgments

This project was inspired by tutorials and resources on machine learning and Streamlit applications. Special thanks to the contributors and the open-source community for their valuable tools and libraries.

---


[1]: https://www.slideshare.net/DivyaTiwari50/predicting-house-price?utm_source=chatgpt.com "Predicting house price | PPT - SlideShare"
