import requests
from bs4 import BeautifulSoup
import re

# Choose webpage
url = "https://en.wikiquote.org/wiki/JoJo%27s_Bizarre_Adventure"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    lines = soup.find_all(["dd", "hr"])
    with open("quotes.txt", "a", encoding="utf-8") as f:
        for line in lines:
            if line.name == "dd":
                result = re.sub(r"\[[0-9]+\]", "", line.text.strip())
                f.write(result + "\n")
            else:
                f.write("\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
