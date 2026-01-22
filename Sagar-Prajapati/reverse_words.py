def rev_words(s):
    sentence_list= s.split(' ')
    list_words = []
    while(len(sentence_list)>0):
        word = sentence_list.pop()
        list_words.append(word)

    return ' '.join(list_words)

print(rev_words("This is GeekCoders"))