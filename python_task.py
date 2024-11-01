
def student_info():
    info=list(dict())
    number_of_student=int(input('Student Number:- '))
    for i in range(number_of_student):
        name=input(f'Name of student number {i+1}:- ')
        age=int(input(f'Age of student number {i+1}:- '))
        grade=float(input(f'Grade of student number {i+1}:- '))
        info.append({'name':name,'age':age,'grade':grade})

    info.sort(key=lambda x: (-x['grade'], x['age']))
    print(info)

student_info()