class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and 
            course in self.courses_in_progress and 
            course in lecturer.courses_attached and
            1 <= grade <= 10):
            if course not in lecturer.grades:
                lecturer.grades[course] = []
            lecturer.grades[course].append(grade)
            lecturer.calculate_average_grade()
            return True
        return False

    def calculate_average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if all_grades:
            self.average_grade = sum(all_grades) / len(all_grades)
        else:
            self.average_grade = 0
        return self.average_grade

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.calculate_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() <= other.calculate_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.calculate_average_grade() == other.calculate_average_grade()
        return NotImplemented


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0

    def calculate_average_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        if all_grades:
            self.average_grade = sum(all_grades) / len(all_grades)
        else:
            self.average_grade = 0
        return self.average_grade

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.calculate_average_grade():.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() < other.calculate_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() <= other.calculate_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.calculate_average_grade() == other.calculate_average_grade()
        return NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress and
            1 <= grade <= 10):
            if course not in student.grades:
                student.grades[course] = []
            student.grades[course].append(grade)
            student.calculate_average_grade()
            return True
        return False

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def calculate_average_student_grade(students, course):
    """
    Подсчет средней оценки студентов по курсу
    """
    all_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            all_grades.extend(student.grades[course])
    
    if all_grades:
        return sum(all_grades) / len(all_grades)
    return 0


def calculate_average_lecturer_grade(lecturers, course):
    """
    Подсчет средней оценки лекторов по курсу
    """
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            all_grades.extend(lecturer.grades[course])
    
    if all_grades:
        return sum(all_grades) / len(all_grades)
    return 0


# СОЗДАЕМ ЭКЗЕМПЛЯРЫ КЛАССОВ
print("=== СОЗДАНИЕ ЭКЗЕМПЛЯРОВ КЛАССОВ ===")

# Создаем студентов
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']

student2 = Student('Alice', 'Smith', 'female')
student2.courses_in_progress = ['Python', 'JavaScript']
student2.finished_courses = ['Основы ООП']

# Создаем лекторов
lecturer1 = Lecturer('John', 'Doe')
lecturer1.courses_attached = ['Python', 'Git']

lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.courses_attached = ['Python', 'JavaScript']

# Создаем проверяющих
reviewer1 = Reviewer('Bob', 'Johnson')
reviewer1.courses_attached = ['Python', 'Git']

reviewer2 = Reviewer('Carol', 'Williams')
reviewer2.courses_attached = ['Python', 'JavaScript']


# ТЕСТИРУЕМ МЕТОДЫ
print("\n=== ТЕСТИРОВАНИЕ МЕТОДОВ ===")

# Проверяющие выставляют оценки студентам
print("Проверяющие выставляют оценки студентам:")
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Git', 9)

reviewer2.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'JavaScript', 8)
reviewer2.rate_hw(student2, 'JavaScript', 9)
print("Оценки успешно выставлены!")

# Студенты оценивают лекторов
print("\nСтуденты оценивают лекторов:")
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 9)
student1.rate_lecture(lecturer1, 'Git', 8)

student2.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 9)

student1.rate_lecture(lecturer2, 'Python', 9)
student1.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'JavaScript', 8)
student2.rate_lecture(lecturer2, 'JavaScript', 9)
print("Лекции успешно оценены!")


# ВЫВОД ИНФОРМАЦИИ О ПЕРСОНАХ
print("\n" + "="*50)
print("ИНФОРМАЦИЯ О СТУДЕНТАХ")
print("="*50)

print("\n--- Студент 1 ---")
print(student1)

print("\n--- Студент 2 ---")
print(student2)

print("\n" + "="*50)
print("ИНФОРМАЦИЯ О ЛЕКТОРАХ")
print("="*50)

print("\n--- Лектор 1 ---")
print(lecturer1)

print("\n--- Лектор 2 ---")
print(lecturer2)

print("\n" + "="*50)
print("ИНФОРМАЦИЯ О ПРОВЕРЯЮЩИХ")
print("="*50)

print("\n--- Проверяющий 1 ---")
print(reviewer1)

print("\n--- Проверяющий 2 ---")
print(reviewer2)


# СРАВНЕНИЕ СТУДЕНТОВ И ЛЕКТОРОВ
print("\n" + "="*50)
print("СРАВНЕНИЕ СТУДЕНТОВ И ЛЕКТОРОВ")
print("="*50)

print("\n--- Сравнение студентов ---")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 <= student2: {student1 <= student2}")
print(f"student1 >= student2: {student1 >= student2}")

print("\n--- Сравнение лекторов ---")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
print(f"lecturer1 <= lecturer2: {lecturer1 <= lecturer2}")
print(f"lecturer1 >= lecturer2: {lecturer1 >= lecturer2}")


# ПОДСЧЕТ СРЕДНИХ ОЦЕНОК ПО КУРСАМ
print("\n" + "="*50)
print("ПОДСЧЕТ СРЕДНИХ ОЦЕНОК ПО КУРСАМ")
print("="*50)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

# Средние оценки студентов по курсам
python_student_avg = calculate_average_student_grade(students_list, 'Python')
git_student_avg = calculate_average_student_grade(students_list, 'Git')
js_student_avg = calculate_average_student_grade(students_list, 'JavaScript')

print(f"\nСредние оценки студентов:")
print(f"Курс 'Python': {python_student_avg:.1f}")
print(f"Курс 'Git': {git_student_avg:.1f}")
print(f"Курс 'JavaScript': {js_student_avg:.1f}")

# Средние оценки лекторов по курсам
python_lecturer_avg = calculate_average_lecturer_grade(lecturers_list, 'Python')
git_lecturer_avg = calculate_average_lecturer_grade(lecturers_list, 'Git')
js_lecturer_avg = calculate_average_lecturer_grade(lecturers_list, 'JavaScript')

print(f"\nСредние оценки лекторов:")
print(f"Курс 'Python': {python_lecturer_avg:.1f}")
print(f"Курс 'Git': {git_lecturer_avg:.1f}")
print(f"Курс 'JavaScript': {js_lecturer_avg:.1f}")

# ДЕТАЛИЗИРОВАННАЯ ИНФОРМАЦИЯ ПО ОЦЕНКАМ
print("\n" + "="*50)
print("ДЕТАЛИЗИРОВАННАЯ ИНФОРМАЦИЯ ПО ОЦЕНКАМ")
print("="*50)

print(f"\nОценки студента 1:")
for course, grades in student1.grades.items():
    print(f"  {course}: {grades}")

print(f"\nОценки студента 2:")
for course, grades in student2.grades.items():
    print(f"  {course}: {grades}")

print(f"\nОценки лектора 1:")
for course, grades in lecturer1.grades.items():
    print(f"  {course}: {grades}")

print(f"\nОценки лектора 2:")
for course, grades in lecturer2.grades.items():
    print(f"  {course}: {grades}")

print("\n" + "="*50)
print("ПОЛЕВЫЕ ИСПЫТАНИЯ ЗАВЕРШЕНЫ УСПЕШНО!")
print("="*50)
