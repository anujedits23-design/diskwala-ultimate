import requests

def get_video_info(url):
    info = {
        "title": url.split("/")[-1][:40],
        "size": "Unknown",
        "quality": "HD"
    }

    try:
        r = requests.head(url, allow_redirects=True)
        size = int(r.headers.get("content-length", 0)) / (1024*1024)
        if size:
            info["size"] = f"{size:.2f} MB"
    except:
        pass

    return info
