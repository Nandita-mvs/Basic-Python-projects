from urllib.request import urlopen

page=urlopen("https://www.udemy.com/course/build-8-mini-projects-in-python-from-scratch/learn/lecture/22124780#content")
print(page.headers)


