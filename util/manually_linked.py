from django.contrib.auth.models import User
from adventure.models import Player, Room

# Link rooms together
r_outside.connectRooms(r_foyer, "e")
r_foyer.connectRooms(r_outside, "w")

r_foyer.connectRooms(r_overlook, "e")
r_overlook.connectRooms(r_foyer, "w")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")




players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()
