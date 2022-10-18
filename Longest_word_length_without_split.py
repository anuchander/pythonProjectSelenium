
def findLongestWordLength(str):
    current_word = ""
    longest_word=""
    for a in str:
        if a==" ":
            if len(current_word)> len(longest_word):
                longest_word=current_word
                current_word=""
                #print(longest_word)
            else:
                current_word=""
        else:
            current_word=current_word+a

    return longest_word




result = findLongestWordLength("The quick brown fox jumped over the lazy dog")
print(result)

