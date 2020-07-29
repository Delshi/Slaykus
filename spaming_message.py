import vk
import time, datetime

APIVersion=5.73

msg = input("Че отправить? (Пиши ска)\n")
print("Отправить всем друзьям" ,"'", msg, "'", '?')
input("Нажмите Enter для продолжения")



#Текущее время
# named_tuple = time.localtime() # получить struct_time
# time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
# print("Текущее время", time_string)
# input("ВЫ УВЕРЕНЫ?")

#Авторизация
session=vk.Session(access_token='10dff9becbfbfcb36b41d835c95d30f244010d4a269c32e53a72e68b3d4169e2204087941c4f97ed6e26d')
api = vk.API(session)

#Получаем список идшников друзей
user_list = api.friends.get(user_id=439068638, v=APIVersion)
#Достаем сами идшники
ids = user_list['items']

#Где-то здесь надо вставить цикл if со временем

#Цикл на отправку
while True:
    i=1
    for i in ids:
        api.messages.send(user_id=i, message=msg, v=APIVersion)
        print("Отправил сообщение для", i)
        i += 1
        time.sleep(10)

