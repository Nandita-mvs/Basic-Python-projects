import wikipedia
search=input("What do you want to search ?")
query=wikipedia.page(search)
print(query.summary)