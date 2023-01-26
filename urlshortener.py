import pyshorteners

url = input("Enter URL :\n")

print("URL after Shrtening :- ", pyshorteners.Shortener().tinyurl(url))