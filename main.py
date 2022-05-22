with open('file1.txt', encoding='utf-8') as file1:
    file1_read = file1.read()

print(file1_read)
with open('file2.txt', 'w', encoding='utf-8') as file2:
    for file1line in reversed(file1_read):
        file2.write(file1line)
print()
with open('file2.txt', encoding='utf-8') as file2_written:
    print(file2_written.read())
