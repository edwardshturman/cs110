patients = [['Milos', 'Jones', 48, 'male', 'smoker', 210],
            ['Delia', 'Chan', 39, 'female', 'non-smoker', 170],
            ['Dan', 'Ross', 62, 'male', 'non-smoker', 200],
            ['Samantha', 'Tan', 28, 'female', 'non-smoker', 180]]

female_patients = []

for patient in patients:
    if patient[3] == 'female':
        female_patients.append(patient[1])

print(female_patients)
