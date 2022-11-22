import math
import time

print ("This is only useful for that one DrFrostMaths homework that was due like 2 days ago (27/09/2022).");
time.sleep(2);
print ("This was actually the biggest waste of time. no joke.");
time.sleep(2);

while True:
    surfaceOrVol = input ("Surface or Volume?");
    if surfaceOrVol == "v":
        shapeASA = float(input ("Shape A Surface Area:"));
        shapeBSA = float(input ("Shape B Surface Area:"));
        shapeVolGiven = input ("What shape's volume has been given?");
        if shapeVolGiven == "a":
            shapeAVol = float(input ("What is the volume of Shape A?"));
            surfADiff = math.sqrt(shapeBSA / shapeASA);
            volMulti = surfADiff ** 3;
            answer = shapeAVol * volMulti;
            print ("The answer is:", answer, "or", math.ceil(answer));
        if shapeVolGiven == "b":
            shapeBVol = float(input ("What is the volume of Shape B?"));
            surfADiff = math.sqrt(shapeBSA / shapeASA);
            volMulti = surfADiff ** 3;
            answer = shapeBVol / volMulti;
            print ("The answer is:", answer, "or", math.ceil(answer));
    if surfaceOrVol == "s":
        shapeAVol = float(input ("Shape A Volume:"));
        shapeBVol = float(input ("Shape B Volume:"));
        shapeSAGiven = input ("What shape's surface area has been given?");
        if shapeSAGiven == "b":
            shapeBSA = float(input ("What is the surface area of Shape B?"));
            volumeDiff = (shapeBVol / shapeAVol) ** (1/3);
            surfAreaMulti = volumeDiff ** 2;
            answer = shapeBSA / surfAreaMulti;
            print ("The answer is:", answer);
        if shapeSAGiven == "a":
            shapeASA = float(input ("What is the surface area of Shape A?"));
            volumeDiff = (shapeBVol / shapeAVol) ** (1/3);
            surfAreaMulti = volumeDiff ** 2;
            answer = shapeASA * surfAreaMulti;
            print ("The answer is:", answer, "or", math.ceil(answer));
        