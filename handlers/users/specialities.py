from aiogram.dispatcher import FSMContext

from .plases import *

from loader import dp



@dp.message_handler(text='Парикмахер')
async def check_spec_1(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer_photo(open("data/photo/Parikmaher.jpg", 'rb'))
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')


@dp.message_handler(text='Мастер по маникюру')
async def check_spec_2(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')
    await print_mgptkshp(message)
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')
    await message.answer_photo(open("data/photo/Maniqur.jpg", 'rb'))


@dp.message_handler(text='Мастер по педикюру')
async def check_spec_3(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer_photo(open("data/photo/Pediqur.jpg", 'rb'))
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')


@dp.message_handler(text='Визажист')
async def check_spec_4(message: types.Message, state: FSMContext):
    await print_mgptkshp(message)
    await message.answer_photo(open("data/photo/Vizazist.jpg", 'rb'))
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')


@dp.message_handler(text='Приемщик заказов')
async def check_spec_5(message: types.Message, state: FSMContext):
    await print_mgptkshp(message)
    await message.answer_photo(open("data/photo/priemzikZakazov.jpg", 'rb'))
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')


@dp.message_handler(text='Оператор прачечного оборудования')
async def check_spec_6(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer_photo(open("data/photo/operPrach.jpg", 'rb'))
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')


@dp.message_handler(text='Контроллер станочных и слесарных работ')
async def check_spec_7(message: types.Message, state: FSMContext):
    await print_mgpl_3(message)
    await message.answer_photo(open("data/photo/KontrollerStanochn.jpg", 'rb'))
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')


@dp.message_handler(text='Оператор станков с ЧПУ')
async def check_spec_8(message: types.Message, state: FSMContext):
    await print_mgpl_3(message)
    await message.answer_photo(open("data/photo/operStankovCHPY.jpg", 'rb'))
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')


@dp.message_handler(text='Токарь')
async def check_spec_9(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/Tokar.jpg", 'rb'))


@dp.message_handler(text='Фрезеровщик')
async def check_spec_10(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/kassirBiletniy.jpg", 'rb'))


@dp.message_handler(text='Шлифовщик')
async def check_spec_11(message: types.Message, state: FSMContext):
    await print_mgpl_3(message)
    await message.answer_photo(open("data/photo/Shlifovchik.jpg", 'rb'))
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')


@dp.message_handler(text='Электрогазосварщик')
async def check_spec_12(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_5(message)
    await message.answer('https://licey5.minskedu.gov.by/')
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await print_mgptksikh(message)
    await message.answer('http://ptk-skh.minsk.edu.by/ru/main.aspx?guid=2591')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await message.answer_photo(open("data/photo/electrogazosvarchik.jpg", 'rb'))


@dp.message_handler(text='Элекросварщик на автоматических и полуавтоматических машинах')
async def check_spec_13(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgptksikh(message)
    await message.answer('http://ptk-skh.minsk.edu.by/ru/main.aspx?guid=2591')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/electrosvarchik.jpg", 'rb'))


@dp.message_handler(text='Элекросварщик ручной сварки')
async def check_spec_14(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/electrosvarchikRychnoy.jpg", 'rb'))


@dp.message_handler(text='Слесарь-инструментальщик')
async def check_spec_15(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/slesarInstrum.jpg", 'rb'))


@dp.message_handler(text='Слесарь механосборочных работ')
async def check_spec_16(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/slesarMehan.jpg", 'rb'))


@dp.message_handler(text='Слесарь-ремонтник')
async def check_spec_17(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/slesarRemontnik.jpg", 'rb'))


@dp.message_handler(text='Слесарь-сбощик бытовой техники')
async def check_spec_18(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await message.answer_photo(open("data/photo/slesarSborchik.jpg", 'rb'))


@dp.message_handler(text='Изолировщик на термоизоляции')
async def check_spec_19(message: types.Message, state: FSMContext):
    await print_mgpl_7(message)
    await message.answer_photo(open("data/photo/izolirovchik.jpg", 'rb'))
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')


@dp.message_handler(text='Маляр')
async def check_spec_20(message: types.Message, state: FSMContext):
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgptksikh(message)
    await message.answer('http://ptk-skh.minsk.edu.by/ru/main.aspx?guid=2591')
    await print_mgpl_5(message)
    await message.answer('https://licey5.minskedu.gov.by/')
    await print_mgpl_10(message)
    await message.answer('http://licey10.minsk.edu.by/ru/main.aspx?guid=1611')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await message.answer_photo(open("data/photo/Malar.jpg", 'rb'))


@dp.message_handler(text='Штукатур')
async def check_spec_21(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await message.answer_photo(open("data/photo/shtykatyr.jpg", 'rb'))


@dp.message_handler(text='Монтажник каркасно-обшивочных конструкций сухого строительства')
async def check_spec_22(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await message.answer_photo(open("data/photo/montajnicKarkasno.jpg", 'rb'))


@dp.message_handler(text='Каменщик')
async def check_spec_23(message: types.Message, state: FSMContext):
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await print_mgpl_5(message)
    await message.answer('https://licey5.minskedu.gov.by/')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await print_mgpl_10(message)
    await message.answer('http://licey10.minsk.edu.by/ru/main.aspx?guid=1611')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await message.answer_photo(open("data/photo/kamenchik.jpg", 'rb'))


@dp.message_handler(text='Монтажник строительных конструкций')
async def check_spec_24(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer_photo(open("data/photo/montajnicStroit.jpg", 'rb'))


@dp.message_handler(text='Мостовщик')
async def check_spec_25(message: types.Message, state: FSMContext):
    await print_mgpl_10(message)
    await message.answer('http://licey10.minsk.edu.by/ru/main.aspx?guid=1611')
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await message.answer_photo(open("data/photo/mostovchik.jpg", 'rb'))


@dp.message_handler(text='Плотник-бетонщик')
async def check_spec_26(message: types.Message, state: FSMContext):
    await print_mgpl_10(message)
    await message.answer('http://licey10.minsk.edu.by/ru/main.aspx?guid=1611')
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await message.answer_photo(open("data/photo/plotnikBetonchik.jpg", 'rb'))


@dp.message_handler(text='Столяр')
async def check_spec_27(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await print_mgpl_5(message)
    await message.answer('https://licey5.minskedu.gov.by/')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await print_mgpl_14(message)
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')
    await message.answer_photo(open("data/photo/stolar.jpg", 'rb'))


@dp.message_handler(text='Плотник')
async def check_spec_28(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await print_mgpl_5(message)
    await message.answer('https://licey5.minskedu.gov.by/')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await print_mgpl_10(message)
    await message.answer('http://licey10.minsk.edu.by/ru/main.aspx?guid=1611')
    await print_mgpl_12(message)
    await message.answer('http://licey12.minsk.edu.by/ru/main.aspx?guid=1061')
    await message.answer_photo(open("data/photo/plotnik.jpg", 'rb'))


@dp.message_handler(text='Паркетчик')
async def check_spec_29(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer_photo(open("data/photo/parketchik.jpg", 'rb'))
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')


@dp.message_handler(text='Кровельщик по рулонным кровлям из штучных материалов')
async def check_spec_30(message: types.Message, state: FSMContext):
    await print_mgptks(message)
    await message.answer_photo(open("data/photo/krovelchik.jpg", 'rb'))
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')


@dp.message_handler(text='Монтаж наружных трубопроводов')
async def check_spec_31(message: types.Message, state: FSMContext):
    await print_mgptkmiptr(message)
    await message.answer_photo(open("data/photo/montajNaryjnihTryb.jpg", 'rb'))
    await message.answer('http://ptk-mpt.minsk.edu.by/ru/main.aspx?guid=1771')


@dp.message_handler(text='Монтажник технологического оборудования и связанных с ним конструкций')
async def check_spec_32(message: types.Message, state: FSMContext):
    await print_mgptkmiptr(message)
    await message.answer_photo(open("data/photo/montajnicTextOboryd.jpg", 'rb'))
    await message.answer('http://ptk-mpt.minsk.edu.by/ru/main.aspx?guid=1771')


@dp.message_handler(text='Овощевод')
async def check_spec_33(message: types.Message, state: FSMContext):
    await print_mgpl_7(message)
    await message.answer_photo(open("data/photo/ovochevod.jpg", 'rb'))
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')


@dp.message_handler(text='Рабочий зеленого строительства')
async def check_spec_34(message: types.Message, state: FSMContext):
    await print_mgpl_7(message)
    await message.answer_photo(open("data/photo/rabochiyZelenogoStoit.jpg", 'rb'))
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')


@dp.message_handler(text='Цветовод')
async def check_spec_35(message: types.Message, state: FSMContext):
    await print_mgpl_7(message)
    await message.answer_photo(open("data/photo/cvetovod.jpg", 'rb'))
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')


@dp.message_handler(text='Водитель автомобиля')
async def check_spec_36(message: types.Message, state: FSMContext):
    await print_mgptkmiptr(message)
    await message.answer('http://ptk-mpt.minsk.edu.by/ru/main.aspx?guid=1771')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await print_mgpl_14(message)
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')
    await message.answer_photo(open("data/photo/voditelAuto.jpg", 'rb'))


@dp.message_handler(text='Водитель погрузчика')
async def check_spec_37(message: types.Message, state: FSMContext):
    await print_mgpl_14(message)
    await message.answer_photo(open("data/photo/voditelPogruzchika.jpg", 'rb'))
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')


@dp.message_handler(text='Машинист экскаватора')
async def check_spec_38(message: types.Message, state: FSMContext):
    await print_mgpl_14(message)
    await message.answer_photo(open("data/photo/MashinistExkavatora.jpg", 'rb'))
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')


@dp.message_handler(text='Слесарь п оремонту дорожно-строительных машин и тракторов')
async def check_spec_39(message: types.Message, state: FSMContext):
    await print_mgpl_14(message)
    await message.answer_photo(open("data/photo/slesarPoRemontyDorojno.jpg", 'rb'))
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')


@dp.message_handler(text='Тракторист-машинист сельскохозяйтвенного производства')
async def check_spec_40(message: types.Message, state: FSMContext):
    await print_mgpl_14(message)
    await message.answer_photo(open("data/photo/tractorist.jpg", 'rb'))
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')


@dp.message_handler(text='Кузовщик')
async def check_spec_41(message: types.Message, state: FSMContext):
    await print_mgpl_3(message)
    await message.answer_photo(open("data/photo/kuzovchik.jpg", 'rb'))
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')


@dp.message_handler(text='Оператор механизированных и автоматизированных складов')
async def check_spec_42(message: types.Message, state: FSMContext):
    await print_mgptklp_kl(message)
    await message.answer_photo(open("data/photo/operMehanSkladov.jpg", 'rb'))
    await message.answer('http://ptk-logist.minsk.edu.by/ru/main.aspx?guid=2601')


@dp.message_handler(text='Слесарь по ремонту автомобилей')
async def check_spec_43(message: types.Message, state: FSMContext):
    await print_mgptkmiptr(message)
    await message.answer('http://ptk-mpt.minsk.edu.by/ru/main.aspx?guid=1771')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_14(message)
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')
    await message.answer_photo(open("data/photo/slesarAuto.jpg", 'rb'))


@dp.message_handler(text='Кассир билетный')
async def check_spec_44(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/kassirBiletniy.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Монтер пути')
async def check_spec_45(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/monterPyti.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Оператор дефектоскопной тележки')
async def check_spec_46(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/operDefTelejki.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Осмотрщик-ремонтник вагонов')
async def check_spec_47(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/osmotrchikVagonov.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Помощник машиниста дизель-поезда')
async def check_spec_48(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/pomochnikDizel.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Помощник машиниста тепловоза')
async def check_spec_49(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/pomochnikTeplovoza.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Помощник машиниста электровоза')
async def check_spec_50(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/pomochnikElectrovoza.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Помощник машиниста электропоезда')
async def check_spec_51(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/pomochnikMachinistaElectro.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Проводник пассажирсткого вагона')
async def check_spec_52(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/provodnik.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Слесарь по ремонту подвижного состава')
async def check_spec_53(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/slesarPoRemontySostava.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Составитель поездов')
async def check_spec_54(message: types.Message, state: FSMContext):
    await print_mgptkjt(message)
    await message.answer_photo(open("data/photo/sostavitelPoezdov.jpg", 'rb'))
    await message.answer('http://ptk-zht.minsk.edu.by/main.aspx?guid=1761')


@dp.message_handler(text='Микро и наноэлектронные технологии и системы – техник-технолог')
async def check_spec_55(message: types.Message, state: FSMContext):
    await print_mgke(message)
    await message.answer_photo(open("data/photo/Micro&nano.jpg", 'rb'))
    await message.answer('http://mgke.minsk.edu.by/ru/main.aspx?guid=1541')


@dp.message_handler(text='Начальное образование – учитель')
async def check_spec_56(message: types.Message, state: FSMContext):
    await print_mgpk(message)
    await message.answer_photo(open("data/photo/NachObr.jpg", 'rb'))
    await message.answer('http://pedkol.minsk.edu.by/ru/main.aspx?guid=3341')


@dp.message_handler(text='Программное обеспечение информационных технологий – техник-программист')
async def check_spec_57(message: types.Message, state: FSMContext):
    await print_mgke(message)
    await message.answer_photo(open("data/photo/POIT.jpg", 'rb'))
    await message.answer('http://mgke.minsk.edu.by/ru/main.aspx?guid=1541')


@dp.message_handler(text='Программируемые мобильные системы – техник-электроник')
async def check_spec_58(message: types.Message, state: FSMContext):
    await print_mgke(message)
    await message.answer_photo(open("data/photo/ProgMobil.jpg", 'rb'))
    await message.answer('http://mgke.minsk.edu.by/ru/main.aspx?guid=1541')


@dp.message_handler(text='Розничные услуги в банке – специалист по оказанию розничных банковских услуг')
async def check_spec_59(message: types.Message, state: FSMContext):
    await print_mgkso(message)
    await message.answer_photo(open("data/photo/RoznUslVBanke.jpg", 'rb'))
    await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')


@dp.message_handler(text='Почтовая связь – техник почтовой связи')
async def check_spec_60(message: types.Message, state: FSMContext):
    await print_mgkso(message)
    await message.answer_photo(open("data/photo/PochtovayaSvaz.jpg", 'rb'))
    await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')


@dp.message_handler(text='Социальная работа – специалист по социальной работе')
async def check_spec_61(message: types.Message, state: FSMContext):
    await print_mgkso(message)
    await message.answer_photo(open("data/photo/SocRabota.jpg", 'rb'))
    await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')


@dp.message_handler(text='Документоведение и документационное обеспечение управления – секретарь-референт')
async def check_spec_62(message: types.Message, state: FSMContext):
    await print_mgke(message)
    await message.answer_photo(open("data/photo/Secretar.jpg", 'rb'))
    await message.answer('http://mgke.minsk.edu.by/ru/main.aspx?guid=1541')


@dp.message_handler(text='Производство и техническая эксплуатация приборов и аппаратов – техник-электромеханик')
async def check_spec_63(message: types.Message, state: FSMContext):
    await print_mgkso(message)
    await message.answer_photo(open("data/photo/Proizv&Texn.jpg", 'rb'))
    await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')


@dp.message_handler(text='Дошкольное образование – воспитатель дошкольного образования')
async def check_spec_64(message: types.Message, state: FSMContext):
    await print_mgpk(message)
    await message.answer_photo(open("data/photo/DoshkObr.jpg", 'rb'))
    await message.answer('http://pedkol.minsk.edu.by/ru/main.aspx?guid=3341')


@dp.message_handler(text='Демонстратор одежды')
async def check_spec_65(message: types.Message, state: FSMContext):
    await print_mgptklp_kl(message)
    await message.answer_photo(open("data/photo/demOdejdi.jpg", 'rb'))
    await message.answer('http://ptk-logist.minsk.edu.by/ru/main.aspx?guid=2601')


@dp.message_handler(text='Изготовитель художественных изделий из керамики')
async def check_spec_66(message: types.Message, state: FSMContext):
    await print_mgptkdpi(message)
    await message.answer_photo(open("data/photo/izgHudIzd.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Изготовитель художественно-оформительных работ')
async def check_spec_67(message: types.Message, state: FSMContext):
    await print_mgptkdpi(message)
    await message.answer_photo(open("data/photo/ispHudOformRabot.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Оператор компьютерной графики')
async def check_spec_68(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')
    await print_mgptkdpi(message)
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')
    await message.answer_photo(open("data/photo/operKompGraf.jpg", 'rb'))


@dp.message_handler(text='Оператор цифровой печати')
async def check_spec_69(message: types.Message, state: FSMContext):
    await print_mgptkp(message)
    await message.answer_photo(open("data/photo/operCifrPechati.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Оператор электронного набора и вёрски')
async def check_spec_70(message: types.Message, state: FSMContext):
    await print_mgptkp(message)
    await message.answer_photo(open("data/photo/operElectrNaboraIVerstki.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Переплетчик')
async def check_spec_71(message: types.Message, state: FSMContext):
    await print_mgptkp(message)
    await message.answer_photo(open("data/photo/Perepletchik.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Печатник плоской печати')
async def check_spec_72(message: types.Message, state: FSMContext):
    await print_mgptkp(message)
    await message.answer_photo(open("data/photo/pechatnikPloskoy.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Печатник флексографской печати')
async def check_spec_73(message: types.Message, state: FSMContext):
    await print_mgptkp(message)
    await message.answer_photo(open("data/photo/pechatnikFlexgraf.jpg", 'rb'))
    await message.answer('http://ptk-dpi.minsk.edu.by/ru/main.aspx?guid=22861')


@dp.message_handler(text='Резчик по дереву и бересте')
async def check_spec_74(message: types.Message, state: FSMContext):
    await print_mgpl_14(message)
    await message.answer_photo(open("data/photo/RezchikPoDerevy.jpg", 'rb'))
    await message.answer('http://licey14.minsk.edu.by/ru/main.aspx?guid=52381')


@dp.message_handler(text='Фотограф')
async def check_spec_75(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer_photo(open("data/photo/Fotograf.jpg", 'rb'))
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')


@dp.message_handler(text='Закройщик')
async def check_spec_76(message: types.Message, state: FSMContext):
    await print_mgptkshp(message)
    await message.answer_photo(open("data/photo/Zakroichik.jpg", 'rb'))
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')


@dp.message_handler(text='Портной')
async def check_spec_77(message: types.Message, state: FSMContext):
    await print_mgptklp_kl(message)
    await message.answer('http://ptk-logist.minsk.edu.by/ru/main.aspx?guid=2601')
    await print_mgptkshp(message)
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')
    await message.answer_photo(open("data/photo/Portnoi.jpg", 'rb'))


@dp.message_handler(text='Пошивщик изделий')
async def check_spec_78(message: types.Message, state: FSMContext):
    await print_mgptkshp(message)
    await message.answer_photo(open("data/photo/PoshivIzd.jpg", 'rb'))
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')


@dp.message_handler(text='Сборщик обуви')
async def check_spec_79(message: types.Message, state: FSMContext):
    await print_mgptklp(message)
    await message.answer_photo(open("data/photo/sborchikObuvi.jpg", 'rb'))
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')


@dp.message_handler(text='Швея')
async def check_spec_80(message: types.Message, state: FSMContext):
    await print_mgptklp_kl(message)
    await message.answer('http://ptk-logist.minsk.edu.by/ru/main.aspx?guid=2601')
    await print_mgptkshp(message)
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')
    await print_mgptklp(message)
    await message.answer('http://ptk-lpbon.minsk.edu.by/ru/main.aspx?guid=3401')
    await message.answer_photo(open("data/photo/Shveya.jpg", 'rb'))


@dp.message_handler(text='Изготовитель мясных полуфабрикатов')
async def check_spec_81(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer_photo(open("data/photo/izgMysnPF.jpg", 'rb'))
    await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')


@dp.message_handler(text='Кулинар мучных изделий')
async def check_spec_82(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer_photo(open("data/photo/KulinarMuchnIzd.jpg", 'rb'))
    await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')


@dp.message_handler(text='Машинист холодильных установок')
async def check_spec_83(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer_photo(open("data/photo/MashinistHolodnYst.jpg", 'rb'))
    await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')


@dp.message_handler(text='Официант')
async def check_spec_84(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer_photo(open("data/photo/Oficiant.jpg", 'rb'))
    await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')


@dp.message_handler(text='Повар')
async def check_spec_85(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('klass') == '11 классов' and data.get('programm') == 'ПТО':
        await print_mgptkk(message)
        await message.answer_photo(open("data/photo/Povar.jpg", 'rb'))
        await message.answer('http://ptk-kulinarii.minsk.edu.by/ru/main.aspx?guid=1871')
    else:
        await print_mgmtpk(message)
        await message.answer_photo(open("data/photo/Povar.jpg", 'rb'))
        await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')


@dp.message_handler(text='Оператор связи')
async def check_spec_86(message: types.Message, state: FSMContext):
    await print_mgkso(message)
    await message.answer_photo(open("data/photo/operSvyzi.jpg", 'rb'))
    await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')


@dp.message_handler(text='Оператор ЭВМ')
async def check_spec_87(message: types.Message, state: FSMContext):
    await print_mgptklp_kl(message)
    await message.answer('http://ptk-logist.minsk.edu.by/ru/main.aspx?guid=2601')
    await print_mgptkshp(message)
    await message.answer('http://ptkshp.minsk.edu.by/ru/main.aspx?guid=1681')
    await print_mgkso(message)
    await message.answer('http://kso.minsk.edu.by/ru/main.aspx?guid=1231')
    await message.answer_photo(open("data/photo/apparatchik_med.jpg", 'rb'))


@dp.message_handler(text='Контроллер-кассир')
async def check_spec_88(message: types.Message, state: FSMContext):
    await print_mgptkt(message)
    await message.answer('http://ptkt.minsk.edu.by/ru/main.aspx?guid=36311')
    await print_mgptkp(message)
    await message.answer('http://ptk-pol.minsk.edu.by/ru/main.aspx?guid=1551')
    await message.answer_photo(open("data/photo/Kontroller-Kassir.jpg", 'rb'))


@dp.message_handler(text='Продавец')
async def check_spec_89(message: types.Message, state: FSMContext):
    await print_mgptkp(message)
    await message.answer_photo(open("data/photo/Prodavec.jpg", 'rb'))
    await message.answer('http://ptkt.minsk.edu.by/ru/main.aspx?guid=36311')


@dp.message_handler(text='Продавец (книжных коваров)')
async def check_spec_90(message: types.Message, state: FSMContext):
    await print_mgptkt(message)
    await message.answer_photo(open("data/photo/Prodavec_knig.jpg", 'rb'))
    await message.answer('http://ptk-pol.minsk.edu.by/ru/main.aspx?guid=1551')


@dp.message_handler(text='Монтажник электрических подъемников (лифтов)')
async def check_spec_91(message: types.Message, state: FSMContext):
    await print_mgpl_7(message)
    await message.answer_photo(open("data/photo/montajnicLiflov.jpg", 'rb'))
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')


@dp.message_handler(text='Электромеханик по лифтам')
async def check_spec_92(message: types.Message, state: FSMContext):
    await print_mgpl_7(message)
    await message.answer_photo(open("data/photo/electromehanikPoLiftam.jpg", 'rb'))
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')


@dp.message_handler(text='Слесарь-электрик по ремонту элекрооборудования')
async def check_spec_93(message: types.Message, state: FSMContext):
    await print_mgpl_9(message)
    await message.answer_photo(open("data/photo/slesarElectric.jpg", 'rb'))
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')


@dp.message_handler(text='Электромонтер по ремонту и обслуживанию электрооборудования')
async def check_spec_94(message: types.Message, state: FSMContext):
    await print_mgptksikh(message)
    await message.answer('http://ptk-stroj.minsk.edu.by/ru/main.aspx?guid=23591')
    await print_mgptkmiptr(message)
    await message.answer('http://ptk-mpt.minsk.edu.by/ru/main.aspx?guid=1771')
    await print_mgpl_3(message)
    await message.answer('http://licey3.minsk.edu.by/ru/main.aspx?guid=2551')
    await print_mgpl_5(message)
    await message.answer(
        'https://licey5.minskedu.gov.by/%D0%BF%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0%D1%8E%D1%89%D0%B8%D0%BC')
    await print_mgpl_7(message)
    await message.answer('http://licey7.minsk.edu.by/ru/main.aspx?guid=22521')
    await print_mgpl_9(message)
    await message.answer('http://licey9.minsk.edu.by/ru/main.aspx?guid=14001')
    await print_mgpl_14(message)
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')
    await message.answer_photo(open("data/photo/electromontajerPoRemonty.jpg", 'rb'))


@dp.message_handler(text='Элекромонтажник по элекрооборудованию, силовым и осветительным сетям')
async def check_spec_95(message: types.Message, state: FSMContext):
    await print_mgpl_14(message)
    await message.answer('http://licey14.minsk.edu.by/main.aspx?guid=1911')
    await print_mgpl_5(message)
    await message.answer('https://licey5.minskedu.gov.by/')
    await message.answer_photo(open("data/photo/electromontajerPoElectrooborydovaniy.jpg", 'rb'))


@dp.message_handler(text='Элекромонтер охранно-пожарной сигнализации')
async def check_spec_96(message: types.Message, state: FSMContext):
    await print_mgptkmiptr(message)
    await message.answer()
    await print_mgpl_5(message)
    await message.answer()
    await message.answer_photo(open("data/photo/electromontajerPoOhrannoPojarnoy.jpg", 'rb'))


@dp.message_handler(text='Аппаратчик широкого профиля производства химико-фамацевтических препаратов')
async def check_spec_97(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer_photo(open("data/photo/apparatchik_med.jpg", 'rb'))
    await message.answer('http://mtk.minsk.edu.by/ru/main.aspx?guid=1061')


@dp.message_handler(text='Дозировщик медицинских препаратов')
async def check_spec_98(message: types.Message, state: FSMContext):
    await print_mgmtpk(message)
    await message.answer_photo(open("data/photo/dizirovchikMed.jpg", 'rb'))
    await message.answer()
