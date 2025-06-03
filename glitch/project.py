import os
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from config import directories
# from webdriver_manager.firefox import GeckoDriverManager

# Load URLs from file
with open("glitch_links.txt", "r") as f:
    urls = [line.strip() for line in f if line.strip()]

# Set up headless Firefox
options = Options()
options.headless = True
service = Service('../drivers/geckodriver')
driver = webdriver.Firefox(service=service, options=options)

def sanitize_folder_name(url):
    parsed = urlparse(url)
    return parsed.netloc.replace(".", "_")

def download_resource(resource_url, folder, base_url):
    try:
        full_url = urljoin(base_url, resource_url)
        r = requests.get(full_url, timeout=10)
        if r.status_code == 200:
            path_parts = resource_url.split("?")[0].split("/")
            local_path = os.path.join(folder, *path_parts)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            with open(local_path, "wb") as f:
                f.write(r.content)
    except Exception as e:
        print(f"[!] Failed to download {resource_url}: {e}")



for key in directories.keys():
    # folder_name = f'./{key}' 
    parent_folder = f'./{key}'
    # print(folder_name)
    # for url in urls:
    #     print(f"📥 Downloading: {url}")
    #     driver.get(url)
    #     time.sleep(3)  # Allow time for dynamic content to load

    #     folder_name = sanitize_folder_name(url)
    #     folder_name = f'{parent_folder}/students/{folder_name}'
    #     os.makedirs(folder_name, exist_ok=True)

    #     # Save page HTML
    #     html = driver.page_source
    #     with open(os.path.join(folder_name, "index.html"), "w", encoding="utf-8") as f:
    #         f.write(html)

    #     # Parse HTML to find static assets
    #     soup = BeautifulSoup(html, "html.parser")
    #     tags = soup.find_all(["img", "link", "script"])

    #     for tag in tags:
    #         src = tag.get("src") or tag.get("href")
    #         if src and not src.startswith("data:"):
    #             download_resource(src, folder_name, url)

driver.quit()
print("✅ All downloads complete.")
