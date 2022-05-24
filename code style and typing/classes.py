import random

from typing import Iterator, Any, Optional, List, Union, NoReturn


class Human:
    """All information about a human"""

    elements: List[str] = []

    def __init__(self, name: Optional[str], last: Optional[str], age: int,
                 birthday: str, zodiac_sign: str,
                 hobby: str, favourite_book: str = None,
                 favourite_film: str = None) -> None:
        self.name = name
        self.last = last
        self.age = age
        self.birthday = birthday
        self.zodiac_sign = zodiac_sign
        self.favourite_book = favourite_book
        self.favourite_film = favourite_film
        self.hobby = hobby
        self.index = 0
        Human.elements.append(self.fullname)

    @property
    def breath(self) -> str:
        return "I can breath"

    @property
    def move(self) -> str:
        return "I can move"

    @property
    def eat(self) -> str:
        return "I can eat"

    @property
    def think(self) -> str:
        return "I can think"

    @property
    def monkey(self) -> str:
        return "My closest relatives are monkeys"

    @property
    def work(self) -> str:
        return "Labor made a man out of a monkey"

    @property
    def human_rights(self) -> str:
        return "My rights include the right to life and liberty," \
               "freedom from slavery and torture," \
               "freedom of opinion and expression, " \
               "the right to work and education, and many more." \
               "Everyone is entitled to these rights, without discrimination."

    @property
    def __str__(self) -> str:
        return f"{self.name} {self.last} is {self.age} years old. " \
               f"He/She was born on the {self.birthday}." \
               f"His/Her zodiac sign is {self.zodiac_sign}"

    @property
    def fullname(self) -> str:
        return f"{self.name} {self.last}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        first, last = name.split()
        self.name = first
        self.last = last

    @fullname.deleter
    def fullname(self) -> None:
        self.name = None
        self.last = None

    @property
    def book_and_film(self) -> str:
        if self.favourite_book and self.favourite_film:
            return f"My favourite book is {self.favourite_book} " \
                   f"and my favourite film is {self.favourite_film}"
        else:
            return "Lack of information"

    @book_and_film.setter
    def book_and_film(self, info: str) -> None:
        book, film = info.split(',')
        self.favourite_book = book
        self.favourite_film = film

    @book_and_film.deleter
    def book_and_film(self) -> None:
        self.favourite_book = None
        self.favourite_film = None

    def __iter__(self) -> Iterator[str]:
        self.index = 0
        return self

    def __next__(self) -> str:
        if self.index >= len(Human.elements):
            raise StopIteration('A lot of elements')
        index = self.index
        self.index += 1
        return Human.elements[index]


class Adult(Human):
    """All information about an adult"""

    num_of_times_part_in_refer = 0
    elements: List[str] = []

    def __init__(self, name: str, last: str, age: int,
                 birthday: str, zodiac_sign: str, hobby: str,
                 favourite_book: str = None, favourite_film: str = None):
        super().__init__(name, last, age, birthday,
                         zodiac_sign, hobby, favourite_book, favourite_film)
        self.index = 0
        Adult.elements = list(Adult.elements)
        Adult.elements.append(self.fullname)

    def vote(self) -> None:
        self.num_of_times_part_in_refer += 1

    @property
    def get_married(self) -> str:
        return "I can get married"

    @property
    def pay_taxes(self) -> str:
        return "I have to pay taxes"

    @property
    def referendums(self) -> str:
        return f"I voted, chose the president " \
               f"or took part in the referendums " \
               f"for {self.num_of_times_part_in_refer} times"

    def __add__(self, other) -> int:
        return self.num_of_times_part_in_refer \
               + other.num_of_times_part_in_refer

    def __next__(self) -> str:
        if self.index >= len(Adult.elements):
            raise StopIteration('A lot of elements')
        index = self.index
        self.index += 1
        return Adult.elements[index]


class Student(Adult):
    """All information about a student"""

    elements: List[str] = []

    def __init__(self, name: str, last: str, age: int, birthday: str,
                 zodiac_sign: str, hobby: str, class_school: Optional[str],
                 class_teacher: Optional[str], favourite_book: str = None,
                 favourite_film: str = None) -> None:
        super().__init__(name, last, age, birthday, zodiac_sign,
                         hobby, favourite_book, favourite_film)
        self.height = random.randint(130, 180)
        self.weight = random.randint(25, 80)
        self.class_school = class_school
        self.class_teacher = class_teacher
        self.index = 0
        Student.elements = list(Student.elements)
        Student.elements.append(self.fullname)

    @property
    def favourite_subject(self) -> str:
        if 7 < int(self.age) < 12:
            list_of_subjects = ['Math', 'English', 'Music',
                                'Ukrainian', 'Art', 'I\'m in the world']
            return f"My favourite subject is {random.choice(list_of_subjects)}"
        elif 12 < int(self.age) < 17:
            list_of_subjects = ['Math', 'English', 'Geography', 'Ukrainian',
                                'Physics', 'History',
                                'Chemistry', 'German']
            return f"My favourite subject is {random.choice(list_of_subjects)}"

    @property
    def school(self) -> str:
        return f"class {self.class_school}, teacher:{self.class_teacher}"

    @school.setter
    def school(self, addit_inf: str) -> None:
        class_school, class_teacher = addit_inf.split(',')
        self.class_school = class_school
        self.class_teacher = class_teacher

    @school.deleter
    def school(self) -> None:
        self.class_school = None
        self.class_teacher = None

    @property
    def info_for_school(self) -> str:
        return f"{self.name}'s height is {self.height} cm " \
               f"and weight is {self.weight} kg"

    @property
    def ZNO_points(self) -> str:
        zno_subjects = ['Geography', 'Physics',
                        'German', 'Chemistry', 'Biology']
        return f"""I want to have:
Ukrainian: {random.randint(170, 200)}
Math: {random.randint(160, 200)}
English: {random.randint(180, 200)}
{random.choice(zno_subjects)}: {random.randint(100, 200)}"""

    def __next__(self) -> str:
        if self.index >= len(Student.elements):
            raise StopIteration('A lot of elements')
        index = self.index
        self.index += 1
        return Student.elements[index]


class Child(Human):
    """All information about a child"""

    elements: List[str] = []

    def __init__(self, name: str, last: str, age: int,
                 birthday: str, zodiac_sign: str,
                 hobby: str, favourite_toy: str, favourite_book: str = None,
                 favourite_film: str = None) -> None:
        super().__init__(name, last, age, birthday, zodiac_sign,
                         hobby, favourite_book, favourite_film)
        if int(self.age) < 4:
            self.height = random.randint(88, 100)
            self.weight = random.randint(12, 17)
        else:
            self.height = random.randint(100, 130)
            self.weight = random.randint(17, 28)
        self.favourite_toy = favourite_toy
        self.index = 0
        Child.elements.append(self.fullname)

    @property
    def dream(self) -> str:
        list_of_dreams = ['Dancer', 'Actor', 'Teacher', 'Musician',
                          'Scientist', 'Firefighter', 'Astronaut',
                          'Veterinarian']
        return f"I want to be a {random.choice(list_of_dreams)}"

    @property
    def inform_for_kindergarten(self) -> str:
        return f"{self.name}'s height is {self.height} cm " \
               f"and weight is {self.weight} kg"


class Worker(Adult):
    """All information about a worker"""

    increase_amount = 1.1
    elements: List[str] = []

    def __init__(self, name: str, last: str, age: int,
                 birthday: str, zodiac_sign: str,
                 hobby: str, pay: str,
                 job: str, qualification: str, favourite_book=None,
                 favourite_film=None) -> None:
        super().__init__(name, last, age, birthday,
                         zodiac_sign, hobby,
                         favourite_book, favourite_film)
        self.pay = pay
        self.job = job
        self.qualification = qualification
        self.index = 0
        Worker.elements = list(Worker.elements)
        Worker.elements.append(self.fullname)

    @property
    def inc_amount(self) -> float:
        return float(self.pay) * self.increase_amount

    @property
    def holidays(self) -> str:
        months = ['January', 'February', 'March', 'April',
                  'May', 'June' 'July', 'August',
                  'September', 'October',
                  'November', 'December']
        return f"{random.randint(24, 54)} days since {random.choice(months)}"

    def __next__(self) -> str:
        if self.index >= len(Worker.elements):
            raise StopIteration
        index = self.index
        self.index += 1
        return Worker.elements[index]


class Teacher(Worker):
    """All information about a teacher"""

    elements: List[str] = []

    def __init__(self, name: str, last: str,
                 age: int, birthday: str, zodiac_sign: str,
                 hobby: str, pay: str, job: str, subject: str,
                 qualification: str, workload: str,
                 workplace: str, students: Any,
                 favourite_book: str = None,
                 favourite_film: str = None) -> None:
        super().__init__(name, last, age, birthday, zodiac_sign,
                         hobby, pay, job, qualification, favourite_book,
                         favourite_film)
        self.subject = subject
        self.workload = workload
        self.workplace = workplace
        for el in students:
            if not isinstance(el, Student):
                raise ValueError('not suitable')
        self.students = students
        self.index = 0
        Teacher.elements.append(self.fullname)

    def add_s(self, std) -> None:
        if std not in self.students:
            self.students.append(std)

    def rem_s(self, std) -> None:
        if std in self.students:
            self.students.remove(std)

    def print_s(self) -> None:
        for std in self.students:
            print(std.fullname)

    def __getitem__(self, el) -> Optional[str]:
        try:
            student = self.students[el]
            return student.fullname
        except IndexError:
            return None

    def __next__(self) -> str:
        if self.index >= len(Teacher.elements):
            raise StopIteration
        index = self.index
        self.index += 1
        return Teacher.elements[index]


class Student_Volunteer(Student, Human):
    """All information about a volunteer"""

    elements: List[str] = []

    print('Student_Volunteer.__init__() ->')

    def __init__(self, name: str, last: str, age: int,
                 birthday: str, zodiac_sign: str,
                 hobby: str, class_school: str,
                 class_teacher: str, favourite_book: str = None,
                 favourite_film: str = None) -> None:
        super().__init__(name, last, age, birthday, zodiac_sign, hobby,
                         class_school, class_teacher, favourite_book,
                         favourite_film)
        self.index = 0
        Student_Volunteer.elements.append(self.fullname)
        print('Student_Volunteer.__init__() <-')

    def __getattr__(self, attr) -> str:
        return attr.upper()

    @property
    def volunteering(self) -> str:
        return "I volunteer in my free time"

    def __next__(self) -> str:
        if self.index >= len(Student_Volunteer.elements):
            raise StopIteration
        index = self.index
        self.index += 1
        return Student_Volunteer.elements[index]


# Child
chi_1 = Child('John', 'Litovskiy', 2, '05/04/2020', 'Taurus', 'play', 'car')
chi_2 = Child('Elona', 'Salt', 4, '18/09/2018', 'Virgo', 'play', 'puzzle')

Child.elements = iter(Child.elements)
print(next(Child.elements))
print(next(Child.elements))
print(chi_1.__str__)
print(chi_2.__str__)
print(chi_2.dream)
print(chi_1.inform_for_kindergarten)
print(chi_2.inform_for_kindergarten)

# Adult
ad_1 = Adult('Olena', 'Reznich', 30, '01.10/1992',
             'Libra', 'go to the disco')
ad_2 = Adult('Yevgenii', 'Shatrov', 28, '07/05/1994',
             'Taurus', 'read books', 'Robinson Crusoe')
for i in Adult.elements:
    print(i)

Adult.elements = iter(Adult.elements)
print(next(Adult.elements))
print(next(Adult.elements))

ad_1.fullname = 'Olena Shatrov'
print(ad_1.name)
print(ad_1.last)
print(ad_1.human_rights)
ad_1.vote()
ad_1.vote()
print(ad_1.referendums)
print(ad_2.__str__)
print(ad_1 + ad_2)

# Student
std_1 = Student('Maria', 'Semenuk', 17, '17/08/2005', 'Leo',
                'ski', '11B', 'Klara Dmitrievna', 'Read and Black',
                'Dynasty')
std_2 = Student('Lena', 'Fedulina', 8, '05/03/2014',
                'Taurus', 'dance', '3B', 'Valeriia Alexandrivna')
for i in Student.elements:
    print(i)

Student.elements = iter(Student.elements)
print(next(Student.elements))
print(next(Student.elements))
print(std_1.school)
std_2.school = '3A, Yevgeniia Alexandrivna'
del std_2.school
print(std_2.class_school)
print(std_2.class_teacher)
print(std_1.ZNO_points)
print(std_2.favourite_subject)
print(std_1.favourite_book)

# Worker
w_1 = Worker('Luidmila', 'Lviv', 45, '06/12/1977', 'Gemini',
             'sing', '10000', 'social worker',
             '1 level', 'Ivanhoe', 'Ivanhoe')
for i in Worker.elements:
    print(i)

Worker.elements = iter(Worker.elements)
print(next(Worker.elements))
del w_1.book_and_film
print(w_1.favourite_film)
print(w_1.inc_amount)
print(w_1.pay_taxes)
print(w_1.holidays)

# Teacher
teach_1 = Teacher('Irina', 'Top', 33, '26/08/1989', 'Virgo', 'read', '17000',
                  'teacher', 'english', 'methodist teacher', '23', 'school 11',
                  [std_1, std_2], 'And Then There Were None')
for i in Teacher.elements:
    print(i)
Teacher.elements = iter(Teacher.elements)
print(next(Teacher.elements))
teach_1.rem_s(std_1)
teach_1.print_s()
print(teach_1.book_and_film)
print(teach_1[1])

# Student_Volunteer
std_v_1 = Student_Volunteer('Maria', 'Semenuk', 17, '17/08/2005', 'Leo',
                            'ski', '11B', 'Klara Dmitrievna',
                            'Read and Black', 'Dynasty')
for i in Student_Volunteer.elements:
    print(i)
Student_Volunteer.elements = iter(Student_Volunteer.elements)
print(next(Student_Volunteer.elements))
print(std_v_1.other_attr)
std_v_1.book_and_film = 'And Then There Were None, Ivanhoe'
print(std_v_1.favourite_book)
