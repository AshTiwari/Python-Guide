#making your own character classes.
import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing,8 maids a milking,7 swans a swimming,6 geese a laying,5 gold rings, badam-pam-pam,4 calling birds,3 French hens,2 turtle dovesAnd ,1 partridge in a pear tree.'

# syntax: r'[]'

vowelRegex = re.compile(r'[aeiouAEIOU]')    #equivalent to (r'a|e|i|o|u')
notvowelRegex = re.compile(r'[^aeiouAEIOU]')    #^ means negative character class.
alphabetRegex = re.compile(r'[a-zA-Z]')         #a-z means all character between a and z.

consonantRegex = re.compile(r'[(a-zA-Z)^(aeiouAEIOU)]')   #creates error.
                                                #can we compile (something) minus (something.) 

print('Printing vowelRegex.')
print(vowelRegex.findall(lyrics))
print('Printing notvowelRegex.')
print(notvowelRegex.findall(lyrics))
print('Printing alphabetRegex.')
print(alphabetRegex.findall(lyrics))
print('Printing consonantRegex.')
#print(consonantRegex.findall(lyrics))


######################
''' TRY TO FIND A WAY TO FIND CONSONANT USING ^.'''
#####################
