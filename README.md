# TikTok Video Downloader Bot 🎥

Telegram bot for downloading TikTok videos without watermark. Built with **aiogram** (Python) and a third-party API (TikWM) for video extraction.

> 🇺🇿 O'zbekcha tavsif quyida (pastda) keltirilgan.

---

# CREATOR DEV

<div align="center">
  <img src="./banner.svg" width="100%"/>
</div>



## ✨ Features

- Download any public TikTok video by sending its link
- Removes the TikTok watermark
- Fast response via third-party API (TikWM)
- Simple, single-command usage — no setup needed from the user's side
- Built on **aiogram 3.x** async framework

## 🛠 Tech Stack

| Component       | Technology              |
|------------------|--------------------------|
| Language          | Python 3.10+             |
| Bot framework     | aiogram (3.x)            |
| Video extraction  | TikWM API (third-party)  |
| HTTP client       | aiohttp                  |

## 🚀 Getting Started

### 1. Clone / copy the project
```bash
git clone <your-repo-url>
cd tiktok-downloader-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure your bot token
Create a `.env` file in the project root:
```env
BOT_TOKEN=your_telegram_bot_token_here
```
Get a token from [@BotFather](https://t.me/BotFather) on Telegram.

### 4. Run the bot
```bash
python bot.py
```

## 💬 Usage

1. Start a chat with the bot and send `/start`
2. Send any TikTok video link, e.g.:
   ```
   https://www.tiktok.com/@username/video/1234567890123456789
   ```
3. The bot fetches the video via the TikWM API and sends it back without the watermark

## ⚠️ Notes & Limitations

- Depends on the TikWM third-party API — if TikWM changes or goes down, downloads may temporarily fail
- Only public videos can be downloaded; private accounts are not supported
- Respect TikTok creators' content rights — use downloaded videos responsibly and avoid redistributing copyrighted content without permission
- Telegram has a 50 MB file size limit for bots sending videos via the standard Bot API; very long/high-quality videos may fail to send

## 📄 License

This project is provided as-is for personal and educational use.

---

---

# TikTok Video Yuklab Oluvchi Bot 🎥

TikTok videolarini suv belgisiz (watermarksiz) yuklab beruvchi Telegram bot. **aiogram** (Python) kutubxonasi va video olish uchun uchinchi tomon API (TikWM) asosida yaratilgan.

## ✨ Imkoniyatlari

- Istalgan ochiq (public) TikTok videosini havola orqali yuklab olish
- TikTok suv belgisini (watermark) olib tashlaydi
- Uchinchi tomon API (TikWM) orqali tezkor javob beradi
- Foydalanuvchi uchun oddiy — faqat havolani yuborish kifoya
- **aiogram 3.x** asinxron freymvorki asosida qurilgan

## 🛠 Texnologiyalar

| Qism              | Texnologiya               |
|--------------------|-----------------------------|
| Dasturlash tili     | Python 3.10+                |
| Bot freymvorki      | aiogram (3.x)                |
| Video olish         | TikWM API (uchinchi tomon)   |
| HTTP klient         | aiohttp                      |

## 🚀 O'rnatish va ishga tushirish

### 1. Loyihani yuklab oling
```bash
git clone <repo-havolangiz>
cd tiktok-downloader-bot
```

### 2. Kerakli kutubxonalarni o'rnating
```bash
pip install -r requirements.txt
```

### 3. Bot tokenini sozlang
Loyiha papkasida `.env` fayl yarating:
```env
BOT_TOKEN=sizning_telegram_bot_tokeningiz
```
Tokenni Telegramdagi [@BotFather](https://t.me/BotFather) orqali oling.

### 4. Botni ishga tushiring
```bash
python bot.py
```

## 💬 Foydalanish

1. Bot bilan suhbatni boshlang: `/start`
2. Istalgan TikTok video havolasini yuboring, masalan:
   ```
   https://www.tiktok.com/@username/video/1234567890123456789
   ```
3. Bot TikWM API orqali videoni topadi va suv belgisisiz holda sizga qaytaradi

## ⚠️ Eslatmalar va cheklovlar

- Bot TikWM uchinchi tomon API'siga bog'liq — agar TikWM o'zgarsa yoki ishlamay qolsa, yuklab olish vaqtincha to'xtab qolishi mumkin
- Faqat ochiq (public) videolarni yuklab olish mumkin; yopiq (private) akkauntlar qo'llab-quvvatlanmaydi
- TikTok kontent yaratuvchilarining huquqlarini hurmat qiling — yuklab olingan videolarni mas'uliyat bilan ishlating va ruxsatsiz tarqatmang
- Telegram Bot API orqali video yuborishda standart 50 MB hajm chegarasi mavjud; juda uzun/sifatli videolar yuborilmasligi mumkin

## 📄 Litsenziya

Ushbu loyiha shaxsiy va ta'lim maqsadlarida, "bor holicha" taqdim etiladi.
