# Lue input
tiedosto = "input1.txt"

lines = []
with open( tiedosto , "r" ) as file:
  for line in file.readlines():
    lines.append( line.strip( "\n" ) )

kirjaimet = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
calibrations = []

for i in range( len( lines ) ):
    line = lines[i]
    for j in range( len( kirjaimet ) ):
        if kirjaimet[j] in line:
            line = line.replace( kirjaimet[j], '' )
        else:
           continue

    if len( line ) > 2:
        line = line[0]+line[-1]
    elif len( line ) == 1:
        line = line[0]+line[0]

    calibrations.append( line )

answer = 0
for l in range( len( calibrations ) ):
    answer += int( calibrations[l] )

print( answer )