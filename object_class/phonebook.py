class Detector:
    def __init__(self, name, email, phone, country):
        self.name = name
        self.email = email
        self.phone = phone
        self.country = country

    def personal_information(self):
        print(f"이름: {self.name}, 이메일: {self.email}, 전화번호: {self.phone}, 사는곳: {self.country}")

class PhoneBook:
    def __init__(self):
        self.information = {}

    def add_information(self, name, email, phone, country):
        self.information[name] = Detector(name, email, phone, country)
        print(f"{name}님의 정보가 등록되었습니다.")

    def find_information(self, name):
        find_who = self.information.get(name)

        if find_who:
            find_who.personal_information()
        else:
            print(f"{find_who}는 등록되지 않은 정보입니다.")
    
    def delete_information(self, name):
        if name in self.information:
            del self.information[name]
            print(f"{name}님은 전화번호부에서 지워졌습니다.")
        else:
            print(f"{name}님은 등록되지 않은 정보입니다.")
    
    def list_all_information(self):
        if not self.information:
            print("전화번호부에 아무런 정보가 없습니다.")
        else:
            for infor in self.information.values():
                infor.personal_information()

my_phonebook = PhoneBook()

my_phonebook.add_information("Mr.kim", "kim@kim.com", "010-1234-5678", "서울")
my_phonebook.list_all_information()
my_phonebook.delete_information("Mr.kim")