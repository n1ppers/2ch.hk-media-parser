import urllib.request as lib
import requests
import json
import os

def main():
    board_id = input("Board identifier: ")
    board = board_id.replace("/", "")
    thread_num = input("Thread number: ")
    url = str("https://2ch.hk/" + board + "/res/" + thread_num + ".json")
    s = lib.urlopen(url)
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

if __name__ == "__main__":
    if not os.path.exists("parsed"):
        os.makedirs("parsed")
    
    main()