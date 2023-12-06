#input file
tiedosto = "input1.txt"

#Read inputs from files
lines = []
with open( tiedosto , "r" ) as file:
  for line in file.readlines():
    lines.append( line.strip( "\n" ) )

#Filter times
times = lines[ 0 ].split( ": " )[ 1 ]
times = times.split( " " )

while "" in times:
  times.remove( "" )

#Filter best distances
best_dist = lines[ 1 ].split( ": " )[ 1 ]
best_dist = best_dist.split( " " )

while "" in best_dist:
  best_dist.remove( "" )

totals_multiplied = 1

for i in range( len( times ) ):
    time = times[ i ]
    start = 0
    total_wins = 0
    for j in range(int( time ), -1, -1 ):
        distance = start * j
        #print(distance)
        if distance > int( best_dist[ i ] ):
            total_wins += 1
        start += 1
    
    totals_multiplied = totals_multiplied*total_wins

print( totals_multiplied )