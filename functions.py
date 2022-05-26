import requests
import os
import httpx
import json

from scratchclient import ScratchSession


def get_user_info(user):
    url = requests.get(f"https://api.scratch.mit.edu/users/{user}/")
    text = url.json()
    user_wiwo = text['profile']['status']
    user_bio = text['profile']['bio']
    user_id = text['id']
    location = text['profile']['country']
    userJoined = text['history']['joined'].split('T')[0]
    scratchteam = text['scratchteam']
    response = httpx.get(f"https://scratchdb.lefty.one/v3/user/info/{ user }")
    
    userData = json.loads(response.text)

    followers = userData["statistics"]["followers"]
    pfp_link = (
        f'https://uploads.scratch.mit.edu/get_image/user/{user_id}_60x60.png')

    return {
        'pfpLink': pfp_link,
        'userId': user_id,
        'userBio': user_bio,
        'userWiwo': user_wiwo,
        'userLocation': location,
        'userJoined': userJoined,
        'userScratchTeam': scratchteam,
        'userFollowersDB': followers
    }


def user_found(user):
    r = requests.head(f"https://api.scratch.mit.edu/users/{user}/")
    if r.status_code == 404:
        user_found = False
    else:
        user_found = True
    return user_found


def scratcher(user):
    url = requests.get(f"https://scratchdb.lefty.one/v3/user/info/{user}")
    text = url.json()
    scratcher = text["status"]
    return scratcher


def featured_project_info(user):
    url = requests.get(f"https://scratch.mit.edu/site-api/users/all/{user}/")
    text = url.json()
    FeaturedThumbnailURL = text["thumbnail_url"]
    FeaturedLabel = text["featured_project_label_name"]
    FeaturedTitle = text["featured_project_data"]["title"]
    FeaturedPID = text['featured_project']
    FeaturedCreator = text["featured_project_data"]["creator"]
    return {
      'featuredThumbnailURL': FeaturedThumbnailURL,
      'featuredLabel': FeaturedLabel,
      'featuredTitle': FeaturedTitle,
      'featuredPID':  FeaturedPID,
      'featuredCreator': FeaturedCreator
    }



def user_followers_list_username(user):
    url = requests.get(f"https://api.scratch.mit.edu/users/jvn11/followers/")
    text = url.json()
    followers = []
  
    for i in (range(0, len(text))):
      followers.append(text[i]['username'])




def login(username,password):
  session = ScratchSession(username, password)