#Web Scrapping.

'''
Automating google map search.
-Copy address
-launch python program
-It will automatically open google maps and paste the address in search bar.
-Click search button.

Copy : Chhatrapati Shivaji Maharaj Terminus
'''
import webbrowser , pyperclip

address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)
