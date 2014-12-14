import urllib2
import json
from common import decoder,data_count_import

url = "http://api.soundcloud.com/tracks/%s.json?client_id=cfcdc7b7c1a1c09c4cd155e85b0c9f80"

def get_info(name):
    name = str(decoder(name))
    json_data = json.load(urllib2.urlopen(url%name))
    return json_data["user"]["username"],json_data["title"]


def main():
    data = data_count_import("group1_in_top30_like.txt")
    for g,t_ID,play,like in data:
        print(get_info(t_ID),like)


if __name__ == '__main__':
    main()