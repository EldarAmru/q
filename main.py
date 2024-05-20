import asyncio
from aiogram import Bot, executor, Dispatcher
from datetime import datetime



bot = Bot(token="6477125057:AAFWfFo8yXMWnr-JYPVyxwSf8Mtz7m9Tbmw")
bot_dispatcher = Dispatcher(bot=bot)
date = datetime.now()
day_of_week = date.weekday()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_name = days[day_of_week]
# day_name = "Tuesday"

@bot_dispatcher.message_handler()
async def n(message):
    timer_seconds = message.text



    if "Ежедневно" in timer_seconds:
        new_message = await bot.send_message(chat_id=message.chat.id, text=f"До нового уведомления {timer_seconds} секунд")
        a = ['1 день', '2 день', '3 день', '4 день', '5 день']
        b = 0
        for i in range(len(a)):
            await bot.send_message(chat_id=message.chat.id, text=f"Сегодня {a[b]}")
            for seconds_left in range(86400 - 1, -1, -1):
                await asyncio.sleep(1)
                await new_message.edit_text(f"До нового уведомления {seconds_left} секунд")
            b += 1

        # schedule.every().minutes.at(':00').do(daily)

        # while True:
        #     schedule.run_pending()

    elif "Рабочие дни" in timer_seconds:
        a = ['1 день', '2 день', '3 день', '4 день', '5 день', '6 день', '7 день', '8 день', '9 день', '10 день', '11 день', '12 день', '13 день', '14 день', '15 день', '16 день', '17 день', '18 день', '19 день', '20 день', '21 день', '21 день', '23 день', '24 день', '25 день', '26 день', '27 день', '28 день', '29 день', '30 день']
        b = 0
        new_message = await bot.send_message(chat_id=message.chat.id, text=f"До нового уведомления {timer_seconds} секунд")
        for i in range(30):
            if "Saturday" in day_name or "Sunday" in day_name:
                await bot.send_message(chat_id=message.chat.id, text='Сегодня выходной')
                for seconds_left in range(86400 - 1, -1, -1):
                    await asyncio.sleep(1)
                    await new_message.edit_text(f"До нового уведомления {seconds_left} секунд")
            else:
                await bot.send_message(chat_id=message.chat.id, text=f"Сегодня {a[b]}")
                for seconds_left in range(86400 - 1, -1, -1):
                    await asyncio.sleep(1)
                    await new_message.edit_text(f"До нового уведомления {seconds_left} секунд")
                b += 1


    elif "Выходные" in timer_seconds:
        a = ['1 день', '2 день', '3 день', '4 день', '5 день', '6 день', '7 день', '8 день', '9 день', '10 день', '11 день', '12 день', '13 день', '14 день', '15 день', '16 день', '17 день', '18 день', '19 день', '20 день', '21 день', '21 день', '23 день', '24 день', '25 день', '26 день', '27 день', '28 день', '29 день', '30 день']
        b = 0
        new_message = await bot.send_message(chat_id=message.chat.id, text=f"До нового уведомления {timer_seconds} секунд")
        for i in range(30):
            if "Monday" in day_name or "Tuesday" in day_name or "Wednesday" in day_name or "Thursday" in day_name or "Friday" in day_name:
                await bot.send_message(chat_id=message.chat.id, text='Сегодня рабочий день')
                for seconds_left in range(86400 - 1, -1, -1):
                    await asyncio.sleep(1)
                    await new_message.edit_text(f"До нового уведомления {seconds_left} секунд")
            else:
                await bot.send_message(chat_id=message.chat.id, text=f"Сегодня {a[b]}")
                for seconds_left in range(86400 - 1, -1, -1):
                    await asyncio.sleep(1)
                    await new_message.edit_text(f"До нового уведомления {seconds_left} секунд")
                b += 1



if __name__ == '__main__':
    executor.start_polling(bot_dispatcher)

