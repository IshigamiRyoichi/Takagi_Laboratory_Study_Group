from bs4 import BeautifulSoup
import requests
import os

def get_image(url):
    res_race = requests.get(url)
    res_race.raise_for_status()
    soup = BeautifulSoup(res_race.content, 'lxml')
    img_tags = soup.select('img')
    # print(img_tags)
    for i, img_tag in enumerate(img_tags):
        if 'https:' in img_tag.get('src'): 
            img_url = img_tag.get('src')
        else:
            # img_url = "https:/" + img_tag.get('src')
            img_url = "https://www.pokemon.co.jp" + img_tag.get('src')
        img_res = requests.get(img_url)
        img_data =img_res.content
        if img_res.status_code == 200:
            file_name = "./assets/moodel/img_" + str(i) + ".jpg"
            with open(file_name, 'wb') as f:
                f.write(img_data)


if __name__=='__main__':
    os.makedirs("./assets/moodel/", exist_ok=True)
    get_image("https://www.pokemon.co.jp/")