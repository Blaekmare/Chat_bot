##библеотека для работы с телеграм ботом и inline-buttons
from telegram import Update
from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import InlineQueryHandler
##импорт класса
from searcher import Searcher
##импорт проверки функций на ошибки
from funktion import log_error

##Создание экземпляра класса
search = Searcher()

##Декоратор для создания выпадающего списка
@log_error
def inline_handler(update: Update, context: CallbackContext):
    query = update.inline_query.query
    query = query.strip().lower()
    results = []

    names = search.parse_query(text=query)
    numbers = search.get_prices(name=names)
    for i, (name, number, funam) in enumerate(numbers):
        results.append(
            InlineQueryResultArticle(
                id=i+1,
                title=f'вы имели ввиду {name} ?',
                input_message_content=InputTextMessageContent(
                    message_text=f'{name} \n{funam} \nЦена:{number}',
                ),
            )
        )
    if query == "" or not results:
        results.append(
            InlineQueryResultArticle(
                id=999,
                title='Ничего не нашлось ',
                input_message_content=InputTextMessageContent(
                    message_text=f'Ничего не нашлось по запросу "{query}"',
                ),
            )
        )

    update.inline_query.answer(
        results=results,
        cache_time=10,
    )

@log_error
def inlinebotik():
    updater = Updater(
        token='5655838640:AAGnKAL3fHtHX8WHY6rpNzklkCOBlNf2KAw',
        use_context=True,
    )
    updater.dispatcher.add_handler(InlineQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    inlinebotik()
