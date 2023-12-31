from curses import erasechar
from re import A


users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}


# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathan_twitter_handle = users["Jonathan"]["twitter"]

# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]

# 3. Get the list of Erik's lottery numbers
erik_lottery_nums = users["Erik"]["lottery_numbers"]

# 4. Get the species of Avril's pet Monty
monty_species = users["Avril"]["pets"][0]["species"]

# 5. Get the smallest of Erik's lottery numbers
erik_lottery_nums.sort()
erik_smallest_number = erik_lottery_nums[0]

# 6. Return an list of Avril's lottery numbers that are even
avril_lottery_nums = users["Avril"]["lottery_numbers"]
even_numbers = []
for number in avril_lottery_nums:
  if number % 2 == 0:
    even_numbers.append(number)

# ALTERNATE SOLUTION:
# from itertools import filterfalse
# even_numbers = [] 
# for number in filterfalse(lambda y: y % 2, avril_lottery_nums):
#   even_numbers.append(number)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"
new_pet = {
  "name": "fluffy",
  "species": "dog"
}

users["Erik"]["pets"].append(new_pet)

# 10. Add another person to the users dictionary
users["Lebowski"] = {
    "twitter": "thedude",
    "lottery_numbers": [13, 2, 5],
    "home_town": "Los Angeles",
    "pets": []
}
