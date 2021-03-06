       -----------====== CHALLENGE ======-----------

Your task it to write a python program to solve a little 
game. A fireman needs to go from a starting point S to a destination 
point D on a two-dimensional (16x12) map. The map also contains fire (&) 
which obviously need to be avoided at all costs.

For instance, the file "map1" contains:

................
....&...........
..........E.....
&&..&...........
....&&&.........
......&&&&..&&..
................
.......&........
.....&.&........
....S...........
.......&.&&.....
.......&.&&.....

The fireman can walk freely on normal terrain (marked as "." on the map)
in four directions (vertical or horizontal). Easy?
Well.. there is a catch. Or, actally, two of them :)

First, the fireman needs to reach his destination in no more
than 22 moves and he cannot move twice on the same tile.
 
Second, each time the fireman moves, the fire moves as well!!
In particular, a fire tile keeps burning if it is surrounded
(in all 8 directions) by 2 or 3 other fire tiles. Otherwise
it extinguishes. And a normal tile becomes a fire if it is
surrounded but more than 2 fire tiles.

For instance, after the fireman moves, the previous map
becomes:

................
................
................
....&&..........
....&.&&&.......
.....&&&&.......
......&&&.......
......&.........
......&.........
......&.&.......
........&&&.....
........&&&.....

And after the second move:

................
................
................
....&&&&........
....&&..&.......
.........&......
.....&..&.......
.....&&&........
.....&&&........
.......&&&......
.......&..&.....
........&.&.....


Your program has one minute of time to print the sequence of steps 
to move the fireman from the start (S) to the end (E) tile.
Four steps are available:
 N to move up (north)
 S to move down (south)
 E to move right (east)
 W to move left (west)

For example, given the previous map, a valid solution is:

NNNWWWNNNNNEEEEEEEEES


IMPORTANT:
 Note that the fireman cannot move in a tile that contains
 fire. Also, if the fire moves into the tile where he is, 
 the path is also invalid.

 For instance, in the following situation (where @ is the fireman):

 ....
 ...&
 &@.&
 ...&

 the fireman cannot go west (as there is fire there), but he cannot
 go east ether, as after his move the tiles on his right will be 
 on fire.

       -----------====== SUBMISSION ======-----------

Submit a python program that takes as first parameter the name
of the map and prints the list of moves as its only output.
Make sure to try your program by executing it with "map1" file.


