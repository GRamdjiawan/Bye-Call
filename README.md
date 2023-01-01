# Bye-Call
Have you ever turned off your pc whilst in a Discord call and forgot to leave?
Don't worry I have you covered.
With this file you can leave with only the press of a button.
(This works great with AutoHotKeys.)


## Installation
* If you dont have [Python](https://www.python.org/downloads/release/python-3108/#:~:text=Full%20Changelog-,Files,-Version) install it first.
* After the installation download and extract the zip file at the top or press [this link](https://github.com/GRamdjiawan/Bye-Call/archive/refs/heads/main.zip).
* Then run this command in the cmd to install pyautogui.

```bash
pip install pyautogui
```

## Usage

### AutoHotKeys
* After the installation copy the path to the main.py file 
* Set your code up to look like this

```autohotkey
your_combination::
    ;Leaves the call
    Run, "path_to_file"
    ;Delays shutdown for 1 second
    Sleep, 1000
    ;Turns the pc off
    Shutdown, 1
Return
```

### Otherwise
Just double click the main.py file

