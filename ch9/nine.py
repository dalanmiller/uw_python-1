import urllib

'''
webStringy = urllib.urlopen('http://scintillus.com')
'''
#-------------------------------------------------------------
#ex. 9.1
#only print a word if it has more than 20 characters
def print_longWords(file):
    fin = open(file)
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print word

#print_longWords('words.txt')

#-------------------------------------------------------------
#ex. 9.2
#only print words with no 'e':

def has_no_e(file):
  fin = open(file)
  for line in fin:
    word = line.strip()
    if 'e' not in word:
      print word
      
#has_no_e('words.txt')      

#-------------------------------------------------------------
#ex. 9.2.2
#modify 9.2 to also compute percentage of words in list that have no 'e'

def has_no_ePercentage(file):
  counter_total = 0.0
  counter_no_e = 0.0
  fin = open(file)
  for line in fin:
    counter_total = counter_total + 1
    word = line.strip()
    if 'e' not in word:
      counter_no_e = counter_no_e + 1
  print (counter_no_e/counter_total) * 100, 'percent'

# has_no_ePercentage('words.txt')

#-------------------------------------------------------------
#ex. 9.3
# takes str + forbidden letters, returns True if letters aren't there

def avoids(word, str):
  checker_var = True 
  for char in str:
    if char in word:
      #print char
      checker_var = False
  return checker_var
    
#print avoids('i am flhying on a cloud of baro', 'llllltti')

#-------------------------------------------------------------
#ex. 9.3.2
# user inputs forbidden str, checks agains words.txt. prints ## of words that don't contain the forbidden str

def avoids_list():
  counter = 0
  counter_total = 0
  fin = open('words2.txt')

  #str is the builtin str() function that will attempt to change the input 
  #into a string! You should probably name your variable something else ;)
 
  #str = raw_input('enter the forbidden letters:\n> ') 
  forbiddens = raw_input('enter the forbidden letters:\n> ')
  
  for line in fin:

    #counter_total = counter_total + 1
    #You can increment your integers like this

    counter_total += 1    
  
    word = line.strip()
    for char in str:
      if char in word:
        print char
        print word
        #counter = counter + 1    
        counter += 1

#*********************************************************************
#once counter increments, move on to the next word. HOW TO DO!!!

#I think what you are looking for is the continue keyword, it will stop at that point in the loop and start the
# next iteration. Check out the example in this link. 
#http://docs.python.org/2/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops

#**********************

        print counter
  return counter_total - counter 
  
#print avoids_list()

#-------------------------------------------------------------
#ex. 9.4

#Also shouldn't use str here! 

# get word, str. return True if word uses only letters in allowed_letters
def uses_only(word, allowed_letters):

  #Go through each letter in the word
  for char in word:

    #Check if the letter exists in the allowed_letters string
    if char not in allowed_letters:

      #If letter doesn't exist in the allowed, return False 
      return False

  #Else, eventually after going through all the letters return True 
  return True

#**********************************************************************    
#print uses_only('a barb', 'bar'), 'uses-only'

#-------------------------------------------------------------
#ex. 9.5
# word, str. build string using all letters in str at least once
def uses_all(word, str):
  for char in str:
    if char not in word:
      return False
  return True
  
#print uses_all('abucklp', 'abcp'), 'uses-all'

#-------------------------------------------------------------
#ex. 9.6
# 


#-------------------------------------------------------------
#ex. 9.7
# find a word that has 3 consequtive doubble letters

#Let me know if I can help you with this one! -Daniel 

def threeDoubles(file):
  fin = open(file)
  for line in fin:
    word = line.strip()
    if len(word)> 7:
      i = 0
      while i < len(word):
        counter = 0
        letter1 = word[i]
        #i = i+ 1
        i += 1
        letter2 = word[i]
        if letter1 == letter2:
          #counter = counter + 1
          counter += 1
          if counter == 3:
            print word
        
        
threeDoubles('words.txt')          
