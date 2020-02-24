from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys


key = "67e1a195b2b3bdc77f0a64097980d799"
secret = "c063414ed605bfb4"
wait_time = 1

#保存フォルダの指定
animalname = sys.argv[1]
savedir = './' + animalname

flickrapi = FlickrAPI(key, secret, format='parsed-json')
result = flickrapi.photos.search(
	text = animalname,
	par_page = 400,
	media = 'photos',
	sort = 'relevance',
	safe_serch = 1,
	extras = 'url_q, licence'
)

photos = result['photos']
# pprint(photos)

for i, photo in enumerate(photos['photo']):
	url_q = photo['url_q']
	filepath = savedir + '/' + photo['id'] + '.jpg'
	if os.path.exists(filepath): continue
	urlretrieve(url_q,filepath)
	time.sleep(wait_time)