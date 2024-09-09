#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:35:02 2024

@author: bytechef
"""

import time
import subprocess
from tqdm import tqdm
import os

DARKCYAN = '\033[36m'
BLUE = "\033[94m"
RESET = "\033[0m"
RED = '\033[91m'

def text():
    txt = f"""{DARKCYAN}\
     Being a hacker means not accepting the world 
     as it is, but working to improve it. 
     
     Bytechef
     {RESET}"""
    print(txt)

def art():
    art_art = f"""{RED}\
                                                   
  %#%#%@@*%@==%%%=%%%%#%+#.*#-%=@@%%%%%%%@%*%%  
  @#@#@#%=##+-#%#+**#=+#:+:++-#-#%#@*%##%@#+@%  
  @#%#%#%-##=.#%#-+=-.##.#.=+-=-#*##+#*#@@#+##  
  %@%##**-##=.*%+...#**#=#**...-=+#*-#*#%##+**  
  %@**#*#+*%=.-#...#**##=***#...-+++=#+##**.**  
  %#=**+***%:..+..+##########%....-=-**##***#*  
  %%=#*#+**+=.....#@###%%#*#*%.....--+-+#**+##  
  %#+#**#.*=.....%#@@@@@@@@@@%#........+***+#*  
  %*+***+.:-....-@@@@@@@@@@@@@@+.......-+*##**  
  %:++*-**-=.....#%@@@@@@@@@@@#........:=**#*+  
  %:+=*.=*=...+***%%%@@@@@@@#@#****....++**#**  
  +*+++=...*#.##*#*%@@#@@@@@@@###*#*##..==*+*#  
  *.......%%#.@+%###@@#@@@@#@#%#*%#%##....-*=+  
  *++*=...@#@.@%#%@%%@#@@@@#@%@##@#@@#.:...++*  
  -..+...#%%@.@%@@@@@@%@@@@#@@@@@@@@@@:%...=++  
  +.....#@@@*.*********************#@#%##.....  
  +....#%+%@@*#*****#**#***********@@@@%:..-+*  
  -...=#%@%@@+****#********#**#****@@@#%%#.:++  
  +=..#%###%%#**#****************#*@@#%#%@.=++  
  ++++@#%####%**#****###*#*#*#****###@#%@%**+*  
  +++*#@@@@@@@*****#########*****##@@@@@@@*#++  
  =.==+**#%@@=*#*%@@@@@@@@@@@@%*##+#@@%##**+-+  
  .-*++##**##@@@%%@@@@@@@@@@@@@@@@%#**#+###+=-  
  {RESET}"""
    print(art_art)
    text()
# List of timetable activities
schedule = [
    {"time": 6 * 60, "activity": "Wake Up", "note": "Morning routine (stretching, meditation)"},
    {"time": 6 * 60 + 30, "activity": "Exercise", "note": "30 minutes of physical activity"},
    {"time": 7 * 60, "activity": "Breakfast", "note": "Healthy meal to fuel the day"},
    {"time": 7 * 60 + 30, "activity": "Power of three", "note": "Set priorities and tasks"},
    {"time": 8 * 60, "activity": "Coding Session 1", "note": "Focus on high-priority tasks"},
    {"time": 10 * 60, "activity": "Break && Lunch", "note": "30-minute break to refresh"},
    {"time": 10 * 60 + 30, "activity": "Coding Session 2", "note": "Continue working on projects"},
    {"time": 12 * 60, "activity": "Learning Session", "note": "Online courses, tutorials, or reading"},
    {"time": 13 * 60, "activity": "Coding Session 3", "note": "Work on coding tasks or collaboration"},
    {"time": 16 * 60, "activity": "Break && Meal", "note": "Short break to stretch and refresh"},
    {"time": 16 * 60 + 30, "activity": "Coding Session 4", "note": "Final push on tasks for the day"},
    {"time": 18 * 60, "activity": "Wrap Up Work", "note": "Review accomplishments, plan for tomorrow"},
    {"time": 19 * 60, "activity": "Personal Projects / Hobbies", "note": "Work on side projects or personal interests"},
    {"time": 21 * 60, "activity": "Wind Down", "note": "Relax with a book, movie, or game"},
    {"time": 22 * 60, "activity": "Prepare for Bed", "note": "Night routine (limit screen time)"},
    {"time": 23 * 60, "activity": "Sleep", "note": "Aim for 7-8 hours of sleep"},
]

def countdown(seconds):
    """Displays a countdown with a loading bar."""
    for _ in tqdm(range(seconds), desc=f"{RED}To next:{RESET}", ncols=100):
        time.sleep(1)

def alarm():
    print("\a")
    while True:
        user_input = input("Enter '1' to stop the alarm: ")
        if user_input == "1":
            break

def run_schedule():
    now = time.localtime()
    current_minutes = now.tm_hour * 60 + now.tm_min
    
    for task in schedule:
        time_to_activity = task["time"] - current_minutes
        if time_to_activity > 0:
            print(f"Next activity: {task['activity']} - {task['note']}")
            countdown(time_to_activity * 60)
            alarm()
            current_minutes = task["time"]
        else:
            continue

if __name__ == "__main__":
    art()
    run_schedule()
