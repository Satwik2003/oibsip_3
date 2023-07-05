import pandas as pd
from scipy.stats import zscore
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import warnings
import numpy as np


warnings.filterwarnings('ignore')

df = pd.read_csv('CarPrice_Assignment.csv')


# Data Cleaning
#    Drop Nulls, CarName, Car_ID
df = df.drop(['car_ID', 'CarName', 'symboling'], axis=1)

#     Find outliers in price, horsepowers and mileage
df = df[zscore(df.price)<3]
df = df[zscore(df.horsepower)<3]
df = df[zscore(df.citympg)<3]
df = df[zscore(df.highwaympg)<3]


# Data Pre-processing
# Binary dummies for fuel type, aspiration, door number, car body, drive wheel, engine location, engine type, cylinder number, and fuel
# system
fuel_dummies = pd.get_dummies(df.fueltype)
df = df.join(fuel_dummies)
df = df.drop('fueltype', 1)

aspiration_dummies = pd.get_dummies(df.aspiration)
df = df.join(aspiration_dummies)
df = df.drop('aspiration', 1)

door_dummies = pd.get_dummies(df.doornumber)
df = df.join(door_dummies)
df = df.drop('doornumber', 1)

body_dummies = pd.get_dummies(df.carbody)
df = df.join(body_dummies)
df = df.drop('carbody', 1)

wheel_dummies = pd.get_dummies(df.drivewheel)
df = df.join(wheel_dummies)
df = df.drop('drivewheel', 1)

engine_loc_dummies = pd.get_dummies(df.enginelocation)
df = df.join(engine_loc_dummies)
df = df.drop('enginelocation', 1)

engine_type_dummies = pd.get_dummies(df.enginetype)
df = df.join(engine_type_dummies)
df = df.drop('enginetype', 1)

cylinder_dummies = pd.get_dummies(df.cylindernumber, prefix="cyl")
df = df.join(cylinder_dummies)
df = df.drop('cylindernumber', 1)

fuel_system_dummies = pd.get_dummies(df.fuelsystem)
df = df.join(fuel_system_dummies)
df = df.drop('fuelsystem', 1)

#print(df.columns)

columns = []

columns.extend(fuel_dummies) 
columns.extend(aspiration_dummies)
columns.extend(door_dummies)
columns.extend(body_dummies)
columns.extend(wheel_dummies)
columns.extend(engine_loc_dummies)
columns.extend(['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight']) #5
columns.extend(engine_type_dummies)
columns.extend(cylinder_dummies)
columns.append('enginesize') #1
columns.extend(fuel_system_dummies)
columns.extend(['boreratio', 'stroke', 'compressionratio', 'horsepower', 'peakrpm', 'citympg', 'highwaympg', 'price']) #8


df = df.loc[ : , columns]


#Prepare data 
data = df.drop('price', 1)
tget = df['price']

x_train, x_test, y_train, y_test = train_test_split(data, tget, test_size=0.2)

#Fit Model
lr = LinearRegression()

lr.fit(x_train, y_train)



#Predict

inp = []

#fuel type 1
feat = input("Enter Fuel Type:\t")

if feat == 'diesel':
    inp.extend([1,0])

elif feat == 'gas':
    inp.extend([0,1])

#aspiration 2
feat = input("Enter Aspiration:\t")

if feat == 'std':
    inp.extend([1,0])

elif feat == 'turbo':
    inp.extend([0,1])

#doors 3
feat1 = input("Enter Number of Doors:\t")

if feat1 == 'four':
    inp.extend([1,0])

elif feat1 == 'two':
    inp.extend([0,1])

#body 4
feat = input("Enter Type of Car:\t")

if feat == 'convertible':
    inp.extend([1, 0, 0, 0, 0])

elif feat == 'hardtop':
    inp.extend([0, 1, 0, 0, 0])

elif feat == 'hatchback':
    inp.extend([0, 0, 1, 0, 0])

elif feat == 'sedan':
    inp.extend([0, 0, 0, 1, 0])

elif feat == 'wagon':
    inp.extend([0, 0, 0, 0, 1])

#wheel 5
feat = input("Enter Drive Wheel:\t")

if feat == '4wd':
    inp.extend([1, 0, 0])

elif feat == 'fwd':
    inp.extend([0, 1, 0])

elif feat == 'rwd':
    inp.extend([0, 0, 1])

#engineloc 6
feat = input("Enter Engine Location:\t")

if feat == 'front':
    inp.extend([1, 0])

elif feat == 'rear':
    inp.extend([0, 1])

#wheelbase 7
feat = float(input('Enter Wheel Base:\t'))
inp.append(feat)

#car length 8
feat = float(input('Enter Car Length:\t'))
inp.append(feat)

#car width 9
feat = float(input('Enter Car Width:\t'))
inp.append(feat)

#car height 10
feat = float(input('Enter Car Height:\t'))
inp.append(feat)

#curb weight 11
feat = int(input('Enter Curb Weight:\t'))
inp.append(feat)

#engine type 12
feat = input("Enter Engine Type:\t")

if feat == 'dohc':
    inp.extend([1, 0, 0, 0, 0, 0])

elif feat == 'l':
    inp.extend([0, 1, 0, 0, 0, 0])

elif feat == 'ohc':
    inp.extend([0, 0, 1, 0, 0, 0])

elif feat == 'ohcf':
    inp.extend([0, 0, 0, 1, 0, 0])

elif feat == 'ohcv':
    inp.extend([0, 0, 0, 0, 1, 0])

elif feat == 'rotor':
    inp.extend([0, 0, 0, 0, 0, 1])


#cylinders 13
feat = input("Enter Number of Cylinders:\t")

if feat == 'eight':
    inp.extend([1, 0, 0, 0, 0])

elif feat == 'five':
    inp.extend([0, 1, 0, 0, 0])

elif feat == 'four':
    inp.extend([0, 0, 1, 0, 0])

elif feat == 'six':
    inp.extend([0, 0, 0, 1, 0])

elif feat == 'two':
    inp.extend([0, 0, 0, 0, 1])


#engine size 14
feat = int(input('Enter Engine Size:\t'))
inp.append(feat)

#fuel system 15
feat = input("Enter Fuel System:\t")

if feat == '1bbl':
    inp.extend([1, 0, 0, 0, 0, 0, 0, 0])

elif feat == '2bbl':
    inp.extend([0, 1, 0, 0, 0, 0, 0, 0])

elif feat == '4bbl':
    inp.extend([0, 0, 1, 0, 0, 0, 0, 0])

elif feat == 'idi':
    inp.extend([0, 0, 0, 1, 0, 0, 0, 0])

elif feat == 'mfi':
    inp.extend([0, 0, 0, 0, 1, 0, 0, 0])

elif feat == 'mpfi':
    inp.extend([0, 0, 0, 0, 0, 1, 0, 0])

elif feat == 'spdi':
    inp.extend([0, 0, 0, 0, 0, 0, 1, 0])

elif feat == 'spfi':
    inp.extend([0, 0, 0, 0, 0, 0, 0, 1])

#bore ratio 16
feat = float(input('Enter Bore Ratio:\t'))
inp.append(feat)

#stroke 17
feat = float(input('Enter Stroke:\t'))
inp.append(feat)

#cr 18
feat = float(input('Enter Compression Ratio:\t'))
inp.append(feat)

#hp 19
feat = int(input('Enter Horse Power:\t'))
inp.append(feat)

#rpm 20
feat = int(input('Enter Peak RPM:\t'))
inp.append(feat)

#citympg 21
feat = int(input('Enter City Mileage:\t'))
inp.append(feat)

#highwaympg 22
feat = int(input('Enter Highway Mileage:\t'))
inp.append(feat)

#print(inp)

inp = np.array(inp).reshape([1, 48])
inp = pd.DataFrame(inp, columns=columns[:-1])

pred = lr.predict(inp)

print("\n\n\nThe Price is {}\n\n\n".format(int(pred[0])))