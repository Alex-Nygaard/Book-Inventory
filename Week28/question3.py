words = input("Please enter comma-separated words: ")

splitWords = words.split(",")
sortedWords = sorted(splitWords)
joinedWords = ",".join(sortedWords)

print(joinedWords)
