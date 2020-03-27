
#problem
# given a list of strings, group the anagrams together
#lst = ["cat", "dog", "tac", "god", "good", "wow", "act"]
"""
Output:
["good"]
["wow"]
["dog", "god"]
["cat", "tac", "act"]
"""

#def find_ana(lst):

lst1 = ["cat", "dog", "tac", "god", "good", "wow", "act"]
word = "cat"

def ana(lst,selected_word):
    """
    -lst parameter takes a list you want to search
    -selected_word parameter takes word you want to search for
    """

    #variables
    result = []
    better_result = []
    expselected_word = list(selected_word)

    #propagate 1st list with len match
    for item in lst:
        if len(item) == len(selected_word):
            result.append(item)

    #propagate 2nd list with char match
    counter = 0
    for item in result:
       if expselected_word[counter] in item:
                better_result.append(item)
                counter += 1

    return(better_result)

#loop for all words
for i in lst1:
    print(ana(lst1,i))



