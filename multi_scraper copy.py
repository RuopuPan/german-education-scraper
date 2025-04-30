import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_bmbf_news():
    url = "https://www.bmbf.de/bmbf/shareddocs/kurzmeldungen/en/kurzmeldungen_en.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("li", class_="teaser__item")
    data = []

    for item in items:
        link_tag = item.find("a")
        if link_tag:
            title = link_tag.get_text(strip=True)
            relative_link = link_tag.get("href")
            full_link = "https://www.bmbf.de" + relative_link
            data.append({"Title": title, "Link": full_link})

    df = pd.DataFrame(data)
    df.to_csv("sample.csv", index=False, encoding="utf-8-sig")
    print("✅ Scraped data saved to sample.csv")

if __name__ == "__main__":
    scrape_bmbf_news()
