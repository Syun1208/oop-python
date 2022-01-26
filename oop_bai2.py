class DogCat:
    stt = 1
    sothutu=1
    score = 100
    #pass #lệnh giữ chỗ (Thuộc tính(Attribute))
    def __init__(self,para_name, para_age, para_major, para_live): #Constructor Function (Initialize Method)
        self.name = para_name
        self.age = para_age
        self.major = para_major
        self.live = para_live
    #Nếu thêm một hàm mới, cách này gọi là Method
    #def Information(self):
        #print("Hello, this is all of my information")
        #print("My name is ",self.name)
        #print("I'm ",self.age)
        #print("My major is ",self.major)
        #print("I live in", self.live)
        self.stt = DogCat.sothutu
        DogCat.sothutu +=1

profile_1 = DogCat("Nguyen Duc Hien", "21 years of age", "English Linguishtics", "Binh Thuan province")    
profile_2 = DogCat("Pham Minh Long", "21 years of age", "Computer Engineerinh Technology", "Binh Thuan province")
profile_3 = DogCat("Pham Minh Long", "21 years of age", "Computer Engineerinh Technology", "Binh Thuan province")
#print("Number: ",DogCat.stt)
#print(DogCat.Information(profile_1))
#print("Number: ", DogCat.stt)
#print(DogCat.Information(profile_2))
print(profile_1.stt)
print(profile_2.stt)
print(profile_3.stt)
print(DogCat.sothutu)