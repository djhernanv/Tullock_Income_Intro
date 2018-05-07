# Letter Counting Task in oTree
This App allows you to create an Experiment with a Real Effort Task of Counting "a"s in a randomly generated string of characters of increasing length.

### Installation

1. In Terminal or PowerShell go to your oTree folder, for instance ```cd oTree```, and create the folder for the app 
with ```mkdir Tullock_Intro_RET``` .
1. Make sure you have "numpy" installed with ```pip install numpy``` or ```pip3 install numpy``` if you use Python 3.
1. Define the App in settings.py with:
~~~
  SESSION_CONFIGS = [
    {
        'name': 'project_2_cont',
        'display_name': "Letter Counting Task - Control Group",
        'num_demo_participants': 5,
        'app_sequence': ['project_2_cont'],
    },
    # other session configs go here ...
  ]
~~~
4. If you want the letter counting task as part of another game, add it to the sequence of that games app.
1. You'll need to install Django's ```humanize```
1. Change the points name to tokens in settings with ```POINTS_CUSTOM_NAME = 'tokens'```
1. Either download or, ideally, clone this repository and add its contents to the "Tullock_Intro_RET" folder.
1. This app is optimized for Chrome.
1. Ready! :-)
