CORRECT_NUMBER_OF_PAIRS = 72125


class QualityMeasure:
    truePositives = 0
    falsePositives = 0
    trueNegatives = 0
    falseNegatives = 0

    def computeMatch(self, publication1, publication2):
        if publication1.attrib == publication2.attrib:
            self.truePositives += 1
        else:
            self.falsePositives += 1

    def computeMeasures(self):
        precision = self.truePositives/(self.falsePositives + self.truePositives)
        print("Precision: " + str(precision))

        self.falseNegatives = CORRECT_NUMBER_OF_PAIRS - self.truePositives
        recall = self.truePositives / (self.falseNegatives + self.truePositives)
        print("Recall: " + str(recall))

        fMeasure = (2 * precision * recall)/(precision + recall)
        print("F-measure: " + str(fMeasure))