# 🌿 AYUR – Health Chatbot

## 📌 Overview
**AYUR – Health Chatbot** is an AI-powered health assistant designed to help users manage their daily health routines.  
It provides:
- Personalized reminders for medicine intake and checkups
- Ayurvedic tips and natural home remedies
- Health-related guidance in a conversational way

The chatbot combines **modern AI** with **Ayurvedic wisdom** to promote holistic health management.

## 🚀 Features
- Medicine intake reminders with schedule tracking
- Periodic health checkup reminders
- Ayurvedic lifestyle tips and home remedies
- Interactive chatbot interface for user queries
- Backend powered by AI models for intelligent responses

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS  
- **Backend**: Django, Streamlit  
- **Database**: SQL  
- **AI/ML**: Gemini API integration for natural language responses  

## 📂 Project Structure
```
AYUR/
│── frontend/           # HTML, CSS files for user interface
│── backend/            # Django + Streamlit backend logic
│   ├── chatbot/        # Chatbot engine and AI integrations
│   ├── reminders/      # Medicine & checkup reminders
│   ├── tips/           # Ayurvedic remedies and suggestions
│── data/               # Knowledge base / training data
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/<your-username>/AYUR.git
cd AYUR

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Usage
```bash
# Run Django server
python manage.py runserver

# Run Streamlit chatbot UI
streamlit run backend/chatbot/app.py
```

## 📊 Future Improvements
- Support for multilingual responses (Hindi, English, etc.)
- Integration with wearable health devices (smartwatch/fitness bands)
- Advanced AI-based personalized health recommendations
- Mobile application support (Android/iOS)

## 🤝 Contributing
1. Fork the project  
2. Create your feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added feature XYZ"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a Pull Request  
---
🌱 *AYUR – Blending AI with Ayurveda for healthier living.*
