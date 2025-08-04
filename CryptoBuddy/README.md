# CryptoBuddy – AI-Inspired Cryptocurrency Advisor Chatbot

## Project Overview

**CryptoBuddy** is a simple rule-based chatbot that gives basic cryptocurrency investment advice. It simulates beginner-friendly AI behavior by processing predefined crypto data and responding to user input based on logical rules.

This chatbot helps users explore two main investment aspects:

- **Profitability**: Evaluated through price trends and market capitalization
- **Sustainability**: Determined by energy usage and sustainability score

The project was developed as part of the PLP Academy Week 1 AI Assignment.

---

## Features

- Text-based chatbot interface in Python
- Answers user queries about crypto investments
- Identifies profitable coins based on price and market cap
- Identifies eco-friendly coins based on sustainability data
- Recommends coins based on defined rules
- Handles general crypto-related questions

---

## Technology Stack

- **Language**: Python 3
- **Platform**: Jupyter Notebook / Google Colab / Local Python IDE
- **Libraries**: No external libraries required

---

## Sample Crypto Dataset

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

## How It Works

**CryptoBuddy** uses basic `if-else` conditions and keyword detection to simulate intelligent conversation. It processes user input, matches it to predefined logic, and selects the most suitable coin based on the question type.

---

## Example Questions It Can Answer

- What’s the most sustainable crypto?
- Which coin is profitable right now?
- What crypto is trending?
- What should I invest in?

---

## How to Run the Chatbot

1. Download or copy the script (`crypto_advisor_chatbot.py`)
2. Open the script in your IDE or a Jupyter/Colab notebook
3. Run the file and enter input when prompted
4. To exit, type `exit` or `quit`

---

## Logic Behind Advice

- **Profitability Rule**: Recommends coins where `price_trend == "rising"` and `market_cap == "high"`
- **Sustainability Rule**: Recommends coins where `energy_use == "low"` and `sustainability_score > 7`

---

## Disclaimer

This chatbot is a simplified educational simulation. It does not analyze real-time cryptocurrency data. The suggestions are based on hardcoded mock data and should not be considered financial advice.

---

## Submission Checklist

- [x] Python script file (`crypto_advisor_chatbot.py`)
- [x] Markdown README file (`README.md`)
- [x] Screenshot of chatbot interaction *(to be added)*
- [x] 30-second screen recording of the chatbot in action
- [x] 50-word summary *(below)*

---

## 50-Word Summary

CryptoBuddy simulates how AI systems assist with financial decisions by applying simple rule-based logic to a fixed dataset. The chatbot provides investment suggestions based on price trends and sustainability data. While not connected to real markets, it demonstrates how AI can be used to solve real-world problems through decision support.

---

## Screenshot

![Chatbot Interaction Screenshot](screenshot.png)

