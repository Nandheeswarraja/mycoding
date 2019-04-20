FileName = ("Path\para.txt")
with open(FileName, 'r') as file:
    lines_in_file = file.read()
    print lines_in_file 
import nltk
FileName = ("Path\para.txt")
with open(FileName, 'r') as file:
    lines_in_file = file.read()   
    nltk_tokens = nltk.word_tokenize(lines_in_file)
    print nltk_tokens
    print "\n"
    print "Number of Words: " , len(nltk_tokens)
