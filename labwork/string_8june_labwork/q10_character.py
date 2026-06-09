'''A compressed message is given:
AAABBBCCCDDDAAA
Tasks
1. Count occurrences of each character.
2. Create a dictionary of character frequencies.
3. Display unique characters.
4. Find the most frequent character.
5. Create a compressed output:
   A3B3C3D3A3
6. Calculate compression ratio.
'''
# to ask user to enter text
text = input("Enter Text: ").strip().upper()
# validating text
if text == "":
    exit("Text cannot be empty.")

print("-----------------------------------------")
# 1 & 2. Count occurrences and create frequency dictionary
frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character Frequencies:")

for ch in frequency:
    print(ch, "->", frequency[ch])

# 3. Display unique characters
unique_characters = list(frequency.keys())

print("Unique Characters:", unique_characters)

# 4. Find the most frequent character
most_frequent = ""
highest_count = 0

for ch in frequency:
    if frequency[ch] > highest_count:
        highest_count = frequency[ch]
        most_frequent = ch

print("Most Frequent Character:", most_frequent)
# 5. Create compressed output
compressed = ""
count = 1

for i in range(1, len(text)):

    if text[i] == text[i - 1]:
        count += 1

    else:
        compressed += text[i - 1] + str(count)
        count = 1

compressed += text[-1] + str(count)

print("Compressed Output:", compressed)

# 6. Calculate compression ratio
original_length = len(text)
compressed_length = len(compressed)

compression_ratio = (compressed_length / original_length) * 100

print("Original Length:", original_length)
print("Compressed Length:", compressed_length)
print("Compression Ratio:", round(compression_ratio, 2), "%")
#output will be
'''Enter Text: AAABBBCCCDDDAAA
-----------------------------------------
Character Frequencies:
A -> 6
B -> 3
C -> 3
D -> 3
Unique Characters: ['A', 'B', 'C', 'D']
Most Frequent Character: A
Compressed Output: A3B3C3D3A3
Original Length: 15
Compressed Length: 10
Compression Ratio: 66.67 %'''

