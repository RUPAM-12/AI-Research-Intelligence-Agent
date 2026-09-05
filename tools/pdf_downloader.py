import requests
import os

def download_pdfs(results, folder):

    os.makedirs(folder, exist_ok=True)

    downloaded = []

    for r in results:

        url = r["url"]

        if ".pdf" in url.lower():

            filename = os.path.join(folder, url.split("/")[-1])

            try:
                response = requests.get(url, timeout=20)

                with open(filename, "wb") as f:
                    f.write(response.content)

                downloaded.append(filename)

            except:
                pass

    return downloaded
