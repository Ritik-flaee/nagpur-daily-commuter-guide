# 🚕 Nagpur Daily Commuter Guide

> AI-powered local travel assistant for Nagpur commuters | Built for Kiro Challenge Week 5

**Live Demo**: (https://nagpur-daily-commuter-guide-cmuzybbw3-ritik-flaees-projects.vercel.app/)

---

## 📖 What is this?

A chat assistant that helps Nagpur residents navigate daily commuting challenges:
- 🚗 **Traffic updates** with real route advice
- 💰 **Auto fare guide** with haggling tips
- 🚇 **Metro information** (operational since 2019)
- 🛡️ **Safety tips** for night travel
- 🌧️ **Monsoon warnings** for flood-prone areas

**No external APIs** - all knowledge comes from a single `product.md` context file, demonstrating Kiro's ability to learn deep local expertise.

---

## 🎯 Problem We're Solving

Every day, Nagpur commuters face:
- ⏰ Hours wasted in unpredictable traffic
- 💸 Getting overcharged by auto drivers
- 😰 Unsafe routes, especially for women at night
- 🌧️ Flooded roads during monsoon with no warnings

**This guide provides instant, reliable local advice** - like having a knowledgeable friend who knows every shortcut in Nagpur.

---

## 🏗️ Project Structure

```
nagpur-daily-commuter-guide/
├── .kiro/
│   └── config.json      # Kiro configuration (REQUIRED for challenge)
├── api/
│   └── index.py         # Flask app with interactive UI
├── product.md           # Knowledge base (REQUIRED - 600+ lines of local expertise)
├── requirements.txt     # Python dependencies
├── vercel.json          # Deployment configuration
└── README.md            # This file
```

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ritik-flaee/nagpur-daily-commuter-guide.git
cd nagpur-daily-commuter-guide
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Locally

```bash
cd api
python index.py
```

### Step 4: Open in Browser

Go to: `http://localhost:5000`

---

## 🌐 Deploy to Vercel

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Deploy

```bash
vercel --prod
```

That's it! Your app will be live.

---

## 💡 How to Use

### Basic Usage

1. **Open the app** in your browser
2. **Type a question** like "How to get from Dharampeth to Sitabuldi at 6 PM?"
3. **Get instant advice** with routes, fares, and tips

### Quick Query Buttons

Click any button to try:
- 🚗 **Sitabuldi Traffic** - Current traffic status
- 💰 **Auto Fares** - Zone-wise fare guide
- 🚇 **Metro Info** - Lines, timings, stations
- 🛡️ **Night Safety** - Safe travel tips
- 🌧️ **Monsoon Tips** - Flood warnings

### Location Feature

1. Click **"Enable Location"**
2. Allow browser permission
3. Get **personalized suggestions** based on your area

---

## 🎨 Features

| Feature | Description |
|---------|-------------|
| **Interactive Cards** | Information displayed in organized, clickable cards |
| **Color-Coded Status** | 🟢 Good, 🟡 Warning, 🔴 Avoid |
| **Quick Actions** | One-click follow-up queries |
| **Location Aware** | Personalized tips based on your area |
| **Dark Theme** | Modern, easy-on-eyes design |
| **Mobile Friendly** | Works on all devices |

---

## 📚 The Knowledge Base (`product.md`)

The `product.md` file contains **600+ lines** of curated Nagpur expertise:

- **Traffic Hotspots**: Sitabuldi, Itwari, Ramdaspeth patterns
- **Metro System**: Aqua & Orange lines, stations, fares
- **Auto Fares**: Zone-wise pricing, negotiation scripts
- **Safety Info**: Women's safety, night travel, emergency contacts
- **Monsoon Data**: Flood-prone areas, safe routes
- **Local Slang**: Nagpuri phrases for better communication

**This single file teaches the AI everything about Nagpur commuting.**

---

## ✅ Kiro Challenge Requirements

| Requirement | Status |
|-------------|--------|
| Theme: City/Culture Understanding | ✅ Nagpur commuter expertise |
| `product.md` Context File | ✅ 600+ lines of local knowledge |
| `.kiro/` Directory | ✅ Included at root |
| Agent Logic for Local Knowledge | ✅ Handles traffic, fares, safety, metro |
| Public GitHub Repository | ✅ |

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Deployment**: Vercel Serverless
- **AI Context**: Custom `product.md` file

---

## 📸 Screenshots

*Add screenshots of your app here for the blog post*

1. Home screen with welcome message
2. Traffic query with card response
3. Metro info with color-coded details
4. Location enabled with personalized tips

---

## 🤝 Contributing

1. Fork the repository
2. Add more knowledge to `product.md`
3. Submit a pull request

Ideas for contribution:
- More route information
- Updated fare data
- New areas coverage
- Festival traffic patterns

---

## 📄 License

MIT License - feel free to use and modify!

---

## 👤 Author

**Ritik** - Built for Kiro Challenge Week 5

---

## 🙏 Acknowledgments

- Kiro team for the amazing AI platform
- Nagpur commuters who shared their daily struggles
- Local auto drivers for fare insights 😄

---

*Made with ❤️ for Nagpur*
