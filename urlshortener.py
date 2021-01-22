import pyshorteners
url=input("Enter URL:")
shortener=pyshorteners.Shortener()
a=shortener.tinyurl.short(url)
print(a)