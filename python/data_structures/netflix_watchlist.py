watchlist = ["Jaws", "Alien", "Up"]

prior = input("Enter highest priority movie: ").strip().title()
remove = input("Enter any movie you already watched: ").strip().title()

watchlist.insert(0, prior)
watchlist.remove(remove)

weekend = [input("Enter any movie you want to watch on weekend: ").strip().title()]
watchlist.extend(weekend)

print(f"All movies: {watchlist}")
