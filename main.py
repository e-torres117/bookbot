with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    count = len(words)


char_dic = {}
for char in file_contents:
    if char.isalpha():
        char = char.lower()
        if char in char_dic:
            char_dic[char] += 1
        else:
            char_dic[char] = 1

char_list = list(char_dic.items())

char_list.sort(key = lambda x: x[1],reverse = True)

#print statment
print("---begin report of books/frankenstein.txt---")
print (f"{count} words found in the document\n")

for k,v in char_list:
    print(f"the {k} character was found {v} times")

print("--- End report ---")