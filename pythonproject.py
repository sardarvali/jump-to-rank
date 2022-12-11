Names = ["Abhishek","Anshul","Rain","Aman","Vivek","Shreyansh","Atul","Virat","Hardik","Krunal","Dinesh","Ravindra","Jasprit","Shami","Ritesh","Akshay","Ajay","Ranbir","Narendra","Rahul","Surya","Yogi","Karan","Satyam","Vasu"]
Marks = [65,91,91,67,43,37,55,77,39,47,79,33,32,31,36,37,44,39,80,80,61,65,78,88,97]
Marks2 = [65,91,91,67,43,37,55,77,39,47,79,33,32,31,36,37,44,39,80,80,61,65,78,88,97]
Update = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Rank = []
ask = input("do you want to update (yes/no): ")
if (ask == "yes") or (ask == "Yes"):
    name = input("Enter name of the student: ")
    if name not in Names:
        print("Please enter a valid name!!!")
    else:
        updateMarks = int(input("Enter updated marks: "))
        index1 = Names.index(name)
        prevMarks = Marks[index1]
        Marks2[index1] = updateMarks
        difference = updateMarks - prevMarks
        dict1 = dict(zip(Names,Marks2))
        for i in Marks2:
            if i == max(Marks2):
                index2 = Marks2.index(i)
        currentTopper = Names[index2]
        print("Name of the student with maximum marks after updation in marks:",currentTopper)
        prevRank = Marks.index(max(Marks))
        Marks = sorted(Marks)
        currentRank = Marks[index1]
        jump = abs(prevRank - currentRank)
        print("The jump in rank is:",jump)