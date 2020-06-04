user = "Saul Vega"

playlist = {
    "Title": "Daily Mix",
    "user": user,
    "songs": [
        {"title": "song1", 'artist': ["blue"], "duration": 1.7},
        {"title": "song2", 'artist': ["dawg"], "duration": 1.2},
        {"title": "song3", 'artist': ["dj doo"], "duration": 1.5}
    ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)
