import time 

bojack = 0
carolyn = 0
diane = 0
pb = 0
todd = 0  

print ("What Bojack Horseman character are you? Take this test!")
time.sleep(1)
print ("How would you describe yourself?")
print ("--------------------------------")
print ("A: Other")
print ("B: Energetic")
print ("C: Independent")
print ("D: Hardworking")
q1=input ("E: Imaginative")

if q1.lower() == "a":
	bojack += 1
if q1.lower() == "b":
	pb += 1
if q1.lower() == "c":
	diane += 1
if q1.lower() == "d":
	carolyn += 1
if q1.lower() == "e":
	todd += 1  

time.sleep(0.5)
print ("What do you enjoy doing?")
print ("------------------------")
print ("Working")
print ("Playing video games")
print ("Sport & outdoor activities")
print ("Sleeping")
q2=input ("Drawing or writing")

if q2.lower() == "a":
	carolyn += 1
if q2.lower() == "b":
	todd += 1
if q2.lower() == "c":
	pb += 1
if q2.lower() == "d":
	bojack += 1
if q2.lower() == "e":
	diane += 1  

time.sleep(0.5)
print ("Your goal in life is to...")
print ("--------------------------")
print ("Find your soulmate")
print ("Escape")
print ("Make change")
print ("Be successful")
q3=input ("I... don't know... ")

if q3.lower() == "a":
	pb += 1
if q3.lower() == "b":
	bojack += 1
if q3.lower() == "c":
	diane += 1
if q3.lower() == "d":
	carolyn += 1
if q3.lower() == "e":
	todd += 1

time.sleep(0.5)
print ("What are your flaws?")
print ("--------------------")
print ("I'm too hard on myself ")
print ("I act childish")
print ("I'm a narcissist")
print ("I work too hard for nothing")
q4=input ("I'm always so stubborn")

if q4.lower() == "a":
	bojack += 1
if q4.lower() == "b":
	todd += 1
if q4.lower() == "c":
	pb += 1
if q4.lower() == "d":
	carolyn += 1
if q4.lower() == "e":
	diane += 1

time.sleep(2)
print ("---------------------------")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(0.5)
q5 = "Are you happy?"
time.sleep(2)
for i in range(len(q5)):
	print (q5[i])
	time.sleep(0.5)
for i in range (1, 12):
	print ("No")
	time.sleep(0.5)
answer = input ("No")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")
time.sleep(0.5)
print (answer, "is not a valid answer.")
for i in range (100):
	print ("-------------------------")
	time.sleep(0.1)
print ("You will never be happy if you continue to search for what happiness consists of.")
print ("You will never live if you are looking for the meaning of life.")
print ("- Albert Camus")
time.sleep(2)

if bojack > max(pb, diane, todd, carolyn):
	print ("You are Bojack Horseman, the self loathing addict.")
if pb > max(bojack, diane, todd, carolyn):
	print ("You are Mr Peanutbutter, the hopeless romantic narcissist.")
if diane > max(bojack, pb, todd, carolyn):
	print ("You are Diane, the misunderstood intellectual.")
if todd > max(bojack, pb, carolyn, diane): 
	print ("You are Todd, the childish but well-meant gentleman.")
if carolyn > max(bojack, pb, todd, diane):
	print ("You are Princess Carolyn, the workaholic optimist.")
else:
	print ("It seems you are a mixed bag ig idfk what this was im honestly bored my brother.")
	print ("In all honesty its just that you have two characters that have the same \"score")
	print ("i guess i'll just keep you guessing *shrug*")
	print ("Keep in mind this was an easy task i put myself to so i just spiced it up a bit")