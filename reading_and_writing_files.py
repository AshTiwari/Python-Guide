#reading and writing files.

#python by-defaut open a file in READ MODE.
print('Open file in READ MODE.')
file = open('C:\\Users\\MSI\\Desktop\\text.txt')        #returns a file object.
file_content = file.read()          #returns a string containing content of file.
print('----File start:----')
print(content)
print('----File End.----')
file.close()

#open can be accessed only one time. For 2nd time, open it again.
print('\nReading each line.')
file = open('C:\\Users\\MSI\\Desktop\\text.txt')    
lines = file.readlines()
print(lines)    
file.close()


#write mode will overwrite an existing file and start from blank.
#if file dosen't already exist, python will create a new file.
print('\nOpen file in WRITE MODE.')
file = open('C:\\Users\\MSI\\Desktop\\CreateNewFile.txt','w')

noOfChar = file.write('Creating or opening new file.') #returns a int i.e no. of characters written.
print('No of characters written is: '+ str(noOfChar))

file.write('Creating or opening new file.') #the message isn't added in new line.
file.write('Creating or opening new file.') #it just add the message in previous line withoout
file.write('Creating or opening new file.') #space or any sepration.
file.write('Creating or opening new file.\n') #to add to new line use \n.

file = open('C:\\Users\\MSI\\Desktop\\CreateNewFile.txt')
content = file.read()
print('----File start:----')
print(content)
print('----File End.----')

file.close()    




#append mode will add new text from bottom of previous text.
#if file dosen't already exist, python will create a new file.
print('\nOpen file in APPEND MODE.')
file = open('C:\\Users\\MSI\\Desktop\\CreateNewFile.txt','a')
file.write('\n\n\nFile wont be overwritten but appended.')

file = open('C:\\Users\\MSI\\Desktop\\CreateNewFile.txt')
content = file.read()
print('----File start:----')
print(content)
print('----File End.----')
file.close()




