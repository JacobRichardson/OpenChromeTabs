# This program uses the pyautogui library to open bunch of websites in different tabs in google chrome.

import pyautogui                                                        # Import pyautogui.

pyautogui.pause = 0.5                                                   # Set pause to 0.5.

websites = [                                                            # List of websites to open.
    'https://www.google.com',
    'https://www.youtube.com',
    'https://www.trello.com',
    'https://www.reddit.com/',
    'https://outlook.office.com',
    'https://mail.google.com',
    'https://www.github.com/JacobRichardson',
]

def main():                                                             # Main function.
    openChomre()                                                        # Call openChrome.
    openWebsites(websites)                                              # Call open websites with the websites.


def openChomre():                                                       # Function to open chrome.
    pyautogui.typewrite(['win'])                                        # Press the windows key.
    pyautogui.typewrite('Google Chrome')                                # Type google chrome.
    pyautogui.typewrite(['enter'])                                      # Press the enter key.
    pyautogui.hotkey('alt', 'space', 'x')                               # Press alt+space+x to maximize chrome.


def openWebsites(list):                                                 # Function that creates a new tab for each website.
    for website in list:                                                # For every website in the list.
        pyautogui.typewrite(website, interval=0.001)                    # Write the website with a 0.001 delay.
        pyautogui.typewrite(['enter'])                                  # Press enter.
        if website != list[-1]:                                         # If we are not at the last element in the list.
            pyautogui.hotkey('ctrl', 't')                               # Open a new tab.

main()                                                                  # Call main.