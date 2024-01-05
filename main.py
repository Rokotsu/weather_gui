import tkinter as tk
import customtkinter as ctk
import datetime
import locale
from PIL import Image
from funcs import get_weather

# Базовая настройка окна для приложения
window = ctk.CTk()
window.title('Weather App')
# window.iconphoto(False, tk.PhotoImage(file="weather_icon.png"))  # Иконка (сука не работает тварь)
window.geometry("800x500+500+200")  # Размер окна и его положение
window.resizable(False, False)  # запретил ресайщ
window.configure(fg_color="#fb8c00")  # цвет фона

# Верхний фрейм top_frame
top_frame = ctk.CTkFrame(window, width=800, height=50, fg_color="#212121",
                         corner_radius=0)  # на окне window, длина ширина, цвет, обнулил кринж скругления
top_frame.pack(fill="x")  # упаковал и растянул по оси x с юзанием pack

# На top_frame размещаю элементы, будет показан тот город, если будет корректный ввод
city_font = ctk.CTkFont(size=15)
city_label = ctk.CTkLabel(top_frame, text='', text_color='#fff',
                          font=city_font)  # Название лейбла, цвет, увеличили размер шрифта
city_label.place(x=20, y=10)  # упаковал методом place

# поле поиска
search_entry = ctk.CTkEntry(top_frame,
                            placeholder_text='Type city...')  # На top_frame также, внутри entry разместил текст для понимания
search_entry.place(x=520, y=10)  # собственно положение entry

# кнопка поиска
search_btn = ctk.CTkButton(top_frame, text='Search', width=100, command=lambda: get_weather(
    elements=window_elements))  # Текст на ней search, ширина 100, команда у неё в виде функции get_weather
search_btn.place(x=670, y=10)
search_entry.bind('<Return>', command=lambda event: get_weather(
    elements=window_elements))  # Дали событие, когда нажимаешь на enter в поле, шоб по кнопке не тыкать постоянно

# стартовый фрейм
start_content_frame = ctk.CTkFrame(window, corner_radius=0,
                                   fg_color='#fb8c00')  # Уже на окне window а не фрейме top, закругления нахуй!
start_content_frame.pack(fill='both', expand=True)  # Занимаем всю область.
# текст на этом фрейме
welcom_font = ctk.CTkFont(size=30)
welcome_label = ctk.CTkLabel(start_content_frame, text='Добро пожаловать в программу показа погоды', text_color='#fff',
                             font=welcom_font)  # На фрейме start_content_frane
welcome_label.place(relx=0.5, rely=0.5,
                    anchor='center')  # Относительная позиция в родительском виджете, и её положение в центре.

# отрисовываем второй экран(фрейм), когда показывается город, тоесть основной контент
# контентовый фрейм
content_frame = ctk.CTkFrame(window, corner_radius=0,
                             fg_color='#fb8c00')  # Уже на окне window а не фрейме top, закругления нахуй! тоесть создали новый фрейм
# content_frame.pack(fill='both', expand=True) #Занимаем всю область.


# Блок для даты
locale.setlocale(locale.LC_TIME,
                 "ru")  # хуячу русский локаль только для даты, если для всего, меня наверн пошлёт нахуй ткинтер. Конфликты все дела
curr_date = datetime.datetime.now().strftime(
    '%a, %B %d')  # Дата в удобном мне формате, да впринципе всем удобно, не ебёт
date_font = ctk.CTkFont(size=20)
date_label = ctk.CTkLabel(content_frame, text=curr_date, text_color='#fff', font=date_font)  # Всё по классике нах.
date_label.place(relx=0.5, y=30, anchor='center')  # размещаем

# Город
city_content_label = ctk.CTkLabel(content_frame, text="Название города", text_color='#fff', font=date_font)
city_content_label.place(relx=0.5, y=60, anchor='center')

# Выводим картинку Icon снизу
# weather_icon = ctk.CTkImage(light_image=Image.open("weather_icon.png"),
#                             size=(150, 150))  # при светлой теме, указывем путь и размер согласно самой картинки.
# weather_icon_label = ctk.CTkLabel(content_frame, text='',
#                                   image=weather_icon)  # в виде лейбла разместили, удаляем нах текст и указываем переменную, где содержится изображение
# weather_icon_label.place(x=30, y=120)  # размещаем

# выводим температуру, да побольше БЛЯ. Чтоб видно было всем
temp_font = ctk.CTkFont(size=50)
temp_label = ctk.CTkLabel(content_frame, text="25 ℃", text_color='#fff', font=temp_font)  # Всё по классике нах.
temp_label.place(x=200, y=150)  # Без относительного rel хуйни и анкор на атомы бля, ото не смотрится

# #Другие данные
data_textbox_font = ctk.CTkFont(size=15, weight="bold")
data_textbox = ctk.CTkTextbox(content_frame, fg_color='#e65100', text_color='#fff', width=300, height=250,
                              font=data_textbox_font, spacing3=5, wrap="word",
                              activate_scrollbars=False)  # Размеры (длина ширина),сам размер текста, спейсинг - межстрочный интервал, перенос по словам (wrap) и отключаем скроллы
data_textbox.place(x=400, y=150)

# слоарь элементов
window_elements = {
    'search_entry': search_entry,
    'content_frame': start_content_frame,
    'city_label': city_label,
    'city_content_label': city_content_label,
    'temp_label': temp_label,
    'data_textbox': data_textbox,
}

window.mainloop()

# pyinstaller --noconfirm --onedir --windowed -i "C:\Users\vultus\PycharmProjects\python\weather_gui\weather_app.ico" --distpath "C:\Users\vultus\PycharmProjects\python\weather_gui\program" --add-data "C:\Users\vultus\PycharmProjects\python\venv\Lib\site-packages\customtkinter;customtkinter\" --add-data "C:\Users\vultus\PycharmProjects\python\weather_gui\weather_icon.png;." main.py
