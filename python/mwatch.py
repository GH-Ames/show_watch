#!/usr/bin/python3

# script to manage a flatfile list of shows

import os

def menu():
    print()
    print('############ Show Watch Main Menu ##############')
    print('A: List all shows')
    print('Q: Quit')
    print("\n")

while True:
    os.system("clear")
    menu()
    val = input("Enter Choice:")
    if val == "A" or val == "a":
        print('You picked:', val)
        os.system("sleep 1")
    elif val == "Q" or val == "q":
        print('You picked:', val)
        os.system("sleep 1")
        print('Exiting...')
        os.system("sleep 1")
        break
    else:
        print("Please select A or Q")
        os.system("sleep 1")
        print('reloading the page')
        os.system("sleep 1")
        os.system("clear")
        menu()

