#character classes
import re

print('Shorthand charcter class \t Represents.')
print('\\d \t \t \t any numeric digit from 0-9')
print('\\D \t \t \t any char not from 0-9')
print('\\w \t \t \t any letter,digit,undercore.')
print('\\W \t \t \t any char not in \w like spaces and other char.')
print('\\s \t \t \t space,tab, new line.')
print('\\S \t \t \t any char not a space, tab or new line.')

print('e.g. 12 days of christmas.')
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing,8 maids a milking,7 swans a swimming,6 geese a laying,5 gold rings, badam-pam-pam,4 calling birds,3 French hens,2 turtle dovesAnd ,1 partridge in a pear tree.'

xmasRegex =re.compile(r'\d{1,2} \w+')

print(xmasRegex.findall(lyrics))





