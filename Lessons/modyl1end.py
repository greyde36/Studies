Grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
Students=sorted({'Johnny','Bilbo','Steve','Khendrik','Aaron'})
Students={Students[0]:sum(Grades[0])/len(Grades[0]),
          Students[1]:sum(Grades[1])/len(Grades[1]),
          Students[2]:sum(Grades[2])/len(Grades[2]),
          Students[3]:sum(Grades[3])/len(Grades[3]),
          Students[4]:sum(Grades[4])/len(Grades[4])}
print(Students)