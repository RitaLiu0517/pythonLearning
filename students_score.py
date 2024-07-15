def second_highest(students):
    
    grades = [s[1] for s in students]
    grades = sorted(grades, reverse=True) ## 排列grades(由大到小)
    second = grades[1]  #找出分數第二高
    print(second)
    
    
    second_high_students = [s[0] for s in students if s[1] == second]
    for student in second_high_students:
        print(student) #列出學生
    
second_highest(students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]] )
