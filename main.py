with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    
words = file_contents.split()
    

num_of_chars = {}
for char in file_contents.lower():
    if char in num_of_chars:
        num_of_chars[char] += 1
    else:
        num_of_chars[char] = 1

# print(f"Number of each character: {num_of_chars}")
char_list = []
for key in num_of_chars:
    if key.isalpha():
        char_list.append(key)
    else:
        pass
char_list.sort()

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} found in the document.")

for char in char_list:
    print(f"The '{char}' character was found {num_of_chars[char]} times.")

print("--- End of Report ---")