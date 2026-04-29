import threading
from flask import Flask, request, jsonify, redirect, send_from_directory
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from config import *
from extractor.main import extract
from services.cache import get, set
from services.metadata import get_video_info
from services.caption import make_caption

# ===== BOT =====
bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message):
    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "🚀 Open Downloader",
            web_app=WebAppInfo(url=DOMAIN)
        )]
    ])
    await message.reply_text("⚡ Open Downloader", reply_markup=btn)

@bot.on_message(filters.text)
async def handle(client, message):
    link = message.text.strip()

    if "diskwala.com/app" not in link:
        return await message.reply_text("❌ Invalid link")

    msg = await message.reply_text("⏳ Processing...")

    cached = get(link)
    if cached:
        direct = cached
    else:
        direct = extract(link)
        if direct:
            set(link, direct)

    if not direct:
        return await msg.edit_text("❌ Failed")

    info = get_video_info(direct)
    caption = make_caption(info)

    final_link = f"{DOMAIN}/fast?url={direct}"

    btn = InlineKeyboardMarkup([
        [InlineKeyboardButton("📥 Open Video", url=final_link)]
    ])

    await msg.edit_text(caption, reply_markup=btn)

# ===== FLASK =====
app = Flask(__name__, static_folder="web")

@app.route("/")
def home():
    return send_from_directory("web", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("web", path)

@app.route("/fast")
def fast():
    return redirect(request.args.get("url"))

@app.route("/extract", methods=["POST"])
def extract_api():
    link = request.json.get("link")

    cached = get(link)
    if cached:
        return jsonify({"status": True, "direct": cached})

    direct = extract(link)

    if not direct:
        return jsonify({"status": False})

    set(link, direct)
    return jsonify({"status": True, "direct": direct})

# ===== RUN BOTH =====
def run_bot():
    bot.run()

threading.Thread(target=run_bot).start()

app.run(host="0.0.0.0", port=5000)
