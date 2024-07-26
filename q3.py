import json

nasa_data = '''{
    "copyright":"Roberto Marinoni",
    "date":"2024-07-26",
    "explanation":"From our vantage point in the Milky Way Galaxy, we see NGC 6946 face-on. The big, beautiful spiral galaxy is located just 20 million light-years away, behind a veil of foreground dust and stars in the high and far-off constellation Cepheus. In this sharp telescopic portrait, from the core outward the galaxy's colors change from the yellowish light of old stars in the center to young blue star clusters and reddish star forming regions along the loose, fragmented spiral arms. NGC 6946 is also bright in infrared light and rich in gas and dust, exhibiting a high star birth and death rate. In fact, since the early 20th century ten confirmed supernovae, the death explosions of massive stars, were discovered in NGC 6946. Nearly 40,000 light-years across, NGC 6946 is also known as the Fireworks Galaxy.",
    "hdurl":"https://apod.nasa.gov/apod/image/2407/NGC6946_verB.jpg",
    "media_type":"image",
    "service_version":"v1",
    "title":"Facing NGC 6946",
    "url":"https://apod.nasa.gov/apod/image/2407/NGC6946_verB1024c.jpg"
}
'''
data = json.loads(nasa_data)
print("Explanation:", data.get("explanation"))
print("Title:", data.get("title"))