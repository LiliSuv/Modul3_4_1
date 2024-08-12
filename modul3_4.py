root_word='оКруг'
other_words='окраина','труд','весна', 'КРуг','окрошка','субокруг', 'листва', 'округлость'

def single_root_words(root_word,*other_words):
    c=[]
    for i in range(len(other_words)):
        b=str(other_words[i]).upper()
        c.append(b)
    other_words=c
    same_words=[]
    for k in range (len(other_words)):
        y=other_words[k]
        if any (i in other_words[k] for i in  [root_word])  > 0:
            same_words.append(other_words[k])
        elif any (i in root_word for i in [ other_words[k]])>0:
            same_words.append (other_words[k])
    print( same_words)
single_root_words(root_word.upper(),*other_words)