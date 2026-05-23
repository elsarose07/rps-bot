<div align="center">

# 🎮 Rock-Paper-Scissors Discord Bot

### *A modern, interactive, and secure Discord bot for the classic game.*

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Discord.py](https://img.shields.io/badge/discord.py-2.0%2B-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discordpy.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Style: Professional](https://img.shields.io/badge/Style-Professional-green.svg?style=for-the-badge)](https://github.com/)

---

[Features](#-features) • [Quick Start](#-quick-start) • [How to Play](#-how-to-play) • [Security](#-security) • [Future Roadmap](#-future-roadmap)

</div>

## ✨ Features

Experience a seamless and modern Rock-Paper-Scissors game directly within your Discord server.

- ⚡ **Slash Commands** - Native Discord integration with `/rps`.
- 🖱️ **Interactive UI** - High-quality button-based gameplay.
- 🎨 **Dynamic Embeds** - Color-coded feedback (Win: 🟢, Lose: 🔴, Draw: 🟡).
- 🔄 **Quick Replay** - Restart games instantly with a single click.
- 🛡️ **Secure** - Built-in support for environment variables to protect your tokens.
- ⏳ **Clean Design** - Automatic button timeouts to prevent channel clutter.

---

## 🚀 Quick Start

Get your bot up and running in minutes.

### 1️⃣ Prepare your Bot
1. Create an application on the [Discord Developer Portal](https://discord.com/developers/applications).
2. Navigate to the **Bot** tab and copy your **Token**.
3. Under **OAuth2** → **URL Generator**, select `bot` and `applications.commands`.
4. Give it permissions: `Send Messages`, `Embed Links`, `Use Slash Commands`, and `Use External Emoji`.
5. Invite the bot to your server using the generated URL.

### 2️⃣ Installation
Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3️⃣ Configuration
Create a `.env` file in the root directory to store your token securely:

```env
DISCORD_TOKEN=your_secret_token_here
```

### 4️⃣ Launch
Start the bot and watch it sync commands:

```bash
python rps-bot.py
```

---

## 🎮 How to Play

1. Type **`/rps`** in any text channel.
2. Click the **"Start Game"** 🎮 button.
3. Select your move: **🪨 Rock**, **📄 Paper**, or **✂️ Scissors**.
4. The bot will reveal its choice and the result in a beautiful embed.
5. Click **"Play Again"** 🔄 to continue the fun!

### 📋 Game Rules
| Move | Beats | Loses to |
| :--- | :--- | :--- |
| **🪨 Rock** | ✂️ Scissors | 📄 Paper |
| **📄 Paper** | 🪨 Rock | ✂️ Scissors |
| **✂️ Scissors** | 📄 Paper | 🪨 Rock |

---

## 🔐 Security Best Practices

We prioritize security. Never expose your bot token!

> [!IMPORTANT]
> Always use environment variables for sensitive data. This project is pre-configured to use `python-dotenv`.

1. **Use `.env`**: Store your secrets in a `.env` file (included in `.gitignore`).
2. **Never Hardcode**: Avoid placing tokens directly in `rps-bot.py`.
3. **Regenerate Often**: If your token is leaked, reset it immediately in the Developer Portal.

---

## 📁 File Structure

```text
.
├── rps-bot.py          # Main bot implementation (Recommended)
├── rps-bot-secure.py   # Secure variant using environment variables
├── .env                # Secret environment variables (Private)
├── .gitignore          # Prevents sensitive files from being committed
├── requirements.txt    # Project dependencies
└── README.md           # You are here!
```

---

## 💡 Future Roadmap

- 📊 **Statistics** - Track lifetime wins and losses.
- 🏆 **Leaderboard** - Server-wide rankings.
- ⚔️ **PvP Mode** - Challenge your friends to a match.
- 🎨 **Theming** - Customizable embed colors per server.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information (or feel free to use it in your own projects!).

<div align="center">

Made with ❤️ for the Discord Community

</div>