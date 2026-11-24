# Full Name: Jhasmine M. Aquino
# Section: IV-BSIT-A
# Activity Code: P2: Custom Module: student_utils
# Date: November 22, 2026

def computeAverage(grades):
    return sum(grades) / len(grades)

def highestGrade(grades):
    return max(grades)

def lowestGrade(grades):
    return min(grades)

def determineStatus(grades):
    averageGrade = computeAverage(grades)

    if averageGrade >= 75:
        return "PASSED"

    else:
        return "FAILED"

    