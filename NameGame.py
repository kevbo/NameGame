name = "Matt"

length = len(name)

import subprocess

if name == "Chuck":
    subprocess.call(['say', "You are naughty! I am not doing that one!"])
else:
    subprocess.call(['say', name + "," + name + "," + "Bo " + "B" + name[1:length] + "."]) 

    subprocess.call(['say', "Banana Fan uh. Fo F" + name[1:length] + "."]) 

    subprocess.call(['say', "Meet my, mo M" + name[1:length] + "."])
    subprocess.call(['say', name+"!" ])
