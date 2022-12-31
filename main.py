import pyautogui
# filters all open windows
def filter_title(window):
    # filters windows for "Discord"
    if  window.title.split()[(len(window.title.split()) - 1)] == 'Discord':
        return window
# gets all open windows
for window in pyautogui.getAllWindows():
    # skips when there's an empty title or filter
    if window.title == '' or not filter_title(window):
        continue
    # if window is minimized it will maximize it
    window.maximize()
    # brings window to the foreground
    window.activate()
    # determines the x postistion for the leave call button
    x = window.left + 290
    # determines the y postistion for the leave call button
    if window.top > 0: 
        y = (window.height + window.top) - 130
    else:
        y = window.height - 130
    # clicks on the leave call button
    pyautogui.click(x, y)