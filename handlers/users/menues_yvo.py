from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.buttons_yvo import *

from .specialities import dp


@dp.message_handler(text='Далее')
async def check_yvo_ped(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('prev_menu_yvo') == 'УВО':
        markup = markup_yvo_2
    elif data.get('prev_menu_yvo') == 'ТЕХНИКА И ТЕХНОЛОГИИ':
        markup = markup_yvo_texn_2
        await state.update_data(prev_menu_yvo='ТЕХНИКА И ТЕХНОЛОГИИ2')
    elif data.get('prev_menu_yvo') == 'ТЕХНИКА И ТЕХНОЛОГИИ2':
        await state.update_data(prev_menu_yvo='ТЕХНИКА И ТЕХНОЛОГИИ3')
        markup = markup_yvo_texn_3
    elif data.get('prev_menu_yvo') == 'ОБОРУДОВАНИЕ':
        markup = markup_yvo_oborud_2
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    elif data.get('prev_menu_yvo') == 'КОММУНИКАЦИИ':
        markup = markup_yvoo_kommunikacii_2
    elif data.get('prev_menu_yvo') == 'ЭКОНОМИКА И УПРАВЛЕНИЕ':
        markup = markup_yvoo_eco_2
    elif data.get('prev_menu_yvo') == 'УПРАВЛЕНИЕ ПОДРАЗДЕЛЕНИЯМИ И ОБЕСПЕЧЕНИЕ ИХ ДЕЯТЕЛЬНОСТИ':
        markup = markup_yvoo_ypravlenie_podrazdeleniami_2
    else:
        print(data.get('prev_menu_yvo'))

    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='Назад')
async def check_yvo_ped(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('prev_menu_yvo') == 'УВО':
        markup = markup_yvo
    elif data.get('prev_menu_yvo') == 'ТЕХНИКА И ТЕХНОЛОГИИ2':
        markup = markup_yvo_texn
        await state.update_data(prev_menu_yvo='ТЕХНИКА И ТЕХНОЛОГИИ')
    elif data.get('prev_menu_yvo') == 'ТЕХНИКА И ТЕХНОЛОГИИ3':
        await state.update_data(prev_menu_yvo='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_texn_2
    elif data.get('prev_menu_yvo') == 'ОБОРУДОВАНИЕ':
        markup = markup_yvo_oborud
    elif data.get('prev_menu_yvo') == 'КОММУНИКАЦИИ':
        markup = markup_yvoo_kommunikacii
    elif data.get('prev_menu_yvo') == 'ЭКОНОМИКА И УПРАВЛЕНИЕ':
        markup = markup_yvoo_eco
    elif data.get('prev_menu_yvo') == 'УПРАВЛЕНИЕ ПОДРАЗДЕЛЕНИЯМИ И ОБЕСПЕЧЕНИЕ ИХ ДЕЯТЕЛЬНОСТИ':
        markup = markup_yvoo_ypravlenie_podrazdeleniami

    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='НАЗАД')
async def check_back(message: types.Message, state: FSMContext):
    data = await state.get_data()
    str = data.get('back')
    print(str)
    markup = ReplyKeyboardRemove()
    if str == 'ПЕДАГОГИКА':
        markup = markup_yvo_ped
    elif str == "ИСКУССТВО И ДИЗАЙН":
        markup = markup_yvo_dizign
    elif str == "ГУМАНИТАРНЫЕ НАУКИ":
        markup = markup_yvo_gum_nauki
    elif str == "КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА":
        markup = markup_yvo_kom
    elif str == "ЕСТЕСТВЕННЫЕ НАУКИ":
        markup = markup_yvo_estestv_nauki
    # elif str =="ЭКОЛОГИЧЕСКИЕ НАУКИ":
    #    markup = markup_yvo_ped
    elif str == "ТЕХНИКА И ТЕХНОЛОГИИ":
        markup = markup_yvo_texn
    elif str == "АРХИТЕКТУРА И СТРОИТЕЛЬСТВО":
        markup = markup_yvo_arh
    elif str == "СЕЛЬСКОЕ И ЛЕСНОЕ ХОЗЯЙСТВО. САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО":
        markup = markup_yvo_s_h
    elif str == "ЗДРАВООХРАНЕНИЕ":
        markup = markup_yvo_zdrav
    # elif str =="СОЦИАЛЬНАЯ ЗАЩИТА":
    #    markup = markup_yvo_zdrav
    elif str == "ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО":
        markup = markup_yvo_fizra
    # elif str =="ОБЩЕСТВЕННОЕ ПИТАНИЕ":
    #    markup = markup_yvo_fizra
    elif str == "СЛУЖБЫ БЕЗОПАСНОСТИ":
        markup = markup_yvo_sl_bezop
    elif str == "ПЕДАГОГИКА ДЕТСТВА":
        await state.update_data(back='ПЕДАГОГИКА')
        markup = markup_yvo_ped_det
    elif str == "ПЕДАГОГИКА ПОДРОСТКОВОГО И ЮНОШЕСКОГО ВОЗРАСТА":
        await state.update_data(back='ПЕДАГОГИКА')
        markup = markup_yvo_ped_podr
    elif str == "ПЕДАГОГИКА ОБЩЕВОЗРАСТНАЯ":
        await state.update_data(back='ПЕДАГОГИКА')
        markup = markup_yvo_ped_obsh
    elif str == "УВО":
        markup = markup_yvo
    elif str == "ИСКУССТВО ИЗОБРАЗИТЕЛЬНОЕ. ИСКУССТВО ДЕКОРАТИВНО-ПРИКЛАДНОЕ":
        await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
        markup = markup_yvo_isk_izobr
    elif str == "ИСКУССТВО И ДИЗАЙН":
        await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
        markup = markup_yvo_dizign
    elif str == "ИСКУССТВО СЦЕНИЧЕСКОЕ И ЭКРАННОЕ":
        await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
        markup = markup_yvo_isk_scen
    elif str == "КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА":
        markup = markup_yvo_kom
    elif str == "ЭКОНОМИКА":
        await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
        markup = markup_yvo_econ
    elif str == "УПРАВЛЕНИЕ":
        await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
        markup = markup_yvo_ypr
    elif str == "ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВ":
        await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
        markup = markup_yvo_econ_i_org_prva
    elif str == "ЕСТЕСТВЕННЫЕ НАУКИ":
        markup = markup_yvo_estestv_nauki
    elif str == "ОБОРУДОВАНИЕ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_oborud
    elif str == "ТРАНСПОРТ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_transport
    elif str == "ПРИБОРЫ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_pribory
    elif str == "РАДИОЭЛЕКТРОННАЯ ТЕХНИКА":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_rad_texn
    elif str == "ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_inf
    elif str == "КОМПОНЕНТЫ ОБОРУДОВАНИЯ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_komp_oboryd
    elif str == "ТЕХНИКА И ТЕХНОЛОГИИ":
        markup = markup_yvo_texn
    elif str == "ТЕХНИКА И ТЕХНОЛОГИИ2":
        markup = markup_yvo_texn_2
    elif str == "ТЕХНИКА И ТЕХНОЛОГИИ3":
        markup = markup_yvo_texn_3
    elif str == "СВЯЗЬ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_svyz
    elif str == "ЛЕСНАЯ ПРОМЫШЛЕННОСТЬ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_lesn_prom
    elif str == "ХИМИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
        markup = markup_yvo_him_prom
    elif str == "ПОЛИГРАФИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_poligraf_prom
    elif str == "ПИЩЕВАЯ ПРОМЫШЛЕННОСТЬ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_pisch_prom
    elif str == "ГОРНОДОБЫВАЮЩАЯ ПРОМЫШЛЕННОСТЬ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_gorn_prom
    elif str == "ПРОЧИЕ ВИДЫ ПРОИЗВОДСТВА":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_proch_vidy_prva
    elif str == "АВТОМАТИЗАЦИЯ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_avtomaizacia
    elif str == "ОБЕСПЕЧЕНИЕ КАЧЕСТВА":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ2')
        markup = markup_yvo_obespech_kach_va
    elif str == "ЭРГОНОМИКА":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ3')
        markup = markup_yvo_ergonomika
    elif str == "ЗЕМЛЕУСТРОЙСТВО, ГЕОДЕЗИЯ, КАРТОГРАФИЯ И ТОПОГРАФИЯ":
        await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ3')
        markup = markup_yvo_zeml_geod
    elif str == "АРХИТЕКТУРА И СТРОИТЕЛЬСТВО":
        markup = markup_yvo_arh
    elif str == "СТРОИТЕЛЬСТВО":
        await state.update_data(back='АРХИТЕКТУРА И СТРОИТЕЛЬСТВО')
        markup = markup_yvo_stroitelstvo
    elif str == "СЕЛЬСКОЕ ХОЗЯЙСТВО":
        markup = markup_yvo_s_h
    elif str == "ЗДРАВООХРАНЕНИЕ":
        markup = markup_yvo_zdrav
    elif str == "ЛЕСНОЕ ХОЗЯЙСТВО И САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО":
        markup = markup_yvoo_lesnoe_hozaystvo
    elif str == "ТЕХНИКО-ЛАБОРАТОРНОЕ ОБЕСПЕЧЕНИЕ":
        markup = markup_yvo_tehn_lab_obespech
    elif str == "УВО2":
        markup = markup_yvo_2
    elif str == "ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ":
        await state.update_data(back='ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО')
        markup = markup_yvo_fiz_kult_i_sport
    elif str == "ТУРИЗМ. ГОСТЕПРИИМСТВО":
        await state.update_data(back='ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО')
        markup = markup_yvo_turizm
    elif str == "ВОЕННОЕ ДЕЛО":
        await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
        markup = markup_yvo_voennoe_delo
    elif str == "ЗАЩИТА ОТ ЧРЕЗВЫЧАЙНЫХ СИТУАЦИЙ":
        await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
        markup = markup_yvo_zasch_ot_chp
    elif str == "ЭКОНОМИЧЕСКАЯ БЕЗОПАСНОСТЬ":
        await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
        markup = markup_yvo_econom_bezop
    elif str == "ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ":
        await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
        markup = markup_yvo_inf_bezop
    elif str == "ЭКОЛОГИЧЕСКАЯ БЕЗОПАСНОСТЬ":
        await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
        markup = markup_yvo_ecolog_bezop

    else:
        print(str)
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup)


@dp.message_handler(text='К списку категорий')
async def check_yvo_ped(message: types.Message, state: FSMContext):
    await state.update_data(prev_menu_yvo='УВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo)

@dp.callback_query_handler(text='ПЕДАГОГИКА')
async def check_yvo_ped(call: CallbackQuery, state: FSMContext):
    await check_yvo_ped(call.message, state)
@dp.message_handler(text='ПЕДАГОГИКА')
async def check_yvo_ped(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_ped)

@dp.callback_query_handler(text='ИСКУССТВО И ДИЗАЙН')
async def check_yvo_dizign(call: CallbackQuery, state: FSMContext):
    await check_yvo_dizign(call.message, state)
@dp.message_handler(text='ИСКУССТВО И ДИЗАЙН')
async def check_yvo_dizign(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_dizign)

@dp.callback_query_handler(text='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
async def check_yvo_kom(call: CallbackQuery, state: FSMContext):
    await check_yvo_kom(call.message, state)
@dp.message_handler(text='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
async def check_yvo_kom(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_kom)

@dp.callback_query_handler(text='ТЕХНИКА И ТЕХНОЛОГИИ')
async def check_yvo_texn(call: CallbackQuery, state: FSMContext):
    await check_yvo_texn(call.message, state)
@dp.message_handler(text='ТЕХНИКА И ТЕХНОЛОГИИ')
async def check_yvo_texn(message: types.Message, state: FSMContext):
    await state.update_data(prev_menu_yvo='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_texn)


@dp.message_handler(text='АРХИТЕКТУРА И СТРОИТЕЛЬСТВО')
async def check_yvo_arh(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_arh)


@dp.message_handler(text='СЕЛЬСКОЕ И ЛЕСНОЕ ХОЗЯЙСТВО. САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
async def check_yvo_s_h(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_s_h)


@dp.message_handler(text='ЗДРАВООХРАНЕНИЕ')
async def check_yvo_zdrav(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_zdrav)

@dp.callback_query_handler(text='ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО')
async def check_yvo_fizra(call: CallbackQuery, state: FSMContext):
    await check_yvo_fizra(call.message, state)
@dp.message_handler(text='ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО')
async def check_yvo_fizra(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_fizra)

@dp.callback_query_handler(text='СЛУЖБЫ БЕЗОПАСНОСТИ')
async def check_yvo_sl_bezop(call: CallbackQuery, state: FSMContext):
    await check_yvo_sl_bezop(call.message, state)
@dp.message_handler(text='СЛУЖБЫ БЕЗОПАСНОСТИ')
async def check_yvo_sl_bezop(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_sl_bezop)


@dp.message_handler(text='ПЕДАГОГИКА ДЕТСТВА')
async def check_yvo_ped_det(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_ped_det)


@dp.message_handler(text='ПЕДАГОГИКА ПОДРОСТКОВОГО И ЮНОШЕСКОГО ВОЗРАСТА')
async def check_yvo_ped_podr(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_ped_podr)


@dp.message_handler(text='ПЕДАГОГИКА ОБЩЕВОЗРАСТНАЯ')
async def check_yvo_ped_obsh(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_ped_obsh)


@dp.message_handler(text='ИСКУССТВО ИЗОБРАЗИТЕЛЬНОЕ. ИСКУССТВО ДЕКОРАТИВНО-ПРИКЛАДНОЕ')
async def check_yvo_isk_izobr(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_isk_izobr)


@dp.message_handler(text='ИСКУССТВО СЦЕНИЧЕСКОЕ И ЭКРАННОЕ')
async def check_yvo_isk_scen(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_isk_scen)

@dp.callback_query_handler(text='ГУМАНИТАРНЫЕ НАУКИ')
async def check_yvo_gum_nauki(call: CallbackQuery, state: FSMContext):
    await check_yvo_gum_nauki(call.message, state)
@dp.message_handler(text='ГУМАНИТАРНЫЕ НАУКИ')
async def check_yvo_gum_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='УВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_gum_nauki)


@dp.message_handler(text='ЭКОНОМИКА')
async def check_yvo_econ(message: types.Message, state: FSMContext):
    await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_econ)


@dp.message_handler(text='УПРАВЛЕНИЕ')
async def check_yvo_ypr(message: types.Message, state: FSMContext):
    await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_ypr)


@dp.message_handler(text='ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
async def check_yvo_econ_i_org_prva(message: types.Message, state: FSMContext):
    await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_econ_i_org_prva)


@dp.message_handler(text='ЕСТЕСТВЕННЫЕ НАУКИ')
async def check_yvo_estestv_nauki(message: types.Message, state: FSMContext):
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_estestv_nauki)


@dp.message_handler(text='ОБОРУДОВАНИЕ')
async def check_yvo_oborud(message: types.Message, state: FSMContext):
    await state.update_data(prev_menu_yvo='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_oborud)


@dp.message_handler(text='ТРАНСПОРТ')
async def check_yvo_transport(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_transport)


@dp.message_handler(text='ПРИБОРЫ')
async def check_yvo_pribory(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_pribory)


@dp.message_handler(text='РАДИОЭЛЕКТРОННАЯ ТЕХНИКА')
async def check_yvo_rad_texn(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_rad_texn)


@dp.message_handler(text='ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА')
async def check_yvo_inf(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_inf)


@dp.message_handler(text='КОМПОНЕНТЫ ОБОРУДОВАНИЯ')
async def check_yvo_komp_oboryd(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_komp_oboryd)


@dp.message_handler(text='СВЯЗЬ')
async def check_yvo_svyz(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_svyz)


@dp.message_handler(text='ЛЕСНАЯ ПРОМЫШЛЕННОСТЬ')
async def check_yvo_lesn_prom(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_lesn_prom)


@dp.message_handler(text='ПОЛИГРАФИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ')
async def check_yvo_poligraf_prom(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_poligraf_prom)


@dp.message_handler(text='ХИМИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ')
async def check_yvo_him_prom(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_him_prom)


@dp.message_handler(text='ПИЩЕВАЯ ПРОМЫШЛЕННОСТЬ')
async def check_yvo_pisch_prom(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_pisch_prom)


@dp.message_handler(text='ГОРНОДОБЫВАЮЩАЯ ПРОМЫШЛЕННОСТЬ')
async def check_yvo_gorn_prom(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_gorn_prom)


@dp.message_handler(text='ПРОЧИЕ ВИДЫ ПРОИЗВОДСТВА')
async def check_yvo_proch_vidy_prva(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_proch_vidy_prva)


@dp.message_handler(text='АВТОМАТИЗАЦИЯ')
async def check_yvo_avtomaizacia(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_avtomaizacia)


@dp.message_handler(text='ОБЕСПЕЧЕНИЕ КАЧЕСТВА')
async def check_yvo_obespech_kach_va(message: types.Message, state: FSMContext):
    await state.update_data(v='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_obespech_kach_va)

@dp.message_handler(text='ЗЕМЛЕУСТРОЙСТВО, ГЕОДЕЗИЯ, КАРТОГРАФИЯ И ТОПОГРАФИЯ')
async def check_yvo_zeml_geod(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_zeml_geod)


@dp.message_handler(text='ОХРАНА ОКРУЖАЮЩЕЙ СРЕДЫ')
async def check_yvo_ohr_okr_sredy(message: types.Message, state: FSMContext):
    await state.update_data(v='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_ohr_okr_sredy)


@dp.message_handler(text='ЭРГОНОМИКА')
async def check_yvo_ergonomika(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_ergonomika)


@dp.message_handler(text='СТРОИТЕЛЬСТВО')
async def check_yvo_stroitelstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='АРХИТЕКТУРА И СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_stroitelstvo)


@dp.message_handler(text='СЕЛЬСКОЕ ХОЗЯЙСТВО')
async def check_yvo_sels_hoz(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ И ЛЕСНОЕ ХОЗЯЙСТВО. САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_sels_hoz)


@dp.message_handler(text='ЛЕСНОЕ ХОЗЯЙСТВО И САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
async def check_yvo_les_hoz(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ И ЛЕСНОЕ ХОЗЯЙСТВО. САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_les_hoz)


@dp.message_handler(text='ТЕХНИКО-ЛАБОРАТОРНОЕ ОБЕСПЕЧЕНИЕ')
async def check_yvo_tehn_lab_obespech(message: types.Message, state: FSMContext):
    await state.update_data(back='ЗДРАВООХРАНЕНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_tehn_lab_obespech)


@dp.message_handler(text='ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ')
async def check_yvo_fiz_kult_i_sport(message: types.Message, state: FSMContext):
    await state.update_data(back='ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_fiz_kult_i_sport)


@dp.message_handler(text='ТУРИЗМ. ГОСТЕПРИИМСТВО')
async def check_yvo_turizm(message: types.Message, state: FSMContext):
    await state.update_data(back='ФИЗИЧЕСКАЯ КУЛЬТУРА. ТУРИЗМ И ГОСТЕПРИИМСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё', reply_markup=markup_yvo_turizm)


@dp.message_handler(text='ЗАЩИТА ОТ ЧРЕЗВЫЧАЙНЫХ СИТУАЦИЙ')
async def check_yvo_zasch_ot_chp(message: types.Message, state: FSMContext):
    await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_zasch_ot_chp)


@dp.message_handler(text='ВОЕННОЕ ДЕЛО')
async def check_yvo_voennoe_delo(message: types.Message, state: FSMContext):
    await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_voennoe_delo)


@dp.message_handler(text='ЭКОНОМИЧЕСКАЯ БЕЗОПАСНОСТЬ')
async def check_yvo_econom_bezop(message: types.Message, state: FSMContext):
    await state.update_data(v='СЛУЖБЫ БЕЗОПАСНОСТИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_econom_bezop)


@dp.message_handler(text='ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ')
async def check_yvo_inf_bezop(message: types.Message, state: FSMContext):
    await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_inf_bezop)


@dp.message_handler(text='ЭКОЛОГИЧЕСКАЯ БЕЗОПАСНОСТЬ')
async def check_yvo_ecolog_bezop(message: types.Message, state: FSMContext):
    await state.update_data(back='СЛУЖБЫ БЕЗОПАСНОСТИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=markup_yvo_ecolog_bezop)


@dp.message_handler(text='РАЗВИТИЕ ЛИЧНОСТИ ДОШКОЛЬНИКА')
async def check_yvo_razv_lich_doshk(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ДЕТСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет дошкольного образования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РАЗВИТИЕ ЛИЧНОСТИ МЛАДШЕГО ШКОЛЬНИКА')
async def check_yvo_razv_lish_ml(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ДЕТСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет дошкольного образования")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РАЗВИТИЕ ЛИЧНОСТИ ДОШКОЛЬНИКА И МЛАДШЕГО ШКОЛЬНИКА')
async def check_yvo_razv_lish_doshk_i_ml(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ДЕТСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет дошкольного образования")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРЕПОДАВАНИЕ ИСТОРИЧЕСКИХ ДИСЦИПЛИН')
async def check_yvo_prepod_ist_disc(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ПОДРОСТКОВОГО И ЮНОШЕСКОГО ВОЗРАСТА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Исторический факультет")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРЕПОДАВАНИЕ ФИЛОЛОГИЧЕСКИХ ДИСЦИПЛИН')
async def check_yvo_prepod_fifolog_disc(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ПОДРОСТКОВОГО И ЮНОШЕСКОГО ВОЗРАСТА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет начального образования")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Факультет английского языка")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Факультет немецкого языка")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРЕПОДАВАНИЕ БИОЛОГИЧЕСКИХ, ГЕОГРАФИЧЕСКИХ И ХИМИЧЕСКИХ ДИСЦИПЛИН')
async def check_yvo_prepod_biolog_disc(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ПОДРОСТКОВОГО И ЮНОШЕСКОГО ВОЗРАСТА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет естествознания")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРЕПОДАВАНИЕ ФИЗИКО-МАТЕМАТИЧЕСКИХ ДИСЦИПЛИН')
async def check_yvo_prepod_fiz_mat_disc(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ПОДРОСТКОВОГО И ЮНОШЕСКОГО ВОЗРАСТА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Физико-математический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭСТЕТИЧЕСКОЕ РАЗВИТИЕ')
async def check_yvo_estet_razv(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ОБЩЕВОЗРАСТНАЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет эстетического образования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ОБРАЗОВАНИЕ В ОБЛАСТИ ФИЗИЧЕСКОЙ КУЛЬТУРЫ')
async def check_yvo_obr_v_obl_fizry(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ОБЩЕВОЗРАСТНАЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет физического воспитания")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СПЕЦИАЛЬНОЕ ОБРАЗОВАНИЕ')
async def check_yvo_spec_obr(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ОБЩЕВОЗРАСТНАЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Институт инклюзивного образования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СОЦИАЛЬНО-ПЕДАГОГИЧЕСКАЯ И ПСИХОЛОГО-ПЕДАГОГИЧЕСКАЯ ПОДДЕРЖКА')
async def check_yvo_soc_ped(message: types.Message, state: FSMContext):
    await state.update_data(back='ПЕДАГОГИКА ОБЩЕВОЗРАСТНАЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет социально-педагогических технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Институт психологии")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОФЕССИОНАЛЬНОЕ ОБРАЗОВАНИЕ')
async def check_yvo_prof_obr(message: types.Message, state: FSMContext):
    await state.update_data(back='УВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет радиотехники и электроники")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Инженерно-педагогический факультет")],
                                                              [KeyboardButton(
                                                                  "Минский государственный высший радиотехнический колледж - Профессионального образования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСКУССТВО ИЗОБРАЗИТЕЛЬНОЕ')
async def check_yvo_isc_izobr(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО ИЗОБРАЗИТЕЛЬНОЕ. ИСКУССТВО ДЕКОРАТИВНО-ПРИКЛАДНОЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Художественный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСКУССТВО ДЕКОРАТИВНО-ПРИКЛАДНОЕ')
async def check_yvo_isc_dec_prikl(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО ИЗОБРАЗИТЕЛЬНОЕ. ИСКУССТВО ДЕКОРАТИВНО-ПРИКЛАДНОЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Факультет дизайна и декоративно-прикладного искусства")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет художественной культуры")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСКУССТВО МУЗЫКАЛЬНОЕ')
async def check_yvo_isc_music(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Фортепианный и композиторско-музыковедческий факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Оркестровый факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Факультет народных инструментов")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Вокально-хоровой факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет музыкального и хореографического искусства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСКУССТВО ТЕАТРА, КИНО, РАДИО И ТЕЛЕВИДЕНИЯ')
async def check_yvo_isc_teatra(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО СЦЕНИЧЕСКОЕ И ЭКРАННОЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Театральный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Факультет экранных искусств")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Вокально-хоровой факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет художественной культуры")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСКУССТВО ХОРЕОГРАФИЧЕСКОЕ')
async def check_yvo_isc_horeo(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО СЦЕНИЧЕСКОЕ И ЭКРАННОЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Вокально-хоровой факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет музыкального и хореографического искусства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСКУССТВО ЭСТРАДНОЕ И ЦИРКОВОЕ')
async def check_yvo_isc_estard(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО СЦЕНИЧЕСКОЕ И ЭКРАННОЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Институт современных знаний имени А.М.Широкова - Факультет искусств")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет музыкального и хореографического искусства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='НАРОДНОЕ ТВОРЧЕСТВО')
async def check_yvo_nar_tvorchestvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Институт повышения квалификации и переподготовки кадров учреждения образования «Белорусский государственный университет культуры и искусств»")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет музыкального и хореографического искусства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ДИЗАЙН')
async def check_yvo_disign(message: types.Message, state: FSMContext):
    await state.update_data(back='ИСКУССТВО И ДИЗАЙН')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Институт современных знаний имени А.М.Широкова - Факультет искусств")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет социокультурных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Факультет дизайна и декоративно-прикладного искусства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РЕЛИГИОВЕДЧЕСКИЕ НАУКИ')
async def check_yvo_relig_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ГУМАНИТАРНЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Институт теологии имени святых Мефодия и Кирилла БГУ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ФИЛОСОФСКИЕ НАУКИ')
async def check_yvo_filosof_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ГУМАНИТАРНЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет философии и социальных наук")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИСТОРИЧЕСКИЕ НАУКИ')
async def check_yvo_ist_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ГУМАНИТАРНЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Исторический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='КУЛЬТУРОВЕДЧЕСКИЕ НАУКИ')
async def check_yvo_culture_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ГУМАНИТАРНЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия музыки - Фортепианный и композиторско-музыковедческий факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Театральный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Художественный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия искусств - Факультет экранных искусств")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет социокультурных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет культурологии и социально-культурной деятельности")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет художественной культуры")],
                                                              [KeyboardButton(
                                                                  "Институт современных знаний имени А.М.Широкова - Гуманитарный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ФИЛОЛОГИЧЕСКИЕ НАУКИ')
async def check_yvo_fiolog_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ГУМАНИТАРНЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Филологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЛИНГВИСТИЧЕСКИЕ НАУКИ')
async def check_yvo_lingvist_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ГУМАНИТАРНЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет социокультурных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Факультет английского языка")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Факультет китайского языка и культуры")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Факультет немецкого языка")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Факультет романских языков")],
                                                              [KeyboardButton(
                                                                  "Минский государственный лингвистический университет - Переводческий факультет")],
                                                              [KeyboardButton(
                                                                  "Минский инновационный университет - Факультет коммуникаций, экономики и права")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))

@dp.callback_query_handler(text='КОММУНИКАЦИИ')
async def check_yvo_kommunikacii(call: CallbackQuery, state: FSMContext):
    await check_yvo_kommunikacii(call.message, state)
@dp.message_handler(text='КОММУНИКАЦИИ')
async def check_yvo_kommunikacii(message: types.Message, state: FSMContext):
    await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Институт психологии")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Исторический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет философии и социальных наук")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет международных отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Юридический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет журналистики")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет культурологии и социально-культурной деятельности")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет культуры и искусств - Факультет информационно-документных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет международных бизнес-коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Институт социально-гуманитарного образования ")],
                                                              [KeyboardButton(
                                                                  "Международный университет МИТСО - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Минский инновационный университет - Факультет коммуникаций, экономики и права")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРАВО')
async def check_yvo_pravo(message: types.Message, state: FSMContext):
    await state.update_data(back='КОММУНИКАЦИИ. ПРАВО. ЭКОНОМИКА. УПРАВЛЕНИЕ. ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Академия Министерства внутренних дел Республики Беларусь - Факультет милиции")],
                                                              [KeyboardButton(
                                                                  "Академия Министерства внутренних дел Республики Беларусь - Следственно-экспертный факультет")],
                                                              [KeyboardButton(
                                                                  "Академия Министерства внутренних дел Республики Беларусь - Уголовно-исполнительный факультет")],
                                                              [KeyboardButton(
                                                                  "Академия Министерства внутренних дел Республики Беларусь - Факультет повышения квалификации и переподготовки руководящих кадров")],
                                                              [KeyboardButton(
                                                                  "Академия Министерства внутренних дел Республики Беларусь - Факультет права")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет международных отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Юридический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет права")],
                                                              [KeyboardButton(
                                                                  "Белорусский торгово-экономический университет потребительской кооперации - Факультет экономики и управления")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКОНОМИКА И УПРАВЛЕНИЕ')
async def check_yvo_eco(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОНОМИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет международных отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет экономики и бизнес-технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет экономики и менеджмента")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет финансов и банковского дела")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Учетно-экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет коммерции и туристической индустрии")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет международных экономических отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет цифровой экономики")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ГОСУДАРСТВЕННОЕ УПРАВЛЕНИЕ')
async def check_yvo_gos_ypr(message: types.Message, state: FSMContext):
    await state.update_data(back='УПРАВЛЕНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Академия Министерства внутренних дел Республики Беларусь - Факультет повышения квалификации и переподготовки руководящих кадров")],
                                                              [KeyboardButton(
                                                                  "Академия управления при Президенте Республики Беларусь - Институт управленческих кадров")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет экономики и менеджмента")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='БИЗНЕС – УПРАВЛЕНИЕ')
async def check_yvo_business_ypr(message: types.Message, state: FSMContext):
    await state.update_data(back='УПРАВЛЕНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия связи - Факультет инжиниринга и технологий связи")],
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет бизнеса и права")],
                                                              [KeyboardButton(
                                                                  "БГАТУ - Факультет предпринимательства и управления")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Инженерно-экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Исторический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет международных отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет экономики и менеджмента")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет международных экономических отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет маркетинга и логистики")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет маркетинга, менеджмента, предпринимательства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='УПРАВЛЕНИЕ ИНФОРМАЦИОННЫМИ РЕСУРСАМИ')
async def check_yvo_ypr_inf_res(message: types.Message, state: FSMContext):
    await state.update_data(back='УПРАВЛЕНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Академия управления при Президенте Республики Беларусь - Институт управленческих кадров")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - ГУО «Институт бизнеса БГУ»")],
                                                              [KeyboardButton(
                                                                  "Международный университет МИТСО - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
async def check_yvo_economika_i_org_prva(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Автотракторный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Машиностроительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Энергетический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет энергетического строительства")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Строительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКОНОМИКА И ЛОГИСТИКА ПРОИЗВОДСТВА')
async def check_yvo_economika_i_logist_prva(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет управления процессами перевозок")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Автотракторный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - ЭКОНОМИЧЕСКИЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКОНОМИКА И ИННОВАЦИОННОЕ РАЗВИТИЕ ПРОИЗВОДСТВА')
async def check_yvo_economika_i_inovac_razv(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет маркетинга, менеджмента, предпринимательства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКОНОМИКА И УПРАВЛЕНИЕ ЭЛЕКТРОННЫМИ БИЗНЕС-СИСТЕМАМИ')
async def check_yvo_economika_i_ypr_el_bisunes_sist(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОНОМИКА И ОРГАНИЗАЦИЯ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Инженерно-экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский торгово-экономический университет потребительской кооперации - Факультет экономики и управления")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - ЭКОНОМИЧЕСКИЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='БИОЛОГИЧЕСКИЕ НАУКИ')
async def check_yvo_biolog_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ЕСТЕСТВЕННЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Биологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ГЕОГРАФИЧЕСКИЕ НАУКИ')
async def check_yvo_geogr_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ЕСТЕСТВЕННЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет географии и геоинформатики")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='МАТЕМАТИЧЕСКИЕ НАУКИ И ИНФОРМАТИКА')
async def check_yvo_math_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ЕСТЕСТВЕННЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия связи - Факультет инжиниринга и технологий связи")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Механико-математический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет прикладной математики и информатики")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет радиофизики и компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет социокультурных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный экономический университет - Факультет цифровой экономики")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ФИЗИЧЕСКИЕ НАУКИ')
async def check_yvo_fiz_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ЕСТЕСТВЕННЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Физический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет радиофизики и компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ХИМИЧЕСКИЕ НАУКИ')
async def check_yvo_him_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='ЕСТЕСТВЕННЫЕ НАУКИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Химический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКОЛОГИЧЕСКИЕ НАУКИ')
async def check_yvo_ecolog_nauki(message: types.Message, state: FSMContext):
    await state.update_data(back='УВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Биологический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет географии и геоинформатики")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='МАШИНОСТРОИТЕЛЬНОЕ ОБОРУДОВАНИЕ И ТЕХНОЛОГИИ')
async def check_yvo_mashinostr(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет химической технологии и техники")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Автотракторный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Машиностроительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Механико-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - МАШИНОСТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - ИНЖЕНЕРНЫЙ ФАКУЛЬТЕТ ЗАОЧНОГО ОБРАЗОВАНИЯ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='МЕТАЛЛУРГИЯ')
async def check_yvo_metarurg(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Механико-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РАДИОЭЛЕКТРОНИКА')
async def check_yvo_radioelectronika(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет информационных технологий и управления")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЛЕСНОЙ КОМПЛЕКС')
async def check_yvo_lesnoy_komplex(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет лесной инженерии, материаловедения и дизайна")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПОЛИГРАФИЯ')
async def check_yvo_poligrafia(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет принттехнологий и медиакоммуникаций")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ХИМИЧЕСКОЕ ПРОИЗВОДСТВО')
async def check_yvo_him_prvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет химической технологии и техники")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - МАШИНОСТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО ПРОДУКТОВ ПИТАНИЯ')
async def check_yvo_proizv_prod_pit(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ГЕОЛОГОРАЗВЕДКА И ГОРНОДОБЫВАЮЩЕЕ ПРОИЗВОДСТВО')
async def check_yvo_geologorazvedka(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет горного дела и инженерной экологии")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СТРОИТЕЛЬСТВО И КОММУНАЛЬНОЕ ХОЗЯЙСТВО')
async def check_yvo_stroitelstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет транспортных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - АВТОМЕХАНИЧЕСКИЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СЕЛЬСКОХОЗЯЙСТВЕННОЕ ПРОИЗВОДСТВО')
async def check_yvo_s_h_proizvodstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГАТУ - Агромеханический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ОБЩЕОТРАСЛЕВОЕ ОБОРУДОВАНИЕ')
async def check_yvo_obscheotraslevoe_oborud(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБОРУДОВАНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет маркетинга, менеджмента, предпринимательства")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Инженерно-педагогический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='АВТОМОБИЛИ, ТРАКТОРЫ, ЭЛЕКТРИЧЕСКИЕ И АВТОНОМНЫЕ ТРАНСПОРТНЫЕ СРЕДСТВА')
async def check_yvo_auto(message: types.Message, state: FSMContext):
    await state.update_data(back='ТРАНСПОРТ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Военно-транспортный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Автотракторный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Военно-Технический Факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - АВТОМЕХАНИЧЕСКИЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЖЕЛЕЗНОДОРОЖНЫЙ ТРАНСПОРТ')
async def check_yvo_jeleznodorosniy_transport(message: types.Message, state: FSMContext):
    await state.update_data(back='ТРАНСПОРТ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Строительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Электротехнический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ВОДНЫЙ ТРАНСПОРТ')
async def check_yvo_vodniy_transport(message: types.Message, state: FSMContext):
    await state.update_data(back='ТРАНСПОРТ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет энергетического строительства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ВОЗДУШНЫЙ ТРАНСПОРТ')
async def check_yvo_vozdyshniy_transport(message: types.Message, state: FSMContext):
    await state.update_data(back='ТРАНСПОРТ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия авиации - Факультет гражданской авиации")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия авиации - Факультет военный")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Электротехнический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ОБЩЕЕ НАЗНАЧЕНИЕ')
async def check_yvo_obschee_naznachenie(message: types.Message, state: FSMContext):
    await state.update_data(back='ПРИБОРЫ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Приборостроительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СПЕЦИАЛЬНОЕ НАЗНАЧЕНИЕ')
async def check_yvo_spec_nazn(message: types.Message, state: FSMContext):
    await state.update_data(back='ПРИБОРЫ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Приборостроительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СХЕМЫ РАДИОЭЛЕКТРОННЫХ УСТРОЙСТВ И СИСТЕМ')
async def check_yvo_shemy_rad(message: types.Message, state: FSMContext):
    await state.update_data(back='РАДИОЭЛЕКТРОННАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет радиотехники и электроники")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='КОНСТРУКЦИИ РАДИОЭЛЕКТРОННЫХ СРЕДСТВ')
async def check_yvo_konstruct_rad_sredstv(message: types.Message, state: FSMContext):
    await state.update_data(back='РАДИОЭЛЕКТРОННАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОЕКТЫ РАДИОЭЛЕКТРОННЫХ СИСТЕМ И ИХ ПРИМЕНЕНИЕ НА ОБЪЕКТАХ"')
async def check_yvo_proekty_rad_sist(message: types.Message, state: FSMContext):
    await state.update_data(back='РАДИОЭЛЕКТРОННАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет радиотехники и электроники")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОГРАММНЫЕ И МАТЕМАТИЧЕСКИЕ СРЕДСТВА')
async def check_yvo_prog_i_mat(message: types.Message, state: FSMContext):
    await state.update_data(back='ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет информационных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных систем и сетей")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет информационных технологий и робототехники")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Международный Институт Дистанционного Образования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='АППАРАТНЫЕ СРЕДСТВА')
async def check_yvo_apparatn_sredstva(message: types.Message, state: FSMContext):
    await state.update_data(back='ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных систем и сетей")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Военный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИНТЕЛЛЕКТУАЛЬНЫЕ КОМПЬЮТЕРНЫЕ СИСТЕМЫ')
async def check_yvo_intelectual_komp_sistemy(message: types.Message, state: FSMContext):
    await state.update_data(back='ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет информационных технологий и управления")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИНФОРМАТИКА И ТЕХНОЛОГИИ ПРОГРАММИРОВАНИЯ')
async def check_yvo_inform_i_tehn_prog(message: types.Message, state: FSMContext):
    await state.update_data(back='ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных систем и сетей")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИНФОРМАЦИОННЫЕ СИСТЕМЫ И ТЕХНОЛОГИИ')
async def check_yvo_inform_sist_i_tehn(message: types.Message, state: FSMContext):
    await state.update_data(back='ИНФОРМАТИКА И ВЫЧИСЛИТЕЛЬНАЯ ТЕХНИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет информационных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет информационных технологий и управления")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Инженерно-экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет экономики и бизнес-технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет информационных технологий и робототехники")],
                                                              [KeyboardButton(
                                                                  "Белорусский торгово-экономический университет потребительской кооперации - Факультет коммерции и финансов ")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - МАШИНОСТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - ИНЖЕНЕРНЫЙ ФАКУЛЬТЕТ ЗАОЧНОГО ОБРАЗОВАНИЯ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РАДИО-, МИКРО- И НАНОЭЛЕКТРОННАЯ ТЕХНИКА')
async def check_yvo_radio_electr_tehnika(message: types.Message, state: FSMContext):
    await state.update_data(back='КОМПОНЕНТЫ ОБОРУДОВАНИЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет радиотехники и электроники")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Приборостроительный факультет")],

                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭЛЕКТРОЭНЕРГЕТИКА, ТЕПЛОЭНЕРГЕТИКА')
async def check_yvo_electroenergetika(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет лесной инженерии, материаловедения и дизайна")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Энергетический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ТРАНСПОРТНАЯ ДЕЯТЕЛЬНОСТЬ')
async def check_yvo_transport_deyat(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия авиации - Факультет гражданской авиации")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет управления процессами перевозок")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Автотракторный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИНФОКОММУНИКАЦИОННЫЕ ТЕХНОЛОГИИ И СИСТЕМЫ СВЯЗИ')
async def check_yvo_infokommun_tehnologii(message: types.Message, state: FSMContext):
    await state.update_data(back='СВЯЗЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия связи - Факультет инжиниринга и технологий связи")],
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия связи - Факультет электросвязи")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет инфокоммуникаций")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПОЧТОВАЯ СВЯЗЬ')
async def check_yvo_pochtovaya_svaz(message: types.Message, state: FSMContext):
    await state.update_data(back='СВЯЗЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия связи - Факультет инжиниринга и технологий связи")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЗАГОТОВКА И ПЕРЕРАБОТКА ДРЕВЕСИНЫ')
async def check_yvo_zagotovka_i_pererabotka_drevesiny(message: types.Message, state: FSMContext):
    await state.update_data(back='ЛЕСНАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет лесной инженерии, материаловедения и дизайна")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИЗДАТЕЛЬСКОЕ ДЕЛО')
async def check_yvo_izdatelskoe_delo(message: types.Message, state: FSMContext):
    await state.update_data(back='ПОЛИГРАФИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет принттехнологий и медиакоммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет информационных технологий")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО ПОЛИГРАФИЧЕСКОЕ')
async def check_yvo_proizvodstvo_poligraph(message: types.Message, state: FSMContext):
    await state.update_data(back='ПОЛИГРАФИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет принттехнологий и медиакоммуникаций")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО ХИМИЧЕСКОЕ')
async def check_yvo_proizvodstvo_him(message: types.Message, state: FSMContext):
    await state.update_data(back='ХИМИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет технологии органических веществ")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет химической технологии и техники")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Химико-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО БИОХИМИЧЕСКОЕ И МИКРОБИОЛОГИЧЕСКОЕ')
async def check_yvo_proizvodstvo_bio_him(message: types.Message, state: FSMContext):
    await state.update_data(back='ХИМИЧЕСКАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет технологии органических веществ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО ПРОДУКТОВ ПИТАНИЯ')
async def check_yvo_proizvodstvo_prod_pit(message: types.Message, state: FSMContext):
    await state.update_data(back='ПИЩЕВАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Технологический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Химико-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РАЗВЕДКА МЕСТОРОЖДЕНИЙ ПОЛЕЗНЫХ ИСКОПАЕМЫХ')
async def check_yvo_razvedka_mest_pol_isk(message: types.Message, state: FSMContext):
    await state.update_data(back='ГОРНОДОБЫВАЮЩАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет географии и геоинформатики")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='РАЗРАБОТКА МЕСТОРОЖДЕНИЙ ПОЛЕЗНЫХ ИСКОПАЕМЫХ')
async def check_yvo_razrabotka_mest_pol(message: types.Message, state: FSMContext):
    await state.update_data(back='ГОРНОДОБЫВАЮЩАЯ ПРОМЫШЛЕННОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет горного дела и инженерной экологии")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО ЮВЕЛИРНЫХ ИЗДЕЛИЙ')
async def check_yvo_proizvodstvo_uvelirn_izd(message: types.Message, state: FSMContext):
    await state.update_data(back='ПРОЧИЕ ВИДЫ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Приборостроительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭКСПОЗИЦИОННО-РЕКЛАМНОЕ ПРОИЗВОДСТВО')
async def check_yvo_exposic_reclamn_proisvodstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ПРОЧИЕ ВИДЫ ПРОИЗВОДСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет маркетинга, менеджмента, предпринимательства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='АВТОМАТИЗАЦИЯ ТЕХНОЛОГИЧЕСКИХ ПРОЦЕССОВ, ПРОИЗВОДСТВ И УПРАВЛЕНИЯ')
async def check_yvo_automatiz_tehn_processov(message: types.Message, state: FSMContext):
    await state.update_data(back='АВТОМАТИЗАЦИЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГАТУ - Агроэнергетический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет химической технологии и техники")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет информационных технологий и управления")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Механический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Машиностроительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Энергетический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет информационных технологий и робототехники")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - МАШИНОСТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - ЭЛЕКТРОТЕХНИЧЕСКИЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='МЕТРОЛОГИЯ, СТАНДАРТИЗАЦИЯ И СЕРТИФИКАЦИЯ. ТЕХНИЧЕСКАЯ ДИАГНОСТИКА')
async def check_yvo_metrolologiya(message: types.Message, state: FSMContext):
    await state.update_data(back='ОБЕСПЕЧЕНИЕ КАЧЕСТВА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГАТУ - Инженерно-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет технологии органических веществ")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Приборостроительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - ЭЛЕКТРОТЕХНИЧЕСКИЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ИНТЕЛЛЕКТУАЛЬНЫЕ СИСТЕМЫ')
async def check_yvo_intelectyal_sistemy(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Машиностроительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЗЕМЛЕУСТРОЙСТВО')
async def check_yvo_zemleystroistvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ЗЕМЛЕУСТРОЙСТВО, ГЕОДЕЗИЯ, КАРТОГРАФИЯ И ТОПОГРАФИЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Землеустроительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ГЕОДЕЗИЯ, КАРТОГРАФИЯ И ТОПОГРАФИЯ')
async def check_yvo_geodesia(message: types.Message, state: FSMContext):
    await state.update_data(back='ЗЕМЛЕУСТРОЙСТВО, ГЕОДЕЗИЯ, КАРТОГРАФИЯ И ТОПОГРАФИЯ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет географии и геоинформатики")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Военный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет транспортных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ОХРАНА ОКРУЖАЮЩЕЙ СРЕДЫ')
async def check_yvo_ohrana_okr_sredy(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет химической технологии и техники")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет горного дела и инженерной экологии")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЭРГОНОМИКА В ИНФОРМАЦИОННЫХ СИСТЕМАХ')
async def check_yvo_ergonomika_v_inf_sistemah(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭРГОНОМИКА')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОМЫШЛЕННЫЙ ДИЗАЙН')
async def check_yvo_prom_dizign(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКА И ТЕХНОЛОГИИ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Автотракторный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))

@dp.callback_query_handler(text='АРХИТЕКТУРА')
async def check_yvo_architekture(call: CallbackQuery, state: FSMContext):
    await check_yvo_architekture(call.message, state)

@dp.message_handler(text='АРХИТЕКТУРА')
async def check_yvo_architekture(message: types.Message, state: FSMContext):
    await state.update_data(back='АРХИТЕКТУРА И СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет промышленного и гражданского строительства")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Архитектурный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СТРОИТЕЛЬНЫЕ МАТЕРИАЛЫ, ИЗДЕЛИЯ И КОНСТРУКЦИИ')
async def check_yvo_stroi_mat(message: types.Message, state: FSMContext):
    await state.update_data(back='СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Строительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЗДАНИЯ И СООРУЖЕНИЯ')
async def check_yvo_zdania_i_soor(message: types.Message, state: FSMContext):
    await state.update_data(back='СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет промышленного и гражданского строительства")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Строительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - СТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ДОРОГИ И ДРУГИЕ ТРАНСПОРТНЫЕ ОБЪЕКТЫ')
async def check_yvo_dorogy(message: types.Message, state: FSMContext):
    await state.update_data(back='СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Строительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет транспортных коммуникаций")],
                                                              [KeyboardButton(
                                                                  "Белорусско-Российский университет - СТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СИСТЕМЫ ВОДНОГО ХОЗЯЙСТВА И ТЕПЛОГАЗОСНАБЖЕНИЯ')
async def check_yvo_sistemy_vadnogo_hozaistva(message: types.Message, state: FSMContext):
    await state.update_data(back='СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Строительный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет энергетического строительства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ТЕПЛОВЫЕ И АТОМНЫЕ ЭЛЕКТРОСТАНЦИИ')
async def check_yvo_teplovie_i_atomnie_electrostancii(message: types.Message, state: FSMContext):
    await state.update_data(back='СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет энергетического строительства")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СЕЛЬСКОХОЗЯЙСТВЕННЫЙ МЕНЕДЖМЕНТ')
async def check_yvo_s_h_menejment(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ ХОЗЯЙСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "БГАТУ - Факультет предпринимательства и управления")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОИЗВОДСТВО, ХРАНЕНИЕ И ПЕРЕРАБОТКА ПРОДУКЦИИ РАСТЕНИЕВОДСТВА')
async def check_yvo_proizv_hranenie_i_pererabotka(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ ХОЗЯЙСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Агрономический факультет")],
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Агроэкологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЖИВОТНОВОДСТВО. РЫБОВОДСТВО. ПЧЕЛОВОДСТВО')
async def check_yvo_jivotnovodstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ ХОЗЯЙСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет биотехнологии и аквакультуры")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СЕЛЬСКОЕ СТРОИТЕЛЬСТВО И ОБУСТРОЙСТВО ТЕРРИТОРИЙ')
async def check_yvo_selskoe_stroitelstvo_i_obystroistvo(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ ХОЗЯЙСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Мелиоративно-строительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='МЕЛИОРАЦИЯ И ВОДНОЕ ХОЗЯЙСТВО')
async def check_yvo_melioracia(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ ХОЗЯЙСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Мелиоративно-строительный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='АГРОИНЖЕНЕРИЯ')
async def check_yvo_agroijeneria(message: types.Message, state: FSMContext):
    await state.update_data(back='СЕЛЬСКОЕ ХОЗЯЙСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет механизации сельского хозяйства")],
                                                              [KeyboardButton(
                                                                  "БГАТУ - Агромеханический факультет")],
                                                              [KeyboardButton(
                                                                  "БГАТУ - Агроэнергетический факультет")],
                                                              [KeyboardButton(
                                                                  "БГАТУ - Инженерно-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЛЕСНОЕ ХОЗЯЙСТВО')
async def check_yvo_lesnoe_hozaystvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ЛЕСНОЕ ХОЗЯЙСТВО И САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Лесохозяйственный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
async def check_yvo_sadovo_parkovoe_stroitelstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ЛЕСНОЕ ХОЗЯЙСТВО И САДОВО-ПАРКОВОЕ СТРОИТЕЛЬСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Лесохозяйственный факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРОФИЛАКТИКА, ДИАГНОСТИКА, ЛЕЧЕНИЕ, РЕАБИЛИТАЦИЯ И ОРГАНИЗАЦИЯ ЗДРАВООХРАНЕНИЯ')
async def check_yvo_profilactoka_diagnostika(message: types.Message, state: FSMContext):
    await state.update_data(back='ЗДРАВООХРАНЕНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Лечебный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Педиатрический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Стоматологический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Медико-профилактический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Военно-медицинский институт")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Медицинский факультет иностранных учащихся")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный медицинский университет - Фармацевтический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЛАБОРАТОРНОЕ ОБЕСПЕЧЕНИЕ')
async def check_yvo_laboratornoe_obespechenie(message: types.Message, state: FSMContext):
    await state.update_data(back='ТЕХНИКО-ЛАБОРАТОРНОЕ ОБЕСПЕЧЕНИЕ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")],
                                                              [KeyboardButton(
                                                                  "Международный государственный экологический институт имени А.Д.Сахарова Белорусского государственного университета - Факультет экологической медицины")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))

@dp.callback_query_handler(text='СОЦИАЛЬНАЯ ЗАЩИТА')
async def check_yvo_soc_zaschita(call: CallbackQuery, state: FSMContext):
    await check_yvo_soc_zaschita(call.message, state)
@dp.message_handler(text='СОЦИАЛЬНАЯ ЗАЩИТА')
async def check_yvo_soc_zaschita(message: types.Message, state: FSMContext):
    await state.update_data(back='УВО2')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет социально-педагогических технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет философии и социальных наук")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ФИЗИЧЕСКАЯ КУЛЬТУРА')
async def check_yvo_fizicheskaya_kultyra(message: types.Message, state: FSMContext):
    await state.update_data(back='ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет физического воспитания")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Факультет оздоровительной физической культуры")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='СПОРТ')
async def check_yvo_sport(message: types.Message, state: FSMContext):
    await state.update_data(back='ФИЗИЧЕСКАЯ КУЛЬТУРА И СПОРТ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет физического воспитания")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Спортивно-педагогический факультет спортивных игр и единоборств")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Спортивно-педагогический факультет спортивных игр и единоборств")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Факультет оздоровительной физической культуры")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Институт менеджмента спорта и туризма")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ТУРИЗМ И ГОСТЕПРИИМСТВО')
async def check_yvo_tyrizm_igostepreimstvo(message: types.Message, state: FSMContext):
    await state.update_data(back='ТУРИЗМ. ГОСТЕПРИИМСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Институт менеджмента спорта и туризма")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ТУРИЗМ')
async def check_yvo_tyrizm(message: types.Message, state: FSMContext):
    await state.update_data(back='ТУРИЗМ. ГОСТЕПРИИМСТВО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный педагогический университет им. Максима Танка - Факультет физического воспитания")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Лесохозяйственный факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет физической культуры - Институт менеджмента спорта и туризма")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))

@dp.callback_query_handler(text='ОБЩЕСТВЕННОЕ ПИТАНИЕ')
async def check_yvo_ob_pit(call: CallbackQuery, state: FSMContext):
    await check_yvo_ob_pit(call.message, state)
@dp.message_handler(text='ОБЩЕСТВЕННОЕ ПИТАНИЕ')
async def check_yvo_ob_pit(message: types.Message, state: FSMContext):
    await state.update_data(back='УВО2')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет пищевых и химических технологий - Химико-технологический факультет")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ПРЕДУПРЕЖДЕНИЕ И ЛИКВИДАЦИЯ ЧРЕЗВЫЧАЙНЫХ СИТУАЦИЙ')
async def check_yvo_preduprejdenie_i_likvidacia_chp(message: types.Message, state: FSMContext):
    await state.update_data(back='ЗАЩИТА ОТ ЧРЕЗВЫЧАЙНЫХ СИТУАЦИЙ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Университет гражданской защиты Министерства по чрезвычайным ситуациям Республики Беларусь - Факультет предупреждения и ликвидации чрезвычайных ситуаций")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ОБЕСПЕЧЕНИЕ БЕЗОПАСНОСТИ')
async def check_yvo_obespechenie_bezopasnosty(message: types.Message, state: FSMContext):
    await state.update_data(back='ЗАЩИТА ОТ ЧРЕЗВЫЧАЙНЫХ СИТУАЦИЙ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Университет гражданской защиты Министерства по чрезвычайным ситуациям Республики Беларусь - Факультет техносферной безопасности")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='УПРАВЛЕНИЕ ПОДРАЗДЕЛЕНИЯМИ И ОБЕСПЕЧЕНИЕ ИХ ДЕЯТЕЛЬНОСТИ')
async def check_yvo_ypravlenie_podrazdeleniami(message: types.Message, state: FSMContext):
    await state.update_data(back='ВОЕННОЕ ДЕЛО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Военно-транспортный факультет")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Общевойсковой")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Авиационный")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Внутренних войск")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Военной разведки")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Ракетных войск и артиллерии и ракетно-артиллерийского вооружения")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ВОЕННО-ИНЖЕНЕРНАЯ ДЕЯТЕЛЬНОСТЬ')
async def check_yvo_voenno_inj_deyat(message: types.Message, state: FSMContext):
    await state.update_data(back='ВОЕННОЕ ДЕЛО')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусская государственная академия авиации - Факультет военный")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Общевойсковой")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Связи и автоматизированных систем управления")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Противовоздушной обороны")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Внутренних войск")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Военной разведки")],
                                                              [KeyboardButton(
                                                                  "Военная академия Республики Беларусь - Ракетных войск и артиллерии и ракетно-артиллерийского вооружения")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ОБЕСПЕЧЕНИЕ ЭКОНОМИЧЕСКОЙ БЕЗОПАСНОСТИ')
async def check_yvo_obespech_econom_bezop(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОНОМИЧЕСКАЯ БЕЗОПАСНОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Экономический факультет")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет международных отношений")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет транспорта - Факультет экономики и бизнес-технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЗАЩИТА ИНФОРМАЦИИ')
async def check_yvo_zaschita_informacii(message: types.Message, state: FSMContext):
    await state.update_data(back='ИНФОРМАЦИОННАЯ БЕЗОПАСНОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный технологический университет - Факультет информационных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет прикладной математики и информатики")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Факультет радиофизики и компьютерных технологий")],
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет информатики и радиоэлектроники - Факультет инфокоммуникаций")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(text='ЗАЩИТА ОТ ИОНИЗИРУЮЩЕГО ИЗЛУЧЕНИЯ')
async def check_yvo_zaschita_ot_isoniruyuschego_islushenia(message: types.Message, state: FSMContext):
    await state.update_data(back='ЭКОЛОГИЧЕСКАЯ БЕЗОПАСНОСТЬ')
    await message.answer(text='Чтобы узнать подробности о специальности нажмите на неё',
                         reply_markup=ReplyKeyboardMarkup(resize_keyboard=True,
                                                          keyboard=[
                                                              [KeyboardButton(
                                                                  "Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")],
                                                              [KeyboardButton(
                                                                  "Международный государственный экологический институт имени А.Д.Сахарова Белорусского государственного университета - Факультет мониторинга окружающей среды")],
                                                              [KeyboardButton(
                                                                  "НАЗАД")],
                                                          ]))


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет бизнеса и права")
async def check_1(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет бизнеса и права</b>\n"
             "Декан <i>Глушакова Наталья Алексеевна</i>\n"
             "Телефон: 8022337-97-78,7-97-09\n"
             "Сайт: http://baa.by/facultet/bip/\n"
             "Правовое обеспечение бизнеса\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Правовое обеспечение бизнеса\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Правовое обеспечение бизнеса\n"
             "<b>Юрист</b>\n"
             "Время обучения: \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "основы менеджмента (ЭУО),\n"
             "экономика организации (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Институт современных знаний имени А.М.Широкова - Гуманитарный факультет")
async def check_2(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Институт современных знаний имени А.М.Широкова - Гуманитарный факультет</b>\n"
             "Декан <i>Кадира Владислав Николаевич</i>\n"
             "Телефон: (017)2370018\n"
             "Сайт: http://www.isz.minsk.by/history/fakul_tety/gumanitarny.html\n"
             "Культурология (прикладная)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "Лингвистическое обеспечение межкультурных коммуникаций (международный туризм)\n"
             "<b>Специалист по межкультурным коммуникациям,Переводчик-референт (с указанием языков общения)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "английский язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "Культурология (прикладная)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Факультет социально-педагогических технологий")
async def check_3(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Факультет социально-педагогических технологий</b>\n"
             "Декан <i>Мартынова Вера Васильевна</i>\n"
             "Телефон: +375(17)200-15-22200-15-28\n"
             "Сайт: https://fspt.bspu.by/fakultet/istoriya-fakulteta\n"
             "<b>Социальный педагог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог социальный. Педагог-психолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "Социальная работа\n"
             "<b>Специалист по социальной работе-педагог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Социальный педагог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог социальный. Педагог-психолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "Социальная работа\n"
             "<b>Специалист по социальной работе-педагог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Социальный педагог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог социальный. Педагог-психолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "Социальная работа\n"
             "<b>Специалист по социальной работе-педагог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Социальный педагог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог социальный. Педагог-психолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "Социальная работа\n"
             "<b>Специалист по социальной работе-педагог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Международный государственный экологический институт имени А.Д.Сахарова Белорусского государственного университета - Факультет мониторинга окружающей среды")
async def check_4(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Международный государственный экологический институт имени А.Д.Сахарова Белорусского государственного университета - Факультет мониторинга окружающей среды</b>\n"
             "Декан <i>Жилко Вячеслав Владимирович</i>\n"
             "Телефон: +(37517)3967177\n"
             "Сайт: http://www.iseu.bsu.by/institut/structura/fmos/\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Эколог. Инженер по охране окружающей среды</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в экологии)\n"
             "<b>Инженер-программист-эколог</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в здравоохранении)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Эколог. Инженер по охране окружающей среды</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в экологии)\n"
             "<b>Инженер-программист-эколог</b>\n"
             "Время обучения: 4 \n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в здравоохранении)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 3 года\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусско-Российский университет - АВТОМЕХАНИЧЕСКИЙ ФАКУЛЬТЕТ")
async def check_5(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Белорусско-Российский университет - АВТОМЕХАНИЧЕСКИЙ ФАКУЛЬТЕТ</b>\n"
             "Декан <i>Мельников Александр Сергеевич</i>\n"
             "Телефон: 8(0222)22-11-93\n"
             "Сайт: \n"
             "1] Подъемно-транспортные, строительные, дорожные машины и оборудование (по направлениям)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Техническая эксплуатация автомобилей (по направлениям)\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет физической культуры - Институт менеджмента спорта и туризма")
async def check_6(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет физической культуры - Институт менеджмента спорта и туризма</b>\n"
             "Директор Института менеджмента спорта и туризма <i>Ананьева Валентина Николаевна</i>\n"
             "Телефон: 8(017)3258130\n"
             "Сайт: \n"
             "Спортивно-педагогическая деятельность (менеджмент в спорте)\n"
             "<b>Менеджер в спорте,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "<b>Специалист в сфере туризма и гостеприимства</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "география (ЦТ)\n"
             "\n"
             "Спортивно-туристская деятельность (спортивный и рекреационный туризм)\n"
             "<b>Инструктор-методист по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Спортивно-туристская деятельность (менеджмент в туризме)\n"
             "<b>Менеджер по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (менеджмент в спорте)\n"
             "<b>Менеджер в спорте,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "<b>Специалист в сфере туризма и гостеприимства</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "география (ЦТ)\n"
             "\n"
             "Спортивно-туристская деятельность (спортивный и рекреационный туризм)\n"
             "<b>Инструктор-методист по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Спортивно-туристская деятельность (менеджмент в туризме)\n"
             "<b>Менеджер по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (менеджмент в спорте)\n"
             "<b>Менеджер в спорте,Преподаватель физической культуры</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "<b>Специалист в сфере туризма и гостеприимства</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "география (ЦТ)\n"
             "\n"
             "Спортивно-туристская деятельность (менеджмент в туризме)\n"
             "<b>Менеджер по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Барановичский государственный университет - Факультет экономики и права")
async def check_7(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Барановичский государственный университет - Факультет экономики и права</b>\n"
             "Декан <i>Лабейко Ольга Анатольевна</i>\n"
             "Телефон: (0163)665378(0163)669477(0163)669478\n"
             "Сайт: https://www.barsu.by/faculties/chairfinancial/financial.php\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Юрист со знанием экономики</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "7] Бухгалтерский учет, анализ и аудит в агропромышленном комплексе\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и организация производства (машиностроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "Хозяйственное право\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Юрист со знанием экономики</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "7] Бухгалтерский учет, анализ и аудит в агропромышленном комплексе\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и организация производства (машиностроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "Хозяйственное право\n"
             "<b>Юрист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 3 года \n"
             "Вступительные испытания: \n"
             "Общая теория права (письменный экзамен сдается в Университете)\n"
             "Гражданское право (письменный экзамен сдается в Университете)\n"
             "\n"
             "Хозяйственное право\n"
             "<b>Юрист</b>\n"
             "Время обучения: 3 года \n"
             "Вступительные испытания: \n"
             "Общая теория права (письменный экзамен сдается в Университете)\n"
             "Гражданское право (письменный экзамен сдается в Университете)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Институт психологии")
async def check_8(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Институт психологии</b>\n"
             "Декан <i>Дьяков Дмитрий Григорьевич</i>\n"
             "Телефон: 369-88-15\n"
             "Сайт: www.ipsy.bspu.by\n"
             "<b>Педагог-психолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Психолог,Преподаватель психологии</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-психолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Психолог,Преподаватель психологии</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-психолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Психолог,Преподаватель психологии</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: биология (ЦТ);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия искусств - Театральный факультет")
async def check_9(message: types.Message,
                  state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия искусств - Театральный факультет</b>\n"
             "Декан <i>Мищанчук Владимир Андреевич</i>\n"
             "Телефон: +375173669879\n"
             "Сайт: http://bdam.by/театральный-факультет/\n"
             "Актерское искусство (драматический театр и кино)\n"
             "<b>Актер драматического театра и кино</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (централизованное тестирование (ЦТ)),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (сценическая речь, сценическая пластика и вокал, мастерство актера)"
             "\n"
             "Актерское искусство (драматический театр и кино)\n"
             "<b>Актер драматического театра и кино</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (централизованное тестирование (ЦТ)),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (сценическая речь, сценическая пластика и вокал, мастерство актера)\n"
             "\n"
             "Актерское искусство (драматический театр и кино)\n"
             "<b>Актер драматического театра и кино</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (сценическая речь, сценическая пластика и вокал, мастерство актера)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Физико-математический факультет")
async def check_10(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Физико-математический факультет</b>\n"
             "Декан <i>Климович Анна Фёдоровна</i>\n"
             "Телефон: 200-22-85\n"
             "Сайт: https://fmath.bspu.byhttps://vk.com/fmf_bspu\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: математика (ЦТ)\n"
             "второе профильное испытание: физика (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физика (ЦТ)\n"
             "второе профильное испытание: математика (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: математика (ЦТ)\n"
             "второе профильное испытание: физика (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физика (ЦТ)\n"
             "второе профильное испытание: математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский национальный технический университет - Факультет информационных технологий и робототехники")
async def check_11(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Факультет информационных технологий и робототехники</b>\n"
             "Декан <i>АВСИЕВИЧ Андрей Михайлович</i>\n"
             "Телефон: 2927153\n"
             "Сайт: http://www.bntu.by/fitr.html\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в проектировании и производстве)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в обработке и представлении информации)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер по автоматизации</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в проектировании и производстве)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в обработке и представлении информации)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер по автоматизации</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Основы электротехники (ПЭ)\n"
             "2. Основы инженерной графики (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет культуры и искусств - Факультет культурологии и социально-культурной деятельности")
async def check_12(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет культуры и искусств - Факультет культурологии и социально-культурной деятельности</b>\n"
             "Декан <i>Шелупенко Наталья Евгеньевна</i>\n"
             "Телефон: +375173748308\n"
             "Сайт: http://www.buk.by/process/fakultet%201/\n"
             "Культурология (специализация Менеджмент социальной и культурной сферы)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Менеджмент рекламы и общественных связей)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Информационные системы в культуре)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Менеджмент международных культурных связей)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Специалист по социально-культурной деятельности,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (культурно-досуговая деятельность; любительское творчество; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Менеджмент рекламы и общественных связей)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Менеджмент международных культурных связей)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Менеджмент социальной и культурной сферы)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Культурология (специализация Информационные системы в культуре)\n"
             "<b>Культуролог-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Специалист по социально-культурной деятельности,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (культурно-досуговая деятельность; любительское творчество; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных технологий")
async def check_13(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных технологий</b>\n"
             "Декан <i>Касанин Сергей Николаевич</i>\n"
             "Телефон: \n"
             "Сайт: https://iti.bsuir.by/faculty/1\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 3,5 года\n"
             "Вступительные испытания: \n"
             "Основы информационных технологий (ПЭ),\n"
             "Охрана труда. Охрана окружающей среды и энергосбережение (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет культуры и искусств - Факультет художественной культуры")
async def check_14(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет культуры и искусств - Факультет художественной культуры</b>\n"
             "Декан <i>Пагоцкая Елена Викторовна</i>\n"
             "Телефон: +375173578351\n"
             "Сайт: http://www.buk.by/process/fakultet%202/\n"
             "Декоративно-прикладное искусство (реставрация изделий)   \n"
             "<b>Художник декоративно-прикладного искусства,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (рисунок; живопись; композиция)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Режиссура праздников (театрализованные)\n"
             "<b>Режиссер,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (актёрское мастерство; режиссура; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (режиссура)\n"
             "<b>Режиссер. Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (актерское мастерство; режиссура; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Режиссер,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (актёрское мастерство; режиссура; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Режиссура праздников (народные)\n"
             "<b>Режиссер,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (народные ремесла)\n"
             "<b>Художник народных ремесел,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="БГАТУ - Агроэнергетический факультет")
async def check_15(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>БГАТУ - Агроэнергетический факультет</b>\n"
             "Декан <i>Протосовицкий Иван Васильевич</i>\n"
             "Телефон: 373-33-83\n"
             "Сайт: http://www.bsatu.by/ru/fakultety/agroenergeticheskiy-fakultet\n"
             "Автоматизация технологических процессов и производств (сельское хозяйство)\n"
             "<b>Инженер по автоматизации</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Энергетическое обеспечение сельского хозяйства (электроэнергетика)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), физика (ЦТ или ЭУО)\n"
             "\n"
             "Энергетическое обеспечение сельского хозяйства (электроэнергетика)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), физика (ЦТ или ЭУО)\n"
             "Энергетическое обеспечение сельского хозяйства (электроэнергетика)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "теоретические основы электротехники (ЭУО), электрические машины (ЭУО)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Академия Министерства внутренних дел Республики Беларусь - Следственно-экспертный факультет")
async def check_16(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Академия Министерства внутренних дел Республики Беларусь - Следственно-экспертный факультет</b>\n"
             "Начальник факультета <i>СКАЧЁК Роман Владимирович</i>\n"
             "Телефон: (017)355-59-03\n"
             "Сайт: https://sef.amia.by/\n"
             "Судебно-прокурорско-следственная деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Судебный эксперт-криминалист. Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный экономический университет - Институт социально-гуманитарного образования ")
async def check_17(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Институт социально-гуманитарного образования </b>\n"
             "Директор <i>Данила Григорьевич Доброродний</i>\n"
             "Телефон: 209-78-47–ДанилаГригорьевичДоброродний,директор\n"
             "Сайт: http://bseu.by/isgo/\n"
             "Психология предпринимательской деятельности\n"
             "<b>Психолог,Преподаватель психологии</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "Экономическая социология\n"
             "<b>Социолог,Преподаватель социологии и социально-политических дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский)язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "Политология (политический менеджмент)\n"
             "<b>Политолог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский)язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "Психология предпринимательской деятельности\n"
             "<b>Психолог,Преподаватель психологии</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "Экономическая социология\n"
             "<b>Социолог,Преподаватель социологии и социально-политических дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский)язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "Политология (политический менеджмент)\n"
             "<b>Политолог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский)язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Военно-Технический Факультет")
async def check_18(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Военно-Технический Факультет</b>\n"
             "Начальник факультета <i>полковник Почебыт Андрей Александрович</i>\n"
             "Телефон: 292-94-82292-32-14\n"
             "Сайт: http://www.bntu.by/vtf.html\n"
             "Финансовое обеспечение и экономика боевой и хозяйственной деятельности войск\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "Подъемно-транспортные, строительные, дорожные машины и оборудование (управление подразделениями инженерных войск)\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Многоцелевые гусеничные и колесные машины (эксплуатация и ремонт бронетанкового вооружения и техники)\n"
             "<b>Инженер-механик,Специалист по управлению</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Техническая эксплуатация автомобилей (военная автомобильная техника)\n"
             "<b>Инженер-механик,Специалист по управлению</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Техническая эксплуатация зданий и сооружений\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет транспорта - Факультет промышленного и гражданского строительства")
async def check_19(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Факультет промышленного и гражданского строительства</b>\n"
             "Декан <i>Ташкинов Анатолий Германович</i>\n"
             "Телефон: (0232)777549(0232)952194\n"
             "Сайт: http://bsut.by/obrazovanie/fakultety/promyshlennoe-i-grajdanskoe-stroite...\n"
             "Архитектура жилых и общественных зданий\n"
             "<b>Архитектор</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭВ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Технология и организация строительного производства\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Архитектура жилых и общественных зданий\n"
             "<b>Архитектор</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭВ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Технология и организация строительного производства\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет пищевых и химических технологий - Экономический факультет")
async def check_20(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет пищевых и химических технологий - Экономический факультет</b>\n"
             "Декан факультета <i>Козлова Елена Алексеевна</i>\n"
             "Телефон: 8022264-75-408022249-49-75\n"
             "Сайт: http://www.bgut.by/faculty-ef/\n"
             "3] Бухгалтерский учет, анализ и аудит в промышленности\n"
             "<b>Экономист</b>\n"
             "Время обучения: 3 года 5 месяцев\n"
             "Вступительные испытания: \n"
             "1. Экономика организации (письменный экзамен)\n"
             "2. Бухгалтерский учет (письменный экзамен)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Инженерно-экономический факультет")
async def check_21(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Инженерно-экономический факультет</b>\n"
             "Декан <i>Лаврова Ольга Игоревна</i>\n"
             "Телефон: (017)293-22-88\n"
             "Сайт: http://www.bsuir.by/ru/iefhttps://vk.com/ief_bsuirhttps://www.instagram.com/ief_bsuir/\n"
             "<b>Экономист-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в экономике)\n"
             "<b>Инженер-программист-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в логистике)\n"
             "<b>Системный программист-логистик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Экономист-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в экономике)\n"
             "<b>Инженер-программист-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в логистике)\n"
             "<b>Системный программист-логистик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Экономист-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусско-Российский университет - СТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")
async def check_22(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусско-Российский университет - СТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ</b>\n"
             "Декан <i>Голушкова Ольга Васильевна</i>\n"
             "Телефон: 8(0222)22-53-13\n"
             "Сайт: \n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет транспорта - Строительный  факультет")
async def check_23(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Строительный  факультет</b>\n"
             "Декан <i>Бочкарёв Дмитрий Игоревич</i>\n"
             "Телефон: (0232)952192(0232)777529\n"
             "Сайт: http://bsut.by/obrazovanie/fakultety/stroitelnyj.html\n"
             "Строительство железных дорог и путевое хозяйство\n"
             "<b>Инженер путей сообщения – строитель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Строительство дорог и аэродромов\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Системы водоснабжения и водоотведения\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Академия Министерства внутренних дел Республики Беларусь - Факультет права")
async def check_24(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Академия Министерства внутренних дел Республики Беларусь - Факультет права</b>\n"
             "Декан <i>ДОЛИДОВИЧ Александр Владимирович</i>\n"
             "Телефон: (+375-17)289-23-24\n"
             "Сайт: https://www.amia.by/structure/faculties/faculty-of-law\n"
             "Судебно-прокурорско-следственная деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Административно-правовая деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный медицинский университет - Фармацевтический факультет")
async def check_25(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Фармацевтический факультет</b>\n"
             "Декан <i>Гурина Наталия Сергеевна</i>\n"
             "Телефон: (017)2074547(017)2772086\n"
             "Сайт: http://www.bsmu.by/page/6/86/\n"
             "<b>Провизор</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Провизор</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Провизор</b>\n"
             "Время обучения: 5,5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Международный университет МИТСО - Экономический факультет")
async def check_26(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Международный университет МИТСО - Экономический факультет</b>\n"
             "декан <i>Моисеенко Евгений Григорьевич</i>\n"
             "Телефон: 80172799834(деканат)80172799845(заместительдекана)80172799845(декан)\n"
             "Сайт: https://www.mitso.by/univiersitiet/fakultetyi/fakul-tiet-miezhdunarodnyk...\n"
             "<b></b>\n"
             "Время обучения: 4,5 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (цт)\n"
             "Иностранный язык (цт)\n"
             "История Беларуси (цт)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык(ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Логистик-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист информационных систем</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия музыки - Вокально-хоровой факультет")
async def check_27(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия музыки - Вокально-хоровой факультет</b>\n"
             "Декан <i>Караев Юрий Анатольевич</i>\n"
             "Телефон: +37517322-11-76\n"
             "Сайт: \n"
             "Дирижирование (академический хор)\n"
             "<b>Артист хора</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "ЦТ, ЭУО\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Военная академия Республики Беларусь - Авиационный")
async def check_28(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Авиационный</b>\n"
             "Начальник факультета <i>Селуянов Кирилл Васильевич </i>\n"
             "Телефон: (017)2874590\n"
             "Сайт: \n"
             "Эксплуатация воздушного транспорта, управление воздушным движением (фронтовая авиация)\n"
             "<b>Пилот-инженер самолета,Специалист по управлению</b>\n"
             "Время обучения: 4 года и 3 месяца\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Военная академия Республики Беларусь - Противовоздушной обороны")
async def check_29(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Противовоздушной обороны</b>\n"
             "Начальник факультета <i>Клишевич Андрей Владимирович</i>\n"
             "Телефон: (017)2874206\n"
             "Сайт: \n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный экономический университет - Факультет коммерции и туристической индустрии")
async def check_30(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Факультет коммерции и туристической индустрии</b>\n"
             "Декан <i>Ерчак Александр Иванович</i>\n"
             "Телефон: +37517209-79-81ДФО+37517209-79-86ЗФО\n"
             "Сайт: http://fcti.by/\n"
             "<b>Товаровед-эксперт</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Товаровед-эксперт</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 3,5\n"
             "Вступительные испытания: \n"
             "экономика организации (ЭУО)\n"
             "основы менеджмента (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных систем и сетей")
async def check_31(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерных систем и сетей</b>\n"
             "Декан <i>Нестеренков Сергей Николаевич</i>\n"
             "Телефон: (017)293-86-63\n"
             "Сайт: https://www.bsuir.by/ru/fksis\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системный программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системный программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системный программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Химический факультет")
async def check_32(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Химический факультет</b>\n"
             "Декан <i>Свиридов Дмитрий Вадимович</i>\n"
             "Телефон: (+375-17)200-69-18(+375-17)209-52-53(+375-17)209-51-74\n"
             "Сайт: www.chemistry.bsu.by\n"
             "Химия (научно-производственная деятельность)\n"
             "<b>Химик,Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Химия (научно-педагогическая деятельность)\n"
             "<b>Химик,Преподаватель химии</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Химия (фармацевтическая деятельность)\n"
             "<b>Химик,Химик-фармацевт</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Химия (охрана окружающей среды)\n"
             "<b>Химик,Химик-эколог</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Университет гражданской защиты Министерства по чрезвычайным ситуациям Республики Беларусь - Факультет предупреждения и ликвидации чрезвычайных ситуаций")
async def check_33(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Университет гражданской защиты Министерства по чрезвычайным ситуациям Республики Беларусь - Факультет предупреждения и ликвидации чрезвычайных ситуаций</b>\n"
             "начальник факультета <i>Вариков Геннадий Анатольевич</i>\n"
             "Телефон: (017)341-72-22\n"
             "Сайт: \n"
             "<b>Инженер по предупреждению и ликвидации чрезвычайных ситуаций</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер по предупреждению и ликвидации чрезвычайных ситуаций</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Энергетический факультет")
async def check_34(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Энергетический факультет</b>\n"
             "Декан <i>ПОНОМАРЕНКО Евгений Геннадьевич</i>\n"
             "Телефон: 292-42-32\n"
             "Сайт: http://www.bntu.by/ef.html\n"
             "Экономика и организация производства (энергетика)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-теплоэнергетик по автоматизации</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Экономика и организация производства (энергетика)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Основы электротехники (ПЭ)\n"
             "2. Основы инженерной графики (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусско-Российский университет - ЭКОНОМИЧЕСКИЙ ФАКУЛЬТЕТ")
async def check_35(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусско-Российский университет - ЭКОНОМИЧЕСКИЙ ФАКУЛЬТЕТ</b>\n"
             "Декан <i>Маковецкий Илья Иванович</i>\n"
             "Телефон: 8(0222)22-13-13\n"
             "Сайт: \n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "Русский (белорусский) язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "Русский (белорусский) язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "Русский (белорусский) язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-программист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Русский (белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Факультет естествознания")
async def check_36(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Факультет естествознания</b>\n"
             "Декан <i>Науменко Наталья Владимировна</i>\n"
             "Телефон: 200-87-72\n"
             "Сайт: http://est.bspu.unibel.by/\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: биология (ЦТ)\n"
             "Второе профильное испытание: химия (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание:  биология (ЦТ)\n"
             "Второе профильное испытание: география (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: биология (ЦТ)\n"
             "Второе профильное испытание: химия (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: география (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Военная академия Республики Беларусь - Связи и автоматизированных систем управления")
async def check_37(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Связи и автоматизированных систем управления</b>\n"
             "Начальник факультета <i>Исаев Александр Александрович </i>\n"
             "Телефон: (017)2874661\n"
             "Сайт: \n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный экономический университет - Факультет цифровой экономики")
async def check_38(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Факультет цифровой экономики</b>\n"
             "Декан <i>Марушко Дмитрий Александрович</i>\n"
             "Телефон: +37517209-79-34\n"
             "Сайт: \n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "белорусский или русский язык (ЦТ)\n"
             "\n"
             "<b>Экономист-информатик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "белорусский или русский язык (ЦТ)\n"
             "\n"
             "Экономическая кибернетика (информационные технологии в экономике)\n"
             "<b>Кибернетик-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "белорусский или русский язык (ЦТ)\n"
             "\n"
             "<b>Экономист-информатик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "белорусский или русский язык (ЦТ)\n"
             "\n"
             "Экономическая кибернетика (информационные технологии в экономике)\n"
             "<b>Кибернетик-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "белорусский или русский язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Биологический факультет")
async def check_39(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Биологический факультет</b>\n"
             "Декан <i>Демидчик Вадим Викторович,</i>\n"
             "Телефон: (+375-17)209-58-08(+375-17)209-58-05\n"
             "Сайт: www.bio.bsu.by\n"
             "Биология (научно-производственная деятельность)\n"
             "<b>Биолог</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "Биология (научно-педагогическая деятельность)\n"
             "<b>Биолог. Преподаватель биологии и химии</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "Биология (биотехнология)\n"
             "<b>Биолог-биотехнолог. Преподаватель биологии</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Биолог. Биохимик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Биолог. Микробиолог</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Биоинженер-биоинформатик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Биология (научно-производственная деятельность)\n"
             "<b>Биолог</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "Биология (научно-педагогическая деятельность)\n"
             "<b>Биолог. Преподаватель биологии и химии</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Биолог. Биохимик</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Биолог. Микробиолог</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Биолог-эколог. Преподаватель биологии и экологии</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "биология (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусско-Российский университет - МАШИНОСТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ")
async def check_40(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусско-Российский университет - МАШИНОСТРОИТЕЛЬНЫЙ ФАКУЛЬТЕТ</b>\n"
             "Декан <i>Свирепа Дмитрий Михайлович</i>\n"
             "Телефон: 8(0222)22-08-38\n"
             "Сайт: \n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в проектировании и производстве)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по автоматизации</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Барановичский государственный университет - Лингвистический факультет")
async def check_41(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Барановичский государственный университет - Лингвистический факультет</b>\n"
             "Декан <i>Круглякова Наталья Николаевна</i>\n"
             "Телефон: (0163)680115(0163)680073(0163)680083\n"
             "Сайт: https://www.barsu.by/faculties/chairlang/lang.php\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский язык (ЦТ)\n"
             "Белорусская литература (письменно) (ЭУО)\n"
             "Английский язык (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Русский язык (ЦТ)\n"
             "Русская литература (устно, сдается в Университете)\n"
             "английский язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный медицинский университет - Стоматологический факультет")
async def check_42(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Стоматологический факультет</b>\n"
             "Декан <i>Шевела Татьяна Леонидовна</i>\n"
             "Телефон: (017)2074613(017)2772758\n"
             "Сайт: http://www.bsmu.by/page/6/89/\n"
             "<b>Врач</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "<b>Врач</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский государственный лингвистический университет - Факультет английского языка")
async def check_43(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Минский государственный лингвистический университет - Факультет английского языка</b>\n"
             "Декан <i>Леонтьев Павел Михайлович</i>\n"
             "Телефон: +37517284-43-86\n"
             "Сайт: http://fen.mslu.by/https://vk.com/fenmsluhttps://www.instagram.com/fen_mslu/\n"
             "Современные иностранные языки (преподавание): Английский язык и второй иностранный язык со специализацией: компьютерная лингвистика, страноведение, риторика, белорусский язык как иностранный, русский язык как иностранный, зарубежная литература, ортофония\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (цт)\n"
             "Английский язык (цт)\n"
             "История Беларуси (цт)\n"
             "\n"
             "Современные иностранные языки (преподавание): Английский язык и второй иностранный язык со специализацией: компьютерная лингвистика, страноведение, риторика, белорусский язык как иностранный, русский язык как иностранный, зарубежная литература, ортофония\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (цт)\n"
             "Английский язык (цт)\n"
             "История Беларуси (цт)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (цт)\n"
             "Английский язык (цт)\n"
             "История Беларуси (цт)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (цт)\n"
             "Английский язык (цт)\n"
             "История Беларуси (цт)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский государственный лингвистический университет - Переводческий факультет")
async def check_44(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Минский государственный лингвистический университет - Переводческий факультет</b>\n"
             "Декан <i>Пониматко Александр Петрович</i>\n"
             "Телефон: 284-82-22\n"
             "Сайт: http://ftr.mslu.by/\n"
             "Современные иностранные языки (перевод): Английский язык и второй иностранный язык со специализацией: художественный перевод, специальный перевод, синхронный перевод\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (перевод): Немецкий язык и второй иностранный язык со специализацией: специальный перевод, синхронный перевод\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Немецкий язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (перевод): Испанский язык и второй иностранный язык со специализацией: специальный перевод\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Испанский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (перевод): Английский язык и второй иностранный язык со специализацией: художественный перевод, специальный перевод, синхронный перевод\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (перевод): Немецкий язык и второй иностранный язык со специализацией: специальный перевод, синхронный перевод\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Немецкий язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (перевод): Испанский язык и второй иностранный язык со специализацией: специальный перевод\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Испанский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Инженерно-педагогический факультет")
async def check_45(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Инженерно-педагогический факультет</b>\n"
             "Декан <i>Сергей Анатольевич ИВАЩЕНКО</i>\n"
             "Телефон: 26739032370865\n"
             "Сайт: http://www.bntu.by/ipf.html\n"
             "Профессиональное обучение (машиностроение)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (строительство)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (машиностроение)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4,5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Материаловедение (ЭУО)\n"
             "3.Обработка материалов и инструмент (ЭУО)\n"
             "\n"
             "Профессиональное обучение (строительство)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4,5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Строительные материалы и изделия (ЭУО)\n"
             "3.Технология строительного производства (ЭУО)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4,5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Материаловедение (ЭУО)\n"
             "3.Обработка материалов и инструмент (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Институт современных знаний имени А.М.Широкова - Факультет  искусств")
async def check_46(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Институт современных знаний имени А.М.Широкова - Факультет  искусств</b>\n"
             "Декан <i>МОГОЛИНА Марина Петровна</i>\n"
             "Телефон: (017)3698942\n"
             "Сайт: http://www.isz.minsk.by/history/fakul_tety/iskusstv.html\n"
             "Искусство эстрады (инструментальная музыка)\n"
             "<b>Артист. Руководитель эстрадного оркестра,ансамбля. Преподаватель.</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (компьютерная музыка)\n"
             "<b>Аранжировщик компьютерной музыки,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (пение)\n"
             "<b>Певец.Руководитель вокального ансамбля.Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (продюсерство)\n"
             "<b>Продюсер,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Дизайн (предметно-пространственной среды)\n"
             "<b>Дизайнер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (рисунок, композиция) (ЭУО) История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (инструментальная музыка)\n"
             "<b>Артист. Руководитель эстрадного оркестра,ансамбля. Преподаватель.</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (компьютерная музыка)\n"
             "<b>Аранжировщик компьютерной музыки,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (пение)\n"
             "<b>Певец.Руководитель вокального ансамбля.Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (продюсерство)\n"
             "<b>Продюсер,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Творчество (ЭУО)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Академия Министерства внутренних дел Республики Беларусь - Уголовно-исполнительный факультет")
async def check_47(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Академия Министерства внутренних дел Республики Беларусь - Уголовно-исполнительный факультет</b>\n"
             "Начальник факультета <i>САВАСТЕЙ Олег Михайлович</i>\n"
             "Телефон: (017)286-28-75\n"
             "Сайт: \n"
             "Уголовно-исполнительная деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Юридический факультет")
async def check_48(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Юридический факультет</b>\n"
             "Декан <i>Шидловский Андрей Викторович</i>\n"
             "Телефон: (+375-17)209-52-30(+375-17)209-55-82(+375-17)209-55-64,(+375-17)209-57-78\n"
             "Сайт: www.law.bsu.by\n"
             "Политология (политико-юридическая деятельность)\n"
             "<b>Политолог-юрист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист со знанием экономики</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "Политология (политико-юридическая деятельность)\n"
             "<b>Политолог-юрист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "теория права, конституционное и административное право (ЭУО),\n"
             "гражданское и уголовное право (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет бухгалтерского учета")
async def check_49(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет бухгалтерского учета</b>\n"
             "Декан <i>Великоборец Наталья Владимировна</i>\n"
             "Телефон: 8022337-96-06\n"
             "Сайт: http://baa.by/facultet/fbu/\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 г. \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "7] Бухгалтерский учет, анализ и аудит в агропромышленном комплексе\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 г. \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "7] Бухгалтерский учет, анализ и аудит в агропромышленном комплексе\n"
             "<b>Экономист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "экономика организации (ЭУО),\n"
             "бухгалтерский учет (ЭУО)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: \n"
             "Вступительные испытания: \n"
             "экономика организации (ЭУО),\n"
             "бухгалтерский учет (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный экономический университет - Факультет международных экономических отношений")
async def check_50(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Факультет международных экономических отношений</b>\n"
             "Декан <i>Шкутько Оксана Николаевна</i>\n"
             "Телефон: 209-88-84-декан\n"
             "Сайт: http://bseu.by/meo/\n"
             "<b>Экономист,Преподаватель экономических дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-аналитик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист,Преподаватель экономических дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-аналитик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: \n"
             "Вступительные испытания: \n"
             "экономика организации (письменно) (ЭУО)\n"
             "основы менеджмента (письменно) (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Брестский государственный университет имени А.С.Пушкина - Исторический факультет")
async def check_51(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Брестский государственный университет имени А.С.Пушкина - Исторический факультет</b>\n"
             "Декан <i>Бурик Елена Алексеевна</i>\n"
             "Телефон: (8-0162)21-70-27(8-0162)21-78-52\n"
             "Сайт: \n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский или русский язык (ЦТ),\n"
             "всемирная история (новейшее время) (ЦТ)\n"
             "история Беларуси (ЦТ)\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Механико-технологический факультет")
async def check_52(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Механико-технологический факультет</b>\n"
             "Декан <i>Иванов Игорь Аркадьевич</i>\n"
             "Телефон: 292-42-53293-91-66\n"
             "Сайт: http://www.bntu.by/mtf.html\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 3\n"
             "Вступительные испытания: \n"
             "1. Материаловедение и технология материалов (ПЭ)\n"
             "2. Информационные технологии (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Физический факультет")
async def check_53(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Физический факультет</b>\n"
             "Декан <i>Тиванов Михаил Сергеевич</i>\n"
             "Телефон: (+375-17)209-52-67\n"
             "Сайт: Официальныйсайт:www.physics.bsu.byСоциальныесети:www.vk.com/bsuphys\n"
             "Физика (научно-исследовательская деятельность)\n"
             "<b>Физик. Исследователь</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Физика (производственная деятельность)\n"
             "<b>Физик. Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Физик. Инженер</b>\n"
             "Время обучения: 5,5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Физик. Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Физик. Программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="БГАТУ - Факультет предпринимательства и управления")
async def check_54(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>БГАТУ - Факультет предпринимательства и управления</b>\n"
             "Декан <i>Бондарь Светлана Васильевна</i>\n"
             "Телефон: 373-51-83\n"
             "Сайт: http://www.bsatu.by/ru/fakultety/fakultet-predprinimatelstva-i-upravleniya\n"
             "Менеджмент (информационный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), иностранный язык (ЦТ или ЭУО)\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), иностранный язык (ЦТ или ЭУО)\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "экономика организации (ЭУО), основы менеджмента (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Исторический факультет")
async def check_55(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Исторический факультет</b>\n"
             "Декан <i>Кохановский Александр Геннадьевич</i>\n"
             "Телефон: (+375-17)209-55-98(+375-17)209-55-93(+375-17)209-55-92\n"
             "Сайт: www.hist.bsu.by\n"
             "<b></b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "всемирная история новейшего времени (ЦТ)\n"
             "\n"
             "Документоведение (документационное обеспечение управления)\n"
             "<b>Документовед,Организатор документационного обеспечения управления</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история и современная организация государственных учреждений Беларуси (ЭУО)\n"
             "документационное обеспечение управления и архивоведение (ЭУО)\n"
             "\n"
             "Документоведение (документационное обеспечение управления)\n"
             "<b>Документовед,Организатор документационного обеспечения управления</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история и современная организация государственных учреждений Беларуси (ЭУО)\n"
             "документационное обеспечение управления и архивоведение (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет транспорта - Механический факультет")
async def check_56(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Механический факультет</b>\n"
             "Декан <i>Путято Артур Владимирович</i>\n"
             "Телефон: (0232)952193\n"
             "Сайт: https://bsut.by/university/faculties/mf\n"
             "Оборудование и технологии повышения износостойкости и восстановления деталей машин и приборов\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Тяговый состав железнодорожного транспорта (тепловозы)\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Тяговый состав железнодорожного транспорта (электрический транспорт и метрополитен)\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Вагоны\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4,5 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Электроснабжение железных дорог\n"
             "<b>Инженер-энергетик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный технологический университет - Факультет информационных технологий")
async def check_57(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Факультет информационных технологий</b>\n"
             "декан <i>Шиман Дмитрий Васильевич</i>\n"
             "Телефон: +37517399-33-89\n"
             "Сайт: https://www.belstu.by/faculties/fit.htmlhttps://it.belstu.by/\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (издательско-полиграфический комплекс)\n"
             "<b>Инженер-программист-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Дизайнер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (издательско-полиграфический комплекс)\n"
             "<b>Инженер-программист-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Дизайнер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский государственный лингвистический университет - Факультет романских языков")
async def check_58(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Минский государственный лингвистический университет - Факультет романских языков</b>\n"
             "Декан <i>Павловский Валентин Антонович</i>\n"
             "Телефон: +37517284-81-16\n"
             "Сайт: http://ffr.mslu.byhttps://vk.com/lingua_romana_msluhttps://www.instagram.com/lingua_romana_mslu/\n"
             "Современные иностранные языки (преподавание): Французский язык (на базе французского / английского языка) и  второй иностранный язык со специализацией: компьютерная лингвистика, ортофония, зарубежная литература, белорусский  язык как  иностранный\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Французский / Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (преподавание): Испанский язык (на базе испанского / английского языка) и второй иностранный язык со специализацией: компьютерная лингвистика, ортофония, зарубежная литература, белорусский  язык как  иностранный\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Испанский / Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (преподавание): Французский язык (на базе французского / английского языка) и  второй иностранный язык со специализацией: компьютерная лингвистика, ортофония, зарубежная литература, белорусский  язык как  иностранный\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Французский / Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (преподавание): Испанский язык (на базе испанского / английского языка) и второй иностранный язык со специализацией: компьютерная лингвистика, ортофония, зарубежная литература, белорусский  язык как  иностранный.\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Испанский / Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Факультет начального образования")
async def check_59(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Факультет начального образования</b>\n"
             "Декан <i>Жданович Наталья Владимировна</i>\n"
             "Телефон: 311-22-55\n"
             "Сайт: fno.bspu.by\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 3 года 6 месяцев\n"
             "Вступительные испытания: \n"
             "1-й предмет профильного испытания: педагогика (устно)\n"
             "2-й предмет профильного испытания: психология (устно)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Военный факультет")
async def check_60(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Военный факультет</b>\n"
             "Начальник <i>Юнец Александр Иосифович </i>\n"
             "Телефон: (+375-17)209-56-46(+375-17)209-52-83\n"
             "Сайт: \n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет культуры и искусств - Институт повышения квалификации и переподготовки кадров учреждения образования «Белорусский государственный университет культуры и искусств»")
async def check_61(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет культуры и искусств - Институт повышения квалификации и переподготовки кадров учреждения образования «Белорусский государственный университет культуры и искусств»</b>\n"
             "Директор Института повышения квалификации и переподготовки кадров  <i>Филиппов Александр Анатольевич</i>\n"
             "Телефон: +375173780733(приемнаядиректора),+375173782719(зам.директорапоучебнойработе)\n"
             "Сайт: http://www.buk.by/ipk/\n"
             "<b>Преподаватель в соответствии с квалификацией по основному образованию</b>\n"
             "Время обучения: Квалификация: Преподаватель в соответствии с квалификацией по основному образованию\n"
             "Срок обучения: 22 месяца\n"
             "Контактное лицо: Курбацкая Елена Вячеславовна\n"
             "тел.: (017) 368 98 46\n"
             "е-mail: umo-pk@tut.by\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Автотракторный факультет")
async def check_62(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Автотракторный факультет</b>\n"
             "Декан <i>Капский Денис Васильевич</i>\n"
             "Телефон: 2924683деканатдневногоотделения2922274деканатзаочногоотделения\n"
             "Сайт: http://www.bntu.by/atf/\n"
             "Экономика и организация производства (автомобильный транспорт)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Иностранный язык (ЦТ) - 15\n"
             "\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Автомобилестроение (механика)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Автомобилестроение (электроника)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Техническая эксплуатация автомобилей (автотранспорт общего и личного пользования)\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-инспектор</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Промышленный дизайн (транспортных средств)\n"
             "<b>Инженер-дизайнер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Творчество (рисунок - 3,"
             "композиция - 3)\n"
             "3. Математика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "Техническая эксплуатация автомобилей (автотранспорт общего и личного пользования)\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "Техническая эксплуатация автомобилей (автотранспорт общего и личного пользования)\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "Транспортная логистика (автомобильный транспорт)\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Экономика организации (ПЭ)\n"
             "2. Основы менеджмента (ПЭ)\n"
             "\n"
             "Транспортная логистика (автомобильный транспорт)\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Экономика организации (ПЭ)\n"
             "2. Основы менеджмента (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Экономический факультет")
async def check_63(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Экономический факультет</b>\n"
             "Декан <i>Королева Анна Анатольевна</i>\n"
             "Телефон: (+375-17)227-60-25\n"
             "Сайт: http://www.bsu.by/ru/main.aspx?guid=4741\n"
             "<b>Экономист,Преподаватель экономических дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Экономист-аналитик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Экономист-информатик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия искусств - Художественный факультет")
async def check_64(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия искусств - Художественный факультет</b>\n"
             "Декан <i>Кононова Анна Владимировна</i>\n"
             "Телефон: 3669869\n"
             "Сайт: http://bdam.by/деканат-художественного-факультет/\n"
             "Живопись (станковая)\n"
             "<b>Художник-живописец.  Преподаватель</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (рисунок, живопись, композиция)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Военная академия Республики Беларусь - Ракетных войск и артиллерии и ракетно-артиллерийского вооружения")
async def check_65(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Ракетных войск и артиллерии и ракетно-артиллерийского вооружения</b>\n"
             "Начальник факультета <i>Рябоконь Вадим Викторович </i>\n"
             "Телефон: (017)2874323\n"
             "Сайт: \n"
             "<b>Специалист по управлению – инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Эксплуатация радиотехнических систем (артиллерии)\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный технологический университет - Факультет лесной инженерии, материаловедения и дизайна")
async def check_66(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Факультет лесной инженерии, материаловедения и дизайна</b>\n"
             "Декан <i>Лой Владимир Николаевич</i>\n"
             "Телефон: +37517365-20-41\n"
             "Сайт: https://www.belstu.by/faculties/ttlp.htmlhttps://ttlp.belstu.by/?_ga=2.148804735.917296700.1613972837-251306727.1...\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-мехатроник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-мехатроник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Международный государственный экологический институт имени А.Д.Сахарова Белорусского государственного университета - Факультет экологической медицины")
async def check_67(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Международный государственный экологический институт имени А.Д.Сахарова Белорусского государственного университета - Факультет экологической медицины</b>\n"
             "Декан <i>Сыса Алексей Григорьевич</i>\n"
             "Телефон: +(37517)379-93-59\n"
             "Сайт: http://www.iseu.bsu.by/institut/structura/fyem/\n"
             "<b>Эколог-эксперт</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "Химия (ЦТ)\n"
             "\n"
             "<b>Биолог-аналитик. Преподаватель биологии</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "Химия (ЦТ)\n"
             "\n"
             "<b>Эколог-эксперт</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "Химия (ЦТ)\n"
             "\n"
             "<b>Биолог-аналитик. Преподаватель биологии</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "Химия (ЦТ)\n"
             "\n"
             "<b>Эколог-эксперт</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "Химия (ЦТ)\n"
             "\n"
             "<b>Эколог-эксперт</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "Химия (ЦТ)\n"
             "\n"
             "<b>Эколог-эксперт</b>\n"
             "Время обучения: 3,5 года\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусско-Российский университет - ЭЛЕКТРОТЕХНИЧЕСКИЙ ФАКУЛЬТЕТ")
async def check_68(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусско-Российский университет - ЭЛЕКТРОТЕХНИЧЕСКИЙ ФАКУЛЬТЕТ</b>\n"
             "Декан <i>Болотов Сергей Владимирович</i>\n"
             "Телефон: 8(0222)31-06-26\n"
             "Сайт: \n"
             "<b>Инженер по информационным технологиям</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный технологический университет - Факультет химической технологии и техники")
async def check_69(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Факультет химической технологии и техники</b>\n"
             "Декан <i>Климош Юрий Александрович </i>\n"
             "Телефон: +37517363-58-38\n"
             "Сайт: https://www.belstu.by/faculties/htit.htmlhttp://htit.muzklip.com/\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "математика (ЦТ),\n"
             "физика (ЦТ),\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Факультет инфокоммуникаций")
async def check_70(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Факультет инфокоммуникаций</b>\n"
             "Декан <i>Дробот Сергей Викторович</i>\n"
             "Телефон: (017)293-85-65\n"
             "Сайт: https://www.bsuir.by/ru/fik\n"
             "Инфокоммуникационные технологии (системы телекоммуникаций)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (сети инфокоммуникаций)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (цифровое теле- и радиовещание)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (системы распределения мультимедийной информации)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные системы (стандартизация, сертификация и контроль параметров)\n"
             "<b>Инженер по стандартизации,сертификации и контролю параметров инфокоммуникационных систем</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Специалист по защите информации,Инженер по телекоммуникациям</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (системы телекоммуникаций)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (сети инфокоммуникаций)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (цифровое теле- и радиовещание)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (системы распределения мультимедийной информации)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные системы (стандартизация, сертификация и контроль параметров)\n"
             "<b>Инженер по стандартизации,сертификации и контролю параметров инфокоммуникационных систем</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Специалист по защите информации,Инженер по телекоммуникациям</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (сети инфокоммуникаций)\n"
             "<b></b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (сети инфокоммуникаций)\n"
             "<b></b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Филологический факультет")
async def check_71(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Филологический факультет</b>\n"
             "Декан <i>Старичёнок Василий Денисович</i>\n"
             "Телефон: 227-80-09200-84-85\n"
             "Сайт: \n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский язык (ЦТ)\n"
             "первое профильное испытание: белорусская литература (письменно)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский язык (ЦТ)\n"
             "первое профильное испытание: русская литература (писменно)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский язык (ЦТ)\n"
             "первое профильное испытание: белорусская литература (письменно)\n"
             "второе профильное испытание: английский язык (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский язык (ЦТ)\n"
             "первое профильное испытание: русская литература (письменно)\n"
             "второе профильное испытание: английский язык (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский язык (ЦТ)\n"
             "первое профильное испытание: белорусская литература (письменно)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский язык (ЦТ)\n"
             "первое профильное испытание: русская литература (писменно)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский язык (ЦТ)\n"
             "первое профильное испытание: белорусская литература (письменно)\n"
             "второе профильное испытание: английский язык (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский язык (ЦТ)\n"
             "первое профильное испытание: русская литература (письменно)\n"
             "второе профильное испытание: английский язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Академия Министерства внутренних дел Республики Беларусь - Факультет повышения квалификации и переподготовки руководящих кадров")
async def check_72(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Академия Министерства внутренних дел Республики Беларусь - Факультет повышения квалификации и переподготовки руководящих кадров</b>\n"
             "Начальник факультета <i>ЛОМОТЬ Иван Викторович</i>\n"
             "Телефон: (017)289-22-50\n"
             "Сайт: \n"
             "Оперативно-розыскная деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "На базе высшего неюридического образования\n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Административно-правовая деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "- На базе высшего неюридического образования белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "- На базе высшего неюридического образования белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Академия Министерства внутренних дел Республики Беларусь - Факультет милиции")
async def check_73(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Академия Министерства внутренних дел Республики Беларусь - Факультет милиции</b>\n"
             "Начальник факультета <i>ХАНЦЕВИЧ Дмитрий Витальевич</i>\n"
             "Телефон: (017)289-22-23\n"
             "Сайт: \n"
             "Оперативно-розыскная деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Административно-правовая деятельность\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Оперативно-розыскная деятельность\n"
             "<b>Юрист со знанием экономики</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный медицинский университет - Лечебный факультет")
async def check_74(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Лечебный факультет</b>\n"
             "Декан <i>Волотовский Алексей Игоревич</i>\n"
             "Телефон: 8(017)27711688(017)2771759\n"
             "Сайт: http://www.bsmu.by/page/6/92/\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет социокультурных коммуникаций")
async def check_75(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет социокультурных коммуникаций</b>\n"
             "Декан <i>Прохоренко Олеся Геннадьевна </i>\n"
             "Телефон: (+375-17)209-59-11\n"
             "Сайт: http://www.bsu.by/ru/main.aspx?guid=4781\n"
             "Дизайн (предметно-пространственной среды)\n"
             "<b>Дизайнер</b>\n"
             "Менеджмент (социально-административный)\n"
             "<b>Менеджер-экономист</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусская государственная академия музыки - Фортепианный и композиторско-музыковедческий факультет")
async def check_76(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия музыки - Фортепианный и композиторско-музыковедческий факультет</b>\n"
             "Декан <i>Коротина Наталья Аркадьевна</i>\n"
             "Телефон: +37517282-06-53\n"
             "Сайт: \n"
             "<b>Композитор. Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "ЦТ, ЭУО\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Агрономический факультет")
async def check_77(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Агрономический факультет</b>\n"
             "Декан <i>Дуктова Наталья Александровна</i>\n"
             "Телефон: 8022337-96-07,7-96-25\n"
             "Сайт: http://baa.by/facultet/agronom/\n"
             "<b>Агроном</b>\n"
             "Время обучения: 4 г. \n"
             "Вступительные испытания: \n"
             "биология (ЦТ или ЭУО), \n"
             "химия (ЦТ или ЭУО)\n"
             "\n"
             "<b>Агроном</b>\n"
             "Время обучения: 5 лет \n"
             "Вступительные испытания: \n"
             "биология (ЦТ или ЭУО)\n"
             "химия (ЦТ или ЭУО)\n"
             "\n"
             "<b>Агроном</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "растениеводство (ЭУО),\n"
             "земледелие (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный технологический университет - Лесохозяйственный факультет")
async def check_78(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Лесохозяйственный факультет</b>\n"
             "Декан <i>Ярмолович Василий Александрович</i>\n"
             "Телефон: +37517379-74-52\n"
             "Сайт: https://www.belstu.by/faculties/lh.htmlhttps://lh.belstu.by/?_ga=2.197766955.584529427.1558331120-1670493189.15...\n"
             "<b>Инженер лесного хозяйства</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер садово-паркового строительства</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Специалист по туризму и природопользованию</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физическая культура и спорт (ЭУО)\n"
             "биология (ЦТ)\n"
             "\n"
             "<b>Инженер лесного хозяйства</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер садово-паркового строительства</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Специалист по туризму и природопользованию</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физическая культура и спорт (ЭУО)\n"
             "биология (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет - Институт теологии имени святых Мефодия и Кирилла БГУ")
async def check_79(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Институт теологии имени святых Мефодия и Кирилла БГУ</b>\n"
             "Ректор <i>Митрополит Минский и Заславский Павел (Пономарев Георгий Васильевич)</i>\n"
             "Телефон: (+375-17)289-11-61(+375-17)220-23-55\n"
             "Сайт: www.inst.by\n"
             "<b>Теолог-религиовед,Преподаватель обществоведческих дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Теолог-религиовед,Преподаватель обществоведческих дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия искусств - Факультет экранных искусств")
async def check_80(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия искусств - Факультет экранных искусств</b>\n"
             "Декан <i>Иванов Павел Владимирович </i>\n"
             "Телефон: \n"
             "Сайт: http://bdam.by/деканат-факультета-экранных-искусст/\n"
             "Кинотелеоператорство (кинооператорство)\n"
             "<b>Кинооператор</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Машиностроительный факультет")
async def check_81(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Машиностроительный факультет</b>\n"
             "Декан <i>Сафонов Андрей Иванович</i>\n"
             "Телефон: 292-41-01292-94-07деканатдневногоотделения292-85-10деканатзаочногоотделения\n"
             "Сайт: http://www.bntu.by/msf.html\n"
             "Экономика и организация производства (машиностроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "Экономика и организация производства (приборостроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Иностранный язык (ЦТ) - 15\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Автоматизация технологических процессов и производств (машиностроение и приборостроение)\n"
             "<b>Инженер по автоматизации</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по интеллектуальным системам</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4,5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Экономика и организация производства (машиностроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "Экономика и организация производства (приборостроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Иностранный язык (ЦТ) - 15\n"
             "\n"
             "Экономика и организация производства (машиностроение)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Экономика организации (ПЭ)\n"
             "2. Основы менеджмента (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Приборостроительный факультет")
async def check_82(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Приборостроительный факультет</b>\n"
             "Декан <i>Александр Иванович Свистун</i>\n"
             "Телефон: 292-72-55292-67-93\n"
             "Сайт: http://www.bntu.by/psf.html\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-технолог</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "Метрология, стандартизация и сертификация (по направлениям)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электроник</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Основы электротехники (ПЭ)\n"
             "2. Основы инженерной графики (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Военная академия Республики Беларусь - Военной разведки")
async def check_83(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Военной разведки</b>\n"
             "Начальник факультета <i>Борисик Сергей Алексеевич</i>\n"
             "Телефон: (017)287-43-60\n"
             "Сайт: \n"
             "<b>Специалист по управлению со знанием иностранных языков</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Специалист по управлению со знанием иностранных языков</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Специалист по управлению-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Специалист по управлению со знанием иностранных языков</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Телекоммуникационные системы (радиоэлектронная борьба)\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Телекоммуникационные системы (радиоэлектронная разведка)\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Телекоммуникационные системы (радиоэлектронная разведка) в интересах Государственного пограничного комитета\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер. Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет культуры и искусств - Факультет информационно-документных коммуникаций")
async def check_84(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет культуры и искусств - Факультет информационно-документных коммуникаций</b>\n"
             "Декан <i>Галковская Юлия Николаевна</i>\n"
             "Телефон: +375172555307\n"
             "Сайт: http://www.buk.by/process/fakultet%204/\n"
             "<b>Библиотекарь-библиограф</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Библиотекарь-библиограф</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Библиотечно-информационная деятельность (менеджмент)\n"
             "<b>Менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Музейное дело и охрана историко-культурного наследия (культурное наследие и туризм)\n"
             "<b>Менеджер по культурному наследию и туризму</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Всемирная история (новейшее время) (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Библиотечно-информационная деятельность (менеджмент)\n"
             "<b>Менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Библиотекарь-библиограф</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "библиотековедение (устный экзамен);\n"
             "библиография (устный экзамен)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет радиофизики и компьютерных технологий")
async def check_85(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет радиофизики и компьютерных технологий</b>\n"
             "Декан <i>Ушаков Дмитрий Владимирович </i>\n"
             "Телефон: +375(17)209-59-03\n"
             "Сайт: www.rfe.by\n"
             "Прикладная информатика (информационные технологии телекоммуникационных систем)\n"
             "<b>Информатик,Специалист по информационным технологиям телекоммуникационных систем</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Радиофизик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Физик-инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Радиофизик,Специалист по аэрокосмическим радиоэлектронным и информационным системам и технологиям</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Компьютерная безопасность (радиофизические методы и программно-технические средства)\n"
             "<b>Специалист по защите информации,Радиофизик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Прикладная информатика (информационные технологии телекоммуникационных систем)\n"
             "<b>Информатик,Специалист по информационным технологиям телекоммуникационных систем</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный технологический университет - Факультет технологии органических веществ")
async def check_86(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Факультет технологии органических веществ</b>\n"
             "Декан <i>Радченко Юрий Сергеевич</i>\n"
             "Телефон: +37517363-26-58\n"
             "Сайт: https://www.belstu.by/faculties/tov.htmlhttps://tov.belstu.by/?_ga=2.231525019.584529427.1558331120-1670493189.1...\n"
             "<b>Инженер-химик-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-химик-технолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-химик-технолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер по сертификации</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-химик-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-химик-технолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-химик-технолог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер по сертификации</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет пищевых и химических технологий - Химико-технологический факультет")
async def check_87(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет пищевых и химических технологий - Химико-технологический факультет</b>\n"
             "Декан <i>Шкабров Олег Владимирович</i>\n"
             "Телефон: 8(0222)63-35-41\n"
             "Сайт: http://bgut.by/faculty-htf/\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Факультет дошкольного образования")
async def check_89(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Факультет дошкольного образования</b>\n"
             "Декан <i>Анцыпирович Ольга Николаевна</i>\n"
             "Телефон: 340-95-95(декан)341-39-18(деканат)\n"
             "Сайт: www.fdo.bspu.by/\n"
             "<b>Педагог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: биология (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог</b>\n"
             "Время обучения: 3 года 6 месяцев\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: педагогика (устно)\n"
             "второе профильное испытание: психология (устно)\n"
             "\n"
             "<b>Педагог</b>\n"
             "Время обучения: 3 года 6 месяцев\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: педагогика (Устно)\n"
             "второе профильное испытание: психология (устно)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Факультет физического воспитания")
async def check_90(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Факультет физического воспитания</b>\n"
             "Декан <i>Касперович Александр Николаевич</i>\n"
             "Телефон: 227-49-74\n"
             "Сайт: \n"
             "Физкультурно-оздоровительная и туристско-рекреационная деятельность\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Физическая культура (лечебная)\n"
             "<b>Инструктор-методист по лечебной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Оздоровительная и адаптивная физическая культура (оздоровительная)\n"
             "<b>Инструктор-методист по оздоровительной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (спортивная режиссура)\n"
             "<b>Менеджер-режиссер спортивно-массовых мероприятий,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Спортивно-туристская деятельность (менеджмент в туризме)\n"
             "<b>Менеджер по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Физкультурно-оздоровительная и туристско-рекреационная деятельность\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Физическая культура (лечебная)\n"
             "<b>Инструктор-методист по лечебной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Оздоровительная и адаптивная физическая культура (оздоровительная)\n"
             "<b>Инструктор-методист по оздоровительной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (спортивная режиссура)\n"
             "<b>Менеджер-режиссер спортивно-массовых мероприятий,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Спортивно-туристская деятельность (менеджмент в туризме)\n"
             "<b>Менеджер по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: физическая культура\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Оздоровительная и адаптивная физическая культура (оздоровительная)\n"
             "<b>Инструктор-методист по оздоровительной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: физическая культура;\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
             "Спортивно-туристская деятельность (менеджмент в туризме)\n"
             "<b>Менеджер по туризму,Преподаватель физической культуры</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: физическая культура;\n"
             "второе профильное испытание: биология (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный экономический университет - Факультет международных бизнес-коммуникаций")
async def check_91(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Факультет международных бизнес-коммуникаций</b>\n"
             "Декан <i>Мишкевич Михаил Вацлавович</i>\n"
             "Телефон: 209-78-55-МишкевичМихаилВацлавович,декан229-12-99-ГончаровРусланЕгорович,заместительдекана209-78-68-курсыиностранногоязыка209-78-65-методистыдеканата\n"
             "Сайт: http://fmbk.bseu.by/\n"
             "Лингвистическое обеспечение межкультурных коммуникаций (внешнеэкономические связи) \n"
             "<b>Специалист по межкультурным коммуникациям,Переводчик-референт (с указанием языков общения)</b>\n"
             "Время обучения: 4,5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "Лингвистическое обеспечение межкультурных коммуникаций (внешнеэкономические связи) \n"
             "<b>Специалист по межкультурным коммуникациям,Переводчик-референт (с указанием языков общения)</b>\n"
             "Время обучения: 4,5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный экономический университет - Факультет права")
async def check_92(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Факультет права</b>\n"
             "Декан <i>Шкляревский Александр Николаевич</i>\n"
             "Телефон: 209-79-52-ШкляревскийАлександрНиколаевич,декан209-79-49-зам.декана209-79-65-специалистДФО209-79-63-специалистЗФО\n"
             "Сайт: http://pravo.bseu.by/\n"
             "<b>Юрист</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет физической культуры - Факультет оздоровительной физической культуры")
async def check_93(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет физической культуры - Факультет оздоровительной физической культуры</b>\n"
             "Декан <i>Машарская Наталия Михайловна</i>\n"
             "Телефон: 8(017)3745344\n"
             "Сайт: \n"
             "Физическая культура (лечебная)\n"
             "<b>Инструктор-методист по лечебной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Физическая культура (дошкольников)\n"
             "<b>Инструктор-методист физического воспитания в дошкольных учреждениях,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Оздоровительная и адаптивная физическая культура (оздоровительная)\n"
             "<b>Инструктор-методист по оздоровительной физической культуре,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "общая физическая подготовка (ВЭ)\n"
             "\n"
             "Оздоровительная и адаптивная физическая культура (адаптивная)\n"
             "<b>Инструктор-методист по адаптивной физической культуре,Преподаватель физической культуры</b>\n"
             "\n"
             "Физическая культура (дошкольников)\n"
             "<b>Инструктор-методист физического воспитания в дошкольных учреждениях,Преподаватель физической культуры</b>\n"
             "Время обучения: \n"
             "Вступительные испытания: \n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Экономический факультет")
async def check_94(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Экономический факультет</b>\n"
             "Декан <i>Шафранская  Ирина Викторовна</i>\n"
             "Телефон: 8022337-96-37\n"
             "Сайт: http://baa.by/facultet/ekfac/\n"
             "Управление внешнеэкономической деятельностью\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Математика ЦТ\n"
             "Иностранный язык ЦТ\n"
             "Белорусский (русский) язык ЦТ\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО),\n"
             "иностранный язык (ЦТ или ЭУО)\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "основы менеджмента (ЭУО),\n"
             "экономика организации (ЭУО)\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 5 лет \n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО),\n"

             "иностранный язык (ЦТ или ЭУО)\n"
             "\n"
             "<b>Экономист-организатор</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "основы менеджмента (ЭУО),\n"
             "экономика организации (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Военная академия Республики Беларусь - Внутренних войск")
async def check_95(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Внутренних войск</b>\n"
             "Начальник факультета <i>Жизневский Владимир Иосифович</i>\n"
             "Телефон: (017)2657402\n"
             "Сайт: \n"
             "<b>Специалист по управлению-юрист</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет транспорта - Электротехнический факультет")
async def check_96(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Электротехнический факультет</b>\n"
             "Декан <i>Сатырёв Фёдор Ефимович</i>\n"
             "Телефон: (0232)953207\n"
             "Сайт: http://bsut.by/obrazovanie/fakultety/elektrotehnicheskii.html\n"
             "Автоматика и телемеханика\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Системы передачи и распределения информации\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Микропроцессорные информационно-управляющие системы\n"
             "<b>Инженер-электрик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет прикладной математики и информатики")
async def check_97(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет прикладной математики и информатики</b>\n"
             "Декан <i>Недзьведь Александр Михайлович </i>\n"
             "Телефон: (+375-17)209-52-45(+375-17)209-54-44\n"
             "Сайт: www.fpmi.bsu.by\n"
             "Прикладная математика (научно-производственная деятельность)\n"
             "<b>Математик-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Математик – системный программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Математик-финансист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Экономическая кибернетика (математические методы и компьютерное моделирование в экономике)\n"
             "<b>Математик-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Прикладная информатика (программное обеспечение компьютерных систем)\n"
             "<b>Информатик,Специалист по разработке программного обеспечения</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Компьютерная безопасность (математические методы и программные системы)\n"
             "<b>Специалист по защите информации,Математик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Прикладная математика (научно-производственная деятельность)\n"
             "<b>Математик-программист</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования")
async def check_98(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Факультет компьютерного проектирования</b>\n"
             "Декан <i>Лихачевский Дмитрий Викторович</i>\n"
             "Телефон: (017)293-85-83\n"
             "Сайт: http://www.bsuir.by/ru/fkp\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-проектировщик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по электронным системам</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в обеспечении промышленной безопасности)\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в бизнес-менеджменте)\n"
             "<b>Программист,Бизнес-аналитик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-проектировщик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по электронным системам</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в обеспечении промышленной безопасности)\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в бизнес-менеджменте)\n"
             "<b>Программист,Бизнес-аналитик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-электроник-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по электронным системам</b>\n"
             "Время обучения: 3,5 года\n"
             "Вступительные испытания: \n"
             "Основы информационных технологий (ПЭ),\n"
             "Охрана труда. Охрана окружающей среды и энергосбережение (ПЭ)\n"
             "\n"
             "<b>Инженер по электронным системам</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в бизнес-менеджменте)\n"
             "<b>Программист,Бизнес-аналитик</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный экономический университет - Учетно-экономический факультет")
async def check_99(message: types.Message,
                   state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Учетно-экономический факультет</b>\n"
             "Декан <i>В.А. Березовский</i>\n"
             "Телефон: 209-78-24–БерезовскийВладимирАнтонович,декан209-78-20–БуевАндрейЛеонидович,зам.декана(дневнаяформаобучения)209-78-25–СмоляковаОльгаМечеславовна,зам.декана(заочнаяформаобучения)\n"
             "Сайт: \n"
             "Бухгалтерский учет, анализ и аудит (в бюджетных организациях)\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Бухгалтерский учет, анализ и аудит (в коммерческих и некоммерческих организациях)\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Бухгалтерский учет, анализ и аудит (в бюджетных организациях)\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Бухгалтерский учет, анализ и аудит (в коммерческих и некоммерческих организациях)\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Бухгалтерский учет, анализ и аудит (в коммерческих и некоммерческих организациях)\n"
             "<b>Экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Бухгалтерский учет, анализ и аудит (в бюджетных организациях)\n"
             "<b>Экономист</b>\n"
             "Время обучения: 3,5\n"
             "Вступительные испытания: \n"
             "экономика организации (ЭУО)\n"
             "бухгалтерский учет (ЭУО)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет географии и геоинформатики")
async def check_100(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет географии и геоинформатики</b>\n"
             "Декан <i>Курлович Дмитрий Мирославович</i>\n"
             "Телефон: (+375-17)209-52-57\n"
             "Сайт: www.geo.bsu.by\n"
             "<b></b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "география (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "География (геодемография)\n"
             "<b>Географ. Геодемограф</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Факультет эстетического образования")
async def check_101(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Факультет эстетического образования</b>\n"
             "Декан <i>Рыжикова Ирина Ивановна</i>\n"
             "Телефон: 267-91-05\n"
             "Сайт: https://faest.bspu.by\n"
             "<b>Педагог-художник. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (рисунок);\n"
             "второе творческое испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-художник. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (рисунок);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-музыкант. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (исполнительское мастерство);\n"
             "второе творческое испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (исполнительское мастерство);\n"
             "второе творческое испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-художник. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (рисунок);\n"
             "второе творческое испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-художник. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (рисунок);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-музыкант. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (исполнительское мастерство);\n"
             "второе творческое испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (исполнительское мастерство);\n"
             "второе творческое испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-художник. Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "русский (белорусский) язык (ЦТ);\n"
             "первое профильное испытание: творчество (рисунок);\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Педагог-музыкант. Преподаватель</b>\n"
             "Время обучения: 3.6 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: творчество (элементарная теория музыки)\n"
             "Второе профильное испытание: творчество (исполнительское мастерство: по направлениям)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет международных отношений")
async def check_102(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет международных отношений</b>\n"
             "Декан <i>Достанко Елена Анатольевна</i>\n"
             "Телефон: (+375-17)209-59-77\n"
             "Сайт: www.fir.bsu.by\n"
             "<b>Специалист по международным отношениям,Переводчик-референт (с указанием языков общения)</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Переводчик-референт (с указанием языков общения),Востоковед-международник</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист-международник со знанием иностранных языков (с указанием языков общения)</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Менеджмент (в сфере международного туризма)\n"
             "<b>Менеджер-экономист,Переводчик-референт   (с указанием двух иностранных языков)</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Специалист таможенного дела</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Специалист по международным отношениям,Переводчик-референт (с указанием языков общения)</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Переводчик-референт (с указанием языков общения),Востоковед-международник</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "\n"
             "<b>Юрист-международник со знанием иностранных языков (с указанием языков общения)</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский государственный лингвистический университет - Факультет китайского языка и культуры")
async def check_103(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Минский государственный лингвистический университет - Факультет китайского языка и культуры</b>\n"
             "Декан <i>Олейник Сергей Евгеньевич</i>\n"
             "Телефон: 288-22-15\n"
             "Сайт: http://fes.mslu.by/\n"
             "Современные иностранные языки (преподавание): Китайский язык (на базе  китайского/английского языка) и второй иностранный  язык  со  специализацией: компьютерная лингвистика,  русский язык как иностранный.\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Китайский / Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (перевод): Китайский язык (на базе китайского/английского языка) и второй иностранный язык со специализацией: специальный перевод.\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусская государственная академия искусств - Факультет дизайна и декоративно-прикладного искусства")
async def check_104(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия искусств - Факультет дизайна и декоративно-прикладного искусства</b>\n"
             "Декан <i>Свентоховский Всеволод Петрович</i>\n"
             "Телефон: (017)2927734\n"
             "Сайт: http://bdam.by/деканат-факультета-дизайна-и-декорат/\n"
             "Декоративно-прикладное искусство (изделия из керамики)\n"
             "<b>Художник декоративно-прикладного искусства,Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (академический рисунок, живопись/скульптура, композиция)\n"
             "\n"
             "Декоративно-прикладное искусство (изделия из керамики)\n"
             "<b>Художник декоративно-прикладного искусства,Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Военная академия Республики Беларусь - Общевойсковой")
async def check_105(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Военная академия Республики Беларусь - Общевойсковой</b>\n"
             "Начальник факультета <i>Неверко Артем Валентинович</i>\n"
             "Телефон: (017)2874187\n"
             "Сайт: \n"
             "<b>Специалист по управлению-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Специалист по управлению-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Тыловое обеспечение войск (горюче-смазочными материалами) в интересах Государственного пограничного комитета\n"
             "<b>Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Тыловое обеспечение войск (горюче-смазочными материалами)\n"
             "<b>Специалист по управлению</b>\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Исторический факультет")
async def check_106(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Исторический факультет</b>\n"
             "Декан <i>Касович Александр Валерьевич</i>\n"
             "Телефон: 226-40-26\n"
             "Сайт: \n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "Второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "Второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "Второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "Второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "Второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "Первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "Второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "первое профильное испытание: всемирная история новейшего времени (ЦТ)\n"
             "второе профильное испытание: история Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный педагогический университет им. Максима Танка - Институт инклюзивного образования")
async def check_107(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный педагогический университет им. Максима Танка - Институт инклюзивного образования</b>\n"
             "директор Института инклюзивного образования <i>Хитрюк Вера Валерьевна</i>\n"
             "Телефон: (017) 311-23-57(017) 267 97 73\n"
             "Сайт: http://iio.bspu.by\n"
             "<b>Учитель-логопед.  Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "биология (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия авиации - Факультет гражданской авиации")
async def check_108(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия авиации - Факультет гражданской авиации</b>\n"
             "Декан факультета <i>Машарский Захар Владимирович</i>\n"
             "Телефон: (017)2421442\n"
             "Сайт: https://bgaa.by/obrazovanie/fakultet-grazhdanskoy-aviaciihttps://abiturient.bgaa.by/node/fakultet-grazhdanskoy-aviacii\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Техническая эксплуатация авиационного оборудования (приборное и электросвето-техническое оборудование)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "Техническая эксплуатация авиационного оборудования (радиоэлектронное оборудование)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "1] Техническая эксплуатация беспилотных авиационных комплексов\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Специалист по летной эксплуатации гражданских судов. Инженер-пилот</b>\n"
             "Время обучения: 4.5 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "математика (ЦТ),\n"
             "английский язык (ЦТ),\n"
             "определение уровня физической подготовленности\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 3,5 года\n"
             "Вступительные испытания: \n"
             "Электротехника с основами электроники - устный экзамен\n"
             "Техническая механика - устный экзамен\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 3,5 года\n"
             "Вступительные испытания: \n"
             "Электротехника с основами электроники - устный экзамен\n"
             "Техническая механика - устный экзамен\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет транспорта - Факультет экономики и бизнес-технологий")
async def check_109(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Факультет экономики и бизнес-технологий</b>\n"
             "Декан <i>Шиболович Валерия Валерьевна</i>\n"
             "Телефон: (0232)775560(0232)952171\n"
             "Сайт: https://bsut.by/university/faculties/gef\n"
             "4] Бухгалтерский учет, анализ и аудит на предприятии транспорта\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в бизнес-менеджменте)\n"
             "<b>Программист,Бизнес-аналитик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Экономическое обеспечение таможенной деятельности\n"
             "<b>Специалист таможенного дела</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "4] Бухгалтерский учет, анализ и аудит на предприятии транспорта\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в бизнес-менеджменте)\n"
             "<b>Программист,Бизнес-аналитик</b>\n"
             "Время обучения: 4 года \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Экономическое обеспечение таможенной деятельности\n"
             "<b>Специалист таможенного дела</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Агроэкологический факультет")
async def check_110(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Агроэкологический факультет</b>\n"
             "Декан <i>Какшинцев Андрей Васильевич</i>\n"
             "Телефон: 8022337-96-91,7-96-23\n"
             "Сайт: http://baa.by/facultet/agroek/\n"
             "<b>Агроном</b>\n"
             "Время обучения: 4 г. \n"
             "Вступительные испытания: \n"
             "биология (ЦТ или ЭУО),\n"
             "химия (ЦТ или ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Землеустроительный факультет")
async def check_111(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Землеустроительный факультет</b>\n"
             "Декан <i>ПИСЕЦКАЯ Ольга Николаевна</i>\n"
             "Телефон: 8022337-96-44,7-96-56\n"
             "Сайт: \n"
             "<b>Инженер-землеустроитель</b>\n"
             "Время обучения: 4.5 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4.5 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-землеустроитель</b>\n"
             "Время обучения: 4 г. \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 г. \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-землеустроитель</b>\n"
             "Время обучения: 5 лет \n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный медицинский университет - Военно-медицинский институт")
async def check_112(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Военно-медицинский институт</b>\n"
             "Начальник <i>Богдан Василий Генрихович</i>\n"
             "Телефон: 8(017)379-23-188(017)270-23-39\n"
             "Сайт: http://www.bsmu.by/page/6/218/\n"
             "Военно-медицинское дело (для Вооруженных сил Республики Беларусь)\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Военно-медицинское дело (для Внутренних войск)\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Военно-медицинское дело (для Государственного пограничного комитета Республики Беларусь)\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "Военно-медицинское дело (для Министерства внутренних дел Республики Беларусь)\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия связи - Факультет инжиниринга и технологий связи")
async def check_113(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия связи - Факультет инжиниринга и технологий связи</b>\n"
             "Декан <i>Будник Артур Владимирович</i>\n"
             "Телефон: +37517272-96-07-Декан+37517272-96-58-Деканат\n"
             "Сайт: http://bsac.by/lp/fakultet-inziniringa-i-tehnologii-svazi\n"
             "Маркетинг на предприятиях связи, полный срок получения образования, для выпускников 11 классов (бюджет)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 3 года 10 месяцев\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Прикладная информатика (информационные технологии телекоммуникационных систем), полный срок получения образования, для выпускников 11 классов (бюджет)\n"
             "<b>Информатик,Специалист по информационным технологиям телекоммуникационных систем</b>\n"
             "Время обучения: 3 года 10 мес.\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика - (ЦТ)\n"
             "математика - (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (сети инфокоммуникаций), полный срок получения образования, для выпускников 11 классов (бюджет)\n"
             "<b></b>\n"
             "Время обучения: 3 года 10 месяцев\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика - (ЦТ)\n"
             "математика - (ЦТ)\n"
             "\n"
             "<b>Инженер почтовой связи</b>\n"
             "Время обучения: 2 года 10 месяцев\n"
             "Вступительные испытания: \n"
             "математика (П) ЭУО\n"
             "основы информационных технологий (П) ЭУО\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Университет гражданской защиты Министерства по чрезвычайным ситуациям Республики Беларусь - Факультет техносферной безопасности")
async def check_114(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Университет гражданской защиты Министерства по чрезвычайным ситуациям Республики Беларусь - Факультет техносферной безопасности</b>\n"
             "Начальник факультета <i>Бородако Андрей Владимирович</i>\n"
             "Телефон: (017)341-77-22\n"
             "Сайт: \n"
             "<b>Инженер по пожарной и промышленной безопасности</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер по пожарной и промышленной безопасности</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Академия управления при Президенте Республики Беларусь - Институт управленческих кадров")
async def check_115(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Академия управления при Президенте Республики Беларусь - Институт управленческих кадров</b>\n"
             "Директор <i>Ящук Анна Иосифовна</i>\n"
             "Телефон: +375(17)229-51-05\n"
             "Сайт: \n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист информационных систем</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист информационных систем</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный технологический университет - Факультет принттехнологий и медиакоммуникаций")
async def check_116(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Факультет принттехнологий и медиакоммуникаций</b>\n"
             "Декан <i>Долгова Татьяна Александровна</i>\n"
             "Телефон: +37517379-71-98\n"
             "Сайт: https://www.belstu.by/faculties/idip.htmlhttps://pim.belstu.by/?_ga=2.196199080.584529427.1558331120-1670493189.1...\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Редактор-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-электромеханик</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Редактор-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-технолог</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "химия (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="БГАТУ - Агромеханический факультет")
async def check_117(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>БГАТУ - Агромеханический факультет</b>\n"
             "Декан <i>Ловкис Виктор Болеславович</i>\n"
             "Телефон: 373-44-13\n"
             "Сайт: http://www.bsatu.by/ru/fakultety/agromehanicheskiy-fakultet\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), физика (ЦТ или ЭУО)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "тракторы (ЭУО), сельскохозяйственные машины (ЭУО)\n"
             "\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), физика (ЦТ или ЭУО)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "тракторы (ЭУО), сельскохозяйственные машины (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский государственный лингвистический университет - Факультет немецкого языка")
async def check_118(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Минский государственный лингвистический университет - Факультет немецкого языка</b>\n"
             "Декан <i>Фурашова Наталья Владимировна</i>\n"
             "Телефон: +375172848131\n"
             "Сайт: http://fde.mslu.by/\n"
             "Современные иностранные языки (преподавание): Немецкий язык (на базе немецкого  языка / английского языка)  и  второй иностранный  язык со специализацией:  компьютерная лингвистика, риторика, зарубежная лит.\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Немецкий язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Современные иностранные языки (преподавание): Немецкий  язык  (на базе немецкого  языка / английского языка)  и  второй иностранный  язык со специализацией:  компьютерная лингвистика, риторика, зарубежная лит.\n"
             "<b>Лингвист,Преподаватель двух иностранных языков (с указанием языков)</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Английский язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Немецкий язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Немецкий язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет информатики и радиоэлектроники - Военный факультет")
async def check_119(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Военный факультет</b>\n"
             "начальник факультета <i>Кулешов Юрий Евгеньевич</i>\n"
             "Телефон: 293-23-14293-80-31\n"
             "Сайт: http://www.bsuir.by/ru/vf\n"
             "Радиотехника (специальные системы радиолокации и радионавигации)\n"
             "<b>Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Вычислительные системы и сети специального назначения\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные технологии (системы телекоммуникаций специального назначения)\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Инфокоммуникационные системы (стандартизация, сертификация и контроль параметров)\n"
             "<b>Инженер по стандартизации,сертификации и контролю параметров инфокоммуникационных систем</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет журналистики")
async def check_120(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет журналистики</b>\n"
             "декан <i>Самусевич Ольга Михайловна</i>\n"
             "Телефон: (+375-17)259-70-50(+375-17)259-70-14\n"
             "Сайт: www.journ.bsu.by\n"
             "<b>Специалист по информации и коммуникации</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "Журналистика (печатные СМИ)\n"
             "<b>Журналист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (1 этап — творческое сочинение, 2 этап — творческое тестирование)(ЭВ)\n"
             "\n"
             "<b>Специалист по информации и коммуникации</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "обществоведение (ЦТ)\n"
             "история Беларуси (ЦТ)\n"
             "\n"
             "Журналистика (печатные СМИ)\n"
             "<b>Журналист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ),\n"
             "история Беларуси (ЦТ),\n"
             "творчество (1 этап — творческое сочинение, 2 этап — творческое тестирование)(ЭВ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет физической культуры - Спортивно-педагогический факультет массовых видов спорта")
async def check_121(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет физической культуры - Спортивно-педагогический факультет массовых видов спорта</b>\n"
             "Декан <i>Гуслистова Ирина Иосифовна</i>\n"
             "Телефон: 8(017)3053279\n"
             "Сайт: \n"
             "Спортивно-педагогическая деятельность (тренерская работа с указанием вида спорта)\n"
             "<b>Тренер (по виду спорта),Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "физическая культура (ПИ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (спортивная психология)\n"
             "<b>Психолог,Преподаватель физической культуры</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "физическая культура (ПИ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (спортивная режиссура)\n"
             "<b>Менеджер-режиссер спортивно-массовых мероприятий,Преподаватель физической культуры</b>\n"
             "\n"
             "Спортивно-педагогическая деятельность (тренерская работа с указанием вида спорта)\n"
             "<b>Тренер (по виду спорта),Преподаватель физической культуры</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "физическая культура (ПИ)\n"
             "\n"
             "Спортивно-педагогическая деятельность (тренерская работа с указанием вида спорта)\n"
             "<b>Тренер (по виду спорта),Преподаватель физической культуры</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "физическая культура (ПИ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия музыки - Факультет народных инструментов")
async def check_122(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия музыки - Факультет народных инструментов</b>\n"
             "Декан <i>Корольчук Владимир Николаевич</i>\n"
             "Телефон: 37517355-69-50\n"
             "Сайт: \n"
             "Струнные народные щипково-ударные инструменты (гитара классическая, лютня)\n"
             "<b>Артист-инструменталист. Преподаватель</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "ЦТ, ЭУО\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский торгово-экономический университет потребительской кооперации - Факультет коммерции и финансов ")
async def check_123(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский торгово-экономический университет потребительской кооперации - Факультет коммерции и финансов </b>\n"
             "Декан <i>Астафьева Валентина Александровна</i>\n"
             "Телефон: +375(232)50-03-69-АстафьеваВалентинаАлександровна,декан+375(232)50-03-41-ВишневецкаяЛарисаВикторовна,зам.деканафакультета+375(232)50-03-41-специалистыдеканата\n"
             "Сайт: \n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "<b>Логистик-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "Информационные системы и технологии (в экономике)\n"
             "<b>Инженер-программист-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Физика (ЦТ).\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Экономика организации (ЭУО);\n"
             "Бухгалтерский учёт (ЭУО). \n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский государственный высший радиотехнический колледж - Профессионального образования")
async def check_124(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Минский государственный высший радиотехнический колледж - Профессионального образования</b>\n"
             "Декан <i>Сычева Юлия Сергеевна</i>\n"
             "Телефон: 292-26-61\n"
             "Сайт: \n"
             "Профессиональное обучение (радиоэлектроника)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (экономика и управление)\n"
             "<b>Педагог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (радиоэлектроника)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (экономика и управление)\n"
             "<b>Педагог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (радиоэлектроника)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (экономика и управление)\n"
             "<b>Педагог-экономист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (радиоэлектроника)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (экономика и управление)\n"
             "<b>Педагог-экономист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (радиоэлектроника)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (экономика и управление)\n"
             "<b>Педагог-экономист</b>\n"
             "Время обучения: 4года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (радиоэлектроника)\n"
             "<b>Педагог-инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
             "Профессиональное обучение (экономика и управление)\n"
             "<b>Педагог-экономист</b>\n"
             "Время обучения: 4года\n"
             "Вступительные испытания: \n"
             "Белорусский(русский) язык (ЦТ)\n"
             "Информационные технологии (письменно)\n"
             "Математика (письменно)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет транспорта - Военно-транспортный факультет")
async def check_125(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Военно-транспортный факультет</b>\n"
             "Декан <i>Поддубный Алексей Алексеевич</i>\n"
             "Телефон: (0232)774678(0232)953061(0232)775596\n"
             "Сайт: http://www.bsut.by/university/faculties/vtf\n"
             "Техническая эксплуатация автомобилей (военная автомобильная техника)\n"
             "<b>Инженер-механик,Специалист по управлению</b>\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный медицинский университет - Медико-профилактический факультет")
async def check_126(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Медико-профилактический факультет</b>\n"
             "Декан <i>Гиндюк Андрей Владимирович</i>\n"
             "Телефон: 8(017)2771756\n"
             "Сайт: http://www.bsmu.by/page/6/91/\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия авиации - Факультет военный")
async def check_127(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия авиации - Факультет военный</b>\n"
             "Проректор по государственной авиации -  Начальник военного факультета <i>Кульпанович Андрей Павлович</i>\n"
             "Телефон: (017)345-32-79\n"
             "Сайт: https://bgaa.by/obrazovanie/voennyy-fakultet\n"
             "1] Техническая эксплуатация беспилотных авиационных комплексов\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "\n"
             "2] Технологическая эксплуатация беспилотных авиационных комплексов\n"
             "<b></b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "\n"
             "<b>Инженер,Специалист по управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ).\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет биотехнологии и аквакультуры")
async def check_128(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Факультет биотехнологии и аквакультуры</b>\n"
             "Декан <i>Портной Александр  Иванович</i>\n"
             "Телефон: 8022337-96-78,7-96-29\n"
             "Сайт: http://baa.by/facultet/zoofac/\n"
             "<b>Зооинженер</b>\n"
             "Время обучения: 4 г. 6 мес.\n"
             "Вступительные испытания: \n"
             "биология (ЦТ или ЭУО),\n"
             "химия (ЦТ или ЭУО)\n"
             "\n"
             "<b>Зооинженер</b>\n"
             "Время обучения: 5 лет 6 мес\n"
             "Вступительные испытания: \n"
             "биология (ЦТ или ЭУО)\n"
             "химия (ЦТ или ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский национальный технический университет - Факультет горного дела и инженерной экологии")
async def check_129(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Факультет горного дела и инженерной экологии</b>\n"
             "Декан <i>КОЛОГРИВКО Андрей Андреевич</i>\n"
             "Телефон: 29271822927414\n"
             "Сайт: http://www.bntu.by/fgde.html\n"
             "<b></b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-эколог-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский торгово-экономический университет потребительской кооперации - Факультет экономики и управления")
async def check_130(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский торгово-экономический университет потребительской кооперации - Факультет экономики и управления</b>\n"
             "Декан <i>Лацкевич Наталья Васильевна</i>\n"
             "Телефон: +375(232)50-03-87-ЛацкевичНатальяВасильевна,декан+375(232)50-03-74-МаксименкоНиколайВасильевич,зам.деканапозаочнойформеполученияобразования+375(232)50-03-43-специалистыдеканатаочнойформы;50-03-58-специалистыдеканатазаочнойформы\n"
             "Сайт: \n"
             "<b>Юрист со знанием экономики</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Обществоведение (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "<b>Экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "Менеджмент (социально-административный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "<b>Экономист-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ);\n"
             "Математика (ЦТ);\n"
             "Иностранный язык (ЦТ).\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Экономика организации (ЭУО);\n"
             "Основы менеджмента (ЭУО). \n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="БГАТУ - Инженерно-технологический факультет")
async def check_131(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>БГАТУ - Инженерно-технологический факультет</b>\n"
             "Декан <i>Бренч Андрей Александрович</i>\n"
             "Телефон: 3433996\n"
             "Сайт: http://www.bsatu.by/ru/fakultety/inzhenerno-tehnologicheskiy-fakultet\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО), физика (ЦТ или ЭУО)\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет культуры и искусств - Факультет музыкального и хореографического искусства")
async def check_132(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет культуры и искусств - Факультет музыкального и хореографического искусства</b>\n"
             "Декан <i>Громович Ирина Михайловна</i>\n"
             "Телефон: +375173583213+375173502664\n"
             "Сайт: http://www.buk.by/process/fakultet%203/\n"
             "Духовые инструменты (народные)\n"
             "<b>Артист-инструменталист.  Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Пение (народное)\n"
             "<b>Артист-вокалист. Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Хореографическое искусство (народный танец)\n"
             "<b>Артист народного танца,Преподаватель,Балетмейстер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Хореографическое искусство (бальный танец)\n"
             "<b>Руководитель студии,Тренер,Преподаватель</b>\n"
             "Время обучени\n"
             "\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Хореографическое искусство (эстрадный танец)\n"
             "<b>Артист,Балетмейстер,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (инструментальная музыка)\n"
             "<b>Артист. Руководитель эстрадного оркестра,ансамбля. Преподаватель.</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (компьютерная музыка)\n"
             "<b>Аранжировщик компьютерной музыки,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (пение)\n"
             "<b>Певец.Руководитель вокального ансамбля.Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b></b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (хоровая музыка академическая)\n"
             "<b>Руководитель хора,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (хоровая музыка народная)\n"
             "<b>Руководитель хора,Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (инструментальная музыка народная)\n"
             "<b>Руководитель оркестра (ансамбля),Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (инструментальная музыка духовая)\n"
             "<b>Руководитель оркестра (ансамбля),Преподаватель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (инструментальная музыка)\n"
             "<b>Артист. Руководитель эстрадного оркестра,ансамбля. Преподаватель.</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Искусство эстрады (пение)\n"
             "<b>Певец.Руководитель вокального ансамбля.Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (хоровая музыка академическая)\n"
             "<b>Руководитель хора,Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество (исполнение программы; сольфеджио; коллоквиум)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Народное творчество (инструментальная музыка духовая)\n"
             "<b>Руководитель оркестра (ансамбля),Преподаватель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Белорусский/русский язык (ЦТ)\n"
             "Творчество\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "Хореографическое искусство (народный танец)\n"
             "<b>Артист народного танца,Преподаватель,Балетмейстер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "классический танец (исполнение программы);\n"
             "композиция и постановка танца (исполнение программы)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский национальный технический университет - Факультет маркетинга, менеджмента, предпринимательства")
async def check_133(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Факультет маркетинга, менеджмента, предпринимательства</b>\n"
             "Декан <i>Алексей Васильевич ДАНИЛЬЧЕНКО</i>\n"
             "Телефон: 293-93-09\n"
             "Сайт: http://www.bntu.by/fmmp.html\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Экономист,Проект-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-дизайнер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Экономист,Проект-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-дизайнер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 3\n"
             "Вступительные испытания: \n"
             "1. Экономика организации (ПЭ)\n"
             "2. Основы менеджмента (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный медицинский университет - Педиатрический факультет")
async def check_134(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Педиатрический факультет</b>\n"
             "Декан <i>Филипович Елена Константиновна</i>\n"
             "Телефон: 8(017)27716148(017)2771160\n"
             "Сайт: http://www.bsmu.by/page/6/90/\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "биология (ЦТ)\n"
             "химия (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Факультет энергетического строительства")
async def check_135(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Факультет энергетического строительства</b>\n"
             "Декан <i>Ивашечкин Владимир Васильевич</i>\n"
             "Телефон: 293-96-13\n"
             "Сайт: http://www.bntu.by/fes.html\n"
             "Экономика и организация производства (коммунальное и водное хозяйство)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Иностранный язык (ЦТ) - 15\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "Экономика и организация производства (коммунальное и водное хозяйство)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Иностранный язык (ЦТ) - 15\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Строительные материалы\n"
             "и изделия (ПЭ)\n"
             "2. Основы инженерной графики (ПЭ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Строительные материалы\n"
             "и изделия (ПЭ)\n"
             "2. Основы инженерной графики (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Факультет радиотехники и электроники")
async def check_136(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Факультет радиотехники и электроники</b>\n"
             "Декан <i>Короткевич Александр Васильевич</i>\n"
             "Телефон: (017)293-85-48\n"
             "Сайт: http://www.bsuir.by/ru/fre\n"
             "Радиотехника (программируемые радиоэлектронные средства)\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоинформатике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по электронным системам</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер электронной техники</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер электронной техники</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер электронной техники</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Радиотехника (программируемые радиоэлектронные средства)\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоинформатике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер электронной техники</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер электронной техники</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер электронной техники</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "Профессиональное обучение (информатика)\n"
             "<b>Педагог-программист</b>\n"
             "Время обучения: 3 года\n"
             "Вступительные испытания: \n"
             "Основы алгоритмизации и программирования (ПЭ),\n"
             "Охрана труда. Охрана окружающей среды и энергосбережение (ПЭ)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Строительный факультет")
async def check_137(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Строительный факультет</b>\n"
             "Декан <i>Сергей Николаевич Леонович</i>\n"
             "Телефон: 267-61-56267-92-01369-78-42\n"
             "Сайт: http://www.bntu.by/sf.html\n"
             "Экономика и организация производства (строительство)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель-технолог</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер – специалист по недвижимости</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "Экономика и организация производства (строительство)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер – специалист по недвижимости</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "Экономика и организация производства (строительство)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель-технолог</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер – специалист по недвижимости</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "Экономика и организация производства (строительство)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер – специалист по недвижимости</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2. Математика (ЦТ)\n"
             "3. Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.строительные материалы и изделия (ПЭ)\n"
             "2.основы инженерной графики (ПЭ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский национальный технический университет - Международный Институт  Дистанционного Образования")
async def check_138(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Международный Институт  Дистанционного Образования</b>\n"
             "Директор <i>Седнина Марина Александровна</i>\n"
             "Телефон: 26626582662661\n"
             "Сайт: http://www.bntu.by/mido.html\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Белорусский/русский язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ).\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Белорусский/русский язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ).\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Основы алгоритмизации и программирования (ПЭ)\n"
             "2. Охрана труда. Охрана окружающей среды и энергосбережение (ПЭ)\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова")
async def check_139(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Международный государственный экологический институт имени А.Д.Сахарова</b>\n"
             "директор <i>Маскевич Сергей Александрович</i>\n"
             "Телефон: (+375-17)230-69-98\n"
             "Сайт: www.iseu.by\n"
             "<b>Инженер</b>\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет информатики и радиоэлектроники - Факультет информационных технологий и управления")
async def check_140(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет информатики и радиоэлектроники - Факультет информационных технологий и управления</b>\n"
             "Декан <i>Шилин Леонид Юрьевич</i>\n"
             "Телефон: (017)293-23-66\n"
             "Сайт: http://www.bsuir.by/ru/fitu\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии (в игровой  индустрии)\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям и управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по радиоэлектронике</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Физика (ЦТ)\n"
             "Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-системотехник</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям и управлению</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям и управлению</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям и управлению</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер по информационным технологиям</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Механико-математический факультет")
async def check_141(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Механико-математический факультет</b>\n"
             "Декан <i>Босяков Сергей Михайлович</i>\n"
             "Телефон: (+375-17)209-52-49(+375-17)209-50-46\n"
             "Сайт: www.mmf.bsu.by\n"
             "Математика (научно-производственная деятельность)\n"
             "<b>Математик</b>\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный технологический университет - Инженерно-экономический факультет")
async def check_142(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный технологический университет - Инженерно-экономический факультет</b>\n"
             "Декан <i>Ольферович Андрей Богданович</i>\n"
             "Телефон: тел.:+37517358-97-91\n"
             "Сайт: https://www.belstu.by/faculties/ief.htmlhttps://ief.belstu.by/?_ga=2.164227899.584529427.1558331120-1670493189.1...\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Факультет философии и социальных наук")
async def check_143(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Факультет философии и социальных наук</b>\n"
             "Декан <i>Гигин Вадим Францевич</i>\n"
             "Телефон: (+375-17)259-70-45(+375-17)259-70-47(+375-17)259-74-04\n"
             "Сайт: www.ffsn.bsu.by\n"
             "<b>Философ,Преподаватель философии и социально-гуманитарных дисциплин</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "обществоведение (ЦТ)\n"
             "история Беларуси (ЦТ),\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный экономический университет - Факультет экономики и менеджмента")
async def check_144(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный экономический университет - Факультет экономики и менеджмента</b>\n"
             "Декан <i>Петриченко Елена Владимировна </i>\n"
             "Телефон: +37517209-7829-ПетриченкоЕленаВладимировна,декан\n"
             "Сайт: http://bseu.by/fm/\n"
             "Экономика труда\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Управление интеллектуальной собственностью\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и управление на предприятии промышленности\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и управление на предприятии агропромышленного комплекса\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика природопользования\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-аналитик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (социально-административный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (инновационный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика труда\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Управление интеллектуальной собственностью\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и управление на предприятии промышленности\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и управление на предприятии агропромышленного комплекса\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика природопользования\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-аналитик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (социально-административный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (инновационный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика и управление на предприятии промышленности\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Экономика труда\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 3,5\n"
             "Вступительные испытания: \n"
             "экономика организации (ЭУО)\n"
             "основы менеджмента (ЭУО)\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия связи - Факультет электросвязи")
async def check_145(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия связи - Факультет электросвязи</b>\n"
             "Декан <i>Лапцевич Александр Анатольевич</i>\n"
             "Телефон: +37517360-15-02-Декан+37517272-96-40-Деканат+37517272-96-40-Деканат\n"
             "Сайт: http://bsac.by/lp/fakultet-elektrosvazi\n"
             "Инфокоммуникационные системы (техническая эксплуатация), сокращенный срок получения образования, для выпускников ССО (бюджет)\n"
             "<b>Инженер по инфокоммуникационным системам</b>\n"
             "Время обучения: 2 г. 10 мес.\n"
             "Вступительные испытания: \n"
             "математика (П) ЭУО\n"
             "основы информационных технологий (П) ЭУО\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный медицинский университет - Медицинский факультет иностранных учащихся")
async def check_146(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный медицинский университет - Медицинский факультет иностранных учащихся</b>\n"
             "Декан <i>Ишутин Олег Сергеевич</i>\n"
             "Телефон: (+37517)2772789\n"
             "Сайт: http://www.bsmu.by/page/6/87/\n"
             "<b>Врач</b>\n"
             "Время обучения: 6 лет (на русском или английском языке)\n"
             "Вступительные испытания: \n"
             "1. По результатам итоговой аттестации при освоении содержания образовательной программы подготовки лиц к поступлению в учреждения высшего образования.\n"
             "2. По результатам собеседования, устанавливающего уровень владения ими языком, на котором осуществляется образовательный процесс, в объеме, достаточном для освоения содержания образовательной программы высшего образования.\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Барановичский государственный университет - Инженерный факультет")
async def check_147(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Барановичский государственный университет - Инженерный факультет</b>\n"
             "Декан <i>Понталёв Олег Владимирович</i>\n"
             "Телефон: (0163)640662(0163)640665\n"
             "Сайт: https://www.barsu.by/faculties/chairengineering/engineering.php\n"
             "Технология машиностроения\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "Информационные системы и технологии\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Математика (ЦТ или письменно (ЭУО))\n"
             "Физика (ЦТ или письменно (ЭУО))\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 3,5 года\n"
             "Вступительные испытания: \n"
             "Материаловедение и технология материалов (письменно) (ЭУО)\n"
             "Основы инженерной графики (письменно) (ЭУО)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 3,5 года\n"
             "Вступительные испытания: \n"
             "Материаловедение и технология материалов (письменно) (ЭУО)\n"
             "Основы инженерной графики (письменно) (ЭУО)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский государственный университет транспорта - Факультет управления процессами перевозок")
async def check_148(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет транспорта - Факультет управления процессами перевозок</b>\n"
             "Декан <i>Берлин Николай Петрович</i>\n"
             "Телефон: (0232)773656(0232)952191\n"
             "Сайт: http://bsut.by/obrazovanie/fakultety/upravlenie-processami-perevozok.html\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Международные автомобильные перевозки\n"
             "<b>Инженер-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Безопасность дорожного движения\n"
             "<b>Инженер-инспектор</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Управление движением\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "физика (ЦТ)\n"
             "математика (ЦТ)\n"
             "\n"
             "<b>Инженер-экономист,Логист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Международные автомобильные перевозки\n"
             "<b>Инженер-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
             "Безопасность дорожного движения\n"
             "<b>Инженер-инспектор</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Мелиоративно-строительный факультет")
async def check_149(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>БГ  орденов Октябрьской Революции и Трудового Красного Знамени сельскохозяйственная академия - Мелиоративно-строительный факультет</b>\n"
             "Декан <i>Дуброва Юрий Николаевич</i>\n"
             "Телефон: 8022337-97-37,7-97-27\n"
             "Сайт: \n"
             "<b>Инженер</b>\n"
             "Время обучения: 4.5 лет\n"
             "Вступительные испытания: \n"
             "математика (ЦТ или ЭУО),\n"
             "физика (ЦТ или ЭУО)\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Минский инновационный университет - Факультет коммуникаций, экономики и права")
async def check_150(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Минский инновационный университет - Факультет коммуникаций, экономики и права</b>\n"
             "Проректор по учебной работе - декан факультета коммуникаций, экономики и права <i>Хмельницкий Владимир Анатольевич</i>\n"
             "Телефон: +375(017)215-27-35-декан+375(017)377-48-38-деканат+375(017)373-26-25-деканат\n"
             "Сайт: http://miu.by/rus/faculty/index.php\n"
             "Современные иностранные языки (перевод)\n"
             "<b>Лингвист; переводчик (с указанием языков)</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Иностранный язык (английский) (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Психолог,Преподаватель психологии</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Биология (ЦТ)\n"
             "История Беларуси (ЦТ)\n"
             "\n"
             "<b>Юрист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Обществоведение (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Иностранный язык (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-программист</b>\n"
             "Время обучения: 5 лет\n"
             "Вступительные испытания: \n"
             "Белорусский (русский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Архитектурный факультет")
async def check_151(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Архитектурный факультет</b>\n"
             "Декан <i>Армен Сергеевич САРДАРОВ</i>\n"
             "Телефон: (017)293-96-77\n"
             "Сайт: http://www.bntu.by/af.html\n"
             "<b>Архитектор</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Творчество (рисунок\n"
             "композиция\n"
             "черчение) (ЭУО)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Архитектор-дизайнер</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Творчество (рисунок\n"
             "композиция\n"
             "живопись) (ЭУО)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Архитектор</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Творчество (рисунок\n"
             "композиция\n"
             "черчение) (ЭУО)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Архитектор-дизайнер</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Творчество (рисунок\n"
             "композиция\n"
             "живопись) (ЭУО)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Архитектор</b>\n"
             "Время обучения: \n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - ГУО «Институт бизнеса БГУ»")
async def check_152(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - ГУО «Институт бизнеса БГУ»</b>\n"
             "Директор <i>Бригадин Петр Иванович</i>\n"
             "Телефон: +375173500020\n"
             "Сайт: www.sb.bsu.byhttps://vk.com/sb__bsuhttps://www.facebook.com/sbmtbsu/https://www.instagram.com/sb.bsu/https://t.me/sb_bsu\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (Финансовый и инвестиционный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (Социально-административный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Маркетинг (Рекламная деятельность)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Маркетинг (Международный маркетинг)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Маркетинг (Маркетинг в электронной коммерции)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Логистик-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Логистик-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист информационных систем</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист информационных систем</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (Финансовый и инвестиционный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Менеджмент (Социально-административный)\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Маркетинг (Рекламная деятельность)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Маркетинг (Международный маркетинг)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "Маркетинг (Маркетинг в электронной коммерции)\n"
             "<b>Маркетолог-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Логистик-экономист</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист информационных систем</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "белорусский (русский) язык (ЦТ)\n"
             "математика (ЦТ)\n"
             "иностранный язык (ЦТ)\n"
             "\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(
    text="Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации")
async def check_153(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Факультет технологий управления и гуманитаризации</b>\n"
             "Декан <i>Геннадий Михайлович БРОВКА</i>\n"
             "Телефон: 292-14-63\n"
             "Сайт: http://www.bntu.by/ftug.html\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Менеджер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "Экономика и организация производства (экономическая безопасность промышленного предприятия)\n"
             "<b>Инженер-экономист</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Иностранный язык (ЦТ) - 15\n"
             "\n"
             "<b>Инженер-механик</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "Упаковочное производство (проектирование и дизайн упаковки)\n"
             "<b>Инженер-конструктор-дизайнер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Физика (ЦТ)\n"
             "3.Математика (ЦТ)\n"
             "\n"
             "Промышленный дизайн (производственного оборудования)\n"
             "<b>Инженер-дизайнер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Творчество (рисунок - 3,\n"
             "композиция - 3)\n"
             "3. Математика (ЦТ) - 10\n"
             "\n"
             "<b>Экономист-менеджер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Иностр. язык (ЦТ)\n"
             "\n"
             "<b>Инженер-энергоменеджер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Основы электротехники (ПЭ)\n"
             "2. Основы инженерной графики (ПЭ)\n"
             "\n"

        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский национальный технический университет - Факультет транспортных коммуникаций")
async def check_154(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский национальный технический университет - Факультет транспортных коммуникаций</b>\n"
             "Декан <i>Сергей Егорович КРАВЧЕНКО</i>\n"
             "Телефон: 267-98-84\n"
             "Сайт: http://www.bntu.by/ftk.html\n"
             "<b></b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1. Бел. (рус.) язык (ЦТ) - 10\n"
             "2. Математика (ЦТ) - 20\n"
             "3. Физика (ЦТ) - 10\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер-строитель</b>\n"
             "Время обучения: 6\n"
             "Вступительные испытания: \n"
             "1.Бел.(рус.) язык (ЦТ)\n"
             "2.Математика (ЦТ)\n"
             "3.Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "1. Геодезия (ПЭ)\n"
             "2. Основы информационных технологий (ПЭ)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусско-Российский университет - ИНЖЕНЕРНЫЙ ФАКУЛЬТЕТ ЗАОЧНОГО ОБРАЗОВАНИЯ")
async def check_155(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусско-Российский университет - ИНЖЕНЕРНЫЙ ФАКУЛЬТЕТ ЗАОЧНОГО ОБРАЗОВАНИЯ</b>\n"
             "Декан <i>Рогожин Владимир Дмитриевич</i>\n"
             "Телефон: 8(0222)22-95-87\n"
             "Сайт: \n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "\n"
             "<b>Инженер</b>\n"
             "Время обучения: 5\n"
             "Вступительные испытания: \n"
             "Русский(белорусский) язык (ЦТ)\n"
             "Математика (ЦТ)\n"
             "Физика (ЦТ)\n"
             "<b>Инженер</b>\n"
             "Время обучения: 4\n"
             "Вступительные испытания: \n"
             "Материаловедение и технология материалов (ЭУО, письменно, с использованием тестовых заданий)\n"
             "Основы инженерной графики (ЭУО, письменно, с использованием тестовых заданий)\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусская государственная академия музыки - Оркестровый факультет")
async def check_156(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусская государственная академия музыки - Оркестровый факультет</b>\n"
             "Декан <i>Шкулепа Максим Фомич</i>\n"
             "Телефон: +37517379-19-48+37517379-19-49\n"
             "Сайт: \n"
             "Дирижирование  (оперно-симфоническое)\n"
             "<b>Дирижер. Преподаватель</b>\n"
             "Время обучения: 4 года\n"
             "Вступительные испытания: \n"
             "ЦТ, ЭУО\n"
        , parse_mode=types.ParseMode.HTML)


@dp.message_handler(text="Белорусский государственный университет - Филологический факультет")
async def check_157(message: types.Message,
                    state: FSMContext):
    await message.answer(
        text="<b>Белорусский государственный университет - Филологический факультет</b>\n"
             "Декан <i>Важник Сергей Александрович </i>\n"
             "Телефон: (+375-17)222-34-21\n"
             "Сайт: www.philology.bsu.by\n"
        , parse_mode=types.ParseMode.HTML)



