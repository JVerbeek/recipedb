import os


def to_tex(filename):
    os.system("context {} --purge".format(filename))

to_tex("/home/janneke/recipedb/TeX-templates/recipe-template")
