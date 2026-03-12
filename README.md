# 🇯🇵 Japanese Learning Helper
![demo](fuji.gif)  
A small tool written in **Python** to help learn Japanese kana, verb conjugations, and basic grammar.  
It provides interactive mini-games and a graphical interface to make learning more fun and engaging.  

---

## 🖥 Development Environment
- Windows 10 22H2  
- Python 3.13.1  
- Tkinter + Pygame + gTTS + Janome  

---

## ✨ Features
- **Multi-language support**: English, Simplified Chinese, Traditional Chinese  
- **GUI interface**: clean and beginner-friendly  
- **Difficulty levels**: Easy / Medium / Hard  
- **Pronunciation**: kana reading with gTTS + Pygame  
- **Learning modes**:
    - Guess Romaji from Hiragana  
    - Guess Romaji from Katakana  
    - Guess Hiragana from Romaji  
    - Guess Katakana from Romaji  
    - Guess Katakana from Hiragana  
    - Gojuon chart (with pronunciation)  
    - Verb conjugation practice (supports Ichidan, Godan, and irregular verbs)  

---

## 🚀 Usage  
1. Clone or download this project  
2. Install dependencies:  
    ```bash  
    pip install pygame gTTS janome  
3. Run:  
    python main.py  
4. Keep the **data** folder intact (contains language files and kana mappings).  

---

## 📂 Project Structure  
    Japanese-Learning-Helper/  
    │── main.py              # Main program entry  
    │── data/                # Data folder  
    │   ├── hkr/             # Kana ↔ Romaji mappings  
    │   └── lang/            # Multi-language support  
    │── icon.ico             # Program icon  
    │── fuji.gif             # Demo image  

---

## 🗺 Future Plans  
    - Add more language support (e.g., Korean, French)  
    - Extend verb conjugation (passive, causative, honorific forms)  
    - Add more game modes  
    - Remove Herobrine 👀  
