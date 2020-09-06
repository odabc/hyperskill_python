# put your python code here
classroom_1 = int(input())
classroom_2 = int(input())
classroom_3 = int(input())


def desks(students):
    return (students + 1) // 2


classrooms = [classroom_1, classroom_2, classroom_3]

total_desks = sum(map(desks, classrooms))
print(total_desks)
