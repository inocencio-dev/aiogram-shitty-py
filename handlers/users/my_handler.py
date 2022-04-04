from aiogram import types

from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.inline import markup_1_q
from keyboards.inline.buttons import *
from keyboards.inline.buttons_yvo import *

from .test import dp


@dp.message_handler(Command("spec"))
async def show_menu(message: types.Message, state: FSMContext):
    global markup
    markup = ReplyKeyboardRemove()
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        if data.get('programm') == 'ССО':
            markup = markup_profil_sso
        elif data.get('programm') == 'ПТО':
            markup = markup_profil_pto
        elif data.get('programm') == 'УВО':
            markup = markup_yvo
    elif data.get('klass') == '11 классов':
        if data.get('programm') == 'ССО':
            markup = markup_profil_sso
        elif data.get('programm') == 'ПТО':
            markup = markup_profil_pto_11
        elif data.get('programm') == 'УВО':
            markup = markup_yvo
    else:
        await message.answer(text='Для начала выполните команду /start')
        return

    await state.reset_state(with_data=False)
    await message.answer(text='Какой профиль вас интересует', reply_markup=markup)




@dp.message_handler(text='9 классов')
@dp.message_handler(text='11 классов')
async def button_classes(message: types.Message, state: FSMContext):
    klass = message.text
    markup = ReplyKeyboardRemove()
    if klass == '9 классов':
        await state.update_data(klass=klass)
        markup = markup_programms_9
    elif klass == '11 классов':
        await state.update_data(klass=klass)
        markup = markup_programms_11
    else:
        await message.answer('Нет такого ответа')
        return

    await message.answer(text='Какая программа вас интересует?', reply_markup=markup)

    data = await state.get_data()
    print(data.get('klass'))


@dp.message_handler(text='ССО')
@dp.message_handler(text='ПТО')
@dp.message_handler(text='УВО')
async def button_programms(message: types.Message, state: FSMContext):
    data = await state.get_data()
    programm = message.text
    if programm == 'ССО':
        await state.update_data(programm=programm)
        markup = markup_profil_sso
    elif programm == 'ПТО':
        await state.update_data(programm=programm)
        if data.get('klass') == '9 классов':
            markup = markup_profil_pto
        elif data.get('klass') == '11 классов':
            markup = markup_profil_pto_11
    elif programm == 'УВО':
        await state.update_data(programm=programm)
        await state.update_data(prev_menu_yvo='УВО')
        markup = markup_yvo
    elif programm == 'Назад':
        await button_classes(message, state)
    else:
        await message.answer('Нет такого ответа')

    await message.answer(text='Для просмотра списка стециальностей подходящих под ваши критерии введите команду /spec.\n Также перед этим рекомендум пройти профориентационный тест, отправив команду /test',
                         reply_markup=ReplyKeyboardRemove())

    data = await state.get_data()
    print(data.get('programm'))


@dp.message_handler(text="Вернуться к списку профилей")
async def button_back(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await state.update_data(prev_menu=0)
    if data.get('klass') == '9 классов':
        if data.get('programm') == 'ССО':
            await message.answer(text='Какой профиль вас интересует?', reply_markup=markup_profil_sso)
        elif data.get('programm') == 'ПТО':
            await message.answer(text='Какой профиль вас интересует?', reply_markup=markup_profil_pto)
    elif data.get('klass') == '11 классов':
        if data.get('programm') == 'ССО':
            await message.answer(text='Какой профиль вас интересует?', reply_markup=markup_profil_sso)
        elif data.get('programm') == 'ПТО':
            await message.answer(text='Какой профиль вас интересует?', reply_markup=markup_profil_pto_11)


@dp.message_handler(text='Назад')
async def button_back(message: types.Message, state: FSMContext):
    await message.answer(text='Сколько классов вы закончили?', reply_markup=markup_klasses)


@dp.message_handler(text='Вернуться к выбору программы обучения')
async def button_back_prog(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_programms_9
    elif data.get('klass') == '11 классов':
        markup = markup_programms_11
    await message.answer(text='Какая программа вас интересует?', reply_markup=markup)

'''@dp.message_handler()
async def button_check_menu(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё')
'''