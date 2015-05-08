
import urllib2
import json
from common import decoder, data_import

client_id = "cfcdc7b7c1a1c09c4cd155e85b0c9f80"
track_url = "http://api.soundcloud.com/tracks/%s.json?client_id="+client_id




def track_data(url,track_id):
    try:
        json_data_track = json.load(urllib2.urlopen(url%str(track_id)))
        return (json_data_track["user"]["username"]
                 ,json_data_track["title"])
    except:
        return (None,None)

def main():

    partition = data_import("graph_partition.txt")

    for e in partition.keys():
        with open("group_%s.txt"%str(e),"w") as f:
            for t in partition[e]: # for each track in a partition
                user,track = track_data(track_url,decoder(t))
                if not user: # if track data returns (None,None)
                    continue
                f.write(user.encode('utf-8')+"\t"+track.encode('utf-8')+"\n")


if __name__ == "__main__":
    main()