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
