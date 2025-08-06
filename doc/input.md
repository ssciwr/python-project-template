Here goes a description of the input required for your program.

# Program input

The program options can be displayed by running
`python ./src/mypackage/main.py -h`  

This will return the possible input options and type of parameters. 

For example, to calculate the side length of a square with the same area as a circle of radius $r$ (e.g. $r = 4$), you would run  
`python ./src/mypackage/main.py -o square -r 4`  

For the side length of a pentagon, you would provide  
`python ./src/mypackage/main.py -o pentagon -r 4`  

The program will then return the side length of the selected object.