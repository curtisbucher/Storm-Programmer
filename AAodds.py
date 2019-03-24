#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:39:54 2019

@author: curtisbucher
"""
import random

def roll_dice(lowest):
    return(random.randint(1,6) < lowest)
    
def take_piece(dice_list):
    ## removes the smallest dice from the list
    dice_list.remove(min(a))

## Getting input for the number of units, returns two arrays of dice to roll
def get_players():
    print("Offense")
    print("-------")
    
    infantry = int(input("Infantry: "))
    artillary = int(input("Artillary: " ))
    mech_infantry = int(input("Mechanized Infantry: "))
    tank = int(input("Tanks: "))
    AAA = int(input("AAAs: "))
    
    fighter = int(input("Fighters: "))
    tac_bomber = int(input("Tactical Bombers: "))
    strat_bomber = int(input("Strategic Bombers: "))
    
    battleship = int(input("Battleships: "))
    aircraft_carriers = int(input("Aircraft Carriers: "))
    cruiser = int(input("Cruisers: "))
    destroyer = int(input("Destroyers: "))
    submarine = int(input("Submarines: "))
    transport = int(input("Transports: "))
    
    off_ones = infantry + mech_infantry
    off_twos = artillary + submarine + destroyer
    off_threes = tank + fighter + tac_bomber + cruiser
    off_fours = strat_bomber + battleship
    
    print("Defense")
    print("-------")
    
    infantry = int(input("Infantry: "))
    artillary = int(input("Artillary: " ))
    mech_infantry = int(input("Mechanized Infantry: "))
    tank = int(input("Tanks: "))
    AAA = int(input("AAAs: "))
    
    fighter = int(input("Fighters: "))
    tac_bomber = int(input("Tactical Bombers: "))
    strat_bomber = int(input("Strategic Bombers: "))
    
    battleship = int(input("Battleships: "))
    aircraft_carrier = int(input("Aircraft Carriers: "))
    cruiser = int(input("Cruisers: "))
    destroyer = int(input("Destroyers: "))
    submarine = int(input("Submarines: "))
    transport = int(input("Transports: "))
    
    def_ones = AAA + strat_bomber + submarine
    def_twos = infantry + artillary + mech_infantry + aircraft_carrier + destroyer
    def_threes = tank + tac_bomber + cruiser
    def_fours = fighter + battleship
    
    off_dice += [1]* off_ones + [2]* off_twos + [3]* off_threes + [4]* off_fours
    def_dice += [1]* def_ones + [2]* def_twos + [3]* off_threes + [4]* off_fours
    
    
def play_round(off_list, def_list):
    off_kills = 0
    def_kills = 0
    
    for die in off_list:
        off_kills += roll_dice(die)
    for die in def_kills:
        def_kills += roll_dice(die)

def calc():
    off_dice, def_dice = get_players()
    