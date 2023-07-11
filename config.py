import os

MAIN_DIR = os.getcwd()
PRESENT_DIR = os.path.join(MAIN_DIR, 'presentations')

start_message = 'Для взаимодействия с нашим умным\nботом нажмите на интересующий Вас\nпункт меню ниже'
presentations = os.listdir(PRESENT_DIR)
talks_message = 'Ведущие инфекционисты, педиатры и отоларингологи:\nёмко и по делу о мифах, клинической базе\nи опытеп применения Полиоксидония'
url_youtube = 'https://www.youtube.com/watch?v=IMs2W8IlfvM'
# При запуске генерирует сообщение для вывода презентаций
message_pres = ''
counter = 1
for pres in presentations:
    message_pres += f'[{counter}] - {pres}\n'
    counter += 1
del counter