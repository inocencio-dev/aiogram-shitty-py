from aiogram import types
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from .plases import print_mgpl_7, print_mgpl_9, print_mgpl_10, print_mgptkt, print_mgkso
from aiogram.dispatcher import FSMContext

from keyboards.inline.buttons import *

from .menues_yvo import dp
'''
@dp.message_handler(text='')
async def check_(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_ob_pit)
'''



@dp.message_handler(text='Микро и наноэлектроника')
async def check_micro(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_micro)

@dp.callback_query_handler(text='Программирование')
async def check_prog(call: CallbackQuery, state: FSMContext):
    await check_prog(call.message, state)
@dp.message_handler(text='Программирование')
async def check_prog(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_prog)

@dp.callback_query_handler(text='Сфера обслуживания')
async def check_obsl(call: CallbackQuery, state: FSMContext):
    await check_obsl(call.message, state)
@dp.message_handler(text='Сфера обслуживания')
async def check_obsl(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_obsl)

@dp.callback_query_handler(text='Электроника. Приборы и аппараты')
async def check_electr(call: CallbackQuery, state: FSMContext):
    await check_electr(call.message, state)
@dp.message_handler(text='Электроника. Приборы и аппараты')
async def check_electr(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_electr)

@dp.callback_query_handler(text='Искусство и дизайн. Полиграфия. Фотография')
async def check_dizign(call: CallbackQuery, state: FSMContext):
    await check_dizign(call.message, state)
@dp.message_handler(text='Искусство и дизайн. Полиграфия. Фотография')
async def check_dizign(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_dizign)


@dp.message_handler(text='Общественное питание и перерабатывающая промышленность')
async def check_ob_pit(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_ob_pit)


@dp.message_handler(text='Транспорт')
async def check_transport(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_transport)


@dp.callback_query_handler(text='Электротехника')
async def check_electriotehnika(call: CallbackQuery, state: FSMContext):
    await check_electriotehnika(call.message, state)
@dp.message_handler(text='Электротехника')
async def check_electriotehnika(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_electriotehnika)


@dp.message_handler(text='Металообработка')
async def check_metaoobrabotka(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_metaoobrabotka)


@dp.message_handler(text='Строительно-монтажные и ремонтные работы')
async def check_stroit_mont(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_stroit_mont)


@dp.message_handler(text='Работы по дереву')
async def check_rab_derevo(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_rab_derevo)


@dp.message_handler(text='Садово-парковое строительство')
async def check_sad(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_sad)


@dp.message_handler(text='Автомобильный транспорт')
async def check_auto(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_auto)


@dp.message_handler(text='Железнодорожный транспорт')
async def check_depo(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_depo)


@dp.message_handler(text='Производство медицинских препаратов')
async def check_med(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_med)


'''
@dp.message_handler(text='')
async def check_(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)
'''

@dp.callback_query_handler(text='Педагогика')
async def check_ped(call: CallbackQuery, state: FSMContext):
    await check_ped(call.message, state)
@dp.message_handler(text='Педагогика')
async def check_ped(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_ped
    elif data.get('klass') == '11 классов':
        markup = markup_ped_11
    else:
        markup = ReplyKeyboardRemove()
        await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)
        pass
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)

@dp.callback_query_handler(text='Бытовое обслуживание населения')
async def check_bit(call: CallbackQuery, state: FSMContext):
    await check_bit(call.message, state)
@dp.message_handler(text='Бытовое обслуживание населения')
async def check_bit(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('prev_menu') == 1:
        markup = markup_bitovoe
        await state.update_data(prev_menu=0)
    else:
        markup = markup_bit
        await state.update_data(prev_menu=1)
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Легкая промышленность. Швейное производство')
async def check_legk_prom(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_legk_prom
    elif data.get('klass') == '11 классов':
        markup = markup_legk_prom_11
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)

@dp.callback_query_handler(text='Металообработка. Сварка. Слесарные работы')
async def check_metall(call: CallbackQuery, state: FSMContext):
    await check_metall(call.message, state)
@dp.message_handler(text='Металообработка. Сварка. Слесарные работы')
async def check_metall(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_metall
    elif data.get('klass') == '11 классов':
        markup = markup_metall_11
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Почтовая связь и ЭВМ')
async def check_post(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_post
    elif data.get('klass') == '11 классов':
        await print_mgkso(message)
        await message.answer_photo(open("data/photo/operSvyzi.jpg", 'rb'))
        await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Строительство и комунальное хозяйство')
async def check_stroit(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_stroi
    elif data.get('klass') == '11 классов':
        markup = markup_stroi_11
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)

@dp.callback_query_handler(text='Торговля и коммерческая деятельность')
async def check_torg(call: CallbackQuery, state: FSMContext):
    await check_torg(call.message, state)
@dp.message_handler(text='Торговля и коммерческая деятельность')
async def check_torg(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_torg
    elif data.get('klass') == '11 классов':
        await print_mgptkt(message)
        await message.answer_photo(open("data/photo/Prodavec.jpg", 'rb'))
        await message.answer('http://ptkt.minsk.edu.by/ru/main.aspx?guid=36311')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Парикмахерское искусство и декоративная косметика')
async def check_parik(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_parik
    elif data.get('klass') == '11 классов':
        markup = markup_parik_11
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Сварочные работы')
async def check_svarochner_raboty(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_svarochner_raboty
    elif data.get('klass') == '11 классов':
        await print_mgpl_10(message)
        await message.answer_photo(open("data/photo/electrogazosvarchik.jpg", 'rb'))
        await message.answer('http://licey10.minsk.edu.by/ru/main.aspx?guid=1611')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Слесарные профессии')
async def check_slesarnie_professii(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_slesarnie_professii
    elif data.get('klass') == '11 классов':
        await print_mgpl_9(message)
        await message.answer_photo(open("data/photo/slesarMehan.jpg", 'rb'))
        await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Отделочные работы')
async def check_otdel(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_otdel
    elif data.get('klass') == '11 классов':
        markup = markup_otdel_11
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)

@dp.callback_query_handler(text='Строительные технические работы')
async def check_stroit_tex(call: CallbackQuery, state: FSMContext):
    await check_stroit_tex(call.message, state)
@dp.message_handler(text='Строительные технические работы')
async def check_stroit_tex(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '9 классов':
        markup = markup_stroit_tex
    elif data.get('klass') == '11 классов':
        await print_mgpl_7(message)
        await message.answer_photo(open("data/photo/montajSanTeh.jpg", 'rb'))
        await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)
