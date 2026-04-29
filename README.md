⚡ DiskWala Ultimate

A high-performance Telegram bot + Mini App that extracts direct video links from DiskWala and serves them instantly for browser streaming.

---

🚀 Features

- 🤖 Telegram Bot (Pyrogram based)
- 📱 Telegram Mini App (WebApp UI)
- ⚡ Fast DiskWala link extractor
- 🔗 Direct browser streaming (no download delay)
- 🧠 Smart caching system
- 📦 File size detection
- 🎬 Auto caption generation
- 🔄 Single-process (Bot + API + Web)
- 🚀 Ready for VPS / Railway deployment

---

🏗 Project Structure

diskwala-ultimate/
│── server.py
│── config.py
│── requirements.txt
│── extractor/
│   ├── main.py
│   ├── diskwala.py
│── services/
│   ├── cache.py
│   ├── metadata.py
│   ├── caption.py
│── web/
│   ├── index.html
│   ├── style.css
│   ├── script.js
│── diskwala.service

---

⚙️ Setup

1. Clone Repository

git clone https://github.com/yourusername/diskwala-ultimate.git
cd diskwala-ultimate

---

2. Install Dependencies

pip install -r requirements.txt

---

3. Configure

Edit "config.py":

API_ID = 12345
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"
DOMAIN = "http://yourdomain.com"

---

▶️ Run Project

python server.py

---

🧠 How It Works

🔹 Telegram Bot

- Receives DiskWala link
- Extracts direct video URL
- Sends streaming button

🔹 Mini App

- User pastes link
- API extracts link
- Button appears → opens browser

🔹 API

- "/extract" → returns direct link
- "/fast" → redirects to video stream

---

🌐 API Endpoints

POST "/extract"

Request:

{
  "link": "https://diskwala.com/app/xxxxx"
}

Response:

{
  "status": true,
  "direct": "video_url"
}

---

GET "/fast"

/fast?url=video_link

👉 Redirects to direct video

---

📱 Mini App Flow

1. Open bot
2. Click Open Downloader
3. Paste link
4. Click Generate
5. Click Open Video
6. Video opens in browser

---

🔄 Auto Restart (systemd)

Install service:

sudo mv diskwala.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable diskwala
sudo systemctl start diskwala

Check status:

systemctl status diskwala

---

⚠️ Requirements

- Python 3.9+
- VPS / Server recommended
- Public domain for Mini App

---

🚀 Deployment Options

Platform| Support
VPS| ✅ Recommended
Railway| ✅ (single process)
Render| ✅
Docker| 🔄 Optional

---

⚡ Performance Notes

- In-memory cache (can upgrade to Redis)
- Single process (Bot + API)
- Suitable for low to medium traffic

---

🔐 Disclaimer

This project is for educational purposes only.
Ensure compliance with DiskWala and content hosting policies.

---

👨‍💻 Author

Developed for high-speed link extraction and streaming automation.

---

⭐ Future Improvements

- Redis caching
- Multi-quality streaming
- Thumbnail preview
- User history
- Admin dashboard
- CDN integration

---

💡 Contributing

Pull requests are welcome.
For major changes, open an issue first.

---

📜 License

MIT License
