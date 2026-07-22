import pickle

data = {"name": "rasika raja",
        "course": "python",
        "company":"live wire"
        }

with open("data", "wb") as file:
   pickle.dump(data, file)
