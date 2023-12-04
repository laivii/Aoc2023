#input file
tiedosto = "input1.txt"

#Read inputs from files
lines = []
with open( tiedosto , "r" ) as file:
    for line in file.readlines():
        lines.append( line.strip( "\n" ) )

total_points = 0

for i in range( len( lines ) ):
    line = lines[ i ]
    line = line.split( ": ")[ 1 ]
    line = line.split( " | " )

    points = 0
    
    line[0] = line[0].split( " " )
    line[1] = line[1].split( " " )

    for j in range( len( line[ 1 ] ) ):
        number = line[ 1 ][ j ]

        if number == "":
            continue
        
        if number in line[ 0 ]:
            if points == 0:
                points = 1
            else:
                points = points * 2

    total_points += points

print( total_points )