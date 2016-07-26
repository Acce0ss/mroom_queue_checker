
# coding=utf-8

import select
import urllib2
import json
import sys
import datetime


data = urllib2.urlopen("https://mroom.asioi.fi/api/pob-info-with-queue?city=Tampere")
stuff = json.load(data)
     
for (i,place) in zip(range(1,len(stuff)+1), stuff):
  sys.stdout.write( str(i) + " " + place['name'] + "\n") 

selection = input("Choose place index: ")

while True:

  data = urllib2.urlopen("https://mroom.asioi.fi/api/pob-info-with-queue?city=Tampere")
  stuff = json.load(data)

  place = stuff[int(selection) - 1]
  todayopen = place['week'][datetime.datetime.today().weekday()]
  aukiolo = todayopen['start'] + "-" + todayopen['end']
  sys.stdout.write( str(datetime.datetime.now()) + ", @" + place['name'] + " jonossa " + str(place['queue']['count']) + u', tänään avoinna ' + aukiolo + "\r")
  sys.stdout.flush()
        
  select.select([],[],[],10)
