"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    "Finds Words"

    def __init__(self, path):
        '''Opens file'''
        self.path = open(path, 'r')
        '''Reads opened file'''
        content = self.path.read()
        '''Returns content and counts how many break lines there are'''
        self.words = content.split()
        self.words_quantity = len(content.split())
        print(f'Just read {self.words_quantity} words')

    def randomize(self):
        import random
        randomize = random.choice(self.words)
        return randomize

class SpecialWordFinder(WordFinder):
    def __init__(self,path):
        super().__init__(path)
    def remove_special(self, path):
        return [word.strip() for word in path if word.strip() and not word.startwith('#')]
        
        
                    
            
        

        

        
        
        


        


#= '/Users/EnriqueH/Documents/Google_Drive/4_Learning/Developer/Springboard_Bootcamp/UNIT_2/18_Python_Fundamentals/18.4_Python_OO/18.4_exercises/python-oo-practice/words.txt'):


        
    



    
    

        
        
    
    

    


    