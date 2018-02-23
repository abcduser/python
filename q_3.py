u_words = []
not_unique = []
file = open('text.txt', 'r')
words = file.read().split(' ')
file.close()

for word in words:

    if word not in u_words:
        u_words.append(word)
    else:
        not_unique.append(word)

for word in not_unique:
    u_words.pop(u_words.index(word))
u_words.sort()

for word in u_words:
    print(word)
