from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from keyboards.inline.buttons_test import *
from keyboards.inline.inline import *

from .menues import dp

global markup_lud
global markup_issled
global markup_prvo
global markup_estet
global markup_ex
global markup_econ
global add_text
def pidoras(answer):
    try:
        answer = answer + 1
    except:
        print("ERRRRRRRRROR")
        return 0
    return answer

@dp.message_handler(Command("test"))
async def show_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') is None:
        await message.answer(text='Для начала выполните команду /start')
    await state.update_data(q_first=0)
    await state.update_data(q_second=0)
    await state.update_data(q_third=0)
    await state.update_data(q_fourth=0)
    await state.update_data(q_fifth=0)
    await state.update_data(q_sixth=0)
    await message.answer(
        text="<b>Инструкция</b>\n<i>Тест состоит из 24 вопровов\nЗакончите высказывание выбрав один из вариантов, который больше подходит Вам</i>",
        parse_mode=types.ParseMode.HTML)
    await message.answer(text="1. Мне хотелось бы в своей профессиональной деятельности:", reply_markup=markup_1_q)


# 1
@dp.message_handler(text='А) общаться с самыми разными людьми')
async def q1_1(message: types.Message, state: FSMContext):
    await state.update_data(q_first=1)
    await message.answer(text="2. В книге или кинофильме меня больше всего привлекает:", reply_markup=markup_2_q)


@dp.message_handler(text='Б) за общественную деятельность')
async def q2_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="4. Я скорее соглашусь стать:", reply_markup=markup_4_q)


@dp.message_handler(text='В) взаимопонимание среди людей')
async def q3_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="6. На месте директора школы я прежде всего займусь:", reply_markup=markup_6_q)


@dp.message_handler(text='Б) созданием дружного, сплоченного коллектива')
async def q4_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="7. На технической выставке меня больше всего привлечет:", reply_markup=markup_7_q)


@dp.message_handler(text='Б) дружелюбие, чуткость, отзывчивость')
async def q5_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="9. В свободное от работы время я буду:", reply_markup=markup_9_q)


@dp.message_handler(text='В) о человеческих взаимоотношениях')
async def q6_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="12. Если бы в моей школе было всего три кружка, я бы выбрал:", reply_markup=markup_12_q)


@dp.message_handler(text='А) улучшению взаимопонимания между учителями и учениками')
async def q7_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="14. Я с большим интересом смотрю:", reply_markup=markup_14_q)


@dp.message_handler(text='В) с детьми или сверстниками')
async def q8_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="16. Школа в первую очередь должна:", reply_markup=markup_16_q)


@dp.message_handler(text='Б) учить общению с другими людьми')
async def q9_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="17. Каждый человек должен:", reply_markup=markup_17_q)


@dp.message_handler(text='А) защита интересов и прав граждан')
async def q10_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="19. Мне больше всего нравятся уроки:", reply_markup=markup_19_q)


@dp.message_handler(text='В) заниматься сбытом продукции')
async def q11_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await message.answer(text="21. Я предпочитаю читать статьи:", reply_markup=markup_21_q)


@dp.message_handler(text='А) в помещении, где много людей')
async def q12_1(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_first')
    answer = pidoras(answer)
    await state.update_data(q_first=answer)
    await get_result(message, state)


# 2
@dp.message_handler(text='В) информация, которая может пригодиться в жизни')
async def q1_2(message: types.Message, state: FSMContext):
    await state.update_data(q_second=1)
    await message.answer(text="3. Меня обрадует Нобелевская премия:", reply_markup=markup_3_q)


@dp.message_handler(text='А) в области науки')
async def q2_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="4. Я скорее соглашусь стать:", reply_markup=markup_4_q)


@dp.message_handler(text='А) достижение науки')
async def q3_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="6. На месте директора школы я прежде всего займусь:", reply_markup=markup_6_q)


@dp.message_handler(text='В) разработкой новых технологий обучения')
async def q4_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="7. На технической выставке меня больше всего привлечет:", reply_markup=markup_7_q)


@dp.message_handler(text='Б) внутреннее устройство экспонатов (механизм)')
async def q5_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="8. В людях я ценю прежде всего:", reply_markup=markup_8_q)


@dp.message_handler(text='Б) ставить различные опыты')
async def q6_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="10. В заграничных поездках меня больше всего привлечет:", reply_markup=markup_10_q)


@dp.message_handler(text='Б) о новой научной теории')
async def q7_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="12. Если бы в моей школе было всего три кружка, я бы выбрал:", reply_markup=markup_12_q)


@dp.message_handler(text='А) научно-популярные фильмы')
async def q8_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="15. Мне было бы интереснее работать:", reply_markup=markup_15_q)


@dp.message_handler(text='В) наука и технический прогресс')
async def q9_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="19. Мне больше всего нравятся уроки:", reply_markup=markup_19_q)


@dp.message_handler(text='А) о выдающихся ученых и их открытиях')
async def q10_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="22. Свободное время я охотнее провожу:", reply_markup=markup_22_q)


@dp.message_handler(text='Б) с книгой')
async def q11_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="23. Больший интерес у меня вызовет сообщение:", reply_markup=markup_23_q)


@dp.message_handler(text='В) о научном открытии')
async def q12_2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_second')
    answer = pidoras(answer)
    await state.update_data(q_second=answer)
    await message.answer(text="24. Я предпочитаю работать:", reply_markup=markup_24_q)


# 3
@dp.message_handler(text='Б) главным инженером на производстве')
async def q1_3(message: types.Message, state: FSMContext):
    await state.update_data(q_third=1)
    await message.answer(text="5. Будущее людей определяет:", reply_markup=markup_5_q)


@dp.message_handler(text='Б) развитие производства')
async def q2_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="6. На месте директора школы я прежде всего займусь:", reply_markup=markup_6_q)


@dp.message_handler(text='В) практическое применение экспонатов')
async def q3_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="8. В людях я ценю прежде всего:", reply_markup=markup_8_q)


@dp.message_handler(text='А) о машине нового типа')
async def q4_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="12. Если бы в моей школе было всего три кружка, я бы выбрал:", reply_markup=markup_12_q)


@dp.message_handler(text='А) технический')
async def q5_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="13. В школе больше внимания следует уделять:", reply_markup=markup_13_q)


@dp.message_handler(text='А) с машинами, механизмами')
async def q6_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="16. Школа в первую очередь должна:", reply_markup=markup_16_q)


@dp.message_handler(text='В) обучать навыкам работы')
async def q7_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="17. Каждый человек должен:", reply_markup=markup_17_q)


@dp.message_handler(text='Б) забота о материальном благополучии людей')
async def q8_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="19. Мне больше всего нравятся уроки:", reply_markup=markup_19_q)


@dp.message_handler(text='В) труда')
async def q9_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="20. Мне интереснее было бы:", reply_markup=markup_20_q)


@dp.message_handler(text='Б) изготавливать изделия')
async def q10_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="21. Я предпочитаю читать статьи:", reply_markup=markup_21_q)


@dp.message_handler(text='В) об интересных изобретениях')
async def q11_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="22. Свободное время я охотнее провожу:", reply_markup=markup_22_q)


@dp.message_handler(text='А) делая что-то по хозяйству')
async def q12_3(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_third')
    answer = pidoras(answer)
    await state.update_data(q_third=answer)
    await message.answer(text="23. Больший интерес у меня вызовет сообщение:", reply_markup=markup_23_q)


# 4
@dp.message_handler(text='В) снимать фильмы, рисовать, писать книги, выступать на сцене и т.д.')
async def q1_4(message: types.Message, state: FSMContext):
    await state.update_data(q_fourth=1)
    await message.answer(text="2. В книге или кинофильме меня больше всего привлекает:", reply_markup=markup_2_q)


@dp.message_handler(text='А) художественная форма, мастерство писателя или режиссера')
async def q2_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="3. Меня обрадует Нобелевская премия:", reply_markup=markup_3_q)


@dp.message_handler(text='В) в области искусства')
async def q3_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="4. Я скорее соглашусь стать:", reply_markup=markup_4_q)


@dp.message_handler(text='А) внешний вид экспонатов (цвет, форма)')
async def q4_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="8. В людях я ценю прежде всего:", reply_markup=markup_8_q)


@dp.message_handler(text='А) писать стихи или музыку или рисовать')
async def q5_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="10. В заграничных поездках меня больше всего привлечет:", reply_markup=markup_10_q)


@dp.message_handler(text='В) возможность знакомства с историей и культурой другой страны')
async def q6_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="11. Мне интереснее беседовать:", reply_markup=markup_11_q)


@dp.message_handler(text='Б) музыкальный')
async def q7_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="13. В школе больше внимания следует уделять:", reply_markup=markup_13_q)


@dp.message_handler(text='Б) программы о культуре и спорте')
async def q8_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="15. Мне было бы интереснее работать:", reply_markup=markup_15_q)


@dp.message_handler(text='Б) иметь возможность заниматься творчеством')
async def q9_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="18. Для благополучия общества в первую очередь необходима:", reply_markup=markup_18_q)


@dp.message_handler(text='Б) о творчестве ученых и музыкантов')
async def q10_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="22. Свободное время я охотнее провожу:", reply_markup=markup_22_q)


@dp.message_handler(text='В) на выставках, концертах и пр.')
async def q11_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="23. Больший интерес у меня вызовет сообщение:", reply_markup=markup_23_q)


@dp.message_handler(text='А) о художественной выставке')
async def q12_4(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fourth')
    answer = pidoras(answer)
    await state.update_data(q_fourth=answer)
    await message.answer(text="24. Я предпочитаю работать:", reply_markup=markup_24_q)


# 5
@dp.message_handler(text='Б) сюжет, действие героев')
async def q1_5(message: types.Message, state: FSMContext):
    await state.update_data(q_fifth=1)
    await message.answer(text="3. Меня обрадует Нобелевская премия:", reply_markup=markup_3_q)


@dp.message_handler(text='В) начальником экспедиции')
async def q2_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="5. Будущее людей определяет:", reply_markup=markup_5_q)


@dp.message_handler(text='А) мужество, смелость, выносливость')
async def q3_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="9. В свободное от работы время я буду:", reply_markup=markup_9_q)


@dp.message_handler(text='В) тренироваться')
async def q4_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="10. В заграничных поездках меня больше всего привлечет:", reply_markup=markup_10_q)


@dp.message_handler(text='А) экстремальный туризм (альпинизм, виндсерфинг, горные лыжи)')
async def q5_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="11. Мне интереснее беседовать:", reply_markup=markup_11_q)


@dp.message_handler(text='В) спортивный')
async def q6_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="13. В школе больше внимания следует уделять:", reply_markup=markup_13_q)


@dp.message_handler(text='Б) поддержанию здоровья учащихся, занятиям спортом')
async def q7_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="14. Я с большим интересом смотрю:", reply_markup=markup_14_q)


@dp.message_handler(text='В) спортивные программы')
async def q8_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="15. Мне было бы интереснее работать:", reply_markup=markup_15_q)


@dp.message_handler(text='Б) с объектами природы')
async def q9_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="16. Школа в первую очередь должна:", reply_markup=markup_16_q)


@dp.message_handler(text='А) вести здоровый образ жизни')
async def q10_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="18. Для благополучия общества в первую очередь необходима:", reply_markup=markup_18_q)


@dp.message_handler(text='А) физкультуры')
async def q11_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await message.answer(text="20. Мне интереснее было бы:", reply_markup=markup_20_q)


@dp.message_handler(text='Б) в необычных условиях')
async def q12_5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_fifth')
    answer = pidoras(answer)
    await state.update_data(q_fifth=answer)
    await get_result(message, state)


# 6
@dp.message_handler(text='Б) что-нибудь делать своими руками – мебель, одежду, машины и т.д.')
async def q1_6(message: types.Message, state: FSMContext):
    await state.update_data(q_sixth=1)
    await message.answer(text="2. В книге или кинофильме меня больше всего привлекает:", reply_markup=markup_2_q)


@dp.message_handler(text='А) управляющим банка')
async def q2_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="5. Будущее людей определяет:", reply_markup=markup_5_q)


@dp.message_handler(text='А) благоустройством школы (столовая, спортзал, компьютеры)')
async def q3_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="7. На технической выставке меня больше всего привлечет:", reply_markup=markup_7_q)


@dp.message_handler(text='В) ответственность, аккуратность')
async def q4_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="9. В свободное от работы время я буду:", reply_markup=markup_9_q)


@dp.message_handler(text='Б) деловое общение')
async def q5_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="11. Мне интереснее беседовать:", reply_markup=markup_11_q)


@dp.message_handler(text='В) укреплению дисциплины')
async def q6_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="14. Я с большим интересом смотрю:", reply_markup=markup_14_q)


@dp.message_handler(text='А) давать знания и умения')
async def q7_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="17. Каждый человек должен:", reply_markup=markup_17_q)


@dp.message_handler(text='В) иметь удобные бытовые условия')
async def q8_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="18. Для благополучия общества в первую очередь необходима:", reply_markup=markup_18_q)


@dp.message_handler(text='Б) математики')
async def q9_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="20. Мне интереснее было бы:", reply_markup=markup_20_q)


@dp.message_handler(text='А) планировать производство продукции')
async def q10_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="21. Я предпочитаю читать статьи:", reply_markup=markup_21_q)


@dp.message_handler(text='Б) о ситуации на фондовой бирже')
async def q11_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await message.answer(text="24. Я предпочитаю работать:", reply_markup=markup_24_q)


@dp.message_handler(text='В) в обычном кабинете')
async def q12_6(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer = data.get('q_sixth')
    answer = pidoras(answer)
    await state.update_data(q_sixth=answer)
    await get_result(message, state)


@dp.message_handler(Command("result"))
async def get_result(message: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    if data.get('klass') is None:
        await message.answer(text='Для начала выполните команду /start')
    s_data = {}
    n_data = data
    if n_data.get('klass'):
        del n_data["klass"]
    if n_data.get('programm'):
        del n_data["programm"]
    if n_data.get('prev_menu_yvo'):
        del n_data["prev_menu_yvo"]
    if n_data.get('back'):
        del n_data["back"]
    if n_data.get('q_first') == None and n_data.get('q_second') == None and n_data.get(
            'q_third') == None and n_data.get(
            'q_fourth') == None and n_data.get('q_fifth') == None and n_data.get('q_sixth') == None:
        await message.answer(text="Для начала необходимо пройти тест /test")
        return

    markup_lud = ReplyKeyboardRemove()
    markup_issled = ReplyKeyboardRemove()
    markup_prvo = ReplyKeyboardRemove()
    markup_estet = ReplyKeyboardRemove()
    markup_ex = ReplyKeyboardRemove()
    markup_econ = ReplyKeyboardRemove()
    dataa = await state.get_data()
    print(dataa)
    if dataa.get('programm') == 'ССО':
        print('done!')
        markup_lud = url_lud_sso
        markup_issled = url_issled_sso
        markup_prvo = url_prvo_sso
        markup_estet = ReplyKeyboardRemove()
        markup_ex = ReplyKeyboardRemove()
        markup_econ = ReplyKeyboardRemove()
    elif dataa.get('programm') == 'ПТО':
        print('done!')
        markup_lud = url_lud_pto
        markup_issled = ReplyKeyboardRemove()
        markup_prvo = url_prvo_pto
        markup_estet = url_estet_pto
        markup_ex = url_ex_pto
        markup_econ = url_econ_pto
    elif dataa.get('programm') == 'УВО':
        print('done!')
        markup_lud = url_lud_yvo
        markup_issled = url_issled_yvo
        markup_prvo = url_prvo_yvo
        markup_estet = url_estet_yvo
        markup_ex = url_ex_yvo
        markup_econ = url_econ_yvo
    print('---')
    print(markup_prvo)
    s_keys = sorted(data, key=n_data.get)

    for w in s_keys:
        s_data[w] = n_data[w]

    for k, v in s_data.items():
        if 12 >= v >= 10:
            texxt = " из 12 - ярко выраженная профессиональная склонность"
        elif 9 >= v >= 7:
            texxt = " из 12 - средне выраженная профессиональная склонность"
        elif 6 >= v >= 4:
            texxt = " из 12 - слабо выраженная профессиональная склонность"
        else:
            texxt = " из 12 - профессиональная склонность не выражена"

        if k == 'q_first':
            '''if markup_lud==ReplyKeyboardRemove():
                add_text=''
            else:
                add_text = '\n   Вам могут подойти следующие специальности:'''

            await message.answer(
                text=str(v) + texxt + "<b>. Склонность к работе с людьми. </b><i>Профессии, связанные с "
                                      "обслуживанием "
                                      " (бытовым, медицинским, информационным), управлением, воспитанием и"
                                      " обучением. Люди, успешные в профессиях этой группы, должны уметь и"
                                      " любить общаться, находить общий язык с разными людьми, понимать их"
                                      " настроение, намерения и особенности.</i>"# + add_text
                , reply_markup=markup_lud, parse_mode=types.ParseMode.HTML)
        elif k == 'q_second':
            if markup_issled==ReplyKeyboardRemove():
                add_text=''
            else:
                add_text = '\n   Вам могут подойти следующие специальности:'
            await message.answer(text=str(v) + texxt + "<b>. Склонность к исследовательской деятельности. "
                                                       "</b><i>Профессии, связанные с научной работой. Кроме хорошей "
                                                       "теоретической подготовки в определенных областях науки, людям, "
                                                       "необходимы такие качества, рациональность, независимость и "
                                                       "оригинальность суждений, аналитический склад ума. Как правило, "
                                                       "им больше нравится размышлять о проблеме, чем заниматься ее "
                                                       "реализацией.</i> " + add_text
                                 , reply_markup=markup_issled, parse_mode=types.ParseMode.HTML)
        elif k == 'q_third':
            if markup_prvo==ReplyKeyboardRemove():
                add_text=''
            else:
                add_text = '\n   Вам могут подойти следующие специальности:'
            await message.answer(text=str(v) + texxt + "<b>. Склонность к работе на производстве. </b><i>Круг этих "
                                                       "профессий очень широк: производство и обработка металла; сборка, "
                                                       "монтаж приборов и механизмов; ремонт, наладка, обслуживание "
                                                       "электронного и механического оборудования; монтаж, ремонт зданий, "
                                                       "конструкций; обработка и использование различных материалов; "
                                                       "управление транспортом. Профессии этой группы предъявляют "
                                                       "повышенные требования к здоровью человека, координации движений, "
                                                       "вниманию.</i> " + add_text
                                 , reply_markup=markup_prvo, parse_mode=types.ParseMode.HTML)
        elif k == 'q_fourth':
            if markup_estet==ReplyKeyboardRemove():
                add_text=''
            else:
                add_text = '\n   Вам могут подойти следующие специальности:'
            await message.answer(text=str(v) + texxt + "<b>. Склонность к эстетическим видам деятельности. "
                                                       "</b><i>Профессии творческого характера, связанные с "
                                                       "изобразительной, музыкальной, литературно-художественной, "
                                                       "актерско- сценической деятельностью. Людей творческих профессий, "
                                                       "кроме наличия специальных способностей (музыкальных, "
                                                       "литературных, актерских), отличает оригинальность мышления и "
                                                       "независимость характера, стремление к совершенству.</i> " + add_text
                                 , reply_markup=markup_estet, parse_mode=types.ParseMode.HTML)
        elif k == 'q_fifth':
            if markup_ex==ReplyKeyboardRemove():
                add_text=''
            else:
                add_text = '\n   Вам могут подойти следующие специальности:'
            await message.answer(text=str(v) + texxt + "<b>. Склонность к экстремальным видам деятельности. "
                                                       "</b><i>Профессии, связанные с занятиями спортом, путешествиями, "
                                                       "экспедиционной работой, охранной и оперативно-розыскной "
                                                       "деятельностью, службой в армии. Все они предъявляют особые "
                                                       "требования к физической подготовке, здоровью и морально-волевым "
                                                       "качествам.</i> " + add_text
                                 , reply_markup=markup_ex, parse_mode=types.ParseMode.HTML)
        elif k == 'q_sixth':
            if markup_econ==ReplyKeyboardRemove():
                add_text=''
            else:
                add_text = '\n   Вам могут подойти следующие специальности:'
            await message.answer(text=str(v) + texxt + "<b>. Склонность к планово-экономическим видам деятельности. "
                                                       "</b><i>Профессии, связанные с расчетами и планированием ("
                                                       "бухгалтер, экономист); делопроизводством, анализом и "
                                                       "преобразованием текстов (редактор, переводчик, лингвист); "
                                                       "схематическим изображением объектов (чертежник, топограф). Эти "
                                                       "профессии требуют от человека собранности и аккуратности.</i> " + add_text
                                 , reply_markup=markup_econ, parse_mode=types.ParseMode.HTML)
    await message.answer(
        text="Для того чтобы вернуться к результатам теста введите /result\nДля просмотра специальностей введите команду /spec",
        reply_markup=ReplyKeyboardRemove())
