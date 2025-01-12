# t.me/AI_DianaBot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

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

list_comand = """
/help - назви всіх команд
/hello - привітання
/lesya_poem - вірш Лесі українки
/Taras_poem - вірш Тараса Шевченко
/Franko_poem - вірш Івана Франка
/Tichina_poem - вірш Павла Тичини 
/Simonenko_poem - вірш Василя Симоненко
/Oles_poem - вірш Олександра Олеся
/Kostenko_poem - вірш Ліни Костенко
/Rilskiy_poem - вірш Максима Рильського
/Antonich_poem - вірш Богдана - Ігора Антонича


"""
app = ApplicationBuilder().token("8082885726:AAF3vdHMCZqMzjLducHbbwMS07I3_bZBfBA").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("lesya_poem", lesya_poem))

app.run_polling()