# t.me/AI_DianaBot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(list_command)

async def lesya_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lesya_poem = ("""
    Contra spem spero!
    Гетьте, думи, ви хмари осінні!
    То ж тепера весна золота!
    Чи то так у жалю, в голосінні
    Проминуть молодії літа?
    
    Ні, я хочу крізь сльози сміятись,
    Серед лиха співати пісні,
    Без надії таки сподіватись,
    Жити хочу! Геть, думи сумні!

    """
    )
    await update.message.reply_text(lesya_poem)

async def Taras_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Taras_poem = ("""
    Садок вишневий коло хати,
    Хрущі над вишнями гудуть,
    Плугатарі з плугами йдуть,
    Співають ідучи дівчата,
    А матері вечерять ждуть.
    """
    )
    await update.message.reply_text(Taras_poem)

async def Franko_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Franko_poem =("""
    Як гул століть, як шум віків,
    Як бурі подих, — рідна мова,
    Вишневих ніжних пелюстків,
    І дужих хвиль огниста повінь.           
    """
    )
    await update.message.reply_text(Franko_poem)

async def Tichina_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Tichina_poem = ("""
    А я у гай ходила
    По квітку ось яку!
    А там дерева — люлі,
    І все отак зозулі.
    """
    )
    await update.message.reply_text(Tichina_poem)

async def Simonenko_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Simonenko_poem = ("""
    Ти знаєш, що ти — людина?
    Ти знаєш про це чи ні?
    Усмішка твоя — єдина,
    Мука твоя — єдина,
    Очі твої — одні.
    """
    )
    await update.message.reply_text(Simonenko_poem)

async def Oles_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Oles_poem = ("""
    Чари ночі, ніч чарівна,
    Знову серце п'є з чаші життя.
    Легкокрилі мрії весни
    Знов летять у далеч ясну.
    """
    )
    await update.message.reply_text(Oles_poem)

async def Kostenko_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Kostenko_poem = ("""
    А й правда, крилатим ґрунту не треба.
    Землі немає, то буде небо.
    Немає поля, то буде воля.
    Немає пари, то будуть хмари.
    В цьому, напевно, правда пташина...
    А як же людина? А що ж людина?
    Живе на землі. Сама не літає.
    А крила має. А крила має!
    """
    )
    await update.message.reply_text(Kostenko_poem)

async def Rilskiy_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Rilskiy_poem = ("""
    Із поля дівчина утомлена прийшла
    І, хоч вечеряти дбайлива кличе мати,
    За сапку — і в квітник, де рожа розцвіла,
    Де кучерявляться кущі любистку й м'яти.

    З путі далекої вернувся машиніст,
    Укритий порохом, увесь пропахлий димом,-
    До виноградника! — Чи мільдью часом лист
    Де не попсований? Ну, боротьбу вестимем!
    """
    )
    await update.message.reply_text(Rilskiy_poem)

async def Antonich_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Antonich_poem = ("""
    Запрягти до саней чотири чалі коні
    і в чвал, і в чвал!
    Заіржуть баскі бігуни на реміннім припоні,
    аж луна відіб’ється
    від скал, від скал.
     """
    )
    await update.message.reply_text(Antonich_poem)

async def Susura_poem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Susura_poem = ("""
    Любіть Україну, як сонце любіть,
    як вітер, і трави, і води...
    В годину щасливу і в радості мить,
    любіть у годину негоди.
    Любіть Україну у сні й наяву,
    вишневу свою Україну,
    красу її, вічно живу і нову,
    і мову її солов'їну.
    """
    )
    await update.message.reply_text(Susura_poem)

list_command = """
/help - назви всіх команд
/hello - привітання
/lesya_poem - вірш Лесі Українки
/Taras_poem - вірш Тараса Шевченко
/Franko_poem - вірш Івана Франка
/Tichina_poem - вірш Павла Тичини 
/Simonenko_poem - вірш Василя Симоненко
/Oles_poem - вірш Олександра Олеся
/Kostenko_poem - вірш Ліни Костенко
/Rilskiy_poem - вірш Максима Рильського
/Antonich_poem - вірш Богдана - Ігора Антонича
/Susura_poem - вірш Володимира Сюсюри

"""
app = ApplicationBuilder().token("8082885726:AAF3vdHMCZqMzjLducHbbwMS07I3_bZBfBA").build()

app.add_handler(CommandHandler("help", help ))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("lesya_poem", lesya_poem))
app.add_handler(CommandHandler("Taras_poem", Taras_poem))
app.add_handler(CommandHandler("Franko_poem", Franko_poem))
app.add_handler(CommandHandler("Tichina_poem", Tichina_poem))
app.add_handler(CommandHandler("Simonenko_poem", Simonenko_poem))
app.add_handler(CommandHandler("Oles_poem", Oles_poem))
app.add_handler(CommandHandler("Kostenko_poem", Kostenko_poem))
app.add_handler(CommandHandler("Rilskiy_poem", Rilskiy_poem))
app.add_handler(CommandHandler("Antonich_poem", Antonich_poem))
app.add_handler(CommandHandler("Susura_poem", Susura_poem))

app.run_polling()