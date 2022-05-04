from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

markup_klasses = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [KeyboardButton("9 классов")],
                                         [KeyboardButton("11 классов")]
                                     ]
                                     )

markup_programms_9 = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [KeyboardButton("ССО")],
                                           [KeyboardButton("ПТО")],
                                       ]
                                       )
markup_programms_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [KeyboardButton("ССО")],
                                           [KeyboardButton("ПТО")],
                                           [KeyboardButton("УВО")],
                                       ]
                                       )
markup_profil_sso = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton("Микро и наноэлектроника")],
                                            [KeyboardButton("Педагогика")],
                                            [KeyboardButton("Программирование")],
                                            [KeyboardButton("Сфера обслуживания")],
                                            [KeyboardButton("Электроника. Приборы и аппараты")],
                                            [KeyboardButton("Вернуться к выбору программы обучения")]
                                        ]
                                        )

markup_profil_pto = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton("Бытовое обслуживание населения")],
                                            [KeyboardButton("Искусство и дизайн. Полиграфия. Фотография")],
                                            [KeyboardButton("Легкая промышленность. Швейное производство")],
                                            [KeyboardButton("Металообработка. Сварка. Слесарные работы")],
                                            [KeyboardButton("Общественное питание и перерабатывающая промышленность")],
                                            [KeyboardButton("Почтовая связь и ЭВМ")],
                                            [KeyboardButton("Строительство и комунальное хозяйство")],
                                            [KeyboardButton("Торговля и коммерческая деятельность")],
                                            [KeyboardButton("Транспорт")],
                                            [KeyboardButton("Электротехника")],
                                            [KeyboardButton("Вернуться к выбору программы обучения")]
                                        ]
                                        )

markup_profil_pto_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                           keyboard=[
                                               [KeyboardButton("Бытовое обслуживание населения")],
                                               [KeyboardButton("Легкая промышленность. Швейное производство")],
                                               [KeyboardButton("Металообработка. Сварка. Слесарные работы")],
                                               [KeyboardButton(
                                                   "Общественное питание и перерабатывающая промышленность")],
                                               [KeyboardButton("Почтовая связь и ЭВМ")],
                                               [KeyboardButton("Производство медицинских препаратов")],
                                               [KeyboardButton("Строительство и комунальное хозяйство")],
                                               [KeyboardButton("Торговля и коммерческая деятельность")],
                                               [KeyboardButton("Транспорт")],
                                               [KeyboardButton("Электротехника")],
                                               [KeyboardButton("Вернуться к выбору программы обучения")]
                                           ]
                                           )

markup_bit = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [KeyboardButton("Парикмахерское искусство и декоративная косметика")],
                                     [KeyboardButton("Бытовое обслуживание населения")],
                                     [KeyboardButton("Вернуться к списку профилей")]
                                 ]
                                 )

markup_metall = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton("Металообработка")],
                                        [KeyboardButton("Сварочные работы")],
                                        [KeyboardButton("Слесарные профессии")],
                                        [KeyboardButton("Вернуться к списку профилей")]
                                    ]
                                    )

markup_metall_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [KeyboardButton("Сварочные работы")],
                                           [KeyboardButton("Слесарные профессии")],
                                           [KeyboardButton("Вернуться к списку профилей")]
                                       ]
                                       )

markup_stroi = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [KeyboardButton("Отделочные работы")],
                                       [KeyboardButton("Строительно-монтажные и ремонтные работы")],
                                       [KeyboardButton("Работы по дереву")],
                                       [KeyboardButton("Строительные технические работы")],
                                       [KeyboardButton("Садово-парковое строительство")],
                                       [KeyboardButton("Вернуться к списку профилей")]
                                   ]
                                   )

markup_stroi_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [KeyboardButton("Отделочные работы")],
                                          [KeyboardButton("Строительно-монтажные и ремонтные работы")],
                                          [KeyboardButton("Вернуться к списку профилей")]
                                      ]
                                      )

markup_transport = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [KeyboardButton("Автомобильный транспорт")],
                                           [KeyboardButton("Железнодорожный транспорт")],

                                           [KeyboardButton("Вернуться к списку профилей")]
                                       ]
                                       )

markup_micro = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [KeyboardButton(
                                           "Микро и наноэлектронные технологии и системы – техник-технолог")],
                                       [KeyboardButton("Вернуться к списку профилей")]
                                   ]
                                   )

markup_ped = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [KeyboardButton("Дошкольное образование – воспитатель дошкольного образования")],
                                     [KeyboardButton("Начальное образование – учитель")],
                                     [KeyboardButton("Вернуться к списку профилей")]
                                 ]
                                 )

markup_ped_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton(
                                            "Дошкольное образование – воспитатель дошкольного образования")],
                                        [KeyboardButton("Вернуться к списку профилей")]
                                    ]
                                    )

markup_prog = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [KeyboardButton(
                                          "Программное обеспечение информационных технологий – техник-программист")],
                                      [KeyboardButton("Программируемые мобильные системы – техник-электроник")],
                                      [KeyboardButton("Вернуться к списку профилей")]
                                  ]
                                  )

markup_obsl = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [KeyboardButton(
                                          "Розничные услуги в банке – специалист по оказанию розничных банковских услуг")],
                                      [KeyboardButton("Почтовая связь – техник почтовой связи")],
                                      [KeyboardButton("Социальная работа – специалист по социальной работе")], 
                                      [KeyboardButton("Вернуться к списку профилей")]
                                  ]
                                  )

markup_electr = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton(
                                            "Производство и техническая эксплуатация приборов и аппаратов – "
                                            "техник-электромеханик")],
                                        [KeyboardButton("Вернуться к списку профилей")]
                                    ]
                                    )

markup_parik = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [KeyboardButton("Парикмахер")],
                                       [KeyboardButton("Мастер по маникюру")],
                                       [KeyboardButton("Мастер по педикюру")],
                                       [KeyboardButton("Визажист")],
                                       [KeyboardButton("Вернуться к списку профилей")]
                                   ]
                                   )

markup_parik_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [KeyboardButton("Парикмахер")],
                                          [KeyboardButton("Мастер по маникюру")],
                                          [KeyboardButton("Вернуться к списку профилей")]
                                      ]
                                      )

markup_bitovoe = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [KeyboardButton("Вернуться к списку профилей")]
                                     ]
                                     )

markup_dizign = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton("Демонстратор одежды")],
                                        [KeyboardButton("Изготовитель художественных изделий из керамики")],
                                        [KeyboardButton("Изготовитель художественно-оформительных работ")],
                                        [KeyboardButton("Оператор компьютерной графики")],
                                        [KeyboardButton("Оператор цифровой печати")],
                                        [KeyboardButton("Оператор электронного набора и вёрски")],
                                        [KeyboardButton("Переплетчик")],
                                        [KeyboardButton("Печатник плоской печати")],
                                        [KeyboardButton("Печатник флексографской печати")],
                                        [KeyboardButton("Резчик по дереву и бересте")],
                                        [KeyboardButton("Вернуться к списку профилей")]
                                    ]
                                    )

markup_legk_prom = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [KeyboardButton("Закройщик")],
                                           [KeyboardButton("Портной")],
                                           [KeyboardButton("Пошивщик изделий")],
                                           [KeyboardButton("Сборщик обуви")],
                                           [KeyboardButton("Швея")],
                                           [KeyboardButton("Вернуться к списку профилей")]
                                       ]
                                       )

markup_legk_prom_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                          keyboard=[
                                              [KeyboardButton("Портной")],
                                              [KeyboardButton("Вернуться к списку профилей")]
                                          ]
                                          )

markup_ob_pit = ReplyKeyboardMarkup(resize_keyboard=True,
                                    keyboard=[
                                        [KeyboardButton("Изготовитель мясных полуфабрикатов")],
                                        [KeyboardButton("Кулинар мучных изделий")],
                                        [KeyboardButton("Машинист холодильных установок")],
                                        [KeyboardButton("Официант")],
                                        [KeyboardButton("Повар")],
                                        [KeyboardButton("Вернуться к списку профилей")]
                                    ]
                                    )
''''''
markup_post = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [KeyboardButton("Оператор связи")],
                                      [KeyboardButton("Оператор ЭВМ")],
                                      [KeyboardButton("Вернуться к списку профилей")]
                                  ]
                                  )

markup_torg = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [KeyboardButton("Контроллер-кассир")],
                                      [KeyboardButton("Продавец")],
                                      [KeyboardButton("Продавец (книжных коваров)")],
                                      [KeyboardButton("Вернуться к списку профилей")]
                                  ]
                                  )

markup_electriotehnika = ReplyKeyboardMarkup(resize_keyboard=True,
                                             keyboard=[
                                                 [KeyboardButton("Монтажник электрических подъемников (лифтов)")],
                                                 [KeyboardButton("Электромеханик по лифтам")],
                                                 [KeyboardButton("Слесарь-электрик по ремонту элекрооборудования")],
                                                 [KeyboardButton(
                                                     "Электромонтер по ремонту и обслуживанию электрооборудования")],
                                                 [KeyboardButton(
                                                     "Элекромонтажник по элекрооборудованию, силовым и осветительным сетям")],
                                                 [KeyboardButton("Элекромонтер охранно-пожарной сигнализации")],
                                                 [KeyboardButton("Вернуться к списку профилей")]
                                             ]
                                             )

markup_metaoobrabotka = ReplyKeyboardMarkup(resize_keyboard=True,
                                            keyboard=[
                                                [KeyboardButton("Контроллер станочных и слесарных работ")],
                                                [KeyboardButton("Оператор станков с ЧПУ")],
                                                [KeyboardButton("Токарь")],
                                                [KeyboardButton("Фрезеровщик")],
                                                [KeyboardButton("Шлифовщик")],
                                                [KeyboardButton("Вернуться к списку профилей")]
                                            ]
                                            )

markup_svarochner_raboty = ReplyKeyboardMarkup(resize_keyboard=True,
                                               keyboard=[
                                                   [KeyboardButton("Электрогазосварщик")],
                                                   [KeyboardButton(
                                                       "Элекросварщик на автоматических и полуавтоматических машинах")],
                                                   [KeyboardButton("Элекросварщик ручной сварки")],
                                                   [KeyboardButton("Вернуться к списку профилей")]
                                               ]
                                               )

markup_slesarnie_professii = ReplyKeyboardMarkup(resize_keyboard=True,
                                                 keyboard=[
                                                     [KeyboardButton("Слесарь-инструментальщик")],
                                                     [KeyboardButton("Слесарь механосборочных работ")],
                                                     [KeyboardButton("Слесарь-ремонтник")],
                                                     [KeyboardButton("Слесарь-сбощик бытовой техники")],
                                                     [KeyboardButton("Вернуться к списку профилей")]
                                                 ]
                                                 )

markup_otdel = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [KeyboardButton("Маляр")],
                                       [KeyboardButton(
                                           "Монтажник каркасно-обшивочных конструкций сухого строительства")],
                                       [KeyboardButton("Вернуться к списку профилей")]
                                   ]
                                   )
markup_otdel_11 = ReplyKeyboardMarkup(resize_keyboard=True,
                                      keyboard=[
                                          [KeyboardButton("Маляр")],
                                          [KeyboardButton("Штукатур")],
                                          [KeyboardButton("Вернуться к списку профилей")]
                                      ]
                                      )

markup_stroit_mont = ReplyKeyboardMarkup(resize_keyboard=True,
                                         keyboard=[
                                             [KeyboardButton("Каменщик")],
                                             [KeyboardButton("Монтажник строительных конструкций")],
                                             [KeyboardButton("Мостовщик")],
                                             [KeyboardButton("Плотник-бетонщик")],
                                             [KeyboardButton("Вернуться к списку профилей")]
                                         ]
                                         )

markup_rab_derevo = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton("Столяр")],
                                            [KeyboardButton("Плотник")],
                                            [KeyboardButton("Вернуться к списку профилей")]
                                        ]
                                        )

markup_stroit_tex = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [KeyboardButton("Монтаж наружных трубопроводов")],
                                            [KeyboardButton(
                                                "Монтажник технологического оборудования и связанных с ним конструкций")],
                                            [KeyboardButton("Вернуться к списку профилей")]
                                        ]
                                        )

markup_sad = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [KeyboardButton("Овощевод")],
                                     [KeyboardButton("Вернуться к списку профилей")]
                                 ]
                                 )

markup_auto = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [KeyboardButton("Водитель автомобиля")],
                                      [KeyboardButton("Водитель погрузчика")],
                                      [KeyboardButton("Машинист экскаватора")],
                                      [KeyboardButton("Слесарь п оремонту дорожно-строительных машин и тракторов")],
                                      [KeyboardButton("Тракторист-машинист сельскохозяйтвенного производства")],
                                      [KeyboardButton("Кузовщик")],
                                      [KeyboardButton("Оператор механизированных и автоматизированных складов")],
                                      [KeyboardButton("Слесарь по ремонту автомобилей")],
                                      [KeyboardButton("Вернуться к списку профилей")]
                                  ]
                                  )

markup_depo = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [KeyboardButton("Кассир билетный")],
                                      [KeyboardButton("Монтер пути")],
                                      [KeyboardButton("Оператор дефектоскопной тележки")],
                                      [KeyboardButton("Помощник машиниста дизель-поезда")],
                                      [KeyboardButton("Помощник машиниста тепловоза")],
                                      [KeyboardButton("Помощник машиниста электровоза")],
                                      [KeyboardButton("Помощник машиниста электропоезда")],
                                      [KeyboardButton("Проводник пассажирсткого вагона")],
                                      [KeyboardButton("Слесарь по ремонту подвижного состава")],
                                      [KeyboardButton("Вернуться к списку профилей")]
                                  ]
                                  )

markup_med = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                     [KeyboardButton("Вернуться к списку профилей")]
                                 ]
                                 )



'''
markup_ = ReplyKeyboardMarkup(resize_keyboard=True,
                              keyboard=[
                                  [KeyboardButton],
                                  [KeyboardButton],
                                  [KeyboardButton],
                                  [KeyboardButton],
                                  [KeyboardButton("Вернуться к списку профилей")]
                              ]
                              )
'''
