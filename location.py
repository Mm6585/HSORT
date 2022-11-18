import json
import pandas as pd

with open("location.json", "r") as sample_json:
    sample = json.load(sample_json)
df = pd.DataFrame(sample)

def num_seats():
    return len(df)

class Location:
    room_image = "" # room image path

    def __init__(self, center_x, center_y):
        self.cx = center_x
        self.cy = center_y
        self.location = 0

    def get_location(self):
        for x in range(len(df)):
            if df.loc[x]['start_location_y'] < self.cy < df.loc[x]['end_location_y']: 
                if df.loc[x]['start_location_x'] < self.cx < df.loc[x]['end_location_y']:   
                    self.location = x + 1       
        return self.location