import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from sagemaker.nyc_taxi_utils import preprocess

# df = pd.read_csv('NYC_taxi.csv', parse_dates=['pickup_datetime'], nrows=500000)

# print(df.head())
path = '/Users/yuleinku/Desktop/project/modeling-project/figures'
## Visualizing Geolocation Data #############################################
def clean(df):
    # range of longitude for NYC
    nyc_min_longitude = -74.05
    nyc_max_longitude = -73.75

    # range of latitude for NYC
    nyc_min_latitude = 40.63
    nyc_max_latitude = 40.85

    df2 = df.copy(deep=True)
    for long in ['pickup_longitude', 'dropoff_longitude']:
        df2 = df2[(df2[long] > nyc_min_longitude) & (df2[long] < nyc_max_longitude)]

    for lat in ['pickup_latitude', 'dropoff_latitude']:
        df2 = df2[(df2[lat] > nyc_min_latitude) & (df2[lat] < nyc_max_latitude)]
    return df2

def plot_lat_long(df, landmarks, points='pickup'):
    plt.figure(figsize = (12,12)) # set figure size
    if points == 'pickup':
        plt.plot(list(df.pickup_longitude), list(df.pickup_latitude), '.', markersize=1)
    else:
        plt.plot(list(df.dropoff_longitude), list(df.dropoff_latitude), '.', markersize=1)

    for landmark in landmarks:
        plt.plot(landmarks[landmark][0], landmarks[landmark][1], '*', markersize=15, alpha=1, color='r') # plot landmark location on map
        plt.annotate(landmark, (landmarks[landmark][0]+0.005, landmarks[landmark][1]+0.005), color='r', backgroundcolor='w') # add 0.005 offset on landmark name for aesthetics purposes
  
    plt.title("{} Locations in NYC Illustrated".format(points))
    plt.grid(None)
    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    file_name = os.path.join(path, points+'_loc_nyc.png')
    plt.savefig(file_name)
    plt.show()
    


# plot_lat_long(df2, landmarks, points='Pickup')

# plot_lat_long(df2, landmarks, points='Drop Off')



## Ridership by Day and Hour #############################################
def plot_ridership(df):
#     df['year'] = df['pickup_datetime'].dt.year
#     df['month'] = df['pickup_datetime'].dt.month
#     df['day'] = df['pickup_datetime'].dt.day
#     df['day_of_week'] = df['pickup_datetime'].dt.dayofweek
#     df['hour'] = df['pickup_datetime'].dt.hour

    df['day_of_week'].plot.hist(bins=np.arange(8)-0.5, ec='black', ylim=(60000,75000))
    plt.xlabel('Day of Week (0=Monday, 6=Sunday)')
    plt.title('Day of Week Histogram')
    file_name = os.path.join(path, 'pickup_weekday.png')
    plt.savefig(file_name)
    plt.show()

    df['hour'].plot.hist(bins=24, ec='black')
    plt.title('Pickup Hour Histogram')
    plt.xlabel('Hour')
    file_name = os.path.join(path, 'pickup_hour.png')
    plt.savefig(file_name)
    plt.show()



## Handling Missing Values and Data Anomalies #############################################
def data_anomaly(df):
    print(df.isnull().sum())
    print('')

    df = df.dropna()

    print(df.describe())

    df['fare_amount'].hist(bins=500)
    plt.xlabel("Fare")
    plt.title("Histogram of Fares")
    plt.show()

    df = df[(df['fare_amount'] >=0) & (df['fare_amount'] <= 100)]

    df['passenger_count'].hist(bins=6, ec='black')
    plt.xlabel("Passenger Count")
    plt.title("Histogram of Passenger Count")
    plt.show()

    df.plot.scatter('pickup_longitude', 'pickup_latitude')
    file_name = os.path.join(path, 'anomaly.png')
    plt.savefig(file_name)
    plt.show()



## Geolocation Features #############################################
def geo_feat(df):
    df = preprocess(df)

    def euc_distance(lat1, long1, lat2, long2):
        return(((lat1-lat2)**2 + (long1-long2)**2)**0.5)

    df['distance'] = euc_distance(df['pickup_latitude'], df['pickup_longitude'], df['dropoff_latitude'], df['dropoff_longitude'])

    df.plot.scatter('fare_amount', 'distance')
    plt.show()


