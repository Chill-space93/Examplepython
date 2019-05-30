def signature(s):

    t = list(s)
    t.sort()
    t = "".join(t)
    return t


def all_anagrams(testanagram):

    d = {}
    for line in open("English.txt"):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):

    for v in d.values():
        if len(v) > 1:
            print (len(v), v)


def print_anagram_sets_in_order(d):


    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))
    t.sort()
    for x in t:
        print (x)



if __name__ == "__main__":
    d = all_anagrams("words.txt")
    print_anagram_sets_in_order(d)
