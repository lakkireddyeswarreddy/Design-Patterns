
from weather_station import WeatherStation
from phone_display_observer import PhoneDisplayObserver
from led_board_observer import LEDBoardObserver
from tv_display_observer import TVDisplayObserver


if __name__ == "__main__":
    weather_station = WeatherStation()
    PhoneDisplayObserver(weather_station)
    LEDBoardObserver(weather_station)
    TVDisplayObserver(weather_station)
    weather_station.update_temperature(30.3)