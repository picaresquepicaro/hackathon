from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import google.generativeai as genai
import pandas as pd
import numpy as np

df = pd.read_csv("~/Documents/hackathon/website/shelter_occupancy_200000.csv")

bp = Blueprint('shelter', __name__)

def haversine(lat1, lon1, lat2, lon2, R=6371.0):
    dLat = (lat2 - lat1) * np.pi / 180
    dLon = (lon2 - lon1) * np.pi / 180

    lat1 = (lat1) * np.pi / 180
    lat2 = (lat2) * np.pi / 180

    a = np.sin(dLat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dLon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

@bp.route('/shelter', methods=('GET', 'POST'))
def shelter():
    if request.method == 'POST':
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        genai.configure(api_key="")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Where is this latitude {} and longitude {}".format(latitude, longitude))
       
        df['distance'] = haversine(df['latitude'], df['longitude'], float(latitude), float(longitude))

        df_sort = df.sort_values(by='distance', ascending=True)
        
        shelters = []
        for _, row in df_sort.head(3).iterrows():
            shelters.append({ "shelter_name": row['shelter_name'], "occupancy": str(row['occupancy']), "status": row['status'], "distance": str(row['distance'])})

        print(shelters)

        return render_template('shelter.html', response=response, shelters=shelters) 

    return render_template('shelter.html')
