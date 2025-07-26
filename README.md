# Task-3
# 🤖 AI Chatbot with NLP – CodTech Internship Task 3

This project is a simple rule-based chatbot created using Python and the NLTK library. It answers basic user queries with natural language processing (NLP) techniques and runs in the terminal.

---

## 📌 Features

✅ Uses **NLTK** (Natural Language Toolkit) for NLP  
✅ Supports greetings, name inquiries, help, and farewell interactions  
✅ Handles unmatched inputs with a fallback response  
✅ Fully terminal-based interaction (no GUI needed)  
✅ Easily customizable response patterns

---

## 🛠️ Tech Stack

**Python 3.x**

### Libraries Used:
- `nltk` → Natural Language Processing (tokenizer, reflections)
- `re` → Regex pattern matching (built-in)

---

## 🚀 Installation & Setup

### 1️⃣ Clone this Repository
```bash
git clone https://github.com/your-username/chatbot-nlp.git
cd chatbot-nlp
2️⃣ Install Dependencies
bash
Copy
Edit
pip install nltk
3️⃣ Download NLTK Data
The script automatically downloads punkt, but you can also do it manually:

python
Copy
Edit
import nltk
nltk.download('punkt')
▶️ Running the Script
Run the Python file in your terminal:

bash
Copy
Edit
python Chat-bot.py
✅ Sample Interaction
pgsql
Copy
Edit
Hi! I'm CodTechBot. Type 'quit' or 'bye' to exit.
> hello
Hi there! What can I do for you?
> what is your name?
I'm a chatbot created using Python and NLTK.
> how are you?
I'm doing well, thank you!
> can you help me?
Sure, I'm here to help. What do you need assistance with?
> goodbye
Bye! Have a nice day!
📂 Project Structure
bash
Copy
Edit
chatbot-nlp/
│
├── Chat-bot.py         # Main Python script
├── README.md           # Project documentation (this file)
└── nltk_data/          # Automatically created when nltk downloads data
📋 Task Requirement
This project fulfills Task 3 of the CodTech Internship:

Build a chatbot using NLP libraries like NLTK or spaCy, capable of answering user queries.
Deliverable: A Python script and a working chatbot.

👨‍💻 Author
Sathyasree
🌐 GitHub: github.com/sathyasree-r

🤝 Contributing
Pull requests and feedback are welcome!

📜 License
This project is licensed under the MIT License.
