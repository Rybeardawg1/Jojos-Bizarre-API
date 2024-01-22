import requests
from bs4 import BeautifulSoup

url = "https://transcripts.foreverdreaming.org/viewforum.php?f=1721&start=78"
response = requests.get(url)

season = "03"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")

    with open("data.txt", "a", encoding="utf-8") as f:
        for episode in range(35, 40):
            for link in links:
                if link.text.strip().find(season + "x" + str(episode).zfill(2)) != -1:
                    episode_url = "https://transcripts.foreverdreaming.org" + link.get("href")[1:]
                    print(episode_url)
                    print(link.text.strip())
                    episode_response = requests.get(episode_url)
                    if episode_response.status_code == 200:
                        episode_soup = BeautifulSoup(episode_response.text, "html.parser")
                        episode_transcript = episode_soup.find("div", {"class": "content"}).text.strip()
                        # Write each episode's transcript to the file
                        for i in range(1, 4):
                            f.write(episode_transcript + '\n')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
