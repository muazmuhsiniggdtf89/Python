# function to check whether
# first and last character of words match
def match_words (words):
    count = 0
    lst = []
    for word in words:
        if len(word) > 1 and word [0] == word[-1]:
            count += 1
            lst.append(word)

    print("List of words with first and last character same\n" , lst)
    return count 

count = match_words(['1231' , 'rececar' , 'fdf' , '2342'])
print("Number of words having first and last character same :" , count)
