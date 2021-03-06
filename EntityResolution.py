import time
import xml.etree.ElementTree as ET
from QualityMeasure import QualityMeasure

class EntityResolver:
    def __init__(self):
        self.qualityMeasure = QualityMeasure()

    def match(self, publication1, publication2):
        publication1TitlesList = list(map(lambda x: x.text, publication1.findall("title")))
        publication1TitlesList = list(map(lambda x: x.lower(), publication1TitlesList))
        publication1FullTitleString = " ".join(publication1TitlesList)
        publication1FullTitleString.lower()
        publication1FullTitleString = publication1FullTitleString.replace(',', "")
        publication1FullTitleString = publication1FullTitleString.replace('.', "")

        publication2TitlesList = list(map(lambda x: x.text, publication2.findall("title")))
        publication2TitlesList = list(map(lambda x: x.lower(), publication2TitlesList))
        publication2FullTitleString = " ".join(publication2TitlesList)
        publication2FullTitleString.lower()
        publication2FullTitleString = publication2FullTitleString.replace('.', "")
        publication2FullTitleString = publication2FullTitleString.replace(',', "")

        if publication1FullTitleString == publication2FullTitleString:
            return True
        return False

    def resolve(self, publications):
        for i in range(0, len(publications)):
            for j in range(i + 1, len(publications)):
                if self.match(publications[i], publications[j]):
                    #print("We have a match between entities " + str(publications[i]) + str(publications[j]))
                    self.qualityMeasure.computeMatch(publications[i], publications[j])


if __name__ == '__main__':

    tree = ET.parse('cora-all-id.xml')
    root = tree.getroot()

    startTime = time.time()

    entityResolver = EntityResolver()
    entityResolver.resolve(root)

    print("Entity Resolver execution time: " + str(time.time() - startTime) + " seconds\n")

    entityResolver.qualityMeasure.computeMeasures()