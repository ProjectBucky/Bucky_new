import urllib
import requests
from bs4 import BeautifulSoup
import vlc
Instance = vlc.Instance()
player = Instance.media_player_new()

def search_yt(track):
    global player
    try:
        query = urllib.parse.quote_plus(track)
    except:
        query = urllib.quote_plus(track)
    url = "https://www.youtube.com/results?search_query=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urlobj = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    link = 'https://www.youtube.com' + urlobj[0]['href']
    Media = Instance.media_new(link)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    #Add Stop code
