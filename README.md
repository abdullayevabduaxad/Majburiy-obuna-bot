# Telegram Bot - Kanalga Obuna Tekshiruvi

Ushbu Telegram bot `aiogram` kutubxonasi yordamida yaratilgan. Bot foydalanuvchi ko'rsatilgan kanallarga obuna bo'lganligini tekshiradi. Agar foydalanuvchi barcha kanallarga obuna bo'lmagan bo'lsa, ularni obuna bo'lishga taklif qiladi. Foydalanuvchi obuna bo'lganidan so'ng, botning funksiyalaridan foydalanishi mumkin.

## Xususiyatlar

- Foydalanuvchilarning belgilangan Telegram kanallariga obuna bo'lganligini tekshiradi.
- Agar foydalanuvchi obuna bo'lmagan bo'lsa, kanallarga obuna bo'lish uchun havolalar beradi.
- Foydalanuvchi obuna bo'lganidan keyin, obunasini tekshirishi uchun "✅ Tekshirish" tugmasi mavjud.
- Obuna muvaffaqiyatli amalga oshirilgandan so'ng, foydalanuvchi botdan foydalanishi mumkin.

## Talablar

- Python 3.7+ versiyasi
- `aiogram` kutubxonasi
- [BotFather](https://t.me/BotFather) dan olingan Telegram bot tokeni

## O'rnatish

1. Repodan loyihani yuklab oling:
    ```bash
    git clone https://github.com/your-repository.git
    cd your-repository
    ```

2. Virtual muhit yarating va uni faollashtiring (ixtiyoriy, lekin tavsiya etiladi):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS uchun
    venv\Scripts\activate  # Windows uchun
    ```

3. Kerakli Python kutubxonalarini o'rnating:
    ```bash
    pip install -r requirements.txt
    ```

4. `config.py` faylini yaratib, quyidagi ma'lumotlarni kiriting:
    ```python
    API_TOKEN = 'SIZNING_BOT_API_TOKEN'
    CHANNELS = ['@kanal1', '@kanal2']  # Bot tekshiradigan kanallar ro'yxati
    ```

5. Botingizni `CHANNELS` ro'yxatidagi har bir kanalda **administrator** qilib qo'shing. Bot foydalanuvchi a'zolik maqomini tekshirish uchun admin huquqlariga ega bo'lishi kerak.

## Botni ishga tushirish

Botni ishga tushirish uchun quyidagi buyruqni ishlating:
```bash
python main.py
Botdan foydalanish
Foydalanuvchi botni /start komandasi bilan ishga tushirganda, bot foydalanuvchining belgilangan kanallarga obuna bo'lganligini tekshiradi.
Agar foydalanuvchi barcha kanallarga obuna bo'lsa, botdan foydalanish imkoniyatiga ega bo'ladi.
Agar foydalanuvchi hali obuna bo'lmagan bo'lsa, unga obuna bo'lish uchun kanallarni ko'rsatuvchi tugmalarni yuboradi.
Foydalanuvchi obuna bo'lganidan keyin, "✅ Tekshirish" tugmasi orqali obunasini qayta tekshirishi mumkin.
Eslatma
Bot Admin Huquqlari: Foydalanuvchining kanalga obuna bo'lganligini tekshirish uchun bot kanalning administratori bo'lishi kerak. Shuning uchun, tekshirishni istagan barcha kanallarda botingizni admin sifatida qo'shishni unutmang.
Agar bot foydalanuvchining obuna maqomini tekshirishda xatolik yuzaga kelsa, foydalanuvchiga xabar beradi va qayta urinib ko'rishni so'raydi.
Loglar
Bot logging kutubxonasidan foydalanib, foydalanuvchilarning harakatlari va xatolarni qayd etadi. Ushbu loglarni konsoldan kuzatib, muammolarni hal qilishda foydalanishingiz mumkin


### Qo'shimcha Qadamlar:
1. `SIZNING_BOT_API_TOKEN` ni haqiqiy bot tokeningiz bilan almashtiring.
2. `@kanal1` va `@kanal2` ni tekshirishni xohlagan kanallaringiz nomlari bilan almashtiring.
3. Har bir kanal uchun botingizni administrator sifatida qo'shishni unutmang.
