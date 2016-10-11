my_name = 'Wang Rui'
my_age = 28
my_height = 171.5 #cm
my_weight = 65 #kg
my_teeth = 'White'
my_eyes = 'Brown'
my_hair = 'Black'
my_rough_height = round(my_height)

print "Let's talk about %s." % my_name
print "He's %g cm tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's not too light."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "My rough height is", my_rough_height

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)