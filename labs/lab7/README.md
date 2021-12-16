# 📜 Lab 7

*December 8, 2021*

---

### Unique Words

Write a Python program `unique_words.py` that reads in `US_Constitution.txt` and displays all the unique words found in the file, i.e. it displays every word in the file *once*. If there is a duplicate of the same word, the duplicate cannot be displayed.

Strip all the words of commas, newlines, semicolons, etc. and convert all words into lower case. Hint: you can use `strip()` multiple times e.g. `astring.strip(<something>).strip(<something>)` etc.

Print each unique word out on a newline (with no duplicates, obviously). The words do not need to be ordered.

For this lab, you can only use **1 list** (to work with the file) **and 1 set**. Any extra lists or sets will be marked down.

I encourage you to review the three different Python built-in methods of reading in from a file and pick the best one.

Hint: Think about *one of the properties of sets* that makes them so suitable for this question.

```python
constitution_file = open('US_Constitution.txt', 'r')
constitution_lines = constitution_file.readlines()
constitution_file.close()

unique_words = set()

index = 0
while index < len(constitution_lines):
    constitution_lines[index] = constitution_lines[index]\
        .replace('.', '')\
        .replace(',', '')\
        .replace(';', '')\
        .replace('(', '')\
        .replace(')', '')\
        .replace('-', '')\
        .rstrip('\n')\
        .lower()
    index += 1

for line in constitution_lines:
    words = line.split()
    for word in words:
        unique_words.add(word)

for word in unique_words:
    print(word)
```