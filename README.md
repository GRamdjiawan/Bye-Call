# Bye-Call
Have you ever turned off your pc whilst in a Discord call and forgot to leave?
Don't worry I have you covered.
This works great with AutoHotKeys


## Installation

Use the package manager [pip](https://pyautogui.readthedocs.io/en/latest/install.html#) to install pyautogui.

```bash
pip install pyautogui
```

## Usage

```autohotkey
your_combination::
    ;Leaves the call
    Run, "path_to_file"
    ;Turns the pc off
    Shutdown, 1
Return
```