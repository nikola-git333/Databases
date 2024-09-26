import pymongo

client = pymongo.MongoClient("localhost", 27017)

mydb = client["MoviesDatabase"]
mycol = mydb["Movies"]

movie_list = [
    {"title" : "Shawshank Redemption", "genre" : "Drama", "release_year" : "1994"},
    {"title" : "The Dark Knight", "genre" : "Action/Crime/Drama", "release_year" : "2008"},
    {"title" : "Pulp Fiction", "genre" : "Crime/Drama", "release_year" : "1994"},
    {"title" : "Forrest Gump", "genre" : "Drama/Romance", "release_year" : "1994"},
    {"title" : "Interstellar", "genre" : "Adventure/Drama/Sci-Fi", "release_year" : "2014"}
]

mycol.insert_many(movie_list)

for row in mycol.find():
    print(row)