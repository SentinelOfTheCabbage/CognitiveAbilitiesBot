from random import randrange, shuffle
with open('words_base.txt', 'r', encoding='utf-8') as source:
    words = source.readlines()

words = [line.split() for line in words]


def create_quest(*args):
    i = randrange(len(words))
    ans = words[i][1:3]
    q = words[i][1:]
    shuffle(q)
    return (words[i][0], [q.index(word) for word in ans], q)

if __name__ == '__main__':
    print(create_quest())
