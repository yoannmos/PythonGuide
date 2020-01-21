import pickle

grades = {'Alice': 89, 'Bob': 72, 'Charles': 87}
serial_grades = pickle.dumps(grades)
print(serial_grades)
received_grades = pickle.loads(serial_grades)
print(received_grades)
