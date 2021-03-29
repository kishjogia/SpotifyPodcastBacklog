# Spotify Podcast Backlog

This will add episodes of a podcast to a playlist

## Pre-requristie: 
1. A json file called secret.json in the below format
```json
{
    "client_id":  "123",
    "client_secret": "456",
    "username": "uname"
}
```
Spotipy docs
https://spotipy.readthedocs.io/en/2.17.1/

Spotify scopes
https://developer.spotify.com/documentation/general/guides/scopes/

## ToDo
1. [ ] The order of episodes appears to be random, some are old to new others new to old
so need a consistent method
2. [ ] Be able to more than 50 episodes
