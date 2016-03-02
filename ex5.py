name = 'Jonathon M. Simonton'
age = 29
height = 70
weight = 190
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm_conversion = height / 0.39370
kg_conversion = weight / 2.2046

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually thats not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)

print "In centimeters I am " + str(cm_conversion)) + " tall."
print "In kilograms I am " + str(kg_conversion)) + " heavy."

