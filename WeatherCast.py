from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


'''
This program uses an API to get the weather data of a city and displays it on an interactive user interface.
It displays the current time and date of the city.
It uses the geopy library to get the longitude and latidude of the city and the timezonefinder library to get the timezone of the city.
It uses the tkinter library to create the user interface.
It uses the PIL library to display the weather icons on the user interface.
'''
    
# test commit xomment    
root=Tk()
root.title("Weather Forecast App") #title of the app
root.geometry("890x470+300+300") #size of the app
root.configure(bg="#57adff") #background color of the app 
root.resizable(0,0) #to make the app non resizable


#This function is used to get the weather data from the API
def getWeather(): 
    city=textfield.get() 
    
    geolocator = Nominatim(user_agent="geoapiExercises")  
    location = geolocator.geocode(city) #to get the location of the city
    obj = TimezoneFinder()
    
    #To get the timezone of the city
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude) 
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N{round(location.longitude,4)}°E")
    
    home = pytz.timezone(result) #to get the timezone of the city
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p") #to get the current time of the city and display it on the app
    clock.config(text=current_time)
    current_date = local_time.strftime("%a, %b %d %Y") #to get the current date of the city and display it on the app
    date.config(text=current_date)
    
    
    #Weather API Key and URL.
    api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=imperial&exclude=hourly&appid=edd1d56dc87020dcc2f055e1779c4808"
    json_data = requests.get(api).json() #Sends a request to get the data from the API
    
    #It gets the current temperature, humidity, pressure, wind speed and description of the weather from the API
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
    
    t.config(text=(temp, "°F")) #to display the temperature in Fahrenheit
    h.config(text=(humidity, "%")) #to display the humidity in percentage
    p.config(text=(pressure, "hPa")) #to display the pressure in hectopascals
    w.config(text=(wind, "mph")) #to display the wind speed in miles per hour
    d.config(text=(description)) #to display the description of the weather
    
    
    #First Box: It gets the weather icon of the current day and displays it on the app
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    
    img1 = (Image.open(f"icon/{firstdayimage}@2x.png")) 
    resized_image = img1.resize((75, 75)) #to resize the image
    photo1 = ImageTk.PhotoImage(resized_image)
    firstimage.config(image=photo1) 
    firstimage.image = photo1
    firstimage.place(x=5, y=34)
    
    #It gets the temperature of the day and night and displays it on the app
    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']
    day1temp.config(text=f"Day: {tempday1}°F\nNight: {tempnight1}°F")
    day1temp.place(x=80, y=48)
     
    #Second box: It gets the weather icon of the current day and displays it on the app
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']
    
    img2 = (Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img2.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2
    
    #It gets the temperature of the day and night and displays it on the app
    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']
    day2temp.config(text=f"Day:{tempday2}\nNight:{tempnight2}")

    #Third box: It gets the weather icon of the current day and displays it on the app
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img3 = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img3.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3
    
    #It gets the temperature of the day and night and displays it on the app
    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']
    day3temp.config(text=f"Day:{tempday3}\nNight:{tempnight3}") 

    #Fourth box: It gets the weather icon of the current day and displays it on the app
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img4 = (Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img4.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4
    
    #It gets the temperature of the day and night and displays it on the app
    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']
    day4temp.config(text=f"Day:{tempday4}\nNight:{tempnight4}")
    
    #Fifth box: It gets the weather icon of the current day and displays it on the app
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img5 = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img5.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5
    
    #It gets the temperature of the day and night and displays it on the app
    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{tempday5}\nNight:{tempnight5}")
    
    #Sixth box: It gets the weather icon of the current day and displays it on the app
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']
    
    img6 = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img6.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6
    
    #It gets the temperature of the day and night and displays it on the app
    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{tempday6}\nNight:{tempnight6}")


    #Seventh box: It gets the weather icon of the current day and displays it on the app
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img7 = (Image.open(f"icon/{seventhdayimage}@2x.png"))
    resized_image = img7.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7
    
    #It gets the temperature of the day and night and displays it on the app
    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{tempday7}\nNight:{tempnight7}")

    #Days of the week
    first = datetime.now() #gets the current date
    day1.config(text=first.strftime("%A")) #displays the current day of the week
    
    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    
    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    
    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))
    
    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    
    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    
    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))
    

#ICONS
image_icon=PhotoImage(file="Images/logo.png") #to set the icon of the app
root.iconphoto(False,image_icon) 

Round_box = Image.open("Images/Rounded Rectangle 1.png")   #to set the background of the weather data box
new_size = (225, 115) #to resize the image
resized_image = Round_box.resize(new_size)  
new_image = ImageTk.PhotoImage(resized_image) #to convert the image to a photoimage after resizing
new_label = tk.Label(root, image=new_image, bg="#000000").place(x=30, y=110)


#Labels for the weather data
label1 = Label(root, text="Temperature: ", font = ("Arial", 11, "bold"), bg="#203243", fg="white") 
label1.place(x=40, y=120)

label2 = Label(root, text="Humidity: ", font = ("Arial", 11, "bold"), bg="#203243", fg="white")
label2.place(x=40, y=140)

label3 = Label(root, text="Pressure: ", font = ("Arial", 11, "bold"), bg="#203243", fg="white")
label3.place(x=40, y=160)

label4 = Label(root, text="Wind Speed: ", font = ("Arial", 11, "bold"), bg="#203243", fg="white")
label4.place(x=40, y=180)

label5 = Label(root, text="Description: ", font = ("Arial", 11, "bold"), bg="#203243", fg="white")
label5.place(x=40, y=200)


#Search Box
Search_box = PhotoImage(file="Images/Rounded Rectangle 3.png") #to set the background of the search box
myimage=Label(image=Search_box, bg="#57adff").place(x=270, y=110)

weat_image=PhotoImage(file="Images/Layer 7.png") 
weatherImage=Label(image=weat_image, bg="#203243").place(x=290, y=117)

textfield=tk.Entry(root,justify='center',width=15,font=("Poppins", 25, "bold"), bg="#203243",border=0, fg="white") #to set the search box
textfield.place(x=370, y=120)
textfield.focus() #to set the cursor in the search box

Search_icon=PhotoImage(file="Images/Layer 6.png") #to set the search icon
myimage_icon=Button(image=Search_icon,borderwidth=0, cursor="hand2", bg="#203243",command=getWeather)
myimage_icon.place(x=645, y=115)


#Bottom Half of the App
frame=Frame(root, bg="#212120", width=900, height=180) 
frame.pack(side=BOTTOM)


#Bottom Boxes
firstbox=PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox=PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame,image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame,image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame,image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame,image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame,image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame,image=secondbox, bg="#212120").place(x=800, y=30)


#Clock(for time)
clock=Label(root, font=("Arial", 30, "bold"), bg="#57adff", fg="white")
clock.place(x=50, y=20)

#Date
date=Label(root, font=("Arial", 20), bg="#57adff", fg="white")
date.place(x=30, y=60)

#Timezone
timezone=Label(root, font=("Arial", 20, "bold"), bg="#57adff", fg="white")
timezone.place(x=600, y=25)

long_lat=Label(root, font=("Arial", 10), bg="#57adff", fg="white")
long_lat.place(x=600, y=55)


#Labels for the values of the weather data
t=Label(root, font=("Arial", 11), bg="#203243", fg="white")
t.place(x=140, y=120)

h=Label(root, font=("Arial", 11), bg="#203243", fg="white")
h.place(x=140, y=140)

p=Label(root, font=("Arial", 11), bg="#203243", fg="white")
p.place(x=140, y=160)

w=Label(root, font=("Arial", 11), bg="#203243", fg="white")
w.place(x=140, y=180)

d=Label(root, font=("Arial", 11), bg="#203243", fg="white")
d.place(x=140, y=200)


#First Box
firstframe= Frame(root, bg="#282829", width=230, height=132) #to set the background of the first box
firstframe.place(x=35, y=315)

day1=Label(firstframe, font=("Arial", 20, "bold"), bg="#282829", fg="#fff") #to set the day of the first box
day1.place(relx=0.5, rely=0.17, anchor=CENTER)

firstimage=Label(firstframe, bg="#282829") #to set the image of the first box
firstimage.place(x=1,y=15)

day1temp = Label(firstframe, font=("Arial", 15, "bold"), bg="#282829", fg="#57adff") #to set the temperature of the first box
day1temp.place(x=100, y=50)

#Second Box
secondframe= Frame(root, bg="#282829", width=70, height=115) #to set the background of the second box
secondframe.place(x=305, y=325) 

day2=Label(secondframe, bg="#282829", fg="#fff") #to set the day of the second box
day2.place(relx=0.5, rely=0.12, anchor=CENTER)

secondimage=Label(secondframe, bg="#282829") #to set the image of the second box
secondimage.place(x=7,y=23)

day2temp = Label(secondframe, bg="#282829", fg="#57adff") #to set the temperature of the second box
day2temp.place(relx=0.5, y=88, anchor=CENTER)

#Third Box
thirdframe= Frame(root, bg="#282829", width=70, height=115) #to set the background of the third box
thirdframe.place(x=405, y=325)

day3=Label(thirdframe, bg="#282829", fg="#fff") #to set the day of the third box
day3.place(relx=0.5, rely=0.12, anchor=CENTER)

thirdimage=Label(thirdframe, bg="#282829") #to set the image of the third box
thirdimage.place(x=7,y=23)

day3temp = Label(thirdframe, bg="#282829", fg="#57adff") #to set the temperature of the third box
day3temp.place(relx=0.5, y=88, anchor=CENTER)

#Fourth Box
fourthframe= Frame(root, bg="#282829", width=70, height=115) #to set the background of the fourth box
fourthframe.place(x=505, y=325)

day4=Label(fourthframe, bg="#282829", fg="#fff") #to set the day of the fourth box
day4.place(relx=0.5, rely=0.12, anchor=CENTER)

fourthimage=Label(fourthframe, bg="#282829") #to set the image of the fourth box
fourthimage.place(x=7,y=23)

day4temp = Label(fourthframe, bg="#282829", fg="#57adff") #to set the temperature of the fourth box
day4temp.place(relx=0.5, y=88, anchor=CENTER)

#Fifth Box
fifthframe= Frame(root, bg="#282829", width=70, height=115) #to set the background of the fifth box
fifthframe.place(x=605, y=325)

day5=Label(fifthframe, bg="#282829", fg="#fff") #to set the day of the fifth box
day5.place(relx=0.5, rely=0.12, anchor=CENTER)

fifthimage=Label(fifthframe, bg="#282829") #to set the image of the fifth box
fifthimage.place(x=7,y=23)

day5temp = Label(fifthframe, bg="#282829", fg="#57adff") #to set the temperature of the fifth box
day5temp.place(relx=0.5, y=88, anchor=CENTER)

#Sixth Box
sixthframe= Frame(root, bg="#282829", width=70, height=115) #to set the background of the sixth box
sixthframe.place(x=705, y=325)

day6=Label(sixthframe, bg="#282829", fg="#fff") #to set the day of the sixth box
day6.place(relx=0.5, rely=0.12, anchor=CENTER)

sixthimage=Label(sixthframe, bg="#282829") #to set the image of the sixth box
sixthimage.place(x=7,y=23)

day6temp = Label(sixthframe, bg="#282829", fg="#57adff") #to set the temperature of the sixth box
day6temp.place(relx=0.5, y=88, anchor=CENTER)

#Seventh Box
seventhframe= Frame(root, bg="#282829", width=70, height=115) #to set the background of the seventh box
seventhframe.place(x=805, y=325)

day7=Label(seventhframe, bg="#282829", fg="#fff") #to set the day of the seventh box
day7.place(relx=0.5, rely=0.12, anchor=CENTER)

seventhimage=Label(seventhframe, bg="#282829") #to set the image of the seventh box
seventhimage.place(x=7,y=23)

day7temp = Label(seventhframe, bg="#282829", fg="#57adff") #to set the temperature of the seventh box
day7temp.place(relx=0.5, y=88, anchor=CENTER)


root.mainloop()