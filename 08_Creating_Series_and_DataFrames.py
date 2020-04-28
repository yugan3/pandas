# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:25:32 2020

@author: Gan
"""

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Create a data dictionary
raw_data = { 'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
             'type': ['grass', 'fire', 'water', 'bug'],
             'hp': [45, 39, 44, 45],
             'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
             'pokedex': ['yes', 'no', 'yes', 'no']   
        }

### Step 3. Assign it to a variable called pokemon
pokemon = pd.DataFrame(raw_data)

### Step 4. Ops...it seems the DataFrame columns are in alphabetical order. 
### Place  the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]

### Step 5. Add another column called place, and insert what you have in mind.
pokemon['place'] = ['shibuya', 'hokayido', 'nagoya', 'oosaka']

### Step 6. Present the type of each column
pokemon.dtypes
pokemon.info()

