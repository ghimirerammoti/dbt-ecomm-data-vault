class Person():
    def __init__(self,personlist:list):
        self.personlist=personlist
    def filter_adults(self):
        adult_person=[ (name,age) for name,age in self.personlist if age>18]
        return Person(adult_person)
    def __str__(self):
        return "\n".join(f"Person (Name={name}, Age={age})" for name,age in self.personlist)
    def __len__(self):
        return len(self.personlist)
    def sort_by_age(self, deceding:bool):
        self.personlist=sorted(self.personlist,key=lambda x : x[1],reverse=deceding)
    def __getitem__(self,index):
        return self.personlist[index]
    def __contains__(self,person):
        return any(person==name for name,age in self.personlist)    
    
if __name__=="__main__":
    print("Put all testing here incase if you want to run this directly at test")
    print("This way it won't effect the final execution from main")
    print("if this module is called in main then it won't excute this section")
    print("This only executes only if the file is executed directly")
    people = [("Alice", 20), ("Bob", 17), ("Charlie", 19)]
    cc = Person(people)
    print(len(cc))
    print(cc)
    adults = cc.filter_adults()
    print(adults)
    cc.sort_by_age(deceding=False)
    print(cc[0])
    print("Alice" in cc)
    print("Bob" in adults) 
    print(adults)
