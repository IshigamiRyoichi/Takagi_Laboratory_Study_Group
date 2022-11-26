from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import io

def table_to_df(url):
    res_race = requests.get(url)
    res_race.raise_for_status()
    soup_horse = BeautifulSoup(res_race.content, 'lxml')
    table_horse = soup_horse.select('[class="db_h_race_results nk_tb_common"]')
    with io.StringIO(str(table_horse)) as f:
        # print(f)
        df = pd.read_html(f)[0]
    return df

def save_df_as_csv(df,csv_file):
    df.to_csv(csv_file)

if __name__=='__main__':
    os.makedirs("./assets/csv/", exist_ok=True)
    df= table_to_df("https://db.netkeiba.com/horse/2017100720")
    save_df_as_csv(df, "./assets/csv/tabel.csv")