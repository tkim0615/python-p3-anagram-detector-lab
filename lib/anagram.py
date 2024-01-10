import ipdb
class Anagram:
    def __init__(self, word):
        self.sorted_letter = sorted([letter for letter in word])
    
    def match(self, words_list):
        match_list = []
        for word in words_list:
            if sorted([letter for letter in word]) == self.sorted_letter:
                match_list.append(word)
        return match_list



    







# Your class, Anagram should take a word on initialization; instances should respond
#  to a match() instance method that takes a list of possible anagrams. It should 
#  return all matches in a list. If no matches exist, it should return an empty list.

# In other words, given: 'listen' and ['enlists', 'google', 'inlets', 'banana'] the program should return ['inlets'].

# listen = Anagram("listen")
# listen.match(['enlists', 'google', 'inlets', 'banana'])
# # => ['inlets']