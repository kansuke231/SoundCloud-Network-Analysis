__author__ = 'ikeharakansuke'


import urllib2
import json
import random

client_id = "cfcdc7b7c1a1c09c4cd155e85b0c9f80"
user__favorite_url = "http://api.soundcloud.com/users/%s/" \
                     "favorites.json?client_id="+client_id+"&limit=200&offset=0"
user_url = user__favorite_url.replace("/favorites","")

track_favoriter_url = "http://api.soundcloud.com/tracks/%s/" \
                      "favoriters.json?client_id="+client_id+"&limit=200&offset=0"


me = "27069234"

#########################################################################
# function base26 is inspired by the code
# found at:
# http://stackoverflow.com/questions/2063425/
# python-elegant-inverse-function-of-intstring-base
#########################################################################

def base26(number):

    digit_converter = lambda x: chr(ord("A")+x)

    if number < 0:
        return "-" + base26(-number)
    (d,m) = divmod(number,26)
    if d > 0:
        return base26(d) + digit_converter(m)
    return  digit_converter(m)



def user_to_tracks(url):

    f_favorites = urllib2.urlopen(url) # favorites
    json_data_f = json.load(f_favorites)
    offset = 0
    result = json_data_f

    #if (len(json_data_f) < 1):
    if (len(json_data_f) < 20): #or (len(json_data_f) > 190):
        raise

    while (len(json_data_f) == 200): # for a user who likes over 200 songs
        offset+=200
        f_favorites = urllib2.urlopen(url.replace("offset=0","offset=%s")%str(offset))
        json_data_f = json.load(f_favorites)
        result += json_data_f


    f_user = urllib2.urlopen(url.replace("/favorites",""))
    json_data_u = json.load(f_user)


    edges = []

    print("user: "+json_data_u["username"])
    print("user id:",json_data_u["id"])
    print(len(result))
    print("-------------------------------")

    for j in result:
        #print("title:",j["title"])
        #print("id:",j["id"],base26(j["id"]))
        #print("genre:",j["genre"])
        edges.append((json_data_u["id"],base26(j["id"])))

    return edges



def track_to_users(url):

    json_data_users = json.load(urllib2.urlopen(url))
    json_data_track = json.load(urllib2.urlopen(url.replace("/favoriters","")))


    print("title:",json_data_track["title"])
    print(len(json_data_users))
    for j in json_data_users:
        print("id:",j["id"])
        print("username:",j["username"])



def main():

    count = 0
    result = []

    while count < 500 :
        rand = str(random.randrange(50000000))
        try:
            result+=user_to_tracks(user__favorite_url%rand)
            print("rand: "+rand)
            print("count:",count)
            count+=1
        except:
            continue

    with open("user_to_tracks.txt","w") as f:
        for e in result:
            f.write(str(e[0])+" "+str(e[1])+"\n")

if __name__ == "__main__":
    main()