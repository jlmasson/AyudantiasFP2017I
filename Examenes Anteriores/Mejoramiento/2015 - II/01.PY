def crearDiccionario():
    d = {}
    d["@usuario1"] = ["contenido tuit1 #hashtag1", "contenido #hashtag2 tuit2"]
    d["@usuario2"] = ["#hashtag2 contenido tuitn #hashtagn"]
    return d

def trendTopics(diccionario):
    hashtags = {}
    for tweets in diccionario.values():
        for tweet in tweets:
            partes = tweet.strip().split()
            for elem in partes:
                elem = elem.strip()
                if elem.startswith("#"):
                    if elem in hashtags:
                        hashtags[elem] += 1
                    else:
                        hashtags[elem] = 1
    tendencias = topHashtags(hashtags)
    return tendencias
    
def topHashtags(hashtags):
    items = list(hashtags.items())
    items.sort(key=lambda x : x[1], reverse=True)
    return items

def mostrarPantalla(tendencias):
    for hashtag, veces in tendencias:
        print("{} {:d}".format(hashtag, veces))

diccionario = crearDiccionario()
tendencias = trendTopics(diccionario)
mostrarPantalla(tendencias)