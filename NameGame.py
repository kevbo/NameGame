import subprocess


name = "poop"

length = len(name)

print "Name Variable = " + name
print "Length variable (length of name variable) = " + str(length)

# the slicing syntax below ([1:]) means
# 'from the second character until the end'
shortened_name = name[1:]

values = {'name': name, 'shortened_name': shortened_name}

if name == "Chuck" or name == "chuck" or name == "CHUCK":
    subprocess.call(['say', "You are naughty! I am not doing that one!"])
else:
    subprocess.call(
        ['say', '{name}, {name}, Bo B{shortened_name}.'.format(**values)])

    subprocess.call(
        ['say', "Banana Fan uh. Fo F{shortened_name}.".format(**values)])

    subprocess.call(
        ['say', "Meet my, mo M{shortened_name}.".format(**values)])

    subprocess.call(['say', name + "!"])
