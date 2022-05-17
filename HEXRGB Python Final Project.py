# HEXRGB FNDR By Dominique Hill

import time

# Introduction and Welcome

print("Hello. Here is a simple program that will help users locate RGB and HEX codes")
print("for any color.  Remember the color wheel, this is basically going to take those")
print("colors and convert those colors into both HEX and RGB based on the users choice ")
print("of course. You will have your very own hex/rgb code library right at your fingertips.")

time.sleep(3)

print("Ok...")

time.sleep(5)

print("Let's get started")

# Welcome the User
print("Hello, Welcome to RGB/HEX FNDR")

time.sleep(3)

print("OK...Before we start I will need some information from you.")

time.sleep(2)

name = input("What is your name")

# User chooses if they want to search for the colors hex or rgb value
hxrgb_answr = input("Would you like the hex value or rgb value?")

color = input("What color are you looking for?")

# Colors corresponds to the letter you choose UPPERCASE is for the RGB list and lowercase is for the HEX list
print("Choose a letter from the list to correspond with the RGB and HEX color you want.")
print("R equals red", "B equals blue", "Y equals yellow", "O equals orange", "G equals green", "V equals violet")

# HEX and RGB Lists

hex_list = ["red #fff0000", "blue #0000f", "yellow #ffff00", "orange #ffa500", "green #0080", "violet #ee82ee"]
for x in range(0, 6):
    position = hex_list[x].find(color)
    print(name, "The hex value for", color, "is", hex_list[x])

rgb_list = ["Red-255, 0, 0", "Blue-0, 0, 255", "Yellow-255, 255, 0", "Orange-255, 165, 0",
                "Green-0, 128, 0", "Violet-238, 130, 238"]
for x in range(0, 6):
    position = rgb_list[x].find(color)
    print(name, "The rgb value for", color, "is", rgb_list[x])



# User chooses to choose another color

choose_again = "yes"

while choose_again == "yes":
    hxrgb_answr = input("Would you like the hex value or rgb value?")

    color = input("What color are you looking for?")

  # Choose a letter from the list to correspond with the RGB and HEX color you want.
  # The color(s) with the first letter capitalied is for finding the color code in the rgb list
  # Example: Red, Blue, Green, Orange, Violet
  # The color(s) with the first letter lower cased is for finding the color code in the hex list
  # Example: red, blue, green, orange, violet

    # HEX and RGB Lists

    hex_list = ["red #fff0000", "blue #0000f", "yellow #ffff00", "orange #ffa500", "green #0080", "violet #ee82ee"]
    for x in range(0, 6):
        position = hex_list[x].find(color)
        if position != -1:
            print(name, "The hex value for", color, "is", hex_list[x])

    rgb_list = ["Red-255, 0, 0", "Blue-0, 0, 255", "Yellow-255, 255, 0", "Orange-255, 165, 0",
                "Green-0, 128, 0", "Violet-238, 130, 238"]
    for x in range(0, 6):
        position = rgb_list[x].find(color)
        if position != -1:
            print(name, "The rgb value for", color, "is", rgb_list[x])



    choose_again = input("Would you like to search for another color? yes or no?")

    # If user decides to not choose another color
    if choose_again == "no":
        print("Thanks for using HEXRGB FNDR!", name, "See you next time!")