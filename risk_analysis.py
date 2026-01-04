students = [
    {"gpa": 1.8, "failedModules": 2},
    {"gpa": 3.2, "failedModules": 0}
]

atRiskCount = 0

for student in students:
    if student["gpa"] < 2.2 or student["failedModule"] >= 2:
        student["status"] = "At-Risk"
        atRiskCount += 1
    else:
        student["status"] = "Not At-Risk"

print(atRiskCount)
