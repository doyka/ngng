import requests
import random
import re
import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import urllib.request
import asyncio

def getbalance(arg):
    try:
        myurl = 'http://clrn1w.xyz/casino/getmoney.php?user=' + str(arg)
        r = requests.get(myurl)
        if r.json() == '':
            r = requests.get(myurl)
        else:
            r = requests.get(myurl)
        return r.json()
    except:
        r = requests.get(myurl)
        return r.json()

async def main():
    tok = os.environ.get('bottoken')
    vk_session = vk_api.VkApi(token=tok)
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    keyboard = VkKeyboard(one_time=True)
    servers = ['Emerald', 'Trilliant', 'Crystal', 'Sapphire', 'Amber', 'Ruby']
    last = False
    ss = False
    last1 = False
    ss1 = False
    bank = False
    last2 = False
    ss2 = False
    players = []
    keyboard.add_button('Пополнить', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Баланс', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Казино', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line()
    keyboard.add_button('Вывод виртами', color=VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Вывод рублями', color=VkKeyboardColor.NEGATIVE)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.text == 'Начать' or event.text == 'Меню' or event.text == 'меню':
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Вы находитесь в главном меню.'
                )
                money = getbalance(event.user_id)
            if event.text == 'Вывод рублями' or event.text == 'вывод рублями':
                money = getbalance(event.user_id)
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    message='Вы запрашиваете вывод рублями,\nдля этого укажите количество денег для вывода(от 3ĸĸ)\nи номер Qiwi/Webmoney/Yandex.\n1ĸĸ - 30 рублей.\nПример: 2ĸĸ  qiwi +79871545068\nВводите только целые числа!!!'
                )
                ss = True
            if 'кк' in event.text and ss:
                try:
                    ss = False
                    summ = event.text
                    summin = re.findall(r'\d+', summ)[0]
                    summout = int(summin) * 1000000
                    print(summin)
                    if summout <= money and summout >= 3000000:
                        money -= summout
                        requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Ваш заказ будет обработан в течение нескольких часов.'
                        )
                        vk.messages.send(
                            peer_id=520543707,
                            random_id=get_random_id(),
                            message='Вывод рублями @id' + str(event.user_id) + ' Информация: ' + str(summ)
                        )
                    else:
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Некорректная сумма'
                        )
                except ValueError:
                    vk.messages.send(
                        peer_id=event.user_id,
                        random_id=get_random_id(),
                        message='Некорректная сумма'
                    )
            if event.text == 'Пополнить' or event.text == 'пополнить':
                money = getbalance(event.user_id)
                keyboard3 = VkKeyboard(one_time=True)
                keyboard3.add_button('Оплачено', color=VkKeyboardColor.POSITIVE)
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard3.get_keyboard(),
                    message='Вы собираетесь пополнить счет рублями(от 1ĸĸ), 1ĸĸ - 50 рублей.\nПерейдите по данной ссылке qiwi.com/p/380508817311\nи оплатите нужное для вас количество.\nВ комментарии к переводу укажите своё имя и фамилию.\nПосле оплаты нажмите на кнопку "Оплачено"'
                )
                ss2 = True
            if event.text == 'Оплачено' and ss2:
                ss2 = False
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Заказ на пополнение создан. Ожидайте!'
                )
                vk.messages.send(
                    peer_id=520543707,
                    random_id=get_random_id(),
                    message='Ввод рублями @id' + str(event.user_id)
                )
            if event.text == 'Вывод виртами' or event.text == 'вывод виртами':
                money = getbalance(event.user_id)
                keyboard1 = VkKeyboard(one_time=True)
                keyboard1.add_button('Emerald', color=VkKeyboardColor.POSITIVE)
                keyboard1.add_button('Trilliant', color=VkKeyboardColor.POSITIVE)
                keyboard1.add_button('Crystal', color=VkKeyboardColor.POSITIVE)
                keyboard1.add_line()
                keyboard1.add_button('Sapphire', color=VkKeyboardColor.NEGATIVE)
                keyboard1.add_button('Amber', color=VkKeyboardColor.NEGATIVE)
                keyboard1.add_button('Ruby', color=VkKeyboardColor.NEGATIVE)
                last1 = True
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard1.get_keyboard(),
                    message='Выберите сервер.'
                )
            if last1 and event.text in servers:
                serv = event.text
                last1 = False
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    message='Введите сумму(от 2ĸĸ) и через пробел банк счет. 2ĸĸ в боте равно 1ĸĸ на ДРП. Например: 6ĸĸ 8163.\nВводите только целые числа!!!'
                )
                ss1 = True
            if ss1 and 'кк' in event.text:
                try:
                    ss1 = False
                    summka = event.text
                    summin = re.findall(r'\d+', summka)[0]
                    summout = int(summin) * 1000000
                    print(summin)
                    if summout <= money and summout >= 2000000:
                        money -= summout
                        requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Ваш заказ будет обработан в течение нескольких часов.'
                        )
                        vk.messages.send(
                            peer_id=520543707,
                            random_id=get_random_id(),
                            message='[' + serv + '] Вывод виртами @id' + str(event.user_id) + ' Информация: ' + str(summka)
                        )
                    else:
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Некорректная сумма'
                        )
                except ValueError:
                    vk.messages.send(
                        peer_id=event.user_id,
                        random_id=get_random_id(),
                        message='Некорректная сумма'
                    )
            if event.text == 'Казино':
                money = getbalance(event.user_id)
                mess = 'Текущие игры&#127922;:\n\n'
                page = urllib.request.urlopen('http://clrn1w.xyz/casino/games.php')
                textcas = page.read()
                q = str(textcas)
                textcas = q.replace("b", "")
                textcas = textcas.replace("'", "")
                aye = textcas.split('n')
                for i in range(len(textcas.split('n')) - 1):
                    idd = aye[i].split()[0]
                    mon = aye[i].split()[1]
                    ppl = aye[i].split()[2]
                    w = urllib.request.urlopen('http://clrn1w.xyz/casino/count.php?rm=' + str(idd))
                    cont = w.read()
                    h = str(cont)
                    cont = h.replace("b", "")
                    cont = cont.replace("'", "")
                    cnt = len(cont.split('n')) - 1
                    mess += '&#128309; Игра №' + str(idd) + ': &#128176; ' + str(mon) + '$; &#128101; ' + str(cnt) +'/' + str(ppl) + ';\n'
                    if int(cnt) >= int(ppl):
                        players = []
                        t = urllib.request.urlopen('http://clrn1w.xyz/casino/getplayers.php?id=' + str(idd))
                        requests.get('http://clrn1w.xyz/casino/otmena.php?id=' + str(idd))
                        text = t.read()
                        u = str(text)
                        text = u.replace(".", " ")
                        text = text.replace("b", "")
                        text = text.replace("'", "")
                        for j in range(cnt):
                            pl = text.split()[j]
                            players.append(pl)
                        print(players)
                        random.shuffle(players)
                        random.shuffle(players)
                        random.shuffle(players)
                        rand = random.choice(players)
                        print(players)
                        print(rand)
                        usr = rand
                        print(mon, ppl)
                        mone = getbalance(usr)
                        winpriz = int(ppl) * int(mon)
                        print(winpriz)
                        mone = int(mone) + int(winpriz)
                        requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(mone) + '&user=' + str(usr))
                        print('yes')
                        for j in players:
                            vk.messages.send(
                            peer_id=j,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='С помощь великого рандома выиграл @id' + str(usr) + ' (данный игрок)\nПриз составляет ' + str(winpriz) + '$'
                            )
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message=mess + '\n\nКоманды&#128295;:\n&#128311; Kaзино начать [cумма] [кол-во игроков от 2 до 10] - создать комнату\n&#128311; Kaзинo отменить [№ игры] - отменить игру\n&#128311; Kaзинo играть [№ игры] - зайти в комнату\n&#128311; Кaзинобот [сумма] - игра с ботом'
                )
            if 'Казино начать' in event.text:
                money = getbalance(event.user_id)
                try:
                    ayy = urllib.request.urlopen('http://clrn1w.xyz/casino/checkroom.php?user=' + str(event.user_id))
                    aq = ayy.read()
                    lq = str(aq)
                    aq = lq.replace("b", "")
                    aq = aq.replace("'", "")
                    if aq == '':
                        summ = event.text.split()[2]
                        people = event.text.split()[3]
                        if int(summ) > 0 and int(summ) <= money and 2 <= int(people) <= 10:
                            money -= int(summ)
                            requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                            requests.get('http://clrn1w.xyz/casino/writecasino.php?id=' + str(event.user_id) + '&bet=' + str(summ) + '&amount=' + str(people))
                            vk.messages.send(
                                peer_id=event.user_id,
                                random_id=get_random_id(),
                                keyboard=keyboard.get_keyboard(),
                                message='Вы создали игру. Ожидайте игрока!'
                            )
                    else:
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Вы уже создали игру!'
                        )
                except IndexError:
                    vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Неправильный ввод!'
                    )
            if 'Казино отменить' in event.text:
                money = getbalance(event.user_id)
                try:
                    game = event.text.split()[2]
                    r1 = requests.get('http://clrn1w.xyz/casino/getcas.php?id=' + str(game))
                    text = r1.json()
                    t = str(text)
                    text = t.replace(".", " ")
                    summ = text.split()[0]
                    idd = text.split()[1]
                    if int(idd) == event.user_id:
                        requests.get('http://clrn1w.xyz/casino/otmena.php?id=' + str(game))
                        money += int(summ)
                        requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                        vk.messages.send(
                        peer_id=event.user_id,
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard(),
                        message='Вы отменили игру №' + str(game)
                        )
                    else:
                        vk.messages.send(
                        peer_id=event.user_id,
                        random_id=get_random_id(),
                        keyboard=keyboard.get_keyboard(),
                        message='Игра не ваша!'
                        )
                except:
                    vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Неправильный ввод или игра не принадлежит вам!'
                    )
            if 'Казино играть' in event.text:
                money = getbalance(event.user_id)
                try:
                    game = event.text.split()[2]
                    y = urllib.request.urlopen('http://clrn1w.xyz/casino/checkpl.php?id=' + str(game) + '&user=' + str(event.user_id))
                    a = y.read()
                    aw = str(a)
                    a = aw.replace("b", "")
                    a = a.replace("'", "")
                    if a != '':
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard(),
                            message='Вы уже находитесь в данной комнате'
                        )
                    else:
                        r = requests.get('http://clrn1w.xyz/casino/getcas.php?id=' + str(game))
                        text = r.json()
                        t = str(text)
                        text = t.replace(".", " ")
                        summ = text.split()[0]
                        idd = text.split()[1]
                        if int(summ) <= int(money) and int(idd) != int(event.user_id):
                            money -= int(summ)
                            requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                            requests.get('http://clrn1w.xyz/casino/join.php?user=' + str(event.user_id) + '&rm=' + str(game))
                            vk.messages.send(
                                peer_id=event.user_id,
                                random_id=get_random_id(),
                                keyboard=keyboard.get_keyboard(),
                                message='Вы присоединились к игре №' + str(game)
                            )
                        else:
                            vk.messages.send(
                                peer_id=event.user_id,
                                random_id=get_random_id(),
                                keyboard=keyboard.get_keyboard(),
                                message='Неправильный ввод или игра принадлежит вам!'
                            )
                except:
                    vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Неправильный ввод!'
                    )
            if event.text == 'Баланс' or event.text == 'баланс':
                money = getbalance(event.user_id)
                vk.messages.send(
                    peer_id=event.user_id,
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Ваш баланс: ' + str("%.0f" % money) + '$'
                )
            if event.user_id == 520543707 and '/money' in event.text:
                dengi = event.text.split()[1]
                idchela = event.text.split()[2]
                requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(dengi) + '&user=' + str(idchela))
                vk.messages.send(
                    peer_id=520543707,
                    random_id=get_random_id(),
                    message='success'
                )
            if event.user_id == 520543707 and '/баланс' in event.text:
                usr = event.text.split()[1]
                myurl = 'http://clrn1w.xyz/casino/getmoney.php?user=' + str(usr)
                r = requests.get(myurl)
                vk.messages.send(
                    peer_id=520543707,
                    random_id=get_random_id(),
                    message=str(r.json()) + '$'
                )
            if "Казинобот" in event.text:
                try:
                    money = getbalance(event.user_id)
                    comp = random.random()
                    chel = random.random()
                    cmd = event.text.split()[0]
                    suma = event.text.split()[1]
                    suma = re.findall(r'\d+', suma)[0]
                    if int(suma) > 0 and comp < chel and int(suma) <= money:
                        suma = int(suma) / 100 * 50
                        money += int(suma)
                        requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            message='Вы выиграли ' + str("%.0f" % suma) + '$. Баланс: ' + str(money) + '$'
                        )
                    elif int(suma) > 0 and comp == chel and int(suma) <= money:
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            message='Ничья'
                        )
                    elif int(suma) > 0 and comp > chel and int(suma) <= money:
                        money -= int(suma)
                        requests.get('http://clrn1w.xyz/casino/money.php?mon=' + str(money) + '&user=' + str(event.user_id))
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            message='Вы проиграли ' + str(suma) + '$. Баланс: ' + str(money) + '$'
                        )
                except IndexError:
                        vk.messages.send(
                            peer_id=event.user_id,
                            random_id=get_random_id(),
                            message='Некорректная сумма'
                        ) 

asyncio.run(main())
