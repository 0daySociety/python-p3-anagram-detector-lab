class Anagram:
    def __init__(self,word):
        self.word =word.lower()

    def match(self,match_list):
        # list comprehnsion 
        # we remove the word from the list of the words 
        match_list=[anagram for anagram in match_list if anagram !=self.word]
            #create an empty list for storing the matched words
        match=[]
        for anagram in match_list:
            # we sort the words to match the word we are looking for 
            if sorted(anagram.lower())==sorted(self.word):
                # we append the word in the match list 
                match.append(anagram)

        return match        

      



myword=Anagram("me")
print(myword.match(["em","em","me","em"]))      