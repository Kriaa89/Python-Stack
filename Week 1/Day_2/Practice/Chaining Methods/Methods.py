class user:
    def __init__ (self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_cards_points = 0 
# function to display info
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Reward memeber: {self.is_rewards_member}")
        print(f"Gold card member: {self.gold_cards_points}")
        return self
    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
            return self 
        else:
            self.is_rewards_member = True
            self.gold_cards_points = 200
            return self
        return true
    def spend_points(self, amount):
        if self.gold_cards_points >= amount:
            self.gold_cards_points -= amount
        else:
            print("is not enough point to spend.")
        return self
    

user1 = user("Abdallah", "Kriaa", "abdallahkriaa0gmail.com", 21)

user2 = user("Ahmed", "Yessine", "ahmedyessine@gmail.com", 25)

user3 = user("Ahmed", "Masmoudi", "ahmedmasmoudi@gmail.com", 28)


user1.display_info().enroll().spend_points(50).display_info()

user2.enroll().spend_points(80).display_info()

user3.display_info()


