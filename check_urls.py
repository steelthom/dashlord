import requests

with open("urls.txt", "r", encoding="utf-8") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    try:
        response = requests.get(url, timeout=20)
    except requests.RequestException as e:
        if "NameResolutionError" in str(e):
            with open("urls.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open("urls.txt", "w", encoding="utf-8") as file:
                for line in lines:
                    if line.strip() != url:
                        file.write(line)
            print(f"Deleted URL: {url}")
        else:
            print(f"Error accessing {url}")
