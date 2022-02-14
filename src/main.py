from bs4 import BeautifulSoup
import requests
import zipfile
import os.path
import pandas as pd

from constants import *
from credentials import *
from helpers import *


def main():
    s = requests.Session()  # create session to store cookie & login credentials
    s.get(HOME_URL)  # get request to home page to generate cookie
    s.get(LOGIN_URL)
    s.post(LOGIN_URL, data=PAYLOAD, headers=HEADERS)  # post request with login credentials
    response = s.get(MEMBER_URL) # get request to member page

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        if "Click Here to Download Today's Leads in a .zip File" in link.text:
            download_link = MEMBER_URL + link.get("href").rstrip("\n")
            print(download_link)

    get_zipfile = s.get(download_link, stream=True, headers=HEADERS)  # download zip file
    file_name = download_link.split("/")[-1].rstrip("\n")
    complete_name = os.path.join(SAVE_PATH, file_name)
    with open(complete_name, 'wb') as f:
        for chunk in get_zipfile.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    with zipfile.ZipFile(complete_name, "r") as zip_ref:  # unzip file and save in data/daily
        daily_filename = zip_ref.namelist()[0]  # get the name of the file inside
        zip_ref.extractall("data/daily")

    weekly_filename = create_weeklyCSVfile()  # create the name for weekly leads csv file

    if not os.path.isfile(weekly_filename):
        # create weekly file and then merge daily with weekly
        df = pd.DataFrame(list())
        weekly_directory = "data/weekly/" + weekly_filename
        df.to_csv(weekly_directory)
    frames = [pd.read_csv(os.path.join('data/daily/', daily_filename)), pd.read_csv(os.path.join('data/weekly/', weekly_filename))]
    result = pd.concat(frames, ignore_index=True)
    result.to_csv(os.path.join('data/weekly/', weekly_filename), index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    main()




