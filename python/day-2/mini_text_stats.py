sentence = input("Enter a sentence: ").strip()

print(f"Number of characters: {len(sentence)}")
print(f"Without spaces: {len(sentence) - sentence.count(" ")}")
print(f"Number of spaces: {sentence.count(" ")}")
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")
print(f"Title: {sentence.title()}")