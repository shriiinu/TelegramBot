# Telegram Auto-Reply Bot 🤖

A simple Python-based Telegram bot that automatically replies to messages based on keywords.  
Built using the [`python-telegram-bot`](https://python-telegram-bot.org) library.

---

## Features ✨
- **Keyword-based replies** (e.g., say "hi", "weather", "bye", "help" — get auto responses).
- Works in **real-time** with Telegram chat.
- Easy to modify and add your own keywords.
- Fallback reply for unrecognized messages.

---

## How It Works ⚙️
The bot listens to messages in Telegram and checks for certain keywords.  
It uses simple Python `if-elif-else` conditions to match text and send appropriate replies.

**Example:**
- `hi` → "Hello! How are you?"
- `weather` → "I can't check live weather yet, but it's sunny in my heart ☀️"
- `bye` → "Goodbye! See you soon."
- `help` → "You can say 'hi', 'weather', or 'bye' to see my responses!"
- Any other text → Echoes back what you typed.

---

## Installation 🛠️

1. **Clone this repository**
     ```bash
     git clone https://github.com/yourusername/telegram-auto-reply-bot.git
     cd telegram-auto-reply-bot
   
2. **Install dependencies**
    ```bash
    pip install python-telegram-bot==13.15
3. **Get a Telegram Bot Token**
    Open Telegram.
    Search for @BotFather.
    Type /newbot and follow the instructions.
    Copy your API token.

4. **Add your token**
    Open telegrambot.py.
    Replace YOUR_BOT_TOKEN_HERE with your bot token from BotFather.
