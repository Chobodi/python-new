# Read the file and extract words
import os
print("Current working directory:", os.getcwd())
# 1. Open the file
with open("c:\\Users\\chobodi\\Desktop\\Staff Research\\VCS Research\\Test Project\\data.txt", 'r') as file:
    content = file.read()

# 2. Extract words
import re
words = re.findall(r'\b\w+\b', content)
# 3. Sort the words
words_sorted = sorted(words, key=str.lower)
# 4. Print the sorted words
print("Extracted words:")
for word in words_sorted:
    print(word)

doc = Document()
doc.add_heading('Sorted Words from File', level=1)
for word in words_sorted:
    doc.add_paragraph(word)

# 6. Save the document
doc.save("c:\\Users\\chobodi\\Desktop\\sorted_words.docx")