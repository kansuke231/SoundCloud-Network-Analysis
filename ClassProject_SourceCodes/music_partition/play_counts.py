
import urllib2
import json

client_id = "cfcdc7b7c1a1c09c4cd155e85b0c9f80"
track_url = "http://api.soundcloud.com/tracks/%s.json?client_id="+client_id


def decoder(string):

    result = 0
    digit_decoder = lambda x: ord(x)-ord("A")

    for i,e in enumerate(reversed(string)):
        result+=digit_decoder(e)*26**i

    return result


def count(track_id,which_count="playback_count"):
    # which_count -> either "playback_count" or "favoritings_count"

    track_id = str(track_id) # just in case
    try:
        track = urllib2.urlopen(track_url%track_id)
        json_data = json.load(track)
        print(json_data["title"])
        return json_data[which_count]
    except:
        return 0



def data_import(filename):

    result = []

    with open(filename,"r") as f:
        for i,e in enumerate(f.readlines()):
            e = e.replace(" ",",").replace("\n","")
            e = [(i,track,count(decoder(track)),count(decoder(track),"favoritings_count"))
                 for track in e.split(",")]
            result += e

    return result

def output(array):
    with open("count.txt","w") as f:
        for g,t_ID,play,like in array:
            f.write(str(g)+" "+str(t_ID)+" "+str(play)+" "+str(like)+"\n")

output(data_import("graph_partition.txt"))