class DogCat:
    def __init__(self,para_name, para_age, para_major, para_live): #Constructor Function (Initialize Method)
        self.name = para_name
        self.age = para_age
        self.major = para_major
        self.live = para_live
    def Information():
        print()

profile = DogCat("Nguyen Duc Hien", "21 years of age", "English Linguishtics", "Binh Thuan province")    
print("My name is ",profile.name)
print("I'm ",profile.age)
print("My major is ",profile.major)
print("I live in", profile.live)