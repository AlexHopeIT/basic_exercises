"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. +Вывести айди пользователя, который написал больше всех сообщений.
2. +Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. +Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. +Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. +Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

chat_history = generate_chat_history()

def user_with_max_msg():
    id_user_with_max_msg = []
    for id in chat_history:
        id_user_with_max_msg.append(id['sent_by'])
        return 'Больше всех отправил сообщений: ', max(id_user_with_max_msg, 
                                                     key=id_user_with_max_msg.count)
    

def seen_msg():
    user_with_views = []
    users_with_max_views = []
    for msg in chat_history:
        user_with_views.append(msg['seen_by'])
        max_msg = max(len(views) for views in user_with_views)
        msg_with_max_views = [view for view in user_with_views if len(view) == max_msg]
        users_with_max_views.append(msg['sent_by'])
    return 'Больше всего просмотренных сообщений у следующих пользователей: ', *users_with_max_views

def which_time_msg_most():
    morning = []
    afternoon = []
    evening = []
    for time in chat_history:
        dt = time['sent_at']
        hour_list = [dt.hour]
        if hour_list[0] <= 12:
            morning.append(hour_list[0])
        elif 12 <hour_list[0] <= 18:
            afternoon.append(hour_list[0])
        else:
            evening.append(hour_list[0])
    if len(morning) > len(afternoon) > len(evening):
        return 'Больше всего сообщений утром (до 12)'
    elif len(morning) < len(afternoon) < len(evening):
        return 'Больше всего сообщений вечером (после 18)'
    elif len(morning) < len(evening) < len(afternoon):
        return 'Больше всего сообщений днем (с 12 до 18)'

def longest_thread():
    all_threads = []
    for thread in chat_history:
        if thread['reply_for'] is not None:
            all_threads.append(thread['reply_for'])
    find_longest = None
    max_count = 0
    for reply in all_threads:
        count_thread = all_threads.count(reply)
        if count_thread > max_count:
            max_count = count_thread
        find_longest = reply
        return 'Самый большой тред на сообщение с идентификатором: ', find_longest
    
def most_answer():
    id_most_reply = longest_thread()
    #id_most_reply = "UUID('{}')".format(id_most_reply[1])
    id_asw = []
    for msg in chat_history:
        if msg['id'] in id_most_reply:
            return 'Пользователь, занявший первое место по ответам на его сообщение: ', msg['sent_by']


if __name__ == "__main__":
    print(generate_chat_history())
    print('')
    print(*user_with_max_msg())
    print('')
    print(which_time_msg_most())
    print('')
    print(*longest_thread())
    print('')
    print(*most_answer())
    print('')
    print(*seen_msg())
