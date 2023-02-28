from datetime import date

from db.models import Products, Platforms, Publishers, ContentRatings, Genres




platform1 = Platforms.objects.create(title='PC')
platform2 = Platforms.objects.create(title='PlayStation')
platform3 = Platforms.objects.create(title='Xbox')
platform4 = Platforms.objects.create(title='Nintendo Switch')
platform5 = Platforms.objects.create(title='Mobile')
platform6 = Platforms.objects.create(title='Mac OS')





rating1 = ContentRatings.objects.create(title='6+', ageLimit=6, description='Подходит для детей от 6 лет и старше')
rating2 = ContentRatings.objects.create(title='12+', ageLimit=12, description='Подходит для детей от 12 лет и старше')
rating3 = ContentRatings.objects.create(title='18+', ageLimit=18, description='Подходит только для взрослых')



genre1 = Genres.objects.create(title = 'Симулятор')
genre2 = Genres.objects.create(title = 'Спортивный симулятор')
genre3 = Genres.objects.create(title = 'Игровое моделирование')
genre4 = Genres.objects.create(title = 'Cпорт')
genre5 = Genres.objects.create(title = 'Стратегия')
genre6 = Genres.objects.create(title = 'Шутер от первого лица')
genre7 = Genres.objects.create(title = 'Королевская битва')
genre8 = Genres.objects.create(title = 'Cимулятор жизни')
genre9 = Genres.objects.create(title = 'Приключенческий боевик')
genre10 = Genres.objects.create(title = 'Файтинг')
genre11 = Genres.objects.create(title = 'Приключение') 
genre12 = Genres.objects.create(title = 'Боевик/ролевая игра')
genre13 = Genres.objects.create(title = 'Action')
genre14 = Genres.objects.create(title = 'Тактический шутер')
genre15 = Genres.objects.create(title = 'Открытый мир')
genre16 = Genres.objects.create(title = 'Платформер')
genre17 = Genres.objects.create(title = 'Шутер')
genre18 = Genres.objects.create(title = 'Песочница')
genre19 = Genres.objects.create(title = 'Шутер от третьего лица')
genre20 = Genres.objects.create(title = 'Вестерн')
genre21 = Genres.objects.create(title = 'Экшен')
genre22 = Genres.objects.create(title = 'Ролевая игра')
genre23 = Genres.objects.create(title = 'MMORPG')
genre24 = Genres.objects.create(title = 'Фэнтези')
genre25 = Genres.objects.create(title = 'Круши и руби')
genre26 = Genres.objects.create(title = 'Коллекционная карточная игра')
genre27 = Genres.objects.create(title = 'Гоночная игра')
genre28 = Genres.objects.create(title = 'RPG')
genre29 = Genres.objects.create(title = 'Головоломка')
genre30 = Genres.objects.create(title = 'Музыкальная видеоигра')
genre31 = Genres.objects.create(title = 'фитнес-игра')
genre32 = Genres.objects.create(title = 'Ужас выживания')
genre33 = Genres.objects.create(title = 'Стелс')
genre = Genres.objects.create(title = '')









publisher1 = Publishers.objects.create(title='Electronic Arts (EA)')
publisher2 = Publishers.objects.create(title='Ubisoft')
publisher3 = Publishers.objects.create(title='Rockstar Games')
publisher4 = Publishers.objects.create(title='Square Enix')
publisher5 = Publishers.objects.create(title='Activision Blizzard')




#price = валюта в тг


product1 = Products.objects.create(
    title = 'FIFA 22',
    description = 'FIFA 22 — видеоигра-симулятор футбола, выпущенная Electronic Arts. Это последняя часть серии FIFA с новой игровой механикой, обновленными командами и игроками и улучшенной графикой.',
    publisher = publisher1,
    releaseDate = date(2021, 9, 27),
    price = 19999,
    contentRating = rating1, 
    isAvailable = True
)
product1.platform.add(platform1, platform2, platform3, platform4)

product1.genre.add(genre1, genre2, genre3)


product2 = Products.objects.create(
    title = 'Madden NFL 22',
    description = 'Madden NFL 22 — видеоигра в американский футбол, основанная на Национальной футбольной лиге, разработанная EA Tiburon и опубликованная Electronic Arts.',
    publisher = publisher1,
    releaseDate = date(2021, 8, 17),
    price = 19999,
    contentRating = rating1,
    isAvailable = True
)
product2.platform.add(platform1, platform2, platform3)

product2.genre.add(genre1, genre2, genre3, genre4, genre5)



product3 = Products.objects.create(
    title = 'Apex Legends',
    description = 'Apex Legends — компьютерная игра в жанре многопользовательского геройского шутера от первого лица и королевской битвы.',
    publisher = publisher1,
    releaseDate = date(2019, 2, 4),
    price = 0,
    contentRating = rating2,
    isAvailable = True
)
product3.platform.add(platform1, platform2, platform3, platform4, platform5)

product3.genre.add(genre6, genre7)



product4 = Products.objects.create(
    title = 'Battlefield 2042',
    description = 'Battlefield 2042 — компьютерная игра в жанре шутера от первого лица, разработанная шведской компанией DICE и изданная компанией Electronic Arts. Часть серии игр Battlefield.',
    publisher = publisher1,
    releaseDate = date(2021, 10, 6),
    price = 19999,
    contentRating = rating3,
    isAvailable =  True
)
product4.platform.add(platform1, platform2, platform3)

product4.genre.add(genre6)



product5 = Products.objects.create(
    title = 'The Sims 4',
    description = 'The Sims 4 — однопользовательская компьютерная игра в жанре симулятора жизни, четвёртая по счёту из серии игр The Sims, разработанная компанией Maxis и издаваемая Electronic Arts для Windows и macOS.',
    publisher = publisher1,
    releaseDate = date(2014, 9, 2),
    price = 0,
    contentRating = rating3,  
    isAvailable = True
)
product5.platform.add(platform1, platform2, platform3, platform6)

product5.genre.add(genre8)


product6 = Products.objects.create(
    title = "Assassin's Creed Valhalla",
    description = "Assassin's Creed Valhalla — компьютерная игра в жанре action/RPG, разработанная студией Ubisoft Montreal и изданная компанией Ubisoft. Является двенадцатой игрой в серии игр Assassin’s Creed.",
    publisher = publisher2,
    releaseDate = date(2020, 11, 10),
    price = 14699,
    contentRating = rating3, 
    isAvailable = True
)
product6.platform.add(platform1, platform2, platform3)

product6.genre.add(genre9, genre10, genre11, genre12)



product7 = Products.objects.create(
    title = 'Far Cry 6',
    description = 'Far Cry 6 — компьютерная игра в жанре шутера от первого лица и action-adventure, разработанная студией Ubisoft Toronto и изданная компанией Ubisoft. Является шестой основной игрой из одноимённой серии.',
    publisher = publisher2, 
    releaseDate = date(2021, 10, 7),
    price = 14699,
    contentRating = rating3, 
    isAvailable = True
)
product7.platform.add(platform1, platform2, platform3)

product7.genre.add(genre6, genre13)


product8 = Products.objects.create(
    title = 'Watch Dogs: Legion',
    description = 'Watch Dogs: Legion — компьютерная игра в жанре Action-adventure, разработанная Ubisoft Toronto и издаваемая Ubisoft. Это третья часть серии Watch Dogs и продолжение Watch Dogs 2. Действие игры разворачивается в вымышленном представлении Лондона с открытым миром и видом от третьего лица.',
    publisher = publisher2,
    releaseDate = date(2020, 10, 29),
    price = 14699, 
    contentRating = rating3, 
    isAvailable = True
)
product8.platform.add(platform1, platform2, platform3)

product8.genre.add(genre9)


product9 = Products.objects.create(
    title = "Tom Clancy's Rainbow Six Siege",
    description = "Tom Clancy’s Rainbow Six Siege — тактический шутер от первого лица, разработанный Ubisoft для Windows, Xbox One и PlayStation 4. Игра была анонсирована Ubisoft 9 июня 2014 года на E3 и выпущена 1 декабря 2015 года, а ровно через пять лет, 1 декабря 2020 года, игра вышла для PlayStation 5 и Xbox Series X/S.",
    publisher = publisher2,
    releaseDate = date(2015, 12, 1),
    price = 4899,
    contentRating = rating3, 
    isAvailable = True
)
product9.platform.add(platform1, platform2, platform3)

product9.genre.add(genre14)



product10 = Products.objects.create(
    title = 'Immortals Fenyx Rising',
    description = "Immortals Fenyx Rising — игра в жанре action-adventure с перспективой от третьего лица, разработанная компанией Ubisoft Quebec, издателем является Ubisoft. ",
    publisher = publisher2,
    releaseDate = date(2019, 6, 10),
    price = 14699,
    contentRating = rating2,
    isAvailable = True
)

product10.platform.add(platform1, platform2, platform3, platform4)

product10.genre.add(genre9, genre10, genre11, genre15, genre17)




product11 = Products.objects.create(
    title = 'Grand Theft Auto V',
    description = "Grand Theft Auto V — компьютерная игра в жанре action-adventure с открытым миром, разработанная компанией Rockstar North и изданная компанией Rockstar Games.",
    publisher = publisher3 ,
    releaseDate = date(2013, 9, 17),
    price = 8100,
    contentRating = rating3, 
    isAvailable = True
)
product11.platform.add(platform1, platform2, platform3)

product11.genre.add(genre18, genre15, genre9, genre19, genre11)



product12 = Products.objects.create(
    title = "Red Dead Redemption 2",
    description = "Red Dead Redemption 2 — компьютерная игра в жанрах action-adventure и шутера от третьего лица с открытым миром, разработанная Rockstar Studios и выпущенная Rockstar Games для консолей PlayStation 4 и Xbox One 26 октября 2018 года и для персональных компьютеров под управлением Windows 5 ноября 2019 года.",
    publisher = publisher3,
    releaseDate = date(2018, 10, 26),
    price = 19999, 
    contentRating = rating3, 
    isAvailable = True
)
product12.platform.add(platform1, platform2, platform3)

product12.genre.add(genre15, genre9, genre20, genre6, genre19)


product13 = Products.objects.create(
    title = "Max Payne 3",
    description = "Max Payne 3 — компьютерная игра в жанре шутера от третьего лица, продолжение игрового сериала Max Payne. Новая игра была анонсирована издательством Rockstar Games 23 марта 2009 года. Релиз трейлера к игре состоялся 14 сентября 2011 года.",
    publisher = publisher3,
    releaseDate = date(2012, 5, 15),
    price = 2650,
    contentRating = rating3, 
    isAvailable = True
)
product13.platform.add(platform1, platform2, platform3, platform6)

product13.genre.add(genre19)




product14 = Products.objects.create(
    title = "Bully",
    description = "Bully; также известна как Canis Canem Edit — компьютерная игра в жанре приключенческого боевика с видом от третьего лица и открытым миром, разработанная Rockstar Vancouver и выпущенная Rockstar Games в октябре 2006 года для игровой приставки PlayStation 2.",
    publisher = publisher3,
    releaseDate = date(2006, 10, 17),
    price = 2400,
    contentRating = rating3, 
    isAvailable = True
)
product14.platform.add(platform1, platform2, platform3, platform5)

product14.genre.add(genre15, genre9)



product15 = Products.objects.create(
    title = "Grand Theft Auto: San Andreas",
    description = "Grand Theft Auto: San Andreas — компьютерная игра в жанре action-adventure, разработанная студией Rockstar North и изданная компанией Rockstar Games; пятая по счёту и третья трёхмерная игра во франшизе Grand Theft Auto.",
    publisher = publisher3,
    releaseDate = date(2004, 10, 26),
    price = 4999,
    contentRating = rating3,
    isAvailable = False
)
product15.platform.add(platform1, platform2, platform3, platform5, platform6)

product15.genre.add(genre9)




product16 = Products.objects.create(
    title = "Final Fantasy VII Remake",
    description = "Final Fantasy VII Remake — компьютерная игра в жанре Action/RPG, разработанная и выпущенная компанией Square Enix для PlayStation 4 в 2020 году, ремейк одноимённой игры 1997 года.",
    publisher = publisher4,
    releaseDate = date(2020, 4, 10),
    price = 29900,
    contentRating = rating3,
    isAvailable = True
)
product16.platform.add(platform1, platform2)

product16.genre.add(genre21, genre11, genre22)




product17 = Products.objects.create(
    title = "Kingdom Hearts III",
    description = "Kingdom Hearts III — компьютерная игра в жанре ролевой боевик, разработанная компанией Square Enix для PlayStation 4 и Xbox One. Это первая игра в серии которая посетила консоль от Microsoft и первая вышедшая сразу на две платформы.",
    publisher = publisher4,
    releaseDate = date(2019, 1, 25),
    price = 25080,
    contentRating = rating2,
    isAvailable = True
)
product17.platform.add(platform1, platform2, platform3, platform4)

product17.genre.add(genre12, genre22)





product18 = Products.objects.create(
    title = "Marvel's Avengers",
    description = "Marvel's Avengers — компьютерная игра в жанре action-adventure, разработанная Crystal Dynamics в сотрудничестве с Marvel Games и изданная Square Enix. В основе игры лежит серия комиксов «Мстители» Marvel Comics. Выход игры состоялся 4 сентября 2020 года для PlayStation 4, Xbox One и Windows.",
    publisher = publisher4,
    releaseDate = date(2020, 8, 14),
    price = 13000,
    contentRating = rating2, 
    isAvailable = True
)
product18.platform.add(platform1, platform2, platform3)

product18.genre.add(genre21, genre22, genre11)




product19 = Products.objects.create(
    title = "Dragon Quest XI S: Echoes of an Elusive Age - Definitive Edition",
    description = "Dragon Quest XI: Echoes of an Elusive Age — ролевая видеоигра от Square Enix. Одиннадцатая часть многолетней серии видеоигр Dragon Quest была выпущена в Японии для Nintendo 3DS и PlayStation 4 в июле 2017 года и по всему миру для PlayStation 4 и Windows в сентябре 2018 года.",
    publisher = publisher4,
    releaseDate = date(2017, 7, 29),
    price = 16000,
    contentRating = rating2, 
    isAvailable = True
)
product19.platform.add(platform1, platform2, platform3, platform4)

product19.genre.add(genre11, genre22)



product20 = Products.objects.create(
    title = "Shadow of the Tomb Raider",
    description = "Shadow of the Tomb Raider — компьютерная игра из серии Tomb Raider в жанре action-adventure с видом от третьего лица, разработанная канадской студией Eidos Montreal, известной по ролевым стелс-экшенам Thief, Deus Ex: Human Revolution и Deus Ex: Mankind Divided, а не создателями предыдущих частей Tomb Raider из Crystal ",
    publisher = publisher4,
    releaseDate = date(2018, 9, 12),
    price = 13230, 
    contentRating = rating3,
    isAvailable = True
)
product20.platform.add(platform1, platform2, platform3, platform6)

product20.genre.add(genre11, genre21)



product21 = Products.objects.create(
    title = "Call of Duty: Vanguard",
    description = "Call of Duty: Vanguard — компьютерная игра в жанре шутера от первого лица, восемнадцатая в серии Call of Duty. Релиз игры состоялся 5 ноября 2021 года для Windows, PlayStation 4, PlayStation 5, Xbox One и Xbox Series X/S.",
    publisher = publisher5,
    releaseDate = date(2021, 11, 5),
    price = 13795,
    contentRating = rating3,
    isAvailable = True
)
product21.platform.add(platform1, platform2, platform3)

product21.genre.add(genre6)




product22 = Products.objects.create(
    title = "World of Warcraft",
    description = "World of Warcraft — массовая многопользовательская ролевая онлайн-игра, разработанная и издаваемая компанией Blizzard Entertainment. Действие World of Warcraft происходит в фэнтезийной вселенной Warcraft.",
    publisher = publisher5,
    releaseDate =  date(2004, 11, 23),
    price = 3400,
    contentRating = rating2,
    isAvailable = True
)
product22.platform.add(platform1, platform6)
 
product22.genre.add(genre22, genre23, genre24)


product23 = Products.objects.create(
    title = "Overwatch 2",
    description = "Overwatch 2 — многопользовательская бесплатная компьютерная игра в жанре геройского шутера от первого лица, разрабатываемая и издаваемая компанией Blizzard Entertainment. ",
    publisher = publisher5,
    releaseDate = date(2022, 10, 4),
    price = 17949,
    contentRating = rating2,
    isAvailable = True
)
product23.platform.add(platform1, platform2, platform3, platform4)

product23.genre.add(genre6)




product24 = Products.objects.create(
    title = "Diablo III: Reaper of Souls",
    description = "Diablo III: Reaper of Souls — первое дополнение к игре жанра Action/RPG — Diablo III. Оно было представлено на Gamescom 2013 и разработано для платформ ПК и Mac, позднее выпущено на консолях нового поколения. Релиз дополнения в России и СНГ состоялся 15 апреля 2014 года.",
    publisher = publisher5,
    releaseDate = date(2014, 3, 25),
    price = 14231,
    contentRating = rating3, 
    isAvailable = True
)
product24.platform.add(platform2, platform1, platform3, platform4, platform6)

product24.genre.add(genre25)



product25 = Products.objects.create(
    title = "Hearthstone",
    description = "Hearthstone — коллекционная карточная онлайн-игра по мотивам вселенной Warcraft, разработанная компанией Blizzard Entertainment и распространяемая по модели free-to-play. Игра была выпущена для персональных компьютеров 11 марта 2014 года. Позже она была портирована на платформы iOS и Android.",
    publisher = publisher5,
    releaseDate = date(2014, 3, 11),
    price = 8972,
    contentRating = rating2, 
    isAvailable = True
)
product25.platform.add(platform1, platform6, platform5)

product25.genre.add(genre26)




product26 = Products.objects.create(
    title = "Need for Speed Heat",
    description = "Need for Speed Heat — компьютерная игра в жанре аркадных автогонок, разработанная шведской студией Ghost Games и изданная Electronic Arts для консолей PlayStation 4 и Xbox One, а также для ПК под управлением Windows. Двадцать четвёртая игра в одноимённой серии, выпуск которой состоялся 8 ноября 2019 года. ",
    publisher = publisher1,
    releaseDate = date(2019, 10, 16),
    price = 27500,
    contentRating = rating3, 
    isAvailable = True
)
product26.platform.add(platform1, platform2, platform3)

product26.genre.add(genre27, genre13, genre11)




product27 = Products.objects.create(
    title = "Mass Effect Legendary Edition",
    description = "Mass Effect: Legendary Edition — сборник компьютерных игр в жанре шутера от третьего лица с элементами action/RPG, представляющий собой ремастерированные версии трёх игр серии Mass Effect: Mass Effect, Mass Effect 2 и Mass Effect 3. ",
    publisher = publisher1,
    releaseDate = date(2021, 4, 30),
    price = 19999,
    contentRating = rating3, 
    isAvailable = True
)
product27.platform.add(platform1, platform2, platform3)

product27.genre.add(genre13, genre11, genre19, genre28)





product28 = Products.objects.create(
    title = "Skate 3",
    description = "Skate 3 — видеоигра, симулятор скейтбординга, разработанный EA Black Box и выпущенный Electronic Arts для консолей Xbox 360 и PlayStation 3 в мае 2010 года. Третья и последняя игра в одноименной серии, сиквел игры Skate 2.",
    publisher = publisher1,
    releaseDate = date(2010, 5, 11),
    price = 7287,
    contentRating = rating2, 
    isAvailable = True
)
product28.platform.add(platform2, platform3)

product28.genre.add(genre2, genre3)





product29 = Products.objects.create(
    title = "Titanfall 2",
    description = "Titanfall 2 — компьютерная игра в жанре шутера от первого лица с элементами симулятора меха, разработанная компанией Respawn Entertainment и изданная Electronic Arts. Является сиквелом игры Titanfall, выпущенной в 2014 году.",
    publisher = publisher1,
    releaseDate = date(2016, 10, 28),
    price = 11700,
    contentRating = rating3, 
    isAvailable = True
)
product29.platform.add(platform1, platform2, platform3)

product29.genre.add(genre6)





product30 = Products.objects.create(
    title = "Star Wars Jedi: Fallen Order",
    description = "Star Wars Jedi: Fallen Order (в России издаётся под названием «Звёздные войны. Джедаи: Павший Орден») — компьютерная игра в жанре action-adventure, разработанная американской студией Respawn Entertainment и изданная компанией Electronic Arts в ноябре 2019 года для Windows, PlayStation 4 и Xbox One; в июне 2021 года игра была перевыпущена для консолей девятого поколения — PlayStation 5 и Xbox Series X/S. Это первая игра Respawn Entertainment по вселенной «Звёздных войн». Действие Fallen Order происходит в промежутке между событиями фильмов «Месть ситхов» и «Новая надежда». Галактическая Империя истребила большинство членов Ордена джедаев; молодой падаван Кэл Кестис, один из немногих выживших, вместе с новыми друзьями и союзниками отправляется в путешествие по Галактике в надежде восстановить Орден. По мере прохождения игры герой посещает различные планеты, где должен сражаться с теми или иными врагами, исследовать локации и решать головоломки. Боевая система Fallen Order требует от игрока своевременно блокировать удары врагов световым мечом, парировать или уворачиваться от них.",
    publisher = publisher1,
    releaseDate = date(2019, 11, 11),
    price = 15500,
    contentRating = rating3, 
    isAvailable = True
)
product30.platform.add(platform1, platform2, platform3)

product30.genre.add(genre29, genre9, genre22, genre16, genre10, genre11)





product31 = Products.objects.create(
    title = "Ghost Recon Breakpoint",
    description = "Tom Clancy’s Ghost Recon Breakpoint — компьютерная игра в жанре тактического шутера, разработанная компанией Ubisoft Paris и изданная Ubisoft. Игра была анонсирована 9 мая и вышла 4 октября 2019 года для платформ Windows, PlayStation 4 и Xbox One.",
    publisher = publisher2,
    releaseDate = date(2019, 7, 26),
    price = 14699,
    contentRating = rating3, 
    isAvailable = True
)
product31.platform.add(platform1, platform2, platform3)

product31.genre.add(genre14, genre11, genre22)




product32 = Products.objects.create(
    title = "The Division 2",
    description = "Tom Clancy’s The Division 2 — компьютерная игра в жанре TPS, вторая по счёту из серии игр The Division, которая является продолжением Tom Clancy’s The Division, была разработана шведской студией Massive Entertainment и издана компанией Ubisoft.",
    publisher = publisher2,
    releaseDate = date(2019, 3, 1),
    price = 7349,
    contentRating = rating3, 
    isAvailable = True
)
product32.platform.add(platform1, platform2, platform3)

product32.genre.add(genre13, genre28)





product33 = Products.objects.create(
    title = "For Honor ",
    description = "For Honor (с англ. — «За честь») — компьютерная игра в жанре action с видом от третьего лица. Выпущена компанией Ubisoft для ПК, PlayStation 4 и Xbox One. В For Honor игроки могут управлять различными формами исторических солдат и воителей, из различных фракций, а именно: викингов, рыцарей, самураев, У Линь и фракцией иноземцев. Действие игры происходит в средневековом сеттинге.",
    publisher = publisher2,
    releaseDate = date(2017, 2, 14),
    price = 3675,
    contentRating = rating3, 
    isAvailable = True
)
product33.platform.add(platform1, platform2, platform3)

product33.genre.add(genre13)





product34 = Products.objects.create(
    title = "Just Dance 2022",
    description = "Just Dance 2022 — танцевальная ритм-игра, разработанная и изданная компанией Ubisoft.",
    publisher = publisher2,
    releaseDate = date(2021, 11, 4),
    price = 31990,
    contentRating = rating1, 
    isAvailable = True
)
product34.platform.add(platform2, platform3, platform4)

product34.genre.add(genre30, genre31, genre13)





product35 = Products.objects.create(
    title = "Prince of Persia: The Sands of Time Remake",
    description = "Признанный критиками Prince of Persia: The Sands of Time вернулся! Впервые переделано Ubisoft, переживите эту легендарную историю или откройте для себя ее заново. Отправляйтесь в путешествие в качестве принца, чтобы спасти свое королевство от коварного визиря в этой вневременной классике.",
    publisher = publisher2,
    releaseDate = date(2023, 12, 31),
    price = 17896,
    contentRating = rating3, 
    isAvailable = False
)
product35.platform.add(platform1, platform2, platform3)

product35.genre.add(genre21, genre11)






product36 = Products.objects.create(
    title = "L.A. Noire",
    description = "L.A. Noire — компьютерная игра в жанре action-adventure/симулятор детектива, разработанная австралийской студией Team Bondi и выпущенная издательством Rockstar Games 17 мая 2011 года на PlayStation 3 и Xbox 360. 23 июня 2011 года было заявлено, что игра выйдет на ПК осенью 2011 года.",
    publisher = publisher3,
    releaseDate = date(2011, 5, 17),
    price = 7600,
    contentRating = rating3, 
    isAvailable = True
)
product36.platform.add(platform1, platform2, platform3)

product36.genre.add(genre15, genre9, genre19, genre11, genre5)






product37 = Products.objects.create(
    title = "Grand Theft Auto IV",
    description = "Grand Theft Auto IV — компьютерная игра в жанре action-adventure, девятая в серии Grand Theft Auto, выпущена 29 апреля 2008 года для двух игровых приставок — PlayStation 3 и Xbox 360, также полгода спустя игру портировали на ПК.",
    publisher = publisher3,
    releaseDate = date(2008, 4, 29),
    price = 8199,
    contentRating = rating3, 
    isAvailable = True
)
product37.platform.add(platform1, platform2, platform3)

product37.genre.add(genre13, genre11)







product38 = Products.objects.create(
    title = "Midnight Club 3: Dub Edition",
    description = "Midnight Club 3: DUB Edition — видеоигра в жанре аркадных авто- и мотогонок, изданная американской компанией Rockstar Games в 2005 году для игровых приставок Xbox, PlayStation 2 и PlayStation Portable. Является третьей частью серии Midnight Club.",
    publisher = publisher3,
    releaseDate = date(2005, 4, 11),
    price = 4552,
    contentRating = rating2, 
    isAvailable = False
)
product38.platform.add(platform2, platform3)

product38.genre.add(genre27)






product39 = Products.objects.create(
    title = "Manhunt",
    description = "Manhunt — серия стелс-игр, разработанная Rockstar North, а также несколькими другими студиями Rockstar и изданная Rockstar Games. Серия началась в 2003 году с выпуска Manhunt и завершилась в 2007 году Manhunt 2.",
    publisher = publisher3,
    releaseDate = date(2007, 10, 29),
    price = 14401,
    contentRating = rating3, 
    isAvailable = False
)
product39.platform.add(platform1, platform2)

product39.genre.add(genre32, genre33, genre19)






product40 = Products.objects.create(
    title = "Table Tennis",
    description = "Rockstar Games presents Table Tennis — видеоигра в жанре симулятора настольного тенниса, разработанная студией Rockstar San Diego и изданная компанией Rockstar Games для приставки Xbox 360 в 2006 году. Годом позже была выпущена версия для Wii, разработанная Rockstar Leeds. ",
    publisher = publisher3,
    releaseDate = date(2006, 5, 23),
    price = 3798,
    contentRating = rating2, 
    isAvailable = False
)
product40.platform.add(platform3)

product40.genre.add(genre2, genre3)





product41 = Products.objects.create(
    title = "NieR Replicant ver.1.22474487139...",
    description = "Обновленный приквел NieR:Automata. Во имя спасения своей сестры Йоны, которую поразил смертельный недуг, добросердечный юноша из глухой деревеньки вместе с Белым Гримуаром – говорящей книгой – отправляется на поиски «запечатанных виршей».",
    publisher = publisher4,
    releaseDate = date(2021, 4, 23),
    price = 20000,
    contentRating = rating3, 
    isAvailable = True
)
product41.platform.add(platform1, platform2, platform3)

product41.genre.add(genre13, genre28, genre25)





product42 = Products.objects.create(
    title = "Outriders",
    description = "Outriders — шутер от третьего лица с элементами ролевой игры, разработанный студией People Can Fly и изданный Square Enix. Выход игры на Microsoft Windows, PlayStation 4, PlayStation 5, Xbox One и Xbox Series X/S состоялся 1 апреля 2021 года. ",
    publisher = publisher4,
    releaseDate = date(2021, 3, 1),
    price = 13000,
    contentRating = rating3, 
    isAvailable = True
)
product42.platform.add(platform1, platform2, platform3)

product42.genre.add(genre19, genre22)




product43 = Products.objects.create(
    title = "Balan Wonderworld",
    description = "Balan Wonderworld — платформер 2021 года, в основном разработанный Arzest и изданный Square Enix. Взяв на себя роль двух детей, которых ведет волшебное существо по имени Балан, игрок исследует двенадцать миров, оформленных в стиле сердец несчастных людей.",
    publisher = publisher4,
    releaseDate = date(2021, 3, 26),
    price = 13000,
    contentRating = rating1, 
    isAvailable = True
)
product43.platform.add(platform1, platform2, platform3, platform4)

product43.genre.add(genre21, genre16)





product44 = Products.objects.create(
    title = "Trials of Mana",
    description = "Trials of Mana — это ролевая игра 2020 года, разработанная Xeen и опубликованная Square Enix для Microsoft Windows, Nintendo Switch и PlayStation 4. Мобильный порт выпущен в следующем году. Это 3D-римейк одноименной игры Super Famicom 1995 года, третьей игры в серии Mana.",
    publisher = publisher4,
    releaseDate = date(2020, 3, 24),
    price = 22000,
    contentRating = rating2, 
    isAvailable = True
)
product44.platform.add(platform2, platform4, platform5)

product44.genre.add(genre13, genre28, genre11, genre10)





product45 = Products.objects.create(
    title = "Octopath Traveler",
    description = "Octopath Traveler — японская ролевая игра, разработанная совместно японскими компаниями Square Enix и Acquire и выпущенная компанией Nintendo для консоли Nintendo Switch в 2018 году. В 2019 году игра была выпущена для Microsoft Windows.",
    publisher = publisher4,
    releaseDate = date(2018, 7, 13),
    price = 22572,
    contentRating = rating2, 
    isAvailable = True
)
product45.platform.add(platform1, platform4)

product45.genre.add(genre22)





product46 = Products.objects.create(
    title = "Candy Crush Saga",
    description = "Candy Crush Saga — бесплатная игра-головоломка, выпущенная компанией King 12 апреля 2012 года для игровой платформы социальной сети Facebook; позднее также были выпущены версии для iOS, Android, Windows 10 и Windows Phone.",
    publisher = publisher5,
    releaseDate = date(2012, 3, 12),
    price = 0,
    contentRating = rating1, 
    isAvailable = True
)
product46.platform.add(platform1, platform5)

product46.genre.add(genre29)





product47 = Products.objects.create(
    title = "Tony Hawk's Pro Skater 1 + 2",
    description = "Tony Hawk’s Pro Skater 1 + 2 — видеоигра о скейтбординге 2020 года, разработанная Vicarious Visions и опубликованная Activision. Он был выпущен для PlayStation 4, Windows и Xbox One 4 сентября 2020 г., PlayStation 5 и Xbox Series X / S 26 марта 2021 г. и Nintendo Switch 25 июня 2021 г.",
    publisher = publisher5,
    releaseDate = date(2020, 6, 8),
    price = 19990,
    contentRating = rating2, 
    isAvailable = True
)
product47.platform.add(platform1, platform2, platform3, platform4)

product47.genre.add(genre4)






product48 = Products.objects.create(
    title = "StarCraft II: Wings of Liberty",
    description = "StarCraft II: Wings of Liberty — компьютерная игра в жанре стратегии в реальном времени, продолжение StarCraft. Была анонсирована 19 мая 2007 года на фестивале Blizzard Worldwide Invitational в Сеуле, Южная Корея. ",
    publisher = publisher5,
    releaseDate = date(2010, 7, 27),
    price = 6360,
    contentRating = rating2, 
    isAvailable = True
)
product48.platform.add(platform1, platform6)

product48.genre.add(genre5)






product49 = Products.objects.create(
    title = "Crash Bandicoot 4: It's About Time",
    description = "Crash Bandicoot 4: It’s About Time — компьютерная игра в жанре платформер, разработанная американской компанией Toys For Bob под издательством Activision. ",
    publisher = publisher5,
    releaseDate = date(2020, 10, 2),
    price = 15299,
    contentRating = rating2, 
    isAvailable = True
)
product49.platform.add(platform1, platform2, platform3, platform4)

product49.genre.add(genre16, genre10)








product50 = Products.objects.create(
    title = "Spyro Reignited Trilogy",
    description = "Spyro Reignited Trilogy — сборник ремастеров первых трёх компьютерных игр из серии Spyro the Dragon, разработанный Toys For Bob и изданный Activision на платформы PlayStation 4 и Xbox One. В данный сборник входят ремастеры игр Spyro the Dragon, Spyro 2: Ripto’s Rage!",
    publisher = publisher5,
    releaseDate = date(2018, 11, 13),
    price = 13899,
    contentRating = rating2, 
    isAvailable = True
)
product50.platform.add(platform1, platform2, platform3, platform4)

product50.genre.add(genre16, genre11, genre17, genre10)




