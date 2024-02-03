import logging
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.inline import x_o

API_TOKEN = "5118382129:AAGNQiGeZEKB6tSy846WrWOh7v1ftBCtSZ4"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='game')
async def boshlanishi(message: types.Message):
    await message.answer('O`yin Boshlandi', reply_markup=x_o)


oyinchi = 0
matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]


@dp.callback_query_handler()
async def buttonlar(call: types.CallbackQuery):
    global oyinchi
    if oyinchi % 2 == 0:
        print('x ishladi')
        xonacha_button = int(call.data) - 1
        print('Xonacha button', xonacha_button)
        if matrix[xonacha_button] == 0:
            matrix.pop(xonacha_button)
            matrix.insert(xonacha_button, 1)
        else:
            await call.answer('Bu honacha bo`sh emas')

    else:
        xonacha_button = int(call.data) - 1
        if matrix[xonacha_button] == 0:
            matrix.pop(xonacha_button)
            matrix.insert(xonacha_button, 2)
        else:
            await call.answer('Bu honacha bo`sh emas')
    print(oyinchi)
    oyinchi += 1
    button = InlineKeyboardMarkup()

    result_btn = []

    for n, i in enumerate(matrix, 1):
        if i == 1:
            result_btn.append(InlineKeyboardButton('❌', callback_data=f"{n}"))
        elif i == 2:
            result_btn.append(InlineKeyboardButton('⭕️', callback_data=f"{n}"))
        else:
            result_btn.append(InlineKeyboardButton(' ', callback_data=f"{n}"))

    button.add(*result_btn)
    print(matrix)
    ix_nolik = []
    for i in matrix:
        if i == 1:
            ix_nolik.append('❌')
        elif i == 2:
            ix_nolik.append('⭕️')
        else:
            ix_nolik.append(0)

    if matrix[0] == matrix[1] == matrix[2] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[0]} yutdi")

    elif matrix[3] == matrix[4] == matrix[5] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[3]} yutdi")

    elif matrix[6] == matrix[7] == matrix[8] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[6]} yutdi")

    elif matrix[0] == matrix[3] == matrix[6] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[0]} yutdi")

    elif matrix[1] == matrix[4] == matrix[7] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[1]} yutdi")

    elif matrix[2] == matrix[5] == matrix[8] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[2]} yutdi")

    elif matrix[0] == matrix[4] == matrix[8] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[0]} yutdi")

    elif matrix[2] == matrix[4] == matrix[6] != 0:
        await call.message.delete()
        await call.message.answer(f"{ix_nolik[2]} yutdi")

    if 0 not in matrix:
        await call.message.delete()
        await call.message.answer('O`yin tugadi')
    await call.message.edit_reply_markup(button)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
