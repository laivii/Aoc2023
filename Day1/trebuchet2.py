tiedosto = "input2.txt"

lines = []
with open( tiedosto , "r" ) as file:
  for line in file.readlines():
    lines.append( line.strip( "\n" ) )

letters = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers =['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
calibrations = []

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(numbers)):
       if numbers[j] in line:
            change = ""
            if j == 0:
                change = "1"
            elif j == 1:
               change = "2"
            elif j == 2:
               change = "3"
            elif j == 3:
               change = "4" 
            elif j == 4:
               change = "5"
            elif j == 5:
               change = "6"
            elif j == 6:
               change = "7"
            elif j == 7:
               chnage = "8"
            elif j == 8:
               change = "9"
            
            line = line.replace(numbers[j], numbers[j]+change)
    calibrations.append(line)

print(calibrations)



