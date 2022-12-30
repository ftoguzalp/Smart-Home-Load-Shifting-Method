import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df=pd.read_excel("Electronic.xlsx")

df.drop(["Unnamed: 0","Unnamed: 6"],axis=1,inplace=True)
df.rename(columns = {"Unnamed: 1":'Category',"Unnamed: 2":'Electronic Devices',"Unnamed: 3":"Power","Unnamed: 4":"Hour/Day","Unnamed: 5":"Priority (1-2-3)"}, inplace = True)
df = df.tail(-1)
print(df.head(5))
df.dropna(inplace=True)
df = df.convert_dtypes()
df['Power'] = df['Power'].astype('str')
df['Power'] = df['Power'].str.replace('W', '')
df['Power'] = pd.to_numeric(df['Power'], errors='coerce')
df['Electronic Devices'] = df['Electronic Devices'].astype('str')
df.info()
print(df.head())



f, ax = plt.subplots(1)
xdata = df['Electronic Devices']
ydata = df["Power"]
ax.plot(xdata, ydata)
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
ax.set_title("Electronic Devices Power Level")
plt.xlabel('Name of Electronic Devices')
plt.ylabel("Power Level(W)")
plt.xticks(rotation=90)
plt.tight_layout()



Time_Interval=20

while Time_Interval >24 or Time_Interval<0:
    print("Please write your time interval in HH.MM format" )



if 23.59> Time_Interval >= 22.00 or 06.00> Time_Interval >= 00.00 :
    print("It is night.")
elif 17.00> Time_Interval >= 06.00:
    print("It is daytime.")
elif (22.00> Time_Interval >= 17.00):
   print("It is evening.")


Total_Power = df['Power'].sum()
print(f"Total power of home is equal to = {Total_Power} Watt")

#Total_Power = df['Power'].sum()




#Solar production from 5kW Solar System in winter

def sun_output_winter(Time_Interval):
    if 06.00 >= Time_Interval > 00.00 :
        pv_output=0
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 07.00 >= Time_Interval > 06.00:
        pv_output=300
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 08.00 >= Time_Interval > 07.00:
        pv_output=600
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 09.00 >= Time_Interval > 08.00:
        pv_output=1500
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 10.00 >= Time_Interval > 09.00:
        pv_output=2000
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 11.00 >= Time_Interval > 10.00:
        pv_output=2500
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 12.00 >= Time_Interval > 11.00:
        pv_output=3000
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 13.00 >= Time_Interval > 12.00:
        pv_output=2500
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 14.00 >= Time_Interval > 13.00:
        pv_output=2000
        print(f"Pv output in a winter day is equal to {pv_output}"),
    elif 15.00 >= Time_Interval > 14.00:
        pv_output=1500
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 16.00 >= Time_Interval > 15.00:
        pv_output=550
        print(f"Pv output in a winter day is equal to {pv_output}")
    elif 17.00 >= Time_Interval > 16.00:
        pv_output=300
        print(f"Pv output in a winter day is equal to {pv_output}")
    else:
        pv_output=0
        print(f"Pv output in a winter day is equal to {pv_output}")


pv_summer_output=[0,0,0,0,0,0,0,300,600,1500,2000,2500,3000,2500,2000,1500,550,300,0,0,0,0,0,0]

def sun_output_summer(Time_Interval):
    if 04.00 >= Time_Interval > 00.00 :
        pv_output=0
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 05.00 >= Time_Interval > 04.00:
        pv_output=300
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 06.00 >= Time_Interval > 05.00:
        pv_output=750
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 07.00 >= Time_Interval > 06.00:
        pv_output=1200
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 08.00 >= Time_Interval > 07.00:
        pv_output=1800
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 09.00 >= Time_Interval > 08.00:
        pv_output=2500
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 10.00 >= Time_Interval > 09.00:
        pv_output=3200
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 11.00 >= Time_Interval > 10.00:
        pv_output=3500
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 12.00 >= Time_Interval > 11.00:
        pv_output=4000
        print(f"Pv output in a summer day is equal to {pv_output}"),
    elif 13.00 >= Time_Interval > 12.00:
        pv_output=3500
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 14.00 >= Time_Interval > 13.00:
        pv_output=3200
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 15.00 >= Time_Interval > 14.00:
        pv_output=2500
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 16.00 >= Time_Interval > 15.00:
        pv_output=1800
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 17.00 >= Time_Interval > 16.00:
        pv_output=1200
        print(f"Pv output in a summer day is equal to {pv_output}")
    elif 18.00 >= Time_Interval > 17.00:
        pv_output=700
        print(f"Pv output in a summer day is equal to {pv_output}")
    else:
        pv_output=0
        print(f"Pv output in a summer day is equal to {pv_output}")

pv_summer_output=[0,0,0,0,0,300,750,1200,1800,2500,3200,3500,4000,3500,3200,2500,1800,1200,700,0,0,0,0,0]

#sun_output_winter(Time_Interval)
#sun_output_summer(Time_Interval)

winter_devices = df['Electronic Devices'].tolist()
winter_devices.remove("Air Conditioning 12000BTU")
#print(winter_devices)

summer_devices = df['Electronic Devices'].tolist()
summer_devices.remove("Heater")
#print(summer_devices)

df_summer=df.drop(df.loc[df['Electronic Devices']=="Heater"].index)
df_summer['Hour/Day'] = df_summer['Hour/Day'].str.rstrip('hours')
df_summer['Hour/Day'] = df_summer['Hour/Day'].astype(float)



devicessummer=df_summer.loc[df_summer['Hour/Day']==24]
devices_powersummer=devicessummer["Power"].sum()
print(f"Total power of devices that work all day is {devices_powersummer}")
df_summer2=df_summer.drop(df_summer.loc[df_summer['Hour/Day']==24].index)
df_summer2['Hour/Day'] = df_summer2['Hour/Day'].astype('str')
df_summer2['Hour/Day'] = df_summer2['Hour/Day'].str.rstrip('hours')
df_summer2['Hour/Day'] = df_summer2['Hour/Day'].astype(float)
print(df_summer2)
print(df_summer.tail())

#To avoid rewriting variables I am just gonna change values.
df_winter=df.drop(df.loc[df['Electronic Devices']=="Heater"].index)



df_winter['Hour/Day'] = df_winter['Hour/Day'].str.rstrip('hours')
df_winter['Hour/Day'] = df_winter['Hour/Day'].astype(float)
print(df_winter)
print(df_winter.dtypes)

devices=df_winter.loc[df_winter['Hour/Day']==24]
devices_powerwinter=devices["Power"].sum()
print(f"Total power of devices that work all day is {devices_powerwinter}")
df_winter2=df_winter.drop(df_winter.loc[df_winter['Hour/Day']==24].index)
df_winter2['Hour/Day'] = df_winter2['Hour/Day'].astype('str')
df_winter2['Hour/Day'] = df_winter2['Hour/Day'].str.rstrip('hours')
df_winter2['Hour/Day'] = df_winter2['Hour/Day'].astype(float)
print(df_winter2)
#Asking user to choose which devices they want to enable during time interval.
peak_power=17000
usedpower_forgraph=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
device_dict={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],14:[],15:[],16:[],17:[],18:[],19:[],20:[],21:[],22:[],23:[]}

for x in range(0,24):
    usedpower_forgraph[x]+=devices_powerwinter

battery_soc=peak_power/20
battery_soc_list=[850,850,850,850,850,850,850,0,0,0,0,0,0,0,0,0,0,0,0,0,2550,2550,2550,2550]
stop_count=0
for z in range (17,20):
    usedpower_forgraph[z]-=8500*(3/10)

while True:   
    while True:
            try:
             Time_Interval=float((input("Enter your current time:(Please write your time interval between 0-23)\n")))
            except ValueError:
                print("You have made a mistake with typing.Please try again.")
                continue

        



            if 23.59> Time_Interval >= 22.00 or 06.00> Time_Interval >= 00.00 :
                print("It is night.")
            elif 17.00> Time_Interval >= 06.00:
                print("It is daytime.")
            elif (22.00> Time_Interval >= 17.00):
                print("It is evening.")

       
            break
        
    stop_count+=1
    
    
    for x in range(7,18):
        if pv_summer_output[x] < (peak_power/10):
            battery_soc+=pv_summer_output[x]
            battery_soc_list[x]=battery_soc
        if pv_summer_output[x] >= (peak_power/10) :   
            battery_soc+=(peak_power/10)
            battery_soc_list[x]=battery_soc
        if battery_soc > (peak_power/2)*(8/10):
            battery_soc=(peak_power/2)*(8/10)
            battery_soc_list[x]=battery_soc      
    for x in range (18,20):
        battery_soc-=(peak_power/2)*(3/10)
        battery_soc_list[x]=battery_soc

 #Using battery power to reduce power taken from the grid.
    print(usedpower_forgraph)


    print(device_dict)
    
    for x in range (0,24):
        if usedpower_forgraph[x]>peak_power:
            df_winter2_priority1=df_winter2.loc[df_winter2["Priority (1-2-3)"]==1]
            df_winter2_priority1.drop(["Category","Power","Hour/Day"],axis=1,inplace=True)
            df_winter2_priority1["Electronic Devices"]
            #if df_winter2_priority1["Electronic Devices"] == device_dict[x] :
            df_winter2_priority2=df_winter2.loc[df_winter2["Priority (1-2-3)"]==2]
            df_winter2_priority2.drop(["Category","Power","Hour/Day"],axis=1,inplace=True)
            df_winter2_priority3=df_winter2.loc[df_winter2["Priority (1-2-3)"]==3]
            df_winter2_priority3.drop(["Category","Power","Hour/Day"],axis=1,inplace=True)
            #print(df_winter2_priority1)
            #print(df_winter2_priority2)
            for y in device_dict[x]:
                if y in df_winter2_priority3["Electronic Devices"].tolist():
                    device_dict[x].remove(y)
                    usedpower_forgraph[x]=usedpower_forgraph[x]-((df_winter2["Power"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])*(df_winter2["Hour/Day"].loc[df_winter2["Electronic Devices"]==y].tolist()[0]))
                    print(usedpower_forgraph)
                    loadshifthour=0
                    #int(input("Enter the time you want to shift your loads to.(It must be between 0-23"))
                    device_dict[loadshifthour].append(y)
                    usedpower_forgraph[loadshifthour]+=df_winter2["Power"].loc[df_winter2["Electronic Devices"]==y].tolist()[0]*(df_winter2["Hour/Day"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])
                print(f"Devices that above peak load at {x} o'clock are {device_dict[x]}")   
        if usedpower_forgraph[x]>peak_power:           
            for y in device_dict[x]:
                if y in df_winter2_priority2["Electronic Devices"].tolist():
                    usedpower_forgraph[x]=usedpower_forgraph[x]-((df_winter2["Power"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])*(df_winter2["Hour/Day"].loc[df_winter2["Electronic Devices"]==y].tolist()[0]))
                    device_dict[x].remove(y)
                    print(usedpower_forgraph)
                    device_dict[loadshifthour].append(y)
                    usedpower_forgraph[loadshifthour]+=(df_winter2["Power"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])*(df_winter2["Hour/Day"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])
            
                print(f"Devices that above peak load at {x} o'clock are {device_dict[x]}")
        if usedpower_forgraph[x]>peak_power:           
            for y in device_dict[x]:
                if y in df_winter2_priority1["Electronic Devices"].tolist():
                    usedpower_forgraph[x]=usedpower_forgraph[x]-((df_winter2["Power"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])*(df_winter2["Hour/Day"].loc[df_winter2["Electronic Devices"]==y].tolist()[0]))
                    device_dict[x].remove(y)
                    print(usedpower_forgraph)
                    device_dict[loadshifthour].append(y)
                    usedpower_forgraph[loadshifthour]+=(df_winter2["Power"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])*(df_winter2["Hour/Day"].loc[df_winter2["Electronic Devices"]==y].tolist()[0])
            
                print(f"Devices that above peak load at {x} o'clock are {device_dict[x]}")
        
    category=input("Choose the category your device belongs to ?\nKitchen,Major Appliance,Personal Care,Entertainment,Lighting \n")
    print(device_dict)
    print(usedpower_forgraph)


    if category in df_winter2.Category.unique():
        dfwinter2_devices=df_winter2.loc[df_winter2["Category"]==category]
        dfwinter2_devices2=dfwinter2_devices["Electronic Devices"]
        print(dfwinter2_devices2.tolist())
        device=input("Choose the device you want to add from above options.\n")
        if device in dfwinter2_devices2.tolist():
            df_winter2_device=(df_winter2.loc[df_winter2["Electronic Devices"]==device])
            if df_winter2_device["Hour/Day"].values[0] <= 1:
                usedpower=(df_winter2_device["Power"]*df_winter2_device["Hour/Day"]).values[0]
                usedpower_forgraph[int(Time_Interval)]+=usedpower
                device_dict[int(Time_Interval)].append(device)
            else:
                usedpower=(df_winter2_device["Power"]*1).values[0]
                if Time_Interval+df_winter2_device["Hour/Day"].values[0] >= 24:
                    x=24-(Time_Interval)          
                    for y in range(0,int(x)):
                        usedpower_forgraph[int(Time_Interval+y)]+=usedpower
                        device_dict[int(Time_Interval+y)].append(device)
                    for z in range(0,int(df_winter2_device["Hour/Day"].values[0]-x)):
                        usedpower_forgraph[z]+=usedpower
                        device_dict[z].append(device)
                if Time_Interval+df_winter2_device["Hour/Day"].values[0] < 24:   
                    for x in range(0,int(df_winter2_device["Hour/Day"].values[0])):
                        usedpower_forgraph[int(Time_Interval+x)]+=usedpower 
                        device_dict[int(Time_Interval+x)].append(device)                             
        else:
            print("You have made a mistake with typing.Please try again.")
    else:
        print("You have made a mistake with typing.Please try again.")
    if stop_count>0:
        stop=input("Do you want to stop adding devices?(Y,N)\n")
        if stop=="Y":
            break
        else:
            continue



price=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for x in range(6,18):
    price[x]=(usedpower_forgraph[x]/1000)*2.005109
for x in range (17,23):
    price[x]=(usedpower_forgraph[x]/1000)*3.094456
price[23]=(usedpower_forgraph[23]/1000)*1.133962
for x in range(0,6):
    price[x]=(usedpower_forgraph[x]/1000)*1.133962


print(price)
sumprice=sum(price)
print(f"Daily energy price with/out load shifting in summer is {sumprice}₺")



f, ax = plt.subplots(1)
time = range(0,24)
power = usedpower_forgraph
ax.plot(time,power)
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
ax.set_title("Daily Based/Shifted Loading For Summer")
plt.xlabel('Hours')
plt.ylabel("Power Level(W)")
plt.xticks()
plt.tight_layout()


f, ax = plt.subplots(1)
time2 = range(0,24)
price = price
ax.plot(time,price)
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
ax.set_title("Daily energy prices using triple-time tariff with/out load shifting in summer")
plt.xlabel('Hours')
plt.ylabel("Price(₺)")
plt.xticks()
plt.tight_layout()
plt.show()