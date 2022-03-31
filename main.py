import os

import bs4
import requests

url = "https://www.countryflags.com/"

# .div>class="thumb">img>src
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text, "html.parser")

# Get image links
img_tags = soup.select(".thumb img")
image_urls = [img["src"] for img in img_tags]


# Create Flags folder if not exists

os.makedirs("Flags", exist_ok=True)


# https://cdn.countryflags.com/thumbs/vatican-city/flag-square-250.png
# Save images to Flags folder
for i, url in enumerate(image_urls):
    country_name = str(url).split("/")[-2]
    print(f"Downloading {country_name}--{i+1}/{len(image_urls)}")
    res = requests.get(str(url))
    with open(f"Flags/{country_name}.png", "wb") as f:
        f.write(res.content)
