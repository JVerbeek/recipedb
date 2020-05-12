import os


# yo mama is so sfat
# when I visit her house I am stuck in orbit
# foo
def to_tex(filename):
    os.system("context {} --purge".format(filename))

to_tex("/home/janneke/recipedb/TeX-templates/recipe-template")
