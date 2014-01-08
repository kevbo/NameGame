import subprocess


name = "poop"

length = len(name)

print "Name Variable = " + name
print "Length variable (length of name variable) = " + str(length)

if name == "Chuck" or name == "chuck" or name == "CHUCK":
    subprocess.call(['say', "You are naughty! I am not doing that one!"])
else:
    subprocess.call(['say', name + "," + name + "," + "Bo " + "B" + name[1:length] + "."])

    subprocess.call(['say', "Banana Fan uh. Fo F" + name[1:length] + "."])

    subprocess.call(['say', "Meet my, mo M" + name[1:length] + "."])
    subprocess.call(['say', name + "!"])
