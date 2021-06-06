import pyowm
import config


def weather(var):
    owm = pyowm.OWM(config.key)
    observation = owm.weather_manager().weather_at_place(var)
    w = observation.weather
    a = w.wind()
    b = w.humidity
    c = w.temperature('celsius')
    s = w.status
    stat = 'Краткая сводка - ' + str(s)
    wind = 'Скорость ветра ' + str(a.get("speed")) + ' м/с'
    hum = 'Относительная влажность ' + str(b) + ' мм рт. ст.'
    temp = 'Средняя темперетура ' + str(c.get("temp")) + ' °C'
    tmax = 'Максимальная темперетура ' + str(c.get("temp_max")) + ' °C'
    tmin = 'Минимальная темперетура ' + str(c.get("temp_min")) + ' °C'
    summary = {'stat':stat, 'wind':wind, 'hum':hum,
    'temp':temp, 'tmax':tmax, 'tmin':tmin}
    return summary


def weather_coord(lat, lon):
    owm = pyowm.OWM(config.key)
    observation_list = owm.weather_manager().weather_around_coords(lat, lon)
    observation = observation_list.pop()
    w = observation.weather
    a = w.wind()
    b = w.humidity
    c = w.temperature('celsius')
    s = w.status
    stat = 'Краткая сводка - ' + str(s)
    wind = 'Скорость ветра ' + str(a.get("speed")) + ' м/с'
    hum = 'Относительная влажность ' + str(b) + ' мм рт. ст.'
    temp = 'Средняя темперетура ' + str(c.get("temp")) + ' °C'
    tmax = 'Максимальная темперетура ' + str(c.get("temp_max")) + ' °C'
    tmin = 'Минимальная темперетура ' + str(c.get("temp_min")) + ' °C'
    summary = {'stat':stat, 'wind':wind, 'hum':hum,
    'temp':temp, 'tmax':tmax, 'tmin':tmin}
    return summary
