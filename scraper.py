from bs4 import BeautifulSoup
import requests
import json

with open("champions.json", "r") as f:
    champions = json.load(f)

def main():

    url = "https://wiki.leagueoflegends.com/en-us/List_of_champions"

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    all_champions = soup.find('table', class_="article-table").find_all('tr')

    for champion in all_champions:
        name_info = champion.find('a')
        description_info = champion.find('span', class_="inline-image").find('a')
        class_info = champion.find('span', class_="glossary")
        price_info = champion.find_all('td')
        
        description = ""
        class_type = ""
        be = ""
        rp = ""

        for i in description_info:
            parts = list(i.stripped_strings)   

        if len(parts) > 0:
            description = parts[0]
        
        if class_info:
            class_type = class_info["data-tip"]

        if len(price_info) > 0:
            be = price_info[4].string
            rp = price_info[5].string
 
        name = name_info['title']
        image = "https://wiki.leagueoflegends.com/" + name_info.find('img')['src']

        champ = {
            "name": name,
            "description": description,
            "image": image,
            "class": class_type,
            "be": be.strip(),
            "rp": rp.strip(),
        }

        champions.append(champ)

    with open("champions.json", "w") as f:
        json.dump(champions, f, indent=4)
        

if __name__ == "__main__":
    main()