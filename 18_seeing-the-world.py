destinations = ["norway", "colorado", "maldives", "italy", "brazil"]
print(destinations)
print("Sorted: ", sorted(destinations))
print("Unsorted: ", destinations)
print("Reverse sorted: ", sorted(destinations, reverse=True))
print("Here's the list again in it's original order:\n", destinations)

destinations.reverse()
print("\nList order has been reversed:\n", destinations)

destinations.reverse()
print("\nList has been reversed back to its original order:\n", destinations)

destinations.sort()
print("\nList has been changed so that it's now stored in alphabetical order:\n", destinations)

destinations.sort(reverse=True)
print("\nList has been changed so that it's now stored in reverse alphabetical order:\n", destinations)