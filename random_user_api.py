import os

import pandas as pd

import requests


def results_df():

    url = 'https://randomuser.me/api/?results=10'
    response = requests.get(url)

    if response.status_code == 200:
        response_url = response.json()
        results = response_url["results"]
        
    else:
        print("Error: Unable to fetch data from the API")


    #print(results)


    results_df = pd.DataFrame(results)

    return results_df


