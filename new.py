# Read the file and extract words
import os
print("Current working directory:", os.getcwd())
# 1. Open the file
with open("c:\\Users\\chobodi\\Desktop\\Staff Research\\VCS Research\\Test Project\\data.txt", 'r') as file:
    content = file.read()

# 2. Extract words
import re
words = re.findall(r'\b\w+\b', content)

# 3. Print the words
print("Extracted words:")
for word in words:
    print(word)
