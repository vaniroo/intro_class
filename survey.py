print "Welcome to the survey!"
name = raw_input("What is your name? ")
color = raw_input("What is your favorite color? ")
hobby = raw_input("What is your favorite hobby? ")
movie = raw_input("What is your favorite movie? ")
pets = raw_input("Do you prefer dogs or cats? ")
siblings = raw_input("How many siblings do you have? ")

print name + "'s favorite color is " + color + "."
print "%s's favorite hobby is %s." % (name, hobby)
print name + "'s favorite movie is " + movie + "."
print name, "has", siblings, "siblings!"
print "%s prefers %s." % (name, pets)