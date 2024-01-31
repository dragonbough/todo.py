programs = {"add":[], "subtract":[]}
RAM = {} 

print (*programs.keys())
program = input ("What program would you like to run?")
RAM.update(program:programs[program]) 
programcounter = RAM[program].index([0])
MAR = programcounter
addressbus = MAR
databus = RAM[program][addressbus]
MDR = databus 
instructionregister = MDR 
programcounter += 1

    