#scrapes transcripts.foreverdreaming.org for the script of each episode of Jojo
import requests
from bs4 import BeautifulSoup
# choose webpage
url = "https://transcripts.foreverdreaming.org/viewforum.php?f=1721"
response = requests.get(url)
# choose season
season = "05"

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a")

    with open("data.txt", "a", encoding="utf-8") as f:
        # Iterate through each episode
        for episode in range(3, 39):
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
                        f.write(episode_transcript + '\n')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
