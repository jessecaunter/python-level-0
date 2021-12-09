books = [
    "Behind the Mask",
    "The Last Lecture",
    "The Creakers",
    "Tomorrow, When the War Began",
    "The Dead of the Night",
    "The Third Day, the Frost",
    "Darkness, Be My Friend",
    "Burning for Revenge",
    "The Night is for Hunting",
    "The Other Side of Dawn",
    ]

print("\nFirst book I read in 2021: " + books[0])
print("Most recent book I've read: " + books[-1])

books.append("1984")
books[-1] = "Nineteen Eighty-Four"
books.append("The Lost Fairy Tales")

print("Currently reading: " + books[-2])
print("Currently reading to my daughter: " + books[-1])

books.insert(0, "Cat's Cradle")
print("\nActually, I just remembered...\nThe first book I read in 2021 was: " + books[0])

del books[-1]
popped = books.pop()
print("\nRemoving " + popped + " from the list as I haven't finished it yet.")
childrens = "The Creakers"
books.remove(childrens)
print("Removing " + childrens + " from the list as it's a childrens book.")

books.reverse()
print("\nHere's a list of the books I've read in 2021, starting with the most recent:\n", books)
books.reverse()

print("\nHere's a list of the books I've read in 2021, sorted in reverse alphabetical order:\n", sorted(books, reverse=True))

books.sort()
print("\nAt the end of the year, I will change the list order to be alphabetical, like so:\n", books)

print("\nAs of today, I have read " + str(len(books)) + " adult books this year.")