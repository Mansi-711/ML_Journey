class User():
  def __init__(self,first,last,mail,phn_num):
    self.first_name = first
    self.last_name = last
    self.email = mail
    self.phone_number = phn_num
    self.login_attempt = 0

  def describe_user(self):
    print(f'The name of user is {self.first_name.title()} {self.last_name.title()} with e-mail address {self.email} and phone number {self.phone_number}')

  def greet_user(self):
    print(f'Hello {self.first_name.title()} {self.last_name.title()}')

  def increment_login_attempts(self):
    self.login_attempt += 1
    print(f'The total login attempts are {self.login_attempt}')

  def reset_login_attempt(self):
    self.login_attempt = 0
    print(f'The login attempts are reseted now {self.login_attempt}')

class Priveleges():
  def __init__(self):
    self.privilege = [ "can add post", "can delete post", "can ban user"]
  def show_privileges(self):
    print('Your privileges are: ')
    for i in self.privilege:
      print(i)
  
class Admin(User):
  def __init__(self, first, last, mail, phn_num):
    super().__init__(first, last, mail, phn_num)
    self.privelege = Priveleges()  
      
u1 = User('Albert','einstein','albert@gmail.com',904352)
u1.describe_user()
u1.greet_user()
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.reset_login_attempt()

a1 = Admin('Eric','Matthes', 'eric@gmail.com', 94335)
a1.privelege.show_privileges()

