import datetime
import json
import operator
import time
import urllib.request
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from src.ConstantValue import *

time1 = ''


class WeatherUI:
    def __init__(self, master, data, cityName, latlng):
        root2 = master
        self.data = data
        self.latlng = latlng
        self.city = cityName

        frame = Frame(master)
        frame.pack()
        canvas = Canvas(root2, height=500, width=800)
        canvas.pack(expand=YES, fill=BOTH)
        self.timecanvas = canvas

        canvas.filename = ImageTk.PhotoImage(Image.open(background))
        canvas.create_image(0, 0, anchor=NW, image=canvas.filename)

        canvas.marker = ImageTk.PhotoImage(Image.open(marker64))
        canvas.create_image(90, 20, anchor=NW, image=canvas.marker)
        self.wfname = canvas.create_text(140, 110, text='Weather Forecast in', font='georgia 18 bold', fill='white')

        canvas.pressure = ImageTk.PhotoImage(Image.open(amtmosphericPressure))
        canvas.create_image(20, 140, anchor=NW, image=canvas.pressure)
        self.pressureReading = canvas.create_text(140, 165, text='Pressure : 23.67 inHG', font='georgia 8 bold',
                                                  fill='white')

        canvas.humidity = ImageTk.PhotoImage(Image.open(humidity44))
        canvas.create_image(20, 185, anchor=NW, image=canvas.humidity)
        self.humidityReading = canvas.create_text(125, 210, text='Humidity : 62%', font='georgia 8 bold',
                                                  fill='white')

        canvas.wind = ImageTk.PhotoImage(Image.open(windSpeed44))
        canvas.create_image(20, 230, anchor=NW, image=canvas.wind)
        self.windReading = canvas.create_text(130, 250, text='Wind Speed : 5m/s', font='georgia 8 bold', fill='white')

        canvas.create_line(230, 140, 230, 270, fill='white')

        self.locationName = canvas.create_text(400, 80, text='Hyderabad', font='georgia 20 bold', fill='white')

        canvas.sun100px = ImageTk.PhotoImage(Image.open(sun100))
        self.sun100pxShow = canvas.create_image(350, 110, anchor=NW, image=canvas.sun100px)
        self.sunClear = canvas.create_text(400, 220, text='Sky is clear', font='georgia 10 bold', fill='white')

        self.last_update = canvas.create_text(383, 252, text='Last Updated Fri June 29 06:00 PM 2017',
                                              font='georgia 8 bold',
                                              fill='white')

        canvas.refreshImg = ImageTk.PhotoImage(Image.open(refresh15))
        self.refreshImgShow = canvas.create_image(515, 245, anchor=NW, image=canvas.refreshImg, tags='refreshImg')

        canvas.create_line(560, 140, 560, 270, fill='white')

        canvas.back = ImageTk.PhotoImage(Image.open(cancel))
        self.back_cancel = canvas.create_image(770, 10, anchor=NW, image=canvas.back, tags='cancel')

        self.timeUI = canvas.create_text(670, 80, text='06:15 PM', font='georgia 22 bold', fill='white')

        canvas.create_text(670, 135, text='Min. Temp.', font='georgia 12 bold', fill='white')
        self.minTempReading = canvas.create_text(670, 165, text='23 °C', font='georgia 16 bold', fill='white')
        canvas.minTherm = ImageTk.PhotoImage(Image.open(thermometer44))
        canvas.create_image(710, 135, anchor=NW, image=canvas.minTherm)

        canvas.create_line(620, 190, 720, 190, fill='white')

        canvas.create_text(670, 210, text='Max. Temp.', font='georgia 12 bold', fill='white')
        self.maxTempReading = canvas.create_text(670, 235, text='31 °C', font='georgia 16 bold', fill='white')
        canvas.maxTherm = ImageTk.PhotoImage(Image.open(thermometer44))
        canvas.create_image(710, 205, anchor=NW, image=canvas.maxTherm)

        self.currentTempReading = canvas.create_text(80, 400, text='31 °C', font='georgia 20 bold', fill='white')
        self.currentDay = canvas.create_text(80, 450, text='Friday', font='georgia 18 bold', fill='white')

        canvas.create_line(170, 380, 170, 470, fill='white')

        self.day1 = canvas.create_text(235, 380, text='Sat', font='georgia 12 bold bold', fill='white', tags='')
        canvas.sun64px = ImageTk.PhotoImage(Image.open(sun64))
        self.day1Img = canvas.create_image(204, 393, anchor=NW, image=canvas.sun64px)
        self.day1Temp = canvas.create_text(239, 468, text='26 °C', font='georgia 12 bold', fill='white')

        self.day2 = canvas.create_text(320, 380, text='Sun', font='georgia 12 bold', fill='white')
        canvas.sun64px2 = ImageTk.PhotoImage(Image.open(sun64))
        self.day2Img = canvas.create_image(289, 393, anchor=NW, image=canvas.sun64px2)
        self.day2Temp = canvas.create_text(324, 468, text='28 °C', font='georgia 12 bold', fill='white')

        self.day3 = canvas.create_text(405, 380, text='Mon', font='georgia 12 bold bold', fill='white')
        canvas.rain64px3 = ImageTk.PhotoImage(Image.open(rain64))
        self.day3Img = canvas.create_image(374, 393, anchor=NW, image=canvas.rain64px3)
        self.day3Temp = canvas.create_text(409, 468, text='24 °C', font='georgia 12 bold', fill='white')

        self.day4 = canvas.create_text(490, 380, text='Tues', font='georgia 12 bold bold', fill='white')
        canvas.sun64px4 = ImageTk.PhotoImage(Image.open(sun64))
        self.day4Img = canvas.create_image(459, 393, anchor=NW, image=canvas.sun64px4)
        self.day4Temp = canvas.create_text(494, 468, text='25 °C', font='georgia 12 bold', fill='white')

        self.day5 = canvas.create_text(579, 380, text='Wed', font='georgia 12 bold', fill='white')
        canvas.rain64px5 = ImageTk.PhotoImage(Image.open(rain64))
        self.day5Img = canvas.create_image(544, 393, anchor=NW, image=canvas.rain64px5)
        self.day5Temp = canvas.create_text(579, 468, text='23 °C', font='georgia 12 bold', fill='white')

        self.day6 = canvas.create_text(664, 380, text='Thu', font='georgia 12 bold', fill='white')
        canvas.sun64px6 = ImageTk.PhotoImage(Image.open(sun64))
        self.day6Img = canvas.create_image(629, 393, anchor=NW, image=canvas.sun64px6)
        self.day6Temp = canvas.create_text(664, 468, text='26 °C', font='georgia 12 bold', fill='white')

        self.day7 = canvas.create_text(749, 380, text='Fri', font='georgia 12 bold', fill='white')
        canvas.sun64px7 = ImageTk.PhotoImage(Image.open(sun64))
        self.day7Img = canvas.create_image(714, 393, anchor=NW, image=canvas.sun64px7)
        self.day7Temp = canvas.create_text(749, 468, text='26 °C', font='georgia 12 bold', fill='white')

        self.changes(canvas, data, cityName)
        self.tick()
        canvas.tag_bind(self.refreshImgShow, '<ButtonPress-1>', self.refreshTemp)
        canvas.tag_bind('cancel', '<ButtonPress-1>', self.onObjectClick)
        canvas.tag_bind(self.currentDay, '<ButtonPress-1>', self.onObjectClick)

    def changes(self, master2, json_data, city):
        address = city
        current_pressure = str(round((json_data['currently']['pressure']) * 0.02953, 3))
        current_humidity = str((json_data['currently']['humidity']) * 100)
        current_wind = str(json_data['currently']['windSpeed'])
        min_temperature = str(round((json_data['daily']['data'][0]['temperatureLow'] - 32) * 5 / 9))
        max_temperature = str(round((json_data['daily']['data'][0]['temperatureHigh'] - 32) * 5 / 9))
        status_weather = str(json_data['currently']['summary'])
        updatetime = str(self.update_time(json_data['currently']['time']))
        currentdaytemp = str(self.temperature_conversion(json_data['currently']['temperature']))

        day = {}
        tempDay = {}
        master2.dayImg = {}
        master2.currentDayImg = ''

        for a in range(8):
            day[a] = str(self.weekDay(json_data['daily']['data'][a]['time']))

        for b in range(8):
            tempDay[b] = str(round((json_data['daily']['data'][b]['temperatureHigh'] - 32) * 5 / 9)) + degree_celsius
        self.cuDay = day[0]
        for a in range(8):
            icon = str(json_data['daily']['data'][a]['icon'])
            if icon == 'cloudy':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(cloud64))
            elif icon == 'clear-day':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(sun64))
            elif icon == 'clear-night':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(moon64))
            elif icon == 'rain':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(rain64))
            elif icon == 'snow':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(snow64))
            elif icon == 'sleet':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(sleet64))
            elif icon == 'wind':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(wind64))
            elif icon == 'partly-cloudy-day':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(suncloud64))
            elif icon == 'partly-cloudy-night':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(cloudnight64))
            elif icon == 'fog':
                master2.dayImg[a] = ImageTk.PhotoImage(Image.open(foggyday64))

        icon = str(json_data['currently']['icon'])
        if icon == 'cloudy':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(cloud128))
        elif icon == 'clear-day':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(sun128))
        elif icon == 'clear-night':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(moon128))
        elif icon == 'rain':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(rain128))
        elif icon == 'snow':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(snow128))
        elif icon == 'sleet':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(sleet128))
        elif icon == 'wind':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(wind128))
        elif icon == 'partly-cloudy-day':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(suncloud128))
        elif icon == 'partly-cloudy-night':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(cloudnight128))
        elif icon == 'fog':
            master2.currentDayImg = ImageTk.PhotoImage(Image.open(foggyday128))

        master2.itemconfigure(self.locationName, text=address)
        master2.itemconfigure(self.windReading, text='Windspeed ' + current_wind + "m/s")
        master2.itemconfigure(self.pressureReading, text='Pressure ' + current_pressure + " inHG")
        master2.itemconfigure(self.humidityReading, text='Humidity ' + current_humidity + "%")
        master2.itemconfigure(self.minTempReading, text=min_temperature + degree_celsius)
        master2.itemconfigure(self.maxTempReading, text=max_temperature + degree_celsius)

        master2.itemconfigure(self.sun100pxShow, image=master2.currentDayImg)
        master2.itemconfigure(self.sunClear, text=status_weather)
        master2.itemconfigure(self.last_update, text="Last Update " + updatetime)

        master2.itemconfigure(self.currentDay, text=day[0])
        master2.itemconfigure(self.day1, text=day[1])
        master2.itemconfigure(self.day2, text=day[2])
        master2.itemconfigure(self.day3, text=day[3])
        master2.itemconfigure(self.day4, text=day[4])
        master2.itemconfigure(self.day5, text=day[5])
        master2.itemconfigure(self.day6, text=day[6])
        master2.itemconfigure(self.day7, text=day[7])

        master2.itemconfigure(self.currentTempReading, text=currentdaytemp)
        master2.itemconfigure(self.day1Temp, text=tempDay[1])
        master2.itemconfigure(self.day2Temp, text=tempDay[2])
        master2.itemconfigure(self.day3Temp, text=tempDay[3])
        master2.itemconfigure(self.day4Temp, text=tempDay[4])
        master2.itemconfigure(self.day5Temp, text=tempDay[5])
        master2.itemconfigure(self.day6Temp, text=tempDay[6])
        master2.itemconfigure(self.day7Temp, text=tempDay[7])

        master2.itemconfigure(self.day1Img, image=master2.dayImg[1])
        master2.itemconfigure(self.day2Img, image=master2.dayImg[2])
        master2.itemconfigure(self.day3Img, image=master2.dayImg[3])
        master2.itemconfigure(self.day4Img, image=master2.dayImg[4])
        master2.itemconfigure(self.day5Img, image=master2.dayImg[5])
        master2.itemconfigure(self.day6Img, image=master2.dayImg[6])
        master2.itemconfigure(self.day7Img, image=master2.dayImg[7])

    def tick(self):
        global time1

        time2 = time.strftime('%H:%M:%S')

        if time2 != time1:
            time1 = time2
            self.timecanvas.itemconfigure(self.timeUI, text=time2)

        self.timecanvas.after(100, self.tick)

    def weekDay(self, timestamp):
        value = datetime.datetime.fromtimestamp(timestamp)
        return (value.strftime('%a'))

    def update_time(self, timestamp):
        value = datetime.datetime.fromtimestamp(timestamp)
        return (value.strftime('%a %B %d %r %Y'))

    def sunTime(self, timestamp):
        value = datetime.datetime.fromtimestamp(timestamp)
        return (value.strftime('%r'))

    def refreshTemp(self, event):

        self.timecanvas.refreshImg = ImageTk.PhotoImage(Image.open(ajaxLoader))
        self.refreshImgShow = self.timecanvas.create_image(515, 245, anchor=NW, image=self.timecanvas.refreshImg)

        lat = self.latlng['lat']
        lng = self.latlng['lng']

        jsonData = weather_report(lat, lng)

        if jsonData:
            statusWeatherImg = str(jsonData)
            status_weather = str(jsonData['currently']['summary'])
            update_time = str(self.update_time(jsonData['currently']['time']))

            day = str(self.weekDay(jsonData['currently']['time']))
            day_temp = str(round((jsonData['currently']['temperature'] - 32) * 5 / 9))

            self.timecanvas.itemconfigure(self.sunClear, text=status_weather)

            self.timecanvas.itemconfigure(self.currentDay, text=day)

            self.timecanvas.itemconfigure(self.currentTempReading, text=day_temp + degree_celsius)

            self.timecanvas.itemconfigure(self.last_update, text="Last Update " + update_time)

            self.timecanvas.refreshImg = ImageTk.PhotoImage(Image.open(refresh15))
            self.refreshImgShow = self.timecanvas.create_image(515, 245, anchor=NW, image=self.timecanvas.refreshImg,
                                                               tags='refreshImg')
            self.timecanvas.tag_bind(self.refreshImgShow, '<ButtonPress-1>', self.refreshTemp)

        # print("KP")

    def temperature_conversion(self, temp):
        return round((temp - 32) * 5 / 9)

    def hourlyReport(self, canvas3):
        frame = Frame(canvas3, width=800, height=500)
        frame.pack()
        self.frametime = frame

        canvas_hourly = Canvas(canvas3, width=800, height=1600, scrollregion=(0, 0, 800, 1400))
        canvas_hourly.pack(expand=YES, fill=BOTH)

        self.hourlytime = canvas_hourly

        canvas_hourly.dailyBackground = ImageTk.PhotoImage(Image.open(background2))
        canvas_hourly.create_image(-200, 0, anchor=NW, image=canvas_hourly.dailyBackground)

        canvas_hourly.create_text(370, 40, text='Hourly Reports', fill='orange', font='georgia 30 bold')

        scrollbar = Scrollbar(frame, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        # attach listbox to scrollbar
        canvas_hourly.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=canvas_hourly.yview)

        canvas_hourly.back = ImageTk.PhotoImage(Image.open(cancel))
        self.back_cancel = canvas_hourly.create_image(770, 10, anchor=NW, image=canvas_hourly.back, tags='cancel')

        canvas_hourly.create_rectangle(70, 80, 730, 340, fill='white', width=3, outline='orange')

        self.day = canvas_hourly.create_text(110, 95, text='Tuesday', font='georgia 10 bold')

        self.onehour = canvas_hourly.create_text(200, 95, text='11am', font='georgia 10')
        self.twohour = canvas_hourly.create_text(290, 95, text='12pm', font='georgia 10')
        self.threehour = canvas_hourly.create_text(380, 95, text='1pm', font='georgia 10')
        self.fourhour = canvas_hourly.create_text(470, 95, text='2pm', font='georgia 10')
        self.fivehour = canvas_hourly.create_text(560, 95, text='3pm', font='georgia 10')
        self.sixhour = canvas_hourly.create_text(650, 95, text='4pm', font='georgia 10')

        canvas_hourly.onehourImg = ImageTk.PhotoImage(Image.open(rain24))
        self.onehourImgShow = canvas_hourly.create_image(187, 115, anchor=NW, image=canvas_hourly.onehourImg)

        canvas_hourly.twohourImg = ImageTk.PhotoImage(Image.open(wind24))
        self.twohourImgShow = canvas_hourly.create_image(277, 115, anchor=NW, image=canvas_hourly.twohourImg)

        canvas_hourly.threehourImg = ImageTk.PhotoImage(Image.open(cloudysun24))
        self.threehourImgShow = canvas_hourly.create_image(367, 115, anchor=NW, image=canvas_hourly.threehourImg)

        canvas_hourly.fourhourImg = ImageTk.PhotoImage(Image.open(cloudy24))
        self.fourhourImgShow = canvas_hourly.create_image(457, 115, anchor=NW, image=canvas_hourly.fourhourImg)

        canvas_hourly.fivehourImg = ImageTk.PhotoImage(Image.open(rain24))
        self.fivehourImgShow = canvas_hourly.create_image(547, 115, anchor=NW, image=canvas_hourly.fivehourImg)

        canvas_hourly.sixhourImg6 = ImageTk.PhotoImage(Image.open(wind24))
        self.sixhourImgShow = canvas_hourly.create_image(637, 115, anchor=NW, image=canvas_hourly.sixhourImg6)

        canvas_hourly.create_text(110, 175, text='Forecast', font='georgia 10 bold')

        self.onehourForecast = canvas_hourly.create_text(188, 180, text='All Rights Reserved. AccuWeather.com ',
                                                         font='arial 8', width=80, anchor=CENTER)
        self.twohourForecast = canvas_hourly.create_text(285, 180, text='All Rights Reserved. AccuWeather com ',
                                                         font='arial 8', width=80, anchor=CENTER)
        self.threehourForecast = canvas_hourly.create_text(385, 180, text='All Rights Reserved. AccuWeather com ',
                                                           font='arial 8', width=80, anchor=CENTER)
        self.fourhourForecast = canvas_hourly.create_text(485, 180, text='All Rights Reserved. AccuWeather com ',
                                                          font='arial 8', width=80, anchor=CENTER)
        self.fivehourForecast = canvas_hourly.create_text(585, 180, text='All Rights Reserved. AccuWeather com ',
                                                          font='arial 8', width=80, anchor=CENTER)
        self.sixhourForecast = canvas_hourly.create_text(685, 180, text='All Rights Reserved. AccuWeather com ',
                                                         font='arial 8', width=80, anchor=CENTER)

        canvas_hourly.create_line(75, 215, 725, 215)

        canvas_hourly.create_text(110, 235, text='Temp(°C)', font='georgia 10 bold')

        self.temp1 = canvas_hourly.create_text(200, 235, text='20 °C')
        self.temp2 = canvas_hourly.create_text(295, 235, text='20 °C')
        self.temp3 = canvas_hourly.create_text(380, 235, text='20 °C')
        self.temp4 = canvas_hourly.create_text(470, 235, text='20 °C')
        self.temp5 = canvas_hourly.create_text(560, 235, text='20 °C')
        self.temp6 = canvas_hourly.create_text(650, 235, text='20 °C')

        canvas_hourly.create_line(75, 255, 725, 255)

        canvas_hourly.create_text(107, 275, text='RealFeel', font='georgia 10 bold')

        self.tempfell1 = canvas_hourly.create_text(200, 275, text='20 °C')
        self.tempfell2 = canvas_hourly.create_text(295, 275, text='20 °C')
        self.tempfell3 = canvas_hourly.create_text(380, 275, text='20 °C')
        self.tempfell4 = canvas_hourly.create_text(470, 275, text='20 °C')
        self.tempfell5 = canvas_hourly.create_text(560, 275, text='20 °C')
        self.tempfell6 = canvas_hourly.create_text(650, 275, text='20 °C')

        canvas_hourly.create_line(75, 295, 725, 295)

        canvas_hourly.create_text(123, 315, text='Wind (km/h)', font='georgia 10 bold')

        self.wind1 = canvas_hourly.create_text(200, 315, text='20 °C')
        self.wind2 = canvas_hourly.create_text(295, 315, text='20 °C')
        self.wind3 = canvas_hourly.create_text(380, 315, text='20 °C')
        self.wind4 = canvas_hourly.create_text(470, 315, text='20 °C')
        self.wind5 = canvas_hourly.create_text(560, 315, text='20 °C')
        self.wind6 = canvas_hourly.create_text(650, 315, text='20 °C')

        canvas_hourly.create_rectangle(70, 385, 730, 550, fill='white', width=3, outline='orange')

        canvas_hourly.create_text(110, 405, text='PRECIP', font='georgia 10 bold')

        self.preciponehour = canvas_hourly.create_text(200, 405, text='11am', font='georgia 10')
        self.preciptwohour = canvas_hourly.create_text(290, 405, text='12pm', font='georgia 10')
        self.precipthreehour = canvas_hourly.create_text(380, 405, text='1pm', font='georgia 10')
        self.precipfourhour = canvas_hourly.create_text(470, 405, text='2pm', font='georgia 10')
        self.precipfivehour = canvas_hourly.create_text(560, 405, text='3pm', font='georgia 10')
        self.precipsixhour = canvas_hourly.create_text(650, 405, text='4pm', font='georgia 10')

        canvas_hourly.create_text(110, 455, text='Rain', font='georgia 10 bold')

        self.onehourRect = canvas_hourly.create_rectangle(185, 430, 215, 480, outline='white', fill='gray')
        self.twohourRect = canvas_hourly.create_rectangle(275, 455, 305, 480, outline='white', fill='gray')
        self.threehourRect = canvas_hourly.create_rectangle(365, 430, 395, 480, outline='white', fill='gray')
        self.fourhourRect = canvas_hourly.create_rectangle(455, 430, 485, 480, outline='white', fill='gray')
        self.fivehourRect = canvas_hourly.create_rectangle(545, 430, 575, 480, outline='white', fill='gray')
        self.sixhourRect = canvas_hourly.create_rectangle(635, 430, 665, 480, outline='white', fill='gray')

        self.onehourrain = canvas_hourly.create_text(200, 500, text='100%', anchor=CENTER)
        self.twohourrain = canvas_hourly.create_text(290, 500, text='100%', anchor=CENTER)
        self.threehourrain = canvas_hourly.create_text(380, 500, text='100%', anchor=CENTER)
        self.fourhourrain = canvas_hourly.create_text(470, 500, text='100%', anchor=CENTER)
        self.fivehourrain = canvas_hourly.create_text(560, 500, text='100%', anchor=CENTER)
        self.sixhourrain = canvas_hourly.create_text(650, 500, text='100%', anchor=CENTER)

        canvas_hourly.create_rectangle(70, 590, 730, 835, fill='white', width=3, outline='orange')

        canvas_hourly.create_text(110, 615, text='SKY', font='georgia 10 bold')

        self.skyonehour = canvas_hourly.create_text(200, 615, text='11am', font='georgia 10')
        self.skytwohour = canvas_hourly.create_text(290, 615, text='12pm', font='georgia 10')
        self.skythreehour = canvas_hourly.create_text(380, 615, text='1pm', font='georgia 10')
        self.skyfourhour = canvas_hourly.create_text(470, 615, text='2pm', font='georgia 10')
        self.skyfivehour = canvas_hourly.create_text(560, 615, text='3pm', font='georgia 10')
        self.skysixhour = canvas_hourly.create_text(650, 615, text='4pm', font='georgia 10')

        canvas_hourly.create_text(110, 655, text='UV Index', font='georgia 10 bold')

        self.uvindex1 = canvas_hourly.create_text(200, 655, text='3', font='arial 8')
        self.uvindex2 = canvas_hourly.create_text(290, 655, text='4', font='arial 8')
        self.uvindex3 = canvas_hourly.create_text(380, 655, text='4', font='arial 8')
        self.uvindex4 = canvas_hourly.create_text(470, 655, text='3', font='arial 8')
        self.uvindex5 = canvas_hourly.create_text(560, 655, text='2', font='arial 8')
        self.uvindex6 = canvas_hourly.create_text(650, 655, text='1', font='arial 8')

        canvas_hourly.create_line(75, 675, 725, 675)

        canvas_hourly.create_text(120, 695, text='Cloud Cover', font='georgia 10 bold')

        self.cloudcoverone = canvas_hourly.create_text(200, 695, text='85%', font='arial 8')
        self.cloudcovertwo = canvas_hourly.create_text(290, 695, text='91%', font='arial 8')
        self.cloudcoverthree = canvas_hourly.create_text(380, 695, text='95%', font='arial 8')
        self.cloudcoverfour = canvas_hourly.create_text(470, 695, text='99%', font='arial 8')
        self.cloudcoverfive = canvas_hourly.create_text(560, 695, text='97%', font='arial 8')
        self.cloudcoversix = canvas_hourly.create_text(650, 695, text='96%', font='arial 8')

        canvas_hourly.create_line(75, 715, 725, 715)

        canvas_hourly.create_text(110, 735, text='Humidity', font='georgia 10 bold')

        self.humidityone = canvas_hourly.create_text(200, 735, text='74%', font='arial 8')
        self.humiditytwo = canvas_hourly.create_text(290, 735, text='55%', font='arial 8')
        self.humiditythree = canvas_hourly.create_text(380, 735, text='45%', font='arial 8')
        self.humidityfour = canvas_hourly.create_text(470, 735, text='41%', font='arial 8')
        self.humidityfive = canvas_hourly.create_text(560, 735, text='42%', font='arial 8')
        self.humiditysix = canvas_hourly.create_text(650, 735, text='57', font='arial 8')

        canvas_hourly.create_line(75, 755, 725, 755)

        canvas_hourly.create_text(110, 775, text='Dew Point', font='georgia 10 bold')

        self.dewpointone = canvas_hourly.create_text(200, 775, text='23°', font='arial 8')
        self.dewpointtwo = canvas_hourly.create_text(290, 775, text='23°', font='arial 8')
        self.dewpointthree = canvas_hourly.create_text(380, 775, text='23°', font='arial 8')
        self.dewpointfour = canvas_hourly.create_text(470, 775, text='23°', font='arial 8')
        self.dewpointfive = canvas_hourly.create_text(560, 775, text='23°', font='arial 8')
        self.dewpointsix = canvas_hourly.create_text(650, 775, text='23°', font='arial 8')

        canvas_hourly.create_line(75, 795, 725, 795)

        canvas_hourly.create_text(110, 815, text='Visibility', font='georgia 10 bold')

        self.visibilityone = canvas_hourly.create_text(200, 815, text='6 km', font='arial 8')
        self.visibilitytwo = canvas_hourly.create_text(290, 815, text='16 km', font='arial 8')
        self.visibilitythree = canvas_hourly.create_text(380, 815, text='16 km', font='arial 8')
        self.visibilityfour = canvas_hourly.create_text(470, 815, text='16 km', font='arial 8')
        self.visibilityfive = canvas_hourly.create_text(560, 815, text='14 km', font='arial 8')
        self.visibilitysix = canvas_hourly.create_text(650, 815, text='14 km', font='arial 8')

        canvas_hourly.create_rectangle(70, 855, 730, 1150, fill='white', width=3, outline='orange')

        day = canvas_hourly.create_text(110, 875, text='TEMP °C', font='georgia 10 bold')

        self.temponehour = canvas_hourly.create_text(200, 875, text='11am', font='georgia 10')
        self.temptwohour = canvas_hourly.create_text(290, 875, text='12pm', font='georgia 10')
        self.tempthreehour = canvas_hourly.create_text(380, 875, text='1pm', font='georgia 10')
        self.tempfourhour = canvas_hourly.create_text(470, 875, text='2pm', font='georgia 10')
        self.tempfivehour = canvas_hourly.create_text(560, 875, text='3pm', font='georgia 10')
        self.tempsixhour = canvas_hourly.create_text(650, 875, text='4pm', font='georgia 10')

        self.temperature1 = canvas_hourly.create_text(95, 935, text='35°C', font='georgia 10')

        canvas_hourly.create_line(115, 938, 725, 938)

        self.temperature2 = canvas_hourly.create_text(95, 1035, text='30°C', font='georgia 10')

        canvas_hourly.create_line(115, 1038, 725, 1038)

        self.temperature3 = canvas_hourly.create_text(95, 1135, text='25°C', font='georgia 10')

        canvas_hourly.create_line(115, 1138, 725, 1138)

        self.point1 = canvas_hourly.create_oval(190, 1133, 200, 1143, outline='white', fill='gray')
        self.point2 = canvas_hourly.create_oval(280, 1133, 290, 1143, outline='white', fill='gray')
        self.point3 = canvas_hourly.create_oval(370, 1133, 380, 1143, outline='white', fill='gray')
        self.point4 = canvas_hourly.create_oval(460, 1133, 470, 1143, outline='white', fill='gray')
        self.point5 = canvas_hourly.create_oval(550, 1133, 560, 1143, outline='white', fill='gray')
        self.point6 = canvas_hourly.create_oval(640, 1133, 650, 1143, outline='white', fill='gray')

        self.line1 = canvas_hourly.create_line(200, 1138, 280, 1118, width=2)
        self.line2 = canvas_hourly.create_line(290, 1118, 370, 1098, width=2)
        self.line3 = canvas_hourly.create_line(380, 1098, 460, 1078, width=2)
        self.line4 = canvas_hourly.create_line(470, 1078, 550, 1058, width=2)
        self.line5 = canvas_hourly.create_line(560, 1058, 640, 1038, width=2)

        canvas_hourly.create_rectangle(270, 1190, 530, 1320, fill='white', width=3, outline='orange')

        canvas_hourly.create_text(345, 1215, text='SUNRISE/SUNSET', font='georgia 10 bold')

        canvas_hourly.create_text(305, 1245, text='Sunrise :', font='georgia 10')
        canvas_hourly.create_text(301, 1265, text='Sunset :', font='georgia 10')

        self.sunrise = canvas_hourly.create_text(365, 1245, text='5:46 AM', font='arial 8')
        self.sunset = canvas_hourly.create_text(365, 1265, text='6:56 PM', font='arial 8')

        self.sunduration = canvas_hourly.create_text(340, 1300, text='Duration  13:09 hrs', font='georgia 10')

        canvas_hourly.sun = ImageTk.PhotoImage(Image.open(sun100))
        canvas_hourly.create_image(425, 1200, anchor=NW, image=canvas_hourly.sun)

        self.hourlyreportchange()
        canvas_hourly.tag_bind(self.back_cancel, '<ButtonPress-1>', self.onObjectClick)

    def onObjectClick(self, event):
        print('Got object click', event.x, event.y)
        print(event.widget.find_closest(event.x, event.y))
        d = event.widget.find_closest(event.x, event.y)
        print(d[0])
        if d[0] == 17:
            self.timecanvas.delete(all)
            weather_ui(self.timecanvas)
        elif d[0] == 27 or d[0] == 26:
            self.timecanvas.delete(all)
            self.index = 0
            self.hourlyReport(self.timecanvas)
        elif d[0] == 3:
            # self.hourlytime.delete('all')
            WeatherUI(self.hourlytime, self.data, self.city, self.latlng)

    def hourlyreportchange(self):

        dayoneTime = {}
        hourlyForecast = {}
        temp = {}
        realfeel = {}
        wind = {}
        uvindex = {}
        cloudcover = {}
        humidity = {}
        dewpoint = {}
        visibility = {}
        rain = {}
        self.hourlytime.iconhourly = {}
        sunrise = str(self.sunTime(self.data['daily']['data'][0]['sunriseTime']))
        sunset = str(self.sunTime(self.data['daily']['data'][0]['sunsetTime']))
        totaltime = self.data['daily']['data'][0]['sunsetTime'] - self.data['daily']['data'][0]['sunriseTime']

        # totaltime=str(self.totalTime(totaltime))
        print(totaltime)

        for a in range(6):
            dayoneTime[a] = str(self.time_notation(self.data['hourly']['data'][a]['time']))

        for a in range(6):
            hourlyForecast[a] = str(self.data['hourly']['data'][a]['summary'])

        for a in range(6):
            temp[a] = self.temperature_conversion(self.data['hourly']['data'][a]['temperature'])

        for a in range(6):
            realfeel[a] = str(
                self.temperature_conversion(self.data['hourly']['data'][a]['apparentTemperature'])) + degree_celsius

        for a in range(6):
            wind[a] = str(self.data['hourly']['data'][a]['windSpeed'])

        for a in range(6):
            uvindex[a] = str(self.data['hourly']['data'][a]['uvIndex'])

        for a in range(6):
            cloudcover[a] = str(round(self.data['hourly']['data'][a]['cloudCover'] * 100)) + percentsign

        for a in range(6):
            humidity[a] = str(round(self.data['hourly']['data'][a]['humidity'] * 100)) + percentsign

        for a in range(6):
            dewpoint[a] = str(self.temperature_conversion(self.data['hourly']['data'][a]['dewPoint'])) + degreesign

        for a in range(6):
            visibility[a] = str(self.data['hourly']['data'][a]['visibility'])

        for a in range(6):
            rain[a] = self.data['hourly']['data'][a]['precipProbability']

        for a in range(6):
            pass
            # icon[a] = self.data['hourly']['data'][a]['icon']

        self.hourlytime.itemconfigure(self.day, text=self.cuDay)

        self.hourlytime.itemconfigure(self.onehour, text=dayoneTime[0])
        self.hourlytime.itemconfigure(self.twohour, text=dayoneTime[1])
        self.hourlytime.itemconfigure(self.threehour, text=dayoneTime[2])
        self.hourlytime.itemconfigure(self.fourhour, text=dayoneTime[3])
        self.hourlytime.itemconfigure(self.fivehour, text=dayoneTime[4])
        self.hourlytime.itemconfigure(self.sixhour, text=dayoneTime[5])

        self.hourlytime.itemconfigure(self.onehourForecast, text=hourlyForecast[0])
        self.hourlytime.itemconfigure(self.twohourForecast, text=hourlyForecast[1])
        self.hourlytime.itemconfigure(self.threehourForecast, text=hourlyForecast[2])
        self.hourlytime.itemconfigure(self.fourhourForecast, text=hourlyForecast[3])
        self.hourlytime.itemconfigure(self.fivehourForecast, text=hourlyForecast[4])
        self.hourlytime.itemconfigure(self.sixhourForecast, text=hourlyForecast[5])

        self.hourlytime.itemconfigure(self.temp1, text=str(temp[0]) + degree_celsius)
        self.hourlytime.itemconfigure(self.temp2, text=str(temp[1]) + degree_celsius)
        self.hourlytime.itemconfigure(self.temp3, text=str(temp[2]) + degree_celsius)
        self.hourlytime.itemconfigure(self.temp4, text=str(temp[3]) + degree_celsius)
        self.hourlytime.itemconfigure(self.temp5, text=str(temp[4]) + degree_celsius)
        self.hourlytime.itemconfigure(self.temp6, text=str(temp[5]) + degree_celsius)

        self.hourlytime.itemconfigure(self.tempfell1, text=realfeel[0])
        self.hourlytime.itemconfigure(self.tempfell2, text=realfeel[1])
        self.hourlytime.itemconfigure(self.tempfell3, text=realfeel[2])
        self.hourlytime.itemconfigure(self.tempfell4, text=realfeel[3])
        self.hourlytime.itemconfigure(self.tempfell5, text=realfeel[4])
        self.hourlytime.itemconfigure(self.tempfell6, text=realfeel[5])

        self.hourlytime.itemconfigure(self.wind1, text=wind[0])
        self.hourlytime.itemconfigure(self.wind2, text=wind[1])
        self.hourlytime.itemconfigure(self.wind3, text=wind[2])
        self.hourlytime.itemconfigure(self.wind4, text=wind[3])
        self.hourlytime.itemconfigure(self.wind5, text=wind[4])
        self.hourlytime.itemconfigure(self.wind6, text=wind[5])

        self.hourlytime.itemconfigure(self.preciponehour, text=dayoneTime[0])
        self.hourlytime.itemconfigure(self.preciptwohour, text=dayoneTime[1])
        self.hourlytime.itemconfigure(self.precipthreehour, text=dayoneTime[2])
        self.hourlytime.itemconfigure(self.precipfourhour, text=dayoneTime[3])
        self.hourlytime.itemconfigure(self.precipfivehour, text=dayoneTime[4])
        self.hourlytime.itemconfigure(self.precipsixhour, text=dayoneTime[5])

        self.hourlytime.itemconfigure(self.skyonehour, text=dayoneTime[0])
        self.hourlytime.itemconfigure(self.skytwohour, text=dayoneTime[1])
        self.hourlytime.itemconfigure(self.skythreehour, text=dayoneTime[2])
        self.hourlytime.itemconfigure(self.skyfourhour, text=dayoneTime[3])
        self.hourlytime.itemconfigure(self.skyfivehour, text=dayoneTime[4])
        self.hourlytime.itemconfigure(self.skysixhour, text=dayoneTime[5])

        self.hourlytime.itemconfigure(self.uvindex1, text=uvindex[0])
        self.hourlytime.itemconfigure(self.uvindex2, text=uvindex[1])
        self.hourlytime.itemconfigure(self.uvindex3, text=uvindex[2])
        self.hourlytime.itemconfigure(self.uvindex4, text=uvindex[3])
        self.hourlytime.itemconfigure(self.uvindex5, text=uvindex[4])
        self.hourlytime.itemconfigure(self.uvindex6, text=uvindex[5])

        self.hourlytime.itemconfigure(self.cloudcoverone, text=cloudcover[0])
        self.hourlytime.itemconfigure(self.cloudcovertwo, text=cloudcover[1])
        self.hourlytime.itemconfigure(self.cloudcoverthree, text=cloudcover[2])
        self.hourlytime.itemconfigure(self.cloudcoverfour, text=cloudcover[3])
        self.hourlytime.itemconfigure(self.cloudcoverfive, text=cloudcover[4])
        self.hourlytime.itemconfigure(self.cloudcoversix, text=cloudcover[5])

        self.hourlytime.itemconfigure(self.humidityone, text=humidity[0])
        self.hourlytime.itemconfigure(self.humiditytwo, text=humidity[1])
        self.hourlytime.itemconfigure(self.humiditythree, text=humidity[2])
        self.hourlytime.itemconfigure(self.humidityfour, text=humidity[3])
        self.hourlytime.itemconfigure(self.humidityfive, text=humidity[4])
        self.hourlytime.itemconfigure(self.humiditysix, text=humidity[5])

        self.hourlytime.itemconfigure(self.dewpointone, text=dewpoint[0])
        self.hourlytime.itemconfigure(self.dewpointtwo, text=dewpoint[1])
        self.hourlytime.itemconfigure(self.dewpointthree, text=dewpoint[2])
        self.hourlytime.itemconfigure(self.dewpointfour, text=dewpoint[3])
        self.hourlytime.itemconfigure(self.dewpointfive, text=dewpoint[4])
        self.hourlytime.itemconfigure(self.dewpointsix, text=dewpoint[5])

        self.hourlytime.itemconfigure(self.visibilityone, text=visibility[0])
        self.hourlytime.itemconfigure(self.visibilitytwo, text=visibility[1])
        self.hourlytime.itemconfigure(self.visibilitythree, text=visibility[2])
        self.hourlytime.itemconfigure(self.visibilityfour, text=visibility[3])
        self.hourlytime.itemconfigure(self.visibilityfive, text=visibility[4])
        self.hourlytime.itemconfigure(self.visibilitysix, text=visibility[5])

        self.hourlytime.itemconfigure(self.temponehour, text=dayoneTime[0])
        self.hourlytime.itemconfigure(self.temptwohour, text=dayoneTime[1])
        self.hourlytime.itemconfigure(self.tempthreehour, text=dayoneTime[2])
        self.hourlytime.itemconfigure(self.tempfourhour, text=dayoneTime[3])
        self.hourlytime.itemconfigure(self.tempfivehour, text=dayoneTime[4])
        self.hourlytime.itemconfigure(self.tempsixhour, text=dayoneTime[5])

        for a in range(6):
            icon = str(self.data['daily']['data'][a]['icon'])
            if icon == 'cloudy':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(cloudy24))
            elif icon == 'clear-day':
                pass
                # self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(sun24))
            elif icon == 'clear-night':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(clearnight24))
            elif icon == 'rain':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(rain24))
            elif icon == 'snow':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(snow24))
            elif icon == 'sleet':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(sleet24))
            elif icon == 'wind':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(wind24))
            elif icon == 'partly-cloudy-day':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(cloudysun24))
            elif icon == 'partly-cloudy-night':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(cloudynight24))
            elif icon == 'fog':
                self.hourlytime.iconhourly[a] = ImageTk.PhotoImage(Image.open(foggyday64))

        self.hourlytime.itemconfigure(self.onehourImgShow, image=self.hourlytime.iconhourly[0])
        self.hourlytime.itemconfigure(self.twohourImgShow, image=self.hourlytime.iconhourly[1])
        self.hourlytime.itemconfigure(self.threehourImgShow, image=self.hourlytime.iconhourly[2])
        self.hourlytime.itemconfigure(self.fourhourImgShow, image=self.hourlytime.iconhourly[3])
        self.hourlytime.itemconfigure(self.fivehourImgShow, image=self.hourlytime.iconhourly[4])
        self.hourlytime.itemconfigure(self.sixhourImgShow, image=self.hourlytime.iconhourly[5])

        item1xy = self.get_coordinate(self.onehourRect, self.hourlytime, rain[0])
        item2xy = self.get_coordinate(self.twohourRect, self.hourlytime, rain[1])
        item3xy = self.get_coordinate(self.threehourRect, self.hourlytime, rain[2])
        item4xy = self.get_coordinate(self.fourhourRect, self.hourlytime, rain[3])
        item5xy = self.get_coordinate(self.fivehourRect, self.hourlytime, rain[4])
        item6xy = self.get_coordinate(self.sixhourRect, self.hourlytime, rain[5])

        self.hourlytime.coords(self.onehourRect, item1xy)
        self.hourlytime.itemconfigure(self.onehourRect)

        self.hourlytime.coords(self.twohourRect, item2xy)
        self.hourlytime.itemconfigure(self.twohourRect)

        self.hourlytime.coords(self.threehourRect, item3xy)
        self.hourlytime.itemconfigure(self.threehourRect)

        self.hourlytime.coords(self.fourhourRect, item4xy)
        self.hourlytime.itemconfigure(self.fourhourRect)

        self.hourlytime.coords(self.fivehourRect, item5xy)
        self.hourlytime.itemconfigure(self.fivehourRect)

        self.hourlytime.coords(self.sixhourRect, item6xy)
        self.hourlytime.itemconfigure(self.sixhourRect)

        self.hourlytime.itemconfigure(self.onehourrain, text=str(round(rain[0] * 100)) + percentsign)
        self.hourlytime.itemconfigure(self.twohourrain, text=str(round(rain[1] * 100)) + percentsign)
        self.hourlytime.itemconfigure(self.threehourrain, text=str(round(rain[2] * 100)) + percentsign)
        self.hourlytime.itemconfigure(self.fourhourrain, text=str(round(rain[3] * 100)) + percentsign)
        self.hourlytime.itemconfigure(self.fivehourrain, text=str(round(rain[4] * 100)) + percentsign)
        self.hourlytime.itemconfigure(self.sixhourrain, text=str(round(rain[5] * 100)) + percentsign)

        mintemp = self.min_temp(temp)
        print(temp[mintemp])
        maxtemp = self.max_temp(temp)
        print(temp[maxtemp])

        min = temp[mintemp] % 5
        mintemp = temp[mintemp] - min

        if (temp[maxtemp] - mintemp) < 5:
            maxtemp = mintemp + 10
        elif temp[maxtemp] - mintemp < 10:
            max = temp[maxtemp] % 5
            maxtemp = temp[maxtemp] - max
            maxtemp = maxtemp + 5

        self.hourlytime.itemconfigure(self.temperature3, text=mintemp)
        self.hourlytime.itemconfigure(self.temperature2, text=mintemp + 5)
        self.hourlytime.itemconfigure(self.temperature1, text=maxtemp)

        coord1 = self.get_pointcoords(temp[0], mintemp, self.point1, self.hourlytime)
        coord2 = self.get_pointcoords(temp[1], mintemp, self.point2, self.hourlytime)
        coord3 = self.get_pointcoords(temp[2], mintemp, self.point3, self.hourlytime)
        coord4 = self.get_pointcoords(temp[3], mintemp, self.point4, self.hourlytime)
        coord5 = self.get_pointcoords(temp[4], mintemp, self.point5, self.hourlytime)
        coord6 = self.get_pointcoords(temp[5], mintemp, self.point6, self.hourlytime)

        self.hourlytime.coords(self.point1, coord1)
        self.hourlytime.itemconfigure(self.point1)

        self.hourlytime.coords(self.point2, coord2)
        self.hourlytime.itemconfigure(self.point2)

        self.hourlytime.coords(self.point3, coord3)
        self.hourlytime.itemconfigure(self.point3)

        self.hourlytime.coords(self.point4, coord4)
        self.hourlytime.itemconfigure(self.point4)

        self.hourlytime.coords(self.point5, coord5)
        self.hourlytime.itemconfigure(self.point5)

        self.hourlytime.coords(self.point6, coord6)
        self.hourlytime.itemconfigure(self.point6)

        linecoorsd1 = self.get_linecoords(self.hourlytime, self.line1, self.point1, self.point2)
        linecoorsd2 = self.get_linecoords(self.hourlytime, self.line2, self.point2, self.point3)
        linecoorsd3 = self.get_linecoords(self.hourlytime, self.line3, self.point3, self.point4)
        linecoorsd4 = self.get_linecoords(self.hourlytime, self.line4, self.point4, self.point5)
        linecoorsd5 = self.get_linecoords(self.hourlytime, self.line5, self.point5, self.point6)

        self.hourlytime.coords(self.line1, linecoorsd1)
        self.hourlytime.itemconfigure(self.line1)

        self.hourlytime.coords(self.line2, linecoorsd2)
        self.hourlytime.itemconfigure(self.line1)

        self.hourlytime.coords(self.line3, linecoorsd3)
        self.hourlytime.itemconfigure(self.line3)

        self.hourlytime.coords(self.line4, linecoorsd4)
        self.hourlytime.itemconfigure(self.line4)

        self.hourlytime.coords(self.line5, linecoorsd5)
        self.hourlytime.itemconfigure(self.line5)

        self.hourlytime.itemconfigure(self.sunrise, text=sunrise)
        self.hourlytime.itemconfigure(self.sunset, text=sunset)

    def time_notation(self, timestamp):
        value = datetime.datetime.fromtimestamp(timestamp)
        return (value.strftime('%I%p'))

    def totalTime(self, totaltime):
        value = datetime.datetime.fromtimestamp(totaltime)
        return (value.strftime('%H:%M'))

    def get_coordinate(self, items, canvas4, rainper):
        coordinate = canvas4.coords(items)
        coordinate[1] = coordinate[3] - 50 * rainper
        return coordinate

    def min_temp(self, temp):
        return min(temp.items(), key=operator.itemgetter(1))[0]

    def max_temp(self, temp):
        return max(temp.items(), key=operator.itemgetter(1))[0]

    def get_pointcoords(self, temp, mintemp, items, canvas4):
        pointcor = temp - mintemp
        point = pointcor * 20
        coordinate = canvas4.coords(items)
        coordinate[1] = coordinate[1] - point
        coordinate[3] = coordinate[3] - point
        return coordinate

    def get_linecoords(self, canvas4, items, items1, items2):
        coordinate = canvas4.coords(items)
        coordinate1 = canvas4.coords(items1)
        coordinate2 = canvas4.coords(items2)
        coordinate[1] = coordinate1[1] + 5
        coordinate[3] = coordinate2[1] + 5
        return coordinate


def search_text():
    search_string = hostAddress + search.get() + "&key=" + googleAPIKey
    try:
        python23 = urllib.request.urlopen(search_string)
        python2 = python23.read()
        python24 = python2.decode('utf-8')

        kp = json.loads(python24)
        k = kp['results'][0]['geometry']['location']
        city_name = kp['results'][0]['address_components'][0]['short_name']
        city_name2 = kp['results'][0]['address_components'][2]['short_name']
        lat = str(k['lat'])
        lng = str(k['lng'])
        latlng = {'lat': lat, 'lng': lng}
        city = city_name + " " + city_name2

        kp = weather_report(lat, lng)
        print(kp['hourly']['data'])

        if kp:
            UI = WeatherUI(canvas2, kp, city, latlng)

    except Exception:
        messagebox.showwarning("Error", "Write  right city name")
    # print(python23)


def weather_report(lat, lng):
    darkSkyString = hostWeather + darkSkyAPI + "/" + lat + "," + lng
    python23 = urllib.request.urlopen(darkSkyString)
    python2 = python23.read()
    python24 = python2.decode('utf-8')
    # print(python24)
    kp = json.loads(python24)
    return kp


def weather_ui(canvas3):
    global canvas2, search
    canvas2 = Canvas(canvas3, height=500, width=800)
    canvas2.pack()
    canvas2.filename = ImageTk.PhotoImage(Image.open(background))
    image = canvas2.create_image(0, 0, anchor=NW, image=canvas2.filename)
    title = canvas2.create_text(410, 70, text='Weather Forecast', fill='white', font='georgia 40 bold')
    searchTitle = canvas2.create_text(400, 150, text='Search The Location', fill='white', font='georgia 25 bold')
    search = Entry(canvas2, width=30, borderwidth=5)
    search.place(x=300, y=200)
    searchButton = Button(canvas2, text="Search", bg='white', borderwidth=10, command=search_text)
    searchButton.place(x=350, y=250)


if __name__ == "__main__":
    root = Tk()
    root.maxsize(width=800, height=500)
    root.minsize(width=800, height=500)
    root.title('Weather Forecast')
    weather_ui(root)
    # weather = WeatherUI(root, '', '', '')
    # weather.hourlyReport(root)
    # print(rain128)

    mainloop()
