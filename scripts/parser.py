import xml.etree.ElementTree as ET


def user_input():
    not_exited = True
    print(""" \n
    __________              .__              ________ __________ \n
    \______   \ ____   ____ |__|_____   ____ \______ \\______   \ \n
     |       _// __ \_/ ___\|  \____ \_/ __ \ |    |  \|    |  _/ \n
     |    |   \  ___/\  \___|  |  |_> >  ___/ |    `   \    |   \ \n
     |____|_  /\___  >\___  >__|   __/ \___  >_______  /______  / \n
            \/     \/     \/   |__|        \/        \/       \/ \n

    """)
    while not_exited:
        inp = input("Hallo! Welkom in RecipeDB. Wat wil je koken? \n")
        if "niks" in inp:
            not_exited = False
            print("Ja doei.")
        elif levenshtein("tosti", inp)>3 and "tosti" not in inp:
            print("We hebben helaas niks anders dan tostis.")
        else:
            lees_recept("kaasuitosti.xml")


def lees_recept(filepath):
    root = ET.parse('../recepten/kaasuitosti.xml').getroot()
    stappen = root.findall("*/stap")
    ings = [(i.attrib["naam"], i.attrib["kwantiteit"]) for i in root.findall("*/in")]
    print("\nRECEPT VOOR " + "kaasuitosti")
    print("="*32)
    print("INGREDIENTEN" +"          " +"Kwantiteit")
    print("="*32)
    for i in ings:
        print(i[0],(30-len(i[0])-len(i[1]))*"-",i[1])
    print("\n")
    print("STAPPEN")
    for stap in stappen:
        print(stap.attrib["number"], stap.text.strip())

def levenshtein(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    print(distances[-1])
    return distances[-1]

def main():
    user_input()

if __name__ == "__main__":
    main()
