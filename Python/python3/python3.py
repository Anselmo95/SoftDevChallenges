#!/usr/bin/python
import sys

max_x = 16
max_y = 12
iteration = 22
history = []
sol = []
matrix = [[0]*max_x for x in range(max_y) ]

def printMappa(mappa):
	for y in mappa:
		print ''.join(map(str,y)).strip()
	print

def keepStartBurning(mappa,y,x):
	adj_fire = 0

	if (x-1) >= 0:
		if mappa[y][x-1] == '&':
			adj_fire += 1

		if (y+1) < max_y:
			if mappa[y+1][x-1] == '&':
				adj_fire += 1

		if (y-1) >= 0:
			if mappa[y-1][x-1] == '&':
				adj_fire += 1

	if (x+1) < max_x:
		if mappa[y][x+1] == '&':
			adj_fire += 1

		if (y+1) < max_y:
			if mappa[y+1][x+1] == '&':
				adj_fire += 1

		if (y-1) >= 0:
			if mappa[y-1][x+1] == '&':
				adj_fire += 1

	if (y-1) >= 0:
		if mappa[y-1][x] == '&':
			adj_fire += 1

	if (y+1) < max_y:
		if mappa[y+1][x] == '&':
			adj_fire += 1


	if mappa[y][x] == '&':
		if (adj_fire != 3) and (adj_fire != 2):
			return '.'
	elif adj_fire > 2:
			return '&'

	return mappa[y][x]
	
def genMap(mappa):

	new_mappa = [[None]*max_x for x in range(max_y)]
	for y in range(max_y):
		for x in range(max_x):
			new_mappa[y][x] = keepStartBurning(mappa,y,x) 

	return new_mappa

def getAllMaps(mappa):
	mappa_time = [None]*(iteration+1)
	mappa_time[0] = mappa
	for i in range(1,iteration+1):
		mappa_time[i] = genMap(mappa_time[i-1])
		#printMappa(mappa_time[i])

	return mappa_time

def getMovement(mappa_now,mappa_future,y,x):
	move = []
	
	if (y-1) >= 0:
		if ((mappa_now[y-1][x] == '.') and (matrix[y-1][x] == 0) and (mappa_future[y-1][x] == '.')):
			move.append(['N', y-1, x])

	if (x-1) >= 0:
		if ((mappa_now[y][x-1] == '.') and (matrix[y][x-1] == 0) and (mappa_future[y][x-1] == '.')):
			move.append(['W', y, x-1])
	
	if (x+1) < max_x:
		if ((mappa_now[y][x+1] == '.') and (matrix[y][x+1] == 0) and (mappa_future[y][x+1] == '.')):
			move.append(['E', y, x+1])
	
	if (y+1) < max_y:
		if ((mappa_now[y+1][x] == '.') and (matrix[y+1][x] == 0) and (mappa_future[y+1][x] == '.')):
			move.append(['S', y+1, x])

	return move

def explore(mappa_time, time, posy, posx):

	if (posx == end_posx) and (posy == end_posy):
		#print 'Made IT!', posx, posy
		#print ''.join(map(str,history)).strip()
		global tot_sol
		tot_sol += 1
		#global sol 
		#sol = list(history)
		#sys.exit()
		return
	elif (abs(end_posx - posx) + abs(end_posy - posy) + time) >= iteration:
		return
	elif time >= iteration:
		return

	move_av = getMovement(mappa_time[time],mappa_time[time+1],posy,posx)
	for move in move_av:
		history.append(move[0])
		matrix[move[1]][move[2]] = 1
		explore(mappa_time,time+1,move[1],move[2])
		matrix[move[1]][move[2]] = 0
		history.pop()

	return

if len(sys.argv) != 2:
	sys.exit('Wrong parameters')

mappa_list = []
for y,line in enumerate(open(sys.argv[1])):
	mappa_list.append(list(line.strip('\n')))
	for x,char in enumerate(line):
		if char == 'S':
			start_posy = y
			start_posx = x
			mappa_list[y][x] = '.'
		elif char == 'E':
			end_posy = y
			end_posx = x
			mappa_list[y][x] = '.'


matrix[start_posy][start_posx] = 1
tot_sol = 0 

mappa_time = getAllMaps(mappa_list)

explore(mappa_time,0,start_posy,start_posx)
print tot_sol
#print ''.join(map(str,sol)).strip()