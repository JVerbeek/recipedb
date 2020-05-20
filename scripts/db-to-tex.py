import os


def to_tex(filename):
    os.system("context {} --purge".format(filename))

to_tex("../TeX-templates/recipe-template")
