from common import decoder,data_import
import urllib2
import json

client_id = "cfcdc7b7c1a1c09c4cd155e85b0c9f80"
track_url = "http://api.soundcloud.com/tracks/%s.json?client_id="+client_id


def track_tag(url,track_id):
    try:
        json_data_track = json.load(urllib2.urlopen(url%str(track_id)))
        print(json_data_track["tag_list"])
        print(json_data_track["genre"])
        return json_data_track["tag_list"],\
               json_data_track["genre"]
    except:
        return (None,None)


def main():

    partition = data_import("graph_partition.txt")

    for e in partition.keys():
        with open("group_%s_tag.txt"%str(e),"w") as f:
            for t in partition[e]: # for each track in a partition
                tags,genre = track_tag(track_url,decoder(t))
                if not tags: # if track data returns (None,None)
                    continue
                f.write(genre.encode('utf-8')+" "+tags.encode('utf-8')+"\n")

if __name__ == "__main__":
    main()