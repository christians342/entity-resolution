import xml.etree.ElementTree as ET

def match(publication1, publication2):
    publication1TitlesList = list(map(lambda x: x.text, publication1.findall("title")))
    publication1TitlesList = list(map(lambda x: x.lower(), publication1TitlesList))
    publication1FullTitleString = " ".join(publication1TitlesList)
    publication1FullTitleString.lower()

    publication2TitlesList = list(map(lambda x: x.text, publication2.findall("title")))
    publication2TitlesList = list(map(lambda x: x.lower(), publication2TitlesList))
    publication2FullTitleString = " ".join(publication2TitlesList)
    publication2FullTitleString.lower()

    if publication1FullTitleString == publication2FullTitleString:
        return True
    return False

def entityResolution(publications):
    matches = 0
    for i in range(0, len(publications)):
        for j in range(i + 1, len(publications)):
            if match(publications[i], publications[j]):
                #print("Deu match entre entities " + str(publications[i]) + str(publications[j]))
                matches+=1
    print(matches)
    print(len(publications))



if __name__ == '__main__':

    tree = ET.parse('cora-all-id.xml')
    root = tree.getroot()

    entityResolution(root)