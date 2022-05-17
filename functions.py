import requests

def get_user_info(user):
    url = requests.get(f"https://api.scratch.mit.edu/users/{user}/")
    text = url.json()
    user_wiwo = text['status'] # Assigned but never used (upcoming features)
    user_bio = text['bio'] # Assigned but never used (upcoming features)
    user_id = text['id']
    # reference link:
  #https://uploads.scratch.mit.edu/get_image/user/58524660_90x90.png?v=
  # using the base URL, and putting the user ID in it returns a 404, meaning that the base URL is incorrect
    pfp_link = (f'https://uploads.scratch.mit.edu/get_image/user/{user_id}_90x90')
  # ^ had trouble with this exact URL in MyScratchPage
  # it never ended up working with that URL
  # not sure how 'f' works
  #text['profile']['images']['60x60']
    #I'm going to go right now but I allow you to continue working on this - ScratchTheCoder12345 signing off put the links in readme.md pls thxs bye!
  
    return pfp_link



def user_found(user):
    r = requests.head(f"https://api.scratch.mit.edu/users/{user}/")
    if r.status_code == 404:
        user_found = False
    else:
        user_found = True
    return user_found
  
# https://my-ocular.jeffalo.net/api/user/user/picture is an easy URL to get the user pfp
  # source: https://github.com/JaydenDev/MyScratchPage/blob/master/global.js#L79
  
def scratcher(user):
    url = requests.get(f"https://scratchdb.lefty.one/v3/user/info/{user}")
    text = url.json()
    scratcher = text["status"] 
    return scratcher
# The profile pic is not working...