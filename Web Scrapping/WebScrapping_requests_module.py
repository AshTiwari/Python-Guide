#Downloading from the web with request module.
'''
List of status_code:
404: page not found
200: everything OK.

'''


import requests

downloaded = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(downloaded.status_code)
print(downloaded.text[:500])
print(type(downloaded.text))
print(len(downloaded.text))

#raises error when doenload is failed and ignores if downloaded successfully.
downloaded.raise_for_status()   #gives 404:Not Found Error.


#save the data ina file.
rjFile = open('C://Users//MSI//Desktop//RomeoJuliet.txt','wb')   #wb mode eunsures unicode is preserved.

#saving data in file in chuncks.
for chunk in downloaded.iter_content(50000):
    print(rjFile.write(chunk))

rjFile.close()
    













