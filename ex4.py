
# compresses a string like this:
# aaaanbbbbbd -> a4n1b5d1
def compress(word):
    count = 0
    res = word[0]
    for i in range(1, len(word)):
        count += 1
        if word[i] != word[i-1]:
            res += str(count) + word[i]
            count = 0
    res += str(count+1)
    return res

def main():
    print(compress("aaaabbbbbdsss"))

main()