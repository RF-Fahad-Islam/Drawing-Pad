# Drawing Pad
A python **Tkinter GUI** of the drawing board. You can create art and also save the art on a **.pkl** file to get it later. Work with ```line, rectangle, circle, text, color ```

## Requirements

### Packages or Modules
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyautogui.
```
pip install pyautogui
```
### Imports

**Some Built-in modules used on this program Such as ```tkinter, pickle```**
```
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
from pyautogui import prompt
import pickle
from tkinter.colorchooser import askcolor
```


## Usage

```python
1. Draw your art.
2. with custom colors.
3. Create a rectangle, circle, line, text
4. Save the drawing in a pickle file.
5. Retrieve drawing by opening the pickle file.
```
## How saves the data of art
**It creates a dictionary of drawing information with several objects. such as below (given the structure of the dictionary):**
```
created_element_info_new = {
        "type": shape, #Shape of drawing like line, circle, rectangle
        "color": color, #Color of the shape
        "prev_x": prev_x, #Starting point from the x axis
        "prev_y": prev_y, #Starting point from the y axis
        "x": x, #End point of the x axis
        "y": y #End point of the y axis
    }
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

**For guaranteed pull request:**
```
1 . Describe an issue with the pull request.
2. Adding or suggesting new features
3. Improve the Programme.
4. Fix the Bugs and described
5. Adding functions to do more drawing activities
```
Please make sure to update tests as appropriate.

## Versions 
**Note: This is developed in the:**
```Python 3.9.0``` **environment**

## Contact me

```
Email: rsfahad97@gmail.com
```

## License
**Made by Fahad**


## Thanks for visiting
**Please help me to improve the project further.**
