import random
class Human:
    
    def __init__(self, name, last, age, birthday, zodiac_sign, hobby, favourite_book=None, favourite_film=None):
        self.name = name
        self.last = last
        self.age = age
        self.birthday = birthday
        self.zodiac_sign = zodiac_sign
        self.favourite_book = favourite_book
        self.favourite_film = favourite_film
        self.hobby = hobby

    def breath(self):
        return "I can breath"
    
    def move(self):
        return "I can move"
    
    def eat(self):
        return "I can eat"
   
    def think(self):
        return "I can think"
    
    def monkey(self):
        return "My closest relatives are monkeys"
    
    def work(self):
        return "Labor made a man out of a monkey"
        
    def human_rights(self):
        return "My rights include the right to life and liberty, freedom from slavery and torture, freedom of opinion and expression, the right to work and education, and many more. Everyone is entitled to these rights, without discrimination."
    
    def __str__(self):
        return f"{self.name} {self.last} is {self.age} years old. He/She was born on the {self.birthday}.His/Her zodiac sign is {self.zodiac_sign}"
    
    def fullname(self):
        return f"{self.name} {self.last}"
        
        
class Adult(Human):
    num_of_times_part_in_refer = 0

    def __init__(self, name, last, age, birthday, zodiac_sign, hobby, favourite_book=None, favourite_film=None):
        super().__init__(name, last, age, birthday, zodiac_sign, hobby, favourite_book, favourite_film)   
        
    def vote(self):
        self.num_of_times_part_in_refer += 1
    
    def get_married(self):
        return "I can get married"
    
    def pay_taxes(self):
        return "I have to pay taxes"
    
    def referendums(self):
        return f"I voted, chose the president or took part in the referendums for {self.num_of_times_part_in_refer} times"
    
    def __add__(self, other):
        return self.num_of_times_part_in_refer + other.num_of_times_part_in_refer
        
        
class Student(Adult):
    def __init__(self, name, last, age, birthday, zodiac_sign,hobby, class_school, class_teacher,favourite_book=None, favourite_film=None):
        super().__init__(name, last, age, birthday, zodiac_sign, hobby,favourite_book, favourite_film)
        self.height = random.randint(130,180)
        self.weight = random.randint(25,80)                
        self.class_school = class_school
        self.class_teacher = class_teacher
        
    def favourite_subject(self):
        if 7 < int(self.age) < 12:
            list_of_subjects = ['Math','English','Music','Ukrainian','Art','I\'m in the world']
            return f"My favourite subject is {random.choice(list_of_subjects)}"        
        elif 12 < int(self.age) < 17:
            list_of_subjects = ['Math','English','Geography','Ukrainian','Physics','History','Chemistry','German']
            return f"My favourite subject is {random.choice(list_of_subjects)}"        
        
    def info_for_school(self):
        return f"{self.name}'s height is {self.height} cm and weight is {self.weight} kg"
        
    def ZNO_points(self):
        zno_subjects = ['Geography','Physics','German','Chemistry', 'Biology']
        return f"""I want to have:
Ukrainian: {random.randint(170,200)}
Math: {random.randint(160,200)}
English: {random.randint(180,200)}
{random.choice(zno_subjects)}: {random.randint(100,200)}"""
        
class Child(Human):
    def __init__(self, name, last, age, birthday, zodiac_sign,hobby, favourite_toy, favourite_book=None, favourite_film=None):
        super().__init__(name, last, age, birthday, zodiac_sign, hobby, favourite_book, favourite_film)
        if int(self.age) < 4:
            self.height = random.randint(88,100)
            self.weight = random.randint(12,17) 
        else:
            self.height = random.randint(100,130)
            self.weight = random.randint(17,28)   
        self.favourite_toy = favourite_toy
        
    def dream(self):
        list_of_dreams = ['Dancer','Actor','Teacher','Musician','Scientist','Firefighter','Astronaut','Veterinarian']
        return f"I want to be a {random.choice(list_of_dreams)}"
    
    def inform_for_kindergarten(self):
        return f"{self.name}'s height is {self.height} cm and weight is {self.weight} kg"
            
            
class Worker(Adult):
    increase_amount = 1.1
    
    def __init__(self, name, last, age, birthday, zodiac_sign,hobby, pay, work, qualification, favourite_book=None, favourite_film=None):
        super().__init__(name, last, age, birthday, zodiac_sign, hobby, favourite_book, favourite_film)       
        self. pay = pay
        self.work = work 
        self.qualification = qualification
        
    def inc_amount(self):
        return float(self.pay) * self.increase_amount
    
    def holidays(self):
        months = ['January', 'February', 'March','April', 'May', 'June' 'July', 'August', 'September', 'October', 'November', 'December']
        return f"{random.randint(24,54)} days since {random.choice(months)}"

class Teacher(Worker):
    def __init__(self, name, last, age, birthday, zodiac_sign, hobby, pay, work, subject, qualification, workload, workplace, students, favourite_book=None, favourite_film=None):
        super().__init__(name, last, age, birthday, zodiac_sign, hobby, work, qualification, favourite_book, favourite_film)       
        self.pay = pay
        self.subject = subject
        self.workload = workload
        self.workplace = workplace
        self.students = students
            
    def add_s(self, std):
        if std not in self.students:
            self.students.append(std)
    
    def rem_s(self, std):
        if std in self.students:
            self.students.remove(std)      
            
    def print_s(self):
        for std in self.students:
            print(std)


class Student_Volunteer(Student, Human):
    print('Student_Volunteer.__init__() ->')
    def __init__(self, name, last, age, birthday, zodiac_sign,hobby, class_school, class_teacher,favourite_book=None, favourite_film=None):
        super().__init__(name, last, age, birthday, zodiac_sign,hobby, class_school, class_teacher,favourite_book, favourite_film)    
    
    def __getattr__(self, attr):
            return attr.upper()    
        
    def volunteering(self):
        return "I volunteer in my free time"
    print('Student_Volunteer.__init__() <-')


#Child
chi_1 = Child('John', 'Litovskiy', '2', '05/04/2020', 'Taurus', 'play', 'car')
chi_2 = Child('Elona', 'Salt', '4', '18/09/2018', 'Virgo', 'play', 'puzzle')
print(chi_1.__str__())
print(chi_2.__str__())
print(chi_2.dream())
print(chi_1.inform_for_kindergarten())
print(chi_2.inform_for_kindergarten())

#Adult
ad_1 = Adult('Olena', 'Reznich', '30', '01.10/1992', 'Libra', 'go to the disco')
ad_2 = Adult('Yevgenii', 'Shatrov', '28','07/05/1994', 'Taurus', 'read books', 'Robinson Crusoe')
print(ad_1.human_rights())
ad_1.vote()
ad_1.vote()
print(ad_1.referendums())
print(ad_2.__str__())
print(ad_1 + ad_2)

# Student 
std_1 = Student('Maria','Semenuk', '17', '17/08/2005', 'Leo', 'ski','11B', 'Klara Dmitrievna', 'Read and Black', 'Dynasty')
std_2 = Student('Lena','Fedulina', '8', '05/03/2014', 'Taurus', 'dance', '3B', 'Valeriia Alexandrivna')
print(std_1.ZNO_points())
print(std_2.favourite_subject())
print(std_1.favourite_book)
#Worker 
w_1 = Worker('Luidmila', 'Lviv', '45', '06/12/1977', 'Gemini', 'sing', '10000', 'social worker', '1 level', 'Ivanhoe','Ivanhoe')
print(w_1.inc_amount())
print(w_1.pay_taxes())
print(w_1.favourite_film)
print(w_1.holidays())

#Teacher
teach_1 = Teacher('Irina','Top','33','26/08/1989','Virgo', 'read','17000', 'teacher', 'english', 'methodist teacher', '23', 'school 11',[std_1,std_2],'And Then There Were None')
teach_1.rem_s(std_1)
teach_1.print_s()

#Student_Volunteer
std_v_1 = Student_Volunteer('Maria','Semenuk', '17', '17/08/2005', 'Leo', 'ski','11B', 'Klara Dmitrievna', 'Read and Black', 'Dynasty')
print(std_v_1.other_attr)
