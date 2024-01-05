import datetime
import config
import requests
from tkinter import messagebox
def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
    tz = datetime.timezone(datetime.timedelta(seconds=timezone))
    return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)


#Функция для кнопки search_btn
def get_weather(event="", elements={}): #чтоб ошибки не было при нажатии на кнопку search, делаем событие опциональным, определяем параметры через params
    params = {
        "appid": config.API_KEY,
        "units": config.UNITS,
        "lang": config.LANG,
        "q": elements['search_entry'].get() #метод get - значение из этого поля
    }
    try:
        r = requests.get(config.API_URL, params=params)
        weather = r.json()
        print_weather(weather, elements)
    except:
        print_weather({"cod": 0, "message": "не удалось получить данные"}, elements)



#Функция, которая печатает данные, размещает их в различные места нашей приложухи
#Сука это логика всей программы, что до этого было - лишь составление дизайна интерфейса.
def print_weather(data, elements):
    elements['search_entry'].delete(0, "end")
    if data["cod"] != 200:
        messagebox.showerror("Ошибка", data["message"].ljust(50))
        elements["content_frame"].pack_forget() #Забываем
        elements["start_content_frame"].pack(fill='both', expand=True) #показываем
        elements['city_label'].configure(text="") #если неправильно, обнуляем текст, если он там был епт
    else:
        elements['start_content_frame'].pack_forget() #забываем
        elements['content_frame'].pack(fill='both', expand=True) #показываем
        city = f"{data['name']}, {data['sys']['country']}" #показываем название города
        elements['city_label'].configure(text=city) #сюда говнюкааааа
        elements['city_content_label'].configure(text=city)
        elements['temp_label'].configure(text=f"{data['main']['temp']} ℃") #Температура
        sunrise_time = get_date_time(data["sys"]["sunrise"], data["timezone"])
        sunset_time = get_date_time(data["sys"]["sunset"], data["timezone"])
        data_text = f"""Местоположение: {city}
Температура: {data['main']['temp']} ℃
Атм. давление: {data['main']['pressure']} гПа
Влажность: 70% {data['main']['humidity']} %
Скорость ветра: {data['wind']['speed']} м/c
Погодные условия: {data['weather'][0]['description']}
Восход: {sunrise_time}
Закат: {sunset_time} """
        elements['data_textbox'].configure(state="normal") #конфигурируем текст, чтобы её можно было скопировать но не вставить что-то, дописать
        elements['data_textbox'].delete("0.0", "end") #Удаляем всё что есть в поле
        elements['data_textbox'].insert("1.0", data_text) #вставляем данные
        elements['data_textbox'].configure(state="disabled") #снова в disabled