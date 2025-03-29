# **📊 Product Sentiment Analysis**
> **A Flask-based Sentiment Analysis tool for product reviews using NLP and Machine Learning.**

## **📌 Project Overview**
Analyzing thousands of product reviews manually is time-consuming. This project automates sentiment analysis using **Natural Language Processing (NLP)** and **Machine Learning**, classifying reviews as **Positive, Neutral, or Negative**. It also provides insights such as **keyword extraction** and **customer sentiment trends**.

## **🚀 Features**
✅ **Sentiment Classification** - Detects whether reviews are **positive, negative, or neutral**  
✅ **Bulk Review Analysis** - Upload CSV files for **batch sentiment analysis**  
✅ **Keyword & Trend Analysis** - Extracts common topics from reviews  
✅ **Web Dashboard** - Simple **Flask-based UI** for user interaction  
✅ **API Support** - Exposes a REST API for sentiment analysis  
✅ **Cloud Deployment** - Easily deployable using **Render, Streamlit, or Google Colab**  

## **🛠️ Tech Stack**
| Category        | Technologies Used |
|---------------|-----------------|
| **Programming Language** | Python 🐍 |
| **Frameworks/Libraries** | Flask, Scikit-Learn, NLTK, TextBlob, Pandas |
| **Frontend** | HTML, CSS (Bootstrap optional) |

## **📂 Project Structure**
```
sentiment-analysis/
│── app.py               # Flask application
│── sentiment_model.py   # Sentiment analysis logic
│── templates/
│   ├── index.html       # Web UI
│── static/
│   ├── styles.css       # CSS for styling
│── dataset/
│   ├── sample_reviews.csv  # Sample dataset
│── requirements.txt     # Dependencies
│── README.md            # Project Documentation
```

## **📥 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/aleena24bino/Product-Sentiment-Analysis.git
cd Product-Sentiment-Analysis
```

### **2️⃣ Create a Virtual Environment (Optional)**
```bash
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Download NLTK Data**
```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
```

### **5️⃣ Run the Flask Application**
```bash
python app.py
```
💡 Open **http://127.0.0.1:5000/** in your browser.

## **📊 How to Use**
### **📝 Option 1: Analyze a Single Review**
1. Enter a product review in the **text box**.
2. Click **Analyze**.
3. The system will display the sentiment (**Positive, Neutral, or Negative**).

### **📂 Option 2: Bulk Analysis with CSV**
1. Prepare a **CSV file** with a `review` column.
2. Click **Upload CSV** and select the file.
3. The system will analyze all reviews and display the results.

## **📷 Screenshots**
### **🔹 Sentiment Analysis UI**
![UI Example](https://www.dataquest.io/wp-content/uploads/2022/04/nlp-tutorial.png)

### **🔹 Bulk CSV Analysis Example**
| Review | Sentiment |
|--------|-----------|
| "I love this product!" | Positive |
| "The battery drains too fast." | Negative |
| "It’s okay, nothing special." | Neutral |

## **📡 API Usage (Optional)**
### **🟢 Endpoint: `POST /analyze`**
#### **Request:**
```json
{
    "review": "The product is amazing!"
}
```
#### **Response:**
```json
{
    "sentiment": "Positive"
}
```

## **🙌 Contributing**
1. **Fork** the repo  
2. Create a **new branch**  
3. Commit **your changes**  
4. Open a **Pull Request**  


## **📞 Contact**
💡 **Author:** Aleena Bino  
🔗 **GitHub:** [aleena24bino](https://github.com/aleena24bino)
