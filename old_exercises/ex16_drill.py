from sys import argv

script, filename = argv

txt = open("ex16_sample")
print "\nName of the file:\n", txt.name

line = txt.read()
print "\nRead Line:\n%s" % (line)

txt.close()


