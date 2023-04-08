import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6062124485:AAE4zT8JeJeT-s3V8gl5tgRPuSNOoyoOhcM'

logging.basicConfig(level=logging.DEBUG)

bot=Bot(token=API_TOKEN, parse_mode="HTML")
dp=Dispatcher(bot=bot)

@dp.message_handler(commands="help")
async def help(message: types.Message):
    await message.answer(
        text="Ushbu botni O'zbekiston Respublikasi Davlat Soliq qo'mitasi huzuridagi Fiskal instituti 'Soliq va soliqqa tortish' yo'nalishi 01-22-guruh talabari:\n\nNabiyev Sherzod,\n\nShoanvarov Abdulaziz,\n\nMuhammadsoliyev Musoxon,\n\nBoltaboyev Nuriddin tomonidan yaratildi. "
    )

@dp.message_handler(CommandStart())
async def on_start(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="O'zbekcha 🇺🇿"),
        types.KeyboardButton(text="Ruscha 🇷🇺"),
        types.KeyboardButton(text="Inglizcha 🇬🇧"),
    )
    await message.answer(
        text=f"🇺🇿 Assalomu alaykum! IELTS FIIN botiga hush kelibsiz! Iltimos tilni tanlang!, {message.from_user.full_name} \n🇷🇺 Добро пожаловать в бот IELTS FIIN! Пожалуйста, выберите язык!, {message.from_user.full_name} \n🇬🇧 Welcome to the IELTS FIIN bot! Please select a language!,  {message.from_user.full_name}",
        reply_markup = keyboard
    )

@dp.message_handler(text="O'zbekcha 🇺🇿")
async def uzbek(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS haqida ma'lumotlar"),
        types.KeyboardButton(text="IELTS ga tayyorlanishni boshlash"),
        types.KeyboardButton(text="IELTS ballarni hisoblash"),
        types.KeyboardButton(text="IELTS imtihonlari haqida yangiliklar"),
        types.KeyboardButton(text="Ortga ↩️"),
    )
    await message.answer(
        text="Siz o'zbek tilini tanladingiz! 🇺🇿",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS ga tayyorlanishni boshlash")
async def ieltsstart(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Listening 🎧"),
        types.KeyboardButton(text="Reading 📖"),
        types.KeyboardButton(text="Speaking 🗣"),
        types.KeyboardButton(text="Writing ✍️"),
        types.KeyboardButton(text="Asosiy sahifaga qaytish ↩️")
    )
    await message.answer(
        text="Start IELTS",
        reply_markup=keyboard
    )

@dp.message_handler(text="Listening 🎧")
async def listening(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="L1"),
        types.KeyboardButton(text="L2"),
        types.KeyboardButton(text="L3"),
        types.KeyboardButton(text="L4"),
        types.KeyboardButton(text="BACK 🇺🇿")
    )
    await message.answer(
        text="Listening tasks",
        reply_markup=keyboard
    )

@dp.message_handler(text="Speaking 🗣")
async def listening(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="S1"),
        types.KeyboardButton(text="S2"),
        types.KeyboardButton(text="S3"),
        types.KeyboardButton(text="S4"),
        types.KeyboardButton(text="BACK 🇺🇿")
    )
    await message.answer(
        text="Speaking tasks",
        reply_markup=keyboard
    )

@dp.message_handler(text="Writing ✍️")
async def wrtng(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Writting Task 1"),
        types.KeyboardButton(text="Writting Task 2"),
        types.KeyboardButton(text="BACK 🇺🇿")
    )
    await message.answer(
        text="Writing tasks",
        reply_markup=keyboard
    )

@dp.message_handler(text="Writting Task 1")
async def wrtng1(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧")
    )
    wrtng1 = open("wrt10.pdf", "rb")
    await bot.send_document(message.chat.id, document=wrtng1,
                            reply_markup=keyboard)
    wrtng1 = open("wrt11.pdf", "rb")
    await bot.send_document(message.chat.id, document=wrtng1,
                            reply_markup=keyboard)

@dp.message_handler(text="Writting Task 2")
async def wrtng2(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧")
    )
    wrtng2 = open("wrt20.pdf", "rb")
    await bot.send_document(message.chat.id, document=wrtng2,
                            reply_markup=keyboard)
    wrtng2 = open("wrt21.pdf", "rb")
    await bot.send_document(message.chat.id, document=wrtng2,
                            reply_markup=keyboard)

@dp.message_handler(text="S1")
async def spk1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧")
    )
    spk1 = open("spk1.pdf", "rb")
    await bot.send_document(message.chat.id, document=spk1,
                            reply_markup=keyboard)

@dp.message_handler(text="S2")
async def spk2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧")
    )
    spk2 = open("spk2.pdf", "rb")
    await bot.send_document(message.chat.id, document=spk2,
                            reply_markup=keyboard)

@dp.message_handler(text="S3")
async def spk3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧")
    )
    spk3 = open("spk3.pdf", "rb")
    await bot.send_document(message.chat.id, document=spk3,
                            reply_markup=keyboard)

@dp.message_handler(text="S4")
async def spk4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧")
    )
    spk4 = open("spk4.pdf", "rb")
    await bot.send_document(message.chat.id, document=spk4,
                            reply_markup=keyboard)

@dp.message_handler(text="Reading 📖")
async def listening(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="R1"),
        types.KeyboardButton(text="R2"),
        types.KeyboardButton(text="R3"),
        types.KeyboardButton(text="BACK 🇺🇿")
    )
    await message.answer(
        text="Reading tasks",
        reply_markup=keyboard
    )

@dp.message_handler(text="R1")
async def reading1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys R")
    )
    reading1 = open("reading1.pdf", "rb")
    await bot.send_document(message.chat.id, document=reading1,
                            reply_markup=keyboard)

@dp.message_handler(text="R2")
async def reading2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys R")
    )
    reading2 = open("reading2.pdf", "rb")
    await bot.send_document(message.chat.id, document=reading2,
                            reply_markup=keyboard)

@dp.message_handler(text="R3")
async def reading3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys R")
    )
    reading3 = open("reading3.pdf", "rb")
    await bot.send_document(message.chat.id, document=reading3,
                            reply_markup=keyboard)

@dp.message_handler(text="Keys R")
async def rkeys(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
    )
    rkeys=open("readingkeys.pdf", "rb")
    await bot.send_document(message.chat.id, document=rkeys,
                            reply_markup=keyboard)

@dp.message_handler(text="BACK 🇺🇿")
async def listening(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Listening 🎧"),
        types.KeyboardButton(text="Reading 📖"),
        types.KeyboardButton(text="Speaking 🗣"),
        types.KeyboardButton(text="Writing ✍️"),
        types.KeyboardButton(text="Asosiy sahifaga qaytish ↩️")
    )
    await message.answer(
        text="Oldingi sahifaga qaytildi.",
        reply_markup=keyboard
    )
@dp.message_handler(text="BACK 🇬🇧")
async def listening(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Listening 🎧"),
        types.KeyboardButton(text="Reading 📖"),
        types.KeyboardButton(text="Speaking 🗣"),
        types.KeyboardButton(text="Writing ✍️"),
        types.KeyboardButton(text="Return to the main page ↩️")
    )
    await message.answer(
        text="Returned to the previous page.",
        reply_markup=keyboard
    )

@dp.message_handler(text="BACK 🇷🇺")
async def listening(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Listening 🎧"),
        types.KeyboardButton(text="Reading 📖"),
        types.KeyboardButton(text="Speaking 🗣"),
        types.KeyboardButton(text="Writing ✍️"),
        types.KeyboardButton(text="Вернуться на главную ↩️️")
    )
    await message.answer(
        text="Вы вернулись на предыдущую страницу.",
        reply_markup=keyboard
    )


@dp.message_handler(text="L1")
async def listening1(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys")
    )
    listening1=open("listening1.ogg", "rb")
    await bot.send_audio(message.chat.id, audio=listening1,
                         reply_markup=keyboard)
    listening1 = open("listening1.pdf", "rb")
    await bot.send_document(message.chat.id, document=listening1,
                            reply_markup=keyboard)

@dp.message_handler(text="L2")
async def listening2(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys")
    )
    listening2=open("listening2.ogg", "rb")
    await bot.send_audio(message.chat.id, audio=listening2,
                         reply_markup=keyboard)
    listening2 = open("listening2.pdf", "rb")
    await bot.send_document(message.chat.id, document=listening2,
                            reply_markup=keyboard)

@dp.message_handler(text="L3")
async def listening3(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys")
    )
    listening3=open("listening3.ogg", "rb")
    await bot.send_audio(message.chat.id, audio=listening3,
                         reply_markup=keyboard)
    listening3 = open("listening3.pdf", "rb")
    await bot.send_document(message.chat.id, document=listening3,
                            reply_markup=keyboard)

@dp.message_handler(text="L4")
async def listening4(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
        types.KeyboardButton(text="Keys")
    )
    listening4=open("listening4.ogg", "rb")
    await bot.send_audio(message.chat.id, audio=listening4,
                         reply_markup=keyboard)
    listening4 = open("listening4.pdf", "rb")
    await bot.send_document(message.chat.id, document=listening4,
                            reply_markup=keyboard)

@dp.message_handler(text="Keys")
async def l1keys(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="BACK 🇺🇿"),
        types.KeyboardButton(text="BACK 🇷🇺"),
        types.KeyboardButton(text="BACK 🇬🇧"),
    )
    l1keys=open("keys.pdf", "rb")
    await bot.send_document(message.chat.id, document=l1keys,
                            reply_markup=keyboard)

# @dp.message_handler(text="L1")
# async def listening1(message: types.Message):
#     keyboard=types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)


@dp.message_handler(text="IELTS imtihonlari haqida yangiliklar")
async def news_uz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Asosiy sahifaga qaytish ↩️"),
    )
    await message.answer(
        text="https://t.me/RECENT_IELTS",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS haqida ma'lumotlar")
async def info_uz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Asosiy sahifaga qaytish ↩️"),
    )
    # info_uz=open("info_uz.txt", "rb")
    # await bot.send_document(message.chat.id, document=info_uz)
    await message.answer(
        text="IELTS (inglizcha: International English Language Testing System) — inglizzabon mamlakatda taʼlim olmoqchi, immigratsiya qilmoqchi yoki amaliyot oʻtamoqchi boʻlgan kishilar uchun test sinovi. Test ona tili ingliz tili boʻlmagan insonlarning bu tilni qanchalik chuqur bilishlarini aniqlashga yordam beradi.\n\nAvstraliya, Yangi Zelandiya davlatlariga immigratsiya maqsadida hujjat topshirganlar, Kanada, Avstraliya, Yangi Zelandiya, Amerika, Britaniya, Irlandiya universitetlarida oʻqishni xohlaganlar IELTS testini topshirishlari kerak. IELTS imtihonining yakuniy bahosini tan oladigan dunyo universitetlari muntazam ravishda oshib bormoqda.",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS ballarni hisoblash")
async def score(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS overall band score"),
        types.KeyboardButton(text="Reading score"),
        types.KeyboardButton(text="Listening score"),
        types.KeyboardButton(text="Asosiy sahifaga qaytish ↩️")
    )
    await message.answer(
        text="IELTS ballarini hisoblash haqida ma'lumotlarga ega bo'ling",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS overall band score")
async def allscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Orqaga")
    )
    allscore=open("allscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=allscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Reading score")
async def readingscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Orqaga")
    )
    readingscore=open("readingscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=readingscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Listening score")
async def listeningscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Orqaga")
    )
    listeningscore=open("listeningscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=listeningscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Orqaga")
async def orqaga(message:types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS overall band score"),
        types.KeyboardButton(text="Reading score"),
        types.KeyboardButton(text="Listening score"),
        types.KeyboardButton(text="Asosiy sahifaga qaytish ↩️")
    )
    await message.answer(
        text="Siz ortga qaytdingiz.",
        reply_markup=keyboard
    )


@dp.message_handler(text="Asosiy sahifaga qaytish ↩️")
async def menu_uz(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS haqida ma'lumotlar"),
        types.KeyboardButton(text="IELTS ga tayyorlanishni boshlash"),
        types.KeyboardButton(text="IELTS ballarni hisoblash"),
        types.KeyboardButton(text="IELTS imtihonlari haqida yangiliklar"),
        types.KeyboardButton(text="Ortga ↩️"),
    )
    await message.answer(
        text="Siz asosiy sahifaga qaytdingiz.",
        reply_markup=keyboard
    )

@dp.message_handler(text="Ortga ↩️")
async def on_start(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="O'zbekcha 🇺🇿"),
        types.KeyboardButton(text="Ruscha 🇷🇺"),
        types.KeyboardButton(text="Inglizcha 🇬🇧"),
    )
    await message.answer(
        text="Ortga qaytish",
        reply_markup=keyboard
    )

@dp.message_handler(text="Ruscha 🇷🇺")
async def rus(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Информация об IELTS"),
        types.KeyboardButton(text="Начать подготовку к IELTS"),
        types.KeyboardButton(text="Расчет баллов IELTS"),
        types.KeyboardButton(text="Новости об экзаменах IELTS"),
        types.KeyboardButton(text="Назад ↩️"),
    )
    await message.answer(
        text="Вы выбрали русский язык! 🇷🇺",
        reply_markup=keyboard
    )

@dp.message_handler(text="Новости об экзаменах IELTS")
async def news_ru(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Вернуться на главную ↩"),
    )
    await message.answer(
        text="https://t.me/RECENT_IELTS",
        reply_markup=keyboard
    )

@dp.message_handler(text="Начать подготовку к IELTS")
async def ieltsstart(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Listening 🎧"),
        types.KeyboardButton(text="Reading 📖"),
        types.KeyboardButton(text="Speaking 🗣"),
        types.KeyboardButton(text="Writing ✍️"),
        types.KeyboardButton(text="Вернуться на главную ↩")
    )
    await message.answer(
        text="Start IELTS",
        reply_markup=keyboard
    )

@dp.message_handler(text="Информация об IELTS")
async def info_ru(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Вернуться на главную ↩"),
    )
    await message.answer(
        text="IELTS (англ. International English Language Testing System) — международная система оценки знания английского языка.\n\nПозволяет определить уровень и навыки владения английским у людей, для которых он не является родным",
        reply_markup=keyboard
    )

@dp.message_handler(text="Расчет баллов IELTS")
async def score_ru(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS overall band score 🇷🇺"),
        types.KeyboardButton(text="Reading score 🇷🇺"),
        types.KeyboardButton(text="Listening score 🇷🇺"),
        types.KeyboardButton(text="Вернуться на главную ↩")
    )
    await message.answer(
        text="Получите информацию о расчете баллов IELTS.",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS overall band score 🇷🇺")
async def allscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Назад")
    )
    allscore=open("allscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=allscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Reading score 🇷🇺")
async def readingscoreru(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Назад")
    )
    readingscoreru=open("readingscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=readingscoreru,
                         reply_markup=keyboard)

@dp.message_handler(text="Listening score 🇷🇺")
async def listeningscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Назад")
    )
    listeningscore=open("listeningscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=listeningscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Назад")
async def orqaga(message:types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS overall band score 🇷🇺"),
        types.KeyboardButton(text="Reading score 🇷🇺"),
        types.KeyboardButton(text="Listening score 🇷🇺"),
        types.KeyboardButton(text="Вернуться на главную ↩")
    )
    await message.answer(
        text="Вы вернулись.",
        reply_markup=keyboard
    )

@dp.message_handler(text="Вернуться на главную ↩")
async def menu_ru(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Информация об IELTS"),
        types.KeyboardButton(text="Начать подготовку к IELTS"),
        types.KeyboardButton(text="Расчет баллов IELTS"),
        types.KeyboardButton(text="Новости об экзаменах IELTS"),
        types.KeyboardButton(text="Назад ↩️"),
    )
    await message.answer(
        text="Вы вернулись на главную страницу.",
        reply_markup=keyboard
    )

@dp.message_handler(text="Назад ↩️")
async def on_start(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="O'zbekcha 🇺🇿"),
        types.KeyboardButton(text="Ruscha 🇷🇺"),
        types.KeyboardButton(text="Inglizcha 🇬🇧"),
    )
    await message.answer(
        text="Возвращаться",
        reply_markup=keyboard
    )

@dp.message_handler(text="Inglizcha 🇬🇧")
async def eng(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Information about IELTS"),
        types.KeyboardButton(text="Start preparing for IELTS"),
        types.KeyboardButton(text="IELTS score calculation"),
        types.KeyboardButton(text="News about IELTS exams"),
        types.KeyboardButton(text="Back ↩️"),
        )
    await message.answer(
        text="You selected english language! 🇬🇧",
        reply_markup=keyboard
        )

@dp.message_handler(text="News about IELTS exams")
async def news_eng(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Return to the main page ↩"),
    )
    await message.answer(
        text="https://t.me/RECENT_IELTS",
        reply_markup=keyboard
    )

@dp.message_handler(text="Start preparing for IELTS")
async def ieltsstart(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Listening 🎧"),
        types.KeyboardButton(text="Reading 📖"),
        types.KeyboardButton(text="Speaking 🗣"),
        types.KeyboardButton(text="Writing ✍️"),
        types.KeyboardButton(text="Return to the main page ↩")
    )
    await message.answer(
        text="Start IELTS",
        reply_markup=keyboard
    )

@dp.message_handler(text="Information about IELTS")
async def info_eng(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Return to the main page ↩"),
    )
    await message.answer(
        text="The International English Language Testing System (IELTS /ˈaɪ.ɛlts/),[6] is an international standardized test of English language proficiency for non-native English language speakers. It is jointly managed by the British Council, IDP: IELTS Australia and Cambridge Assessment English,[6] and was established in 1989. IELTS is one of the major English-language tests in the world.\n\nIELTS is accepted by most Australian, British, Canadian, European, Irish and New Zealand academic institutions, by over 3,000 academic institutions in the United States, and by various professional organisations across the world.",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS score calculation")
async def score_ru(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS overall band score 🇬🇧"),
        types.KeyboardButton(text="Reading score 🇬🇧"),
        types.KeyboardButton(text="Listening score 🇬🇧"),
        types.KeyboardButton(text="Return to the main page ↩")
    )
    await message.answer(
        text="Get information about calculating IELTS scores.",
        reply_markup=keyboard
    )

@dp.message_handler(text="IELTS overall band score 🇬🇧")
async def allscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Back")
    )
    allscore=open("allscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=allscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Reading score 🇬🇧")
async def readingscoreru(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Back")
    )
    readingscoreru=open("readingscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=readingscoreru,
                         reply_markup=keyboard)

@dp.message_handler(text="Listening score 🇬🇧")
async def listeningscore(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Back")
    )
    listeningscore=open("listeningscore.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=listeningscore,
                         reply_markup=keyboard)

@dp.message_handler(text="Back")
async def orqaga(message:types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="IELTS overall band score 🇬🇧"),
        types.KeyboardButton(text="Reading score 🇬🇧"),
        types.KeyboardButton(text="Listening score 🇬🇧"),
        types.KeyboardButton(text="Return to the main page ↩")
    )
    await message.answer(
        text="You're back.",
        reply_markup=keyboard
    )

@dp.message_handler(text="Return to the main page ↩")
async def menu_eng(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Information about IELTS"),
        types.KeyboardButton(text="Start preparing for IELTS"),
        types.KeyboardButton(text="IELTS score calculation"),
        types.KeyboardButton(text="News about IELTS exams"),
        types.KeyboardButton(text="Back ↩️"),
    )
    await message.answer(
        text="You have returned to the main page.",
        reply_markup=keyboard
    )

@dp.message_handler(text="Back ↩️")
async def on_start(message: types.Message):
    keyboard=types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="O'zbekcha 🇺🇿"),
        types.KeyboardButton(text="Ruscha 🇷🇺"),
        types.KeyboardButton(text="Inglizcha 🇬🇧"),
    )
    await message.answer(
        text="Go back",
        reply_markup=keyboard
    )


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp)