# tworzenie obiektu - data elements + functions
# T zazwyczaj oznacza new type
# self oznacza every object


class TActivity:
    def __init__(self, activityName, activityGrade):
        self.ActivityName = activityName
        self.ActivityGrade = activityGrade

    def showActivityState(self):
        print(" - " + self.ActivityName + " " + str(self.ActivityGrade))

    def getActivityGrade(self):
        return self.ActivityGrade


class TProcess:
    def __init__(self):
        self.ActivityList = []
        self.noActivities = 0

    def addActivity(self, arg):
        self.ActivityList.insert(self.noActivities, arg)
        self.noActivities = self.noActivities + 1

    def showProcessState(self):
        print("Here is the list of my exams: ")
        for e in self.ActivityList:
            e.showActivityState()
        print("Mean grade of my exams = " + str(self.computeMeanValue()))

    def computeMeanValue(self):
        sumTemp = 0.0
        for e in self.ActivityList:
            sumTemp = sumTemp + e.getActivityGrade()
        return round(sumTemp/self.noActivities, 2)

def main():
    myExams = TProcess()
    myExams.addActivity(TActivity("Statistical Methods", 5.0))
    myExams.addActivity(TActivity("Python Programming", 4.5))
    myExams.addActivity(TActivity("Big Data", 3.0))
    myExams.showProcessState()

if __name__ == "__main__":
    main()


