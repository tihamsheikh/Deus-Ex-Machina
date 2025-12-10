# 🚀 **Deus Ex Machina**

### *A simple approach toward General-Purpose Artificial Intelligence*

---

## 🌐 Overview

**Deus Ex Machina** is an experimental project aimed at building a **general-purpose artificial intelligence system** using the simplest architecture possible.
Think of it as a **single-page mini-Wikipedia powered by AI** — you ask a question, and it returns a clean, summarized explanation using **Google’s Gemini LLM**.

This project combines:

* 🧠 **LLM-powered reasoning**
* 🌐 **Flask web backend**
* 🎨 **Simple but elegant frontend**
* 🔗 **Gemini API integration**
* ⚙️ **Lightweight Python libraries like `requests`**

The goal?
To slowly evolve a basic Q/A system into a more advanced general intelligence.

---

## ✨ Features

### 🔍 **Ask Anything**

Users can enter any question, and the system fetches:

* processed insights
* concise summaries
* cleaned information

…directly from the **Gemini API**.

### ⚡ **Single Page Design**

The entire UI behaves like a one-page knowledge portal — fast, simple, distraction-free.

### 🧱 **Minimal Architecture**

The project uses:

* Flask (as backend)
* Gemini API (for intelligence)
* HTML/CSS/JS (for UI)
* Python libraries (`requests`, etc.)

### 💡 **Easy to Understand & Modify**

The goal is simplicity. Anyone can read, understand, modify, or extend the project.

---

## 🛠️ Tech Stack

| Component | Technology                                   |
| --------- | -------------------------------------------- |
| Backend   | **Flask (Python)**                           |
| AI Model  | **Google Gemini API**                        |
| Frontend  | **HTML, CSS, JavaScript**                    |
| Libraries | `requests`, `json`, and standard Python libs |

---

## 📂 Project Structure

```
Deus Ex Machina v2/       # Updated version
│── app.py                # Main Flask backend
│── templates/
│     └── index.html      # Frontend page
│── static/
│     └── style.css       # Styling

deus-ex-machina-v1/       # Older version
│── main.py               # Main Flask backend
│── page.html             # Frontend page  
├── style.css             # Styling

│── README.md
│── requirements.txt


```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
https://github.com/tihamsheikh/Deus-Ex-Machina.git
cd Deus-Ex-Machina
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your Gemini API key

Create a `.env` file or update your code with:

```
For v2
    api_key=const.key  # gemini api key-> (const.key)

For v1
  apiKey = os.environ['geminiai']  # gemini api key-> (os.environ['geminiai'])

```

### 4️⃣ Run the Flask app

```bash
v2-> python app.py
v1-> python main.py
```

Visit:

```
http://127.0.0.1:5000/
```

---

## 🤝 Contributing

Contributions are welcome!
Whether it's UI enhancement, improving summarization, optimizing Flask routing, or experimenting with more advanced reasoning — **every contribution brings us closer to general intelligence.**

To contribute:

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Create a pull request

---

## 🎯 Vision

This project aims to be a **starting point** — a playground for experimenting with reasoning, intelligence, and language processing.

The long-term dream is to build a system that:

* understands natural language deeply
* learns from interactions
* makes logical inferences
* behaves like a true general-purpose AI

Small steps—big goals.

---

## 📜 License

This project is open-source under the **MIT License**.
Feel free to use, modify, distribute, and expand it.

---

## 🌟 Acknowledgements

Special thanks to:

* **Google Gemini** for powerful language models
* The **Flask** community
* Every contributor dreaming of real AGI

