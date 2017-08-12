from sys import argv

script, user_name = argv
prompt = '> '
enn=">>> "

print "Hi %s, I'm the %s sccript." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you lke me %s?" % user_name
likes = raw_input(enn)

print "where do you live %s?" % user_name
lives = raw_input(enn)

print "what kind of computer do you have?"
computer = raw_input(enn)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)