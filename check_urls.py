import requests

with open("urls.txt", encoding="utf-8") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    try:
        response = requests.get(url, timeout=15)
    except requests.RequestException as e:
        if "NameResolutionError" in str(e):
            print(f"Delete URL: {url}")
            try:
                response = requests.get(url.replace("://", "://www."), timeout=15)
                with open("urls.txt", encoding="utf-8") as file:
                    lines = file.readlines()
                with open("urls.txt", "w", encoding="utf-8") as file:
                    for line in lines:
                        if line.strip() == url:
                            line = line.replace(url, url.replace("://", "://www."))
                        file.write(line)
            except requests.RequestException:
                print(f"Also failed with www: {url}")
                with open("urls.txt", encoding="utf-8") as file:
                    lines = file.readlines()
                with open("urls.txt", "w", encoding="utf-8") as file:
                    for line in lines:
                        if line.strip() != url:
                            file.write(line)
        else:
            print(f"Error accessing {url}")
            print(e, "\n")
