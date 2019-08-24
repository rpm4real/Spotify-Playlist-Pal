import requests

'''
curl -X "GET" "https://api.spotify.com/v1/users/wizzler/playlists" -H "Accept: application/json" -H "Content-Type: application/json" -H "Authorization: Bearer BQC_7N1T6m6VmOGKbJTqAZO35mmwnLsQPvLLzVHHmvZqPWa6feAb72RD-Qy_IzUNjaBIY_Nr_PW7E8ZeetQBixAzMrfwY7PffWcDyRu_TWa3JatlUgrkbsOZiDnFtAy12fkCjlDReNDQVF2SRaI_4Q1NTrTzHnowuyl5l3bBRlt7XiPk8g0oHXCOyV6PcAJ-D3fKPSkrnik"
'''

api_url = "https://api.spotify.com/v1/{0}"
token = 'BQC_7N1T6m6VmOGKbJTqAZO35mmwnLsQPvLLzVHHmvZqPWa6feAb72RD-Qy_IzUNjaBIY_Nr_PW7E8ZeetQBixAzMrfwY7PffWcDyRu_TWa3JatlUgrkbsOZiDnFtAy12fkCjlDReNDQVF2SRaI_4Q1NTrTzHnowuyl5l3bBRlt7XiPk8g0oHXCOyV6PcAJ-D3fKPSkrnik'
headers = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Authorization': 'Bearer {0}'.format(token)
}

def get_user_playlists(user_id):
	endpoint = 'users/{0}/playlists'.format(user_id)
	response = requests.get(api_url.format(endpoint),headers=headers)
	return response.json()

res = get_user_playlists('spotify')

# once relevant playlist is found, get the tracks href 
tracks_href = res['items'][0]['tracks']['href']
playlist_name = res['items'][0]['name']

track_data = requests.get(tracks_href,headers=headers).json()

print('Playlist: {0}'.format(playlist_name))
for track in track_data['items']:
	meta = track['track']
	print(meta['name'])
	for entry in meta['artists']:
		print(entry['name'])
	print('\n')