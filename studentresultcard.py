print("STUDENT REPORT CARD")

#input for name and marks
name=(input("name:"))

print("\n Enter Marks(out of 100) :")
phy=float(input("Physics:" ))
chem=float(input("Chemistry:"))
math=float(input("Maths:"))
eng=float(input("English:"))

#calculate and display persentage
total= phy + chem + math + eng

percentage=(total/400)*100
print("percentage:",percentage ,"%")

#outputsection
print("\n ---report card---")
print("Name:",name)
print("Total marks:",total,"/400")
print("percentage:",percentage ,"%")

 
 #classification of their performance

if(total >= 350):
    print("Excellent Performance")
elif(250<= total<350):
    print("Good")
elif(200<=total<250):
    print("Average")
else:
    print("Needs Improvement")