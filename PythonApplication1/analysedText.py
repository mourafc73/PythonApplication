class analysedTextcls(object):
# utility #tool that can perform analysis on a given piece of text. 
# Complete the class 'analysedText' with the following methods -
#Constructor - Takes argument 'text',makes it lower case and removes all punctuation. Assume only the following punctuation is used - period (.), exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
#freqAll - returns a dictionary of all unique words in the text along with the number of their occurences.
#freqOf - returns the frequency of the word passed in argument.

    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','').lower()

        # make text lowercase
        #formattedText = formattedText.lower()
        text = formattedText
        self.fmtText = formattedText
        ##return text

    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')

        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
