import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"amapiano"}

headers = {
	"X-RapidAPI-Key": "83e85eeea3mshca1d7b11b203688p1c9b97jsn905a0f2a1078",
	"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())