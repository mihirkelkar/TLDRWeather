
def getCodes():
    f = open('weather_funny.txt','r')
    lines = f.readlines()
    f.close()
    codes = {}
    images = {}
    for line in lines:
        l = line.split()
        weather_code = int(l[0])
        codes[weather_code] = " ".join(l[1:])
        
        if weather_code in range(200, 233):
            images[weather_code] = "thunder.png"   
        
        elif weather_code in range(300, 532):
            images[weather_code] = "rain.png"   

        elif weather_code in range(600, 623):
            images[weather_code] = "snow.png"   

        elif weather_code in range(701, 782):
            images[weather_code] = "fog.png"   

        elif weather_code == 800:
            images[weather_code] = "sunny.png"   

        elif weather_code in range(801, 805):
            images[weather_code] = "cloudy.png"   

        elif weather_code == 903:
            images[weather_code] = "cold.png"   

        elif weather_code == 904:
            images[weather_code] = "hot.png"   
            
        elif weather_code == 905:
            images[weather_code] = "windy.png"   

    return codes, images

codes, images = getCodes()
