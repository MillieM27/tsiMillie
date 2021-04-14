import csv


class ReadCSVFile:

    def getFileData(self,fileName):
        fileData = []
        with open('C:/Users/milli/PycharmProjects/tsi_individual/resource/' + fileName, 'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getLastLines(self, fileName, numerOfLines):
        return getFileData(fileName)[-1 * numerOfLines]
