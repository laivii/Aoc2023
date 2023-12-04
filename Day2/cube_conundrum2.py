#input file
tiedosto = "input1.txt"

#Read inputs from files
lines = []
with open( tiedosto , "r" ) as file:
    for line in file.readlines():
        lines.append( line.strip( "\n" ) )

sum_powers = 0

for i in range( len( lines ) ):
    line = lines[ i ]
    game = i+1

    line = line.replace( ";", ',' )
    line = line.split( ": " )[ 1 ]
    line = line.split( ", " )

    max_red = 0
    max_blue = 0
    max_green = 0
    
    for j in range( len( line ) ):
        cubes = line[ j ]
        cubes = cubes.split( " " )
        
        if cubes[ 1 ] == "red":
            if int( cubes[ 0 ] ) > max_red:
                max_red = int( cubes[ 0 ] )
        
        if cubes[1] == "blue":
            if int( cubes[ 0 ] ) > max_blue:
                max_blue = int( cubes[ 0 ] )
        
        
        if cubes[ 1 ] == "green":
            if int( cubes[ 0 ] ) > max_green:
                max_green = int( cubes[ 0 ] )
        
    powers = max_red * max_green * max_blue
    sum_powers += powers

print( sum_powers )