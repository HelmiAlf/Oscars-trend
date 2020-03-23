import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen


def get_HTML(url):
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, 'html.parser')
	# html = soup.prettify('utf-8')
	return soup


def main():
	# wiki_page = get_HTML("https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture")
	# movies = ""
	# wiki_links = ""
	# for table in wiki_page.findAll('table', attrs={'class':'wikitable'}):
	# 	for tr in table.find("tbody").find_all("tr"):
	# 		if(len(tr.find_all("td")) < 2):
	# 			continue
	# 		else:
	# 			movie_name = tr.find_all("td")[0].text.strip()
	# 			if(movie_name=="20th Century Studios"):
	# 				break
	# 			link = tr.find_all("td")[0].find("a")['href']
	# 			wiki_links += link + " \n"
	# 			movies += movie_name+ " \n"

	# textfile = open('moviess.txt', 'w',  encoding='utf-8')
	# textfile.write(movies)
	# textfile.close()
	# another_textfile = open('wiki.txt', 'w',  encoding='utf-8')
	# another_textfile.write(wiki_links)
	# another_textfile.close()
	
	# wiki_links = open('wiki.txt', 'w',  encoding='utf-8')
	# getGenre()

	# checkDescs()
	 # getGenre1()
	# checkDescs1()
	clustered_decades = clusterDecades()
	clustered_genres = clusterGenres(clustered_decades)
	# f = open('clustered_genres.txt', 'w')
	# json.dump(clustered_genres,f)
	text = ""
	for decade in clustered_genres.keys():
		text += decade + "\n "
		for genre in clustered_genres[decade].keys():
			text += "    "+  genre +" : "+ str(clustered_genres[decade][genre]) +"\n"

	f = open('cleadasdasdn.txt','w')
	f.write(text)
	f.close()

def clusterGenres(decades_dict):
	genres_count = {
	
	}

	for decade in decades_dict.keys():
		genre_dict = {}
		string = decades_dict[decade]
		splitted_genre =string.split(" ")
		for genre in splitted_genre:
			if genre not in genre_dict.keys():
				genre_dict[genre] = 1
			else:
				genre_dict[genre] += 1

		genres_count[decade] = genre_dict
		print(genre_dict)

	return genres_count



def checkDescs1():
	filee = open("clean_genres.txt", encoding='utf-8')
	text = filee.readlines()
	filee.close()
	lst = []
	counter = 0
	for movie_genre in text:
		counter += 1
		
		if len(movie_genre) < 12:
			lst += [counter]

	print(lst)

def getGenre1():
	filee = open('movie_desc.txt', encoding='utf-8')
	text = filee.readlines()
	filee.close()

	clean_genres = ""
	for movie_desc in text:
		if ("is a " in movie_desc):
			string = movie_desc.split("is a")[1].strip()
			clean_genres += string.lower() +"\n"
		elif ("is an " in movie_desc):
			string = movie_desc.split("is an")[1].strip()
			clean_genres += string.lower() +"\n"
		else:
			clean_genres += "\n"

	clean_genres_file = open("clean_genres.txt","w", encoding='utf-8')
	clean_genres_file.write(clean_genres)
	clean_genres_file.close()

def checkDescs():
	filee = open('movie_desc.txt', encoding='utf-8')
	text = filee.readlines();
	filee.close()
	counter = 0
	lst = []

	for movie_desc in text:
		counter+=1
		if( " is a " not in movie_desc):
			lst += [counter]
	print(lst)

def getGenre():
	wiki_links_file = open('wiki.txt',encoding='utf-8')
	movie_names_file = open('moviess.txt',encoding='utf-8')

	movie_descs = ""

	wiki_links = wiki_links_file.readlines()
	movie_names = movie_names_file.readlines()

	for i in range(0, len(wiki_links)):
		link = wiki_links[i]
		movie_name = movie_names[i].split(" ")[0]
		print("Get desc of "+movie_names[i])
		wiki_page = get_HTML("https://en.wikipedia.org/"+link)
		tag_p = wiki_page.find_all("p")
	
		for p in tag_p:
			if(p.text.strip().split(" ")[0] == movie_name):
				movie_descs += p.text.strip().split("film")[0]+" film" + "\n"
				break

	movie_descs_file = open('movie_desc.txt', 'w', encoding='utf-8')
	movie_descs_file.write(movie_descs)

	wiki_links_file.close()
	movie_names_file.close()
	movie_descs_file.close()

def clusterDecades():
	filee = open('clean_genres.txt', encoding='utf-8')
	text = filee.readlines()
	filee.close()
	decades_dict = {
	'192':"",
	'193':"",
	'194':"",
	'195':"",
	'196':"",
	'197':"",
	'198':"",
	'199':"",
	'200':"",
	'201':""
	}

	for movie_desc in text:
		# print(movie_desc)
		decade = movie_desc[0:3]
		desc = movie_desc.strip()[5:]+" "
		decades_dict[decade] += desc

	# print(decades_dict['201'])
	return decades_dict
		# movie_desc = movie_desc.split(" ")
		# decade = int(movie_desc[0]) // 10



if __name__ == '__main__':
	main()
