##### Format specifier #####
>3d
0.2f

##### File input and output ##### 
with open('data.txt') as file:
  for line in file:
    print(line, end="") #end omits the extra newline 
