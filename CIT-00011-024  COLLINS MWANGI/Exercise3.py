# 1. Create a tuple for a patient containing: (Name, Age, Blood Pressure, Heart Rate).
patient = ("Joe Biden", 45, "114/80", 70)
# 2. Access and print the patient’s age and heart rate.
age = patient[1]
heartRate = patient[3]
print(age,heartRate)

# 3. Explanation: Tuples are immutable → data safety for medical records.


# 4. Convert the tuple to a list, update the heart rate, and convert it back to a tuple.
patientList = list(patient)
patientList[3] = 75
patient = tuple(patientList)
# 5.Create a tuple of 5 patients ``
patients = (
    ("Joe Biden", 45, "120/80", 75),
    ("Johnson Sakaja", 52, "130/85", 80),
    ("Constantine Wasonga", 29, "110/70", 68),
    ("Daviey Senior", 60, "140/90", 85),
    ("Mary Anne", 35, "115/75", 70)
)

# write code to extract all names
names = [p[0] for p in patients]
print(names)


