#!/bin/python

#Script to talk to the steam api

#Import requirements
import requests
import argparse
import pprint
import json
from prettytable import PrettyTable

#Define variables
playerEndpoint="http://api.steampowered.com/IPlayerService"
userStatsEndpoint="http://api.steampowered.com/ISteamUserStats"
userEndpoint="http://api.steampowered.com/ISteamUser"
api_key="<insert here>"
steam_id="<insert here>"

#Define functions

def getOwnedGames(myEndPoint,myAPIKey, mySteamID):
    #Build URL and make request
    targetURL = myEndPoint+"/GetOwnedGames/v0001/?key="+myAPIKey+"&steamid="+mySteamID+"&format=json&include_appinfo=1"
    r = requests.get(targetURL)

    #Push resultes in to a json object and count the length of it
    results_json = r.json()
    total_games = len(results_json['response']['games'])

    #Define table structure
    t = PrettyTable(['Game', 'Played', 'GameID'])

    #Loop through each json object, pull out the game name and playtime and load it into table rows
    for i in range(0,total_games):
        t.add_row([results_json['response']['games'][i]['name'],results_json['response']['games'][i]['playtime_forever'],results_json['response']['games'][i]['appid']])
    
    #Print out the table build above and the count of games
    print t 
    print "\nTotal games: "+str(total_games)

    return

def getRecentGames(myEndPoint,myAPIKey, mySteamID):
    #Build URL and make request
    targetURL = myEndPoint+"/GetRecentlyPlayedGames/v0001/?key="+myAPIKey+"&steamid="+mySteamID+"&format=json"
    r = requests.get(targetURL)

    #Push resultes in to a json object and count the length of it
    results_json = r.json()
    total_games = len(results_json['response']['games'])
    
    #Define table structure
    t = PrettyTable(['Game', 'Played'])

    #Loop through each json object, pull out the game name and playtime and load it into table rows
    for i in range(0,total_games):
        t.add_row([results_json['response']['games'][i]['name'],results_json['response']['games'][i]['playtime_2weeks']])

    #Print out the table build above and the count of games
    print t

    return

def getAchievement(myEndPoint,myAPIKey,mySteamID,requestedAppID):
    #Build URL and make request
    targetURL = myEndPoint+"/GetPlayerAchievements/v0001/?appid="+requestedAppID+"&key="+myAPIKey+"&steamid="+mySteamID
    r = requests.get(targetURL)

    #Push resultes in to a json object and count the length of it
    results_json = r.json()

    pprint.pprint(results_json)

    return

def getFriends(myEndPoint,myAPIKey,mySteamID):
    #Build URL and make request
    targetURL = myEndPoint+"/GetFriendList/v0001/?key="+myAPIKey+"&steamid="+mySteamID+"&relationship=friend"
    r = requests.get(targetURL)

    #Push resultes in to a json object and count the length of it
    results_json = r.json()

    pprint.pprint(results_json)

    return

#Setup argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--games", help="list games in account", action='store_true', required=False)
parser.add_argument("-r", "--recent", help="list recently played games", action='store_true', required=False)
parser.add_argument("-a", "--achievement", help="list achievements for <appid>", action='store', dest='appid', required=False)
parser.add_argument("-f", "--friends", help="list friends", action='store_true', required=False)
args = parser.parse_args()

#Main code
if args.games:
    getOwnedGames(playerEndpoint, api_key, steam_id)
elif args.recent:
    getRecentGames(playerEndpoint, api_key, steam_id)
elif args.appid:
    getAchievement(userStatsEndpoint, api_key, steam_id, args.appid)
elif args.friends:
    getFriends(userEndpoint, api_key, steam_id)
