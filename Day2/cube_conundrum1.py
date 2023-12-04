#input file
tiedosto = "input1.txt"

#Read inputs from files
lines = []
with open( tiedosto , "r" ) as file:
  for line in file.readlines():
    lines.append( line.strip( "\n" ) )

viable = 0

#Read input lines
for i in range( len( lines ) ):
    line = lines[ i ]
    game = i+1

    line = line.replace( ";", ',' )
    line = line.split( ": " )[ 1 ]
    line = line.split( ", " )
    possible = True
    #Read input lines' items
    for j in range( len( line ) ):
        cubes = line[ j ]
        cubes = cubes.split( " " )
        
        if int( cubes[0] ) > 14 and cubes[1] == "blue":
           possible = False

        if int( cubes[0] ) > 12 and cubes[1] == "red":
           possible = False

        if int( cubes[0] ) > 13 and cubes[1] == "green":
           possible = False
        
    if possible == True:
       viable += game

print( viable )

