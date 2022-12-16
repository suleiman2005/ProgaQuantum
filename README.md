# **Tower Defence**

## О **Tower Defence**

**Tower Defence** -- это компьютерная игра, в которой вам нужно защитить жителей главной башни от злостных врагов.
Вы можете строить военные башни и уничтожать обидчиков на подступах к основному строению, получать за это очки и на них улучшать башни.
**Tower Defence** совершенно бесплатна, что даёт вам доступ ко всем функциям данного приложения. Но вы в любой момент можете поблагодарить
разработчиков этой игры разными способами. Их имена:
1) Калашников Олег, Б02-203
2) Емельянов Артемий, Б02-203
3) Михайлов константин, Б02-203
Год выпуска игры: 2022

## Минимальные требования

В целом, для данной игры от компьютера не требуется больших мощностей. Однако стоит отметить, 
что, так как игра была написана на версии *Python 3.9+*, то она доступна для *Windows 8+*, 
а так же для некоторых дистрибутивов *Linux* и *MacOs* (подробнее читайте ниже в этом разделе).

Для запуска вам потребуется версия *Python 3.9+* (скачать можно [здесь](https://www.python.org/downloads/)), 
а также его модули *pygame, matplotlib, random, numpy*. Установить их можно следующим образом:

* Откройте терминал в папке игры

* Напишите команду 

```
pip3 install pygame matplotlib random numpy
```
* Подождите, пока модули установятся

Также для корректной работы на *MacOs* и некоторых дистрибутивах *Linux* таких как *Ubuntu, Debian, Redhat, CentOS, Fedora*, 
вам стоит следовать инструкциям установки вот [тут](https://www.pypi.org/project/audioplayer).

## Установка

Чтобы установить **Tower Defence**, вы можете как скачать папку с файлами непосредственно с сайта *GitHub*, так и, при наличии git на вашем компьютере 
(скачать *Git* можно [тут](https://git-scm.com/downloads) или [тут](https://gitforwindows.org/)), воспользоваться следующей командой: 

```
git clone https://github.com/suleiman2005/ProgaQuantum
```
## Запуск игры
Для запуска игры вы должны запустить файл *Tower_Defence.py*. Для этого можете запустить терминал в папке игры и воспользоватся командой 
```
python3 Tower_Defence.py
```
При запуске игры вы попадаете в ***главное меню***. Там есть 6 кнопок:

### Start Game

Недоступна до выбора уровня сложности. Появляется после выбора уровня сложности, при нажатии запускает игру.

### Select level

При нажатии ничего не происходит, призывает вас выбрать уровень, нажимая на кнопки ниже.

### level 1

Выбирается уровень сложности 1.

### level 2

Выбирается уровень сложности 2.

### level 3

Выбирается уровень сложности 3.

### Exit

Происходит выход из игры.

### Игровой процесс

При запуске игры вы попадаете на поле, содержащее случайно сгенерированные элементы: траву, цветы, камни, озёра.
Строить башни можно на всём, кроме камней и озёр.

Враги идут с двух направлений, с течением времени их количество увеличивается. Ваша задача - наиболее грамотно распределить доступные
ресурсы и организовать защиту главной башни. При уничтожении врага вам даётся вознаграждение в размере 20 монет.
Стоимость строительства новой башни - 100 монет.
Собрав достаточное количество монет (300 для первого улучшения и 800 для второго), вы можете улучшить одну из построенных башен.

В игре присутствуют два типа башен. Одна из них стреляет мощными пулями, её перезарядка требует времени. Вторая уничтожает врагов мощным лазером
и постоянно наносит небольшой урон.

В игре присутствуют 4 типа врагов. Два из них (жёлтый и красный смайлики) двигаются медленно и имеют большой запас здоровья.
Третий (пчела) двигается быстро, но запас здоровья у неё меньше. Четвёртый элемент секретный и открывается в самом конце игры.

Взаимодействие осуществляется с помощью кнопок на нижней панели в игре путём нажатия на них мышкой или с помощью клавиатуры:
кнопка 1 - строительство первого типа башни
кнопка 2 - строительство второго типа башни
кнопка z - улучшение башни
кнопка x - продажа башни (возвращается половина её общей стоимости)

Всё поле разбито на квадраты. Хорошие графика и музыка в игре присутствуют.
Выбирать квадрат для редактирования можно мышкой, нажав на него, или с помощью стрелок на клавиатуре.

Уровни отличаются друг от друга протяжённостью дороги, ведущей к башне, запасом здоровья врагов, их количеством.

Если неприятели подошли к вашей главной башне, у вас есть время их уничтожить, так как башня имеет запас здоровья.
После уничтожения главной башни игра заканчивается. В таком случае вы попадёте на экран поражения, где вам предложат
перейти в главное меню (exit to the main menu) или выйти из игры (exit).

Также игра закончится после уничтожения вами всех врагов. Их количество зависит от уровня:
100 на первом уровне
500 на втором уровне
1000 на третьем уровне
В этом случае вы попадаете в меню победы, его функции такие же, как у меню поражения.

В любой момент вы можете выйти из игры, нажав кнопку Quit, расположенную в верхнем правом углу игровой зоны, клавишу Esc
или крестик окна приложения.

Настоятельно советуем вам испытать эту игру. Хороший баланс делает первый уровень лёгким, а третий сложным.

Желаем вам успехов в нашей игре. Отзывы оставляйте в нашем гитхабе https://github.com/suleiman2005/ProgaQuantum