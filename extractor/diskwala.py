import requests

def extract_diskwala(link):
    try:
        file_id = link.split("/")[-1]
        api = "https://www.diskwala.com/api/file/details"

        r = requests.post(api, json={"id": file_id}, timeout=5)
        return r.json().get("file", {}).get("url")
    except:
        return None
