import urllib.request as lib
import requests
import json
import os

def main():
    thread_url = input("Thread link: ")
    s = lib.urlopen(GetThreadJson(thread_url))
    with s:
        data = json.loads(s.read().decode())
        threads_array = data['threads']
        for posts_array in threads_array:
            posts = posts_array['posts']
            for files_array in posts:
                files = files_array['files']
                for file_obj in files:
                    path = file_obj['path']
                    name = file_obj['name']
                    download("http://2ch.hk" + path, name)
                    print(path)

    print("卐 success 卍")
        
def download(url, output_name):
    content = requests.get(url).content
    f = open("parsed/" + str(output_name), "wb")
    f.write(content)
    f.close()

def GetThreadJson(url):
    convertedUrl = ""
    if not url.startswith("https://"):
        if url.startswith("http://"):
            convertedUrl = url.replace("http://", "https://")
        else:
            convertedUrl = url.replace("2ch.hk/", "https://2ch.hk/")
    else:
        convertedUrl = url

    if not url.endswith(".html"):
        if url.endswith(".json"):
            return convertedUrl
        else:
            return str(convertedUrl + ".json")
    else:
        return convertedUrl.replace(".html", ".json")


if __name__ == "__main__":
    if not os.path.exists("parsed"):
        os.makedirs("parsed")
    
    main()