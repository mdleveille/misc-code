import time
import webbrowser

x = 0
while x <= 2:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=2EHXH0hYkuU")
    x += 1
    print('Take a break!')
