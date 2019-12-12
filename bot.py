from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import datetime

vk = vk_api.VkApi(token="4cbfa0123da19b0c009dde302c05ce8ed5ad09083c7e6d866aeb9fd4d7fc279422f027eff792c96771ffb")

vk._auth_token()

vk.get_api()

longpoll = VkBotLongPoll(vk, 189648869)

def admin(ses, userid, chatid):
    chatMembers = vk.method('messages.getConversationMembers', {'peer_id': chatid})
    for member in chatMembers['items']:
        if member['member_id'] == userid:
            return member.get('is_admin', False)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id != event.object.from_id:
                try:
                    scs = 2000000008
                    if event.object.text.lower() == "нг" and admin(vk, event.object.from_id, event.object.peer_id) or event.object.peer_id == scs:
                        now = datetime.datetime.today() + datetime.timedelta(hours=3)
                        NY = datetime.datetime(2020, 1, 1)
                        d = NY - now
                        mm, ss = divmod(d.seconds, 60)
                        hh, mm = divmod(mm, 60)
                        date = 'До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss)
                        vk.method("messages.send", {"peer_id": event.object.peer_id, "message": date,
                                                    "random_id": 0, "attachment": 'photo-189648869_457239017'})
                except:
                    vk.method("messages.send", {"peer_id": event.object.peer_id, "message": 'Требуется выдать боту права администратора!',
                                                        "random_id": 0})
            elif event.object.peer_id == event.object.from_id:
                if event.object.text.lower() == "нг":
                    now = datetime.datetime.today() + datetime.timedelta(hours=3)
                    NY = datetime.datetime(2020, 1, 1)
                    d = NY - now
                    mm, ss = divmod(d.seconds, 60)
                    hh, mm = divmod(mm, 60)
                    date = 'До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss)
                    vk.method("messages.send", {"user_id": event.object.from_id, "message": date,
                                                "random_id": 0, "attachment": 'photo-189648869_457239017'})
