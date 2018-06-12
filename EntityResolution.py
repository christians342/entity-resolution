import time
import xml.etree.ElementTree as ET
from QualityMeasure import QualityMeasure

class EntityResolver:
    def __init__(self, publications):
        self.qualityMeasure = QualityMeasure()
        self.matches = {}
        self.publications = publications

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
            self.matches[str(publication1)+str(publication2)] = 1
            return True
        return False

    def resolve(self):
        groups = self.getGroups(self.publications)
        for group in groups:
            self.resolveGroup(group)

    def resolveGroup(self, publications):
        for i in range(0, len(publications)):
            for j in range(i + 1, len(publications)):
                # check whether the comparison was already made before
                if str(publications[i]) + str(publications[j]) in self.matches:
                    #print("Match found in previously found matches.")
                    pass
                elif self.match(publications[i], publications[j]):
                    #print("We have a match between entities " + str(publications[i]) + str(publications[j]))
                    self.qualityMeasure.computeMatch(publications[i], publications[j])

    def getGroups(self, publications):
        groups = {}
        groups["no-title-found"] = []
        for publication in publications:
            publicationTitles = list(map(lambda x: x.text, publication.findall("title")))
            for word in publicationTitles:
                word = word.replace(":", "")
                word = word.replace(".", "")
                word = word.replace(" ", "")
                word = word.replace(",", "")
                word = word.replace("\"", "")
                word = word.replace("-", "")
                word = word.replace(";", "")
                word = word.replace("'", "")
                word = word.replace("`", "")
                word = word.lower()
                if word not in groups:
                    groups[word] = []
                groups[word].append(publication)
            print(len(publicationTitles))
            if len(publicationTitles) == 0:
                groups["no-title-found"].append(publication)

        groups["a"] = []
        groups["as"] = []
        groups["the"] = []
        groups["for"] = []
        groups["an"] = []
        groups["of"] = []
        groups["in"] = []
        groups["and"] = []
        groups["learning"] = []

        for group in groups:
            if len(groups[group]):
                print(str(group) + "[" + str(len(groups[group])) + " items]")

        return groups.values()


if __name__ == '__main__':

    tree = ET.parse('cora-all-id.xml')
    root = tree.getroot()

    startTime = time.time()

    entityResolver = EntityResolver(root)
    entityResolver.resolve()

    print("\nEntity Resolver execution time: " + str(time.time() - startTime) + " seconds\n")

    entityResolver.qualityMeasure.computeMeasures()