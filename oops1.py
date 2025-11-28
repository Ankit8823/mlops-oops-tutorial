#initiate a class
class employee:
    # special method /magig/dunder method -constructor
    def __init__(self):
        print("started executing attributes/data")
        self.id=123
        self.salary=50000
        self.designation="EDE"
        print("attributes /data have been initiated")
        print("object bante hi constroctor call ho jata he")
    def travel(self,designation):
        print("this travel function was called manually")
        print(f"employee is travelling to {designation}")

#create an obj/instance of the calss
sam =employee()
#printing the attributes 
#sam.travel("delhi")
print(type(sam))
