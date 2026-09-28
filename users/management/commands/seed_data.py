from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        from users.models import User, StudentProfile, TeacherProfile, AlumniProfile
        from academic.models import Department, Course, Assignment, PreviousQuestion, Routine
        from library.models import Book
        from campus.models import Canteen, MenuItem, Event, Classroom
        from social.models import Post

        self.stdout.write('Seeding data...')

        # Create admin
        if not User.objects.filter(email='admin@campus.edu').exists():
            admin = User.objects.create_superuser(
                username='admin', email='admin@campus.edu',
                password='admin123', first_name='System', last_name='Admin', role='admin'
            )
            self.stdout.write(self.style.SUCCESS('Admin created: admin@campus.edu / admin123'))

        # Create departments
        dept_cse, _ = Department.objects.get_or_create(name='CSE', defaults={'building': 'Block A'})
        dept_eee, _ = Department.objects.get_or_create(name='EEE', defaults={'building': 'Block B'})
        dept_bba, _ = Department.objects.get_or_create(name='BBA', defaults={'building': 'Block C'})

        # Create teacher
        if not User.objects.filter(email='teacher@campus.edu').exists():
            t_user = User.objects.create_user(username='teacher1', email='teacher@campus.edu',
                password='teacher123', first_name='Dr. Rahim', last_name='Chowdhury', role='teacher')
            TeacherProfile.objects.create(user=t_user, teacher_id='TCH001', department='CSE', designation='Associate Professor')
            self.stdout.write(self.style.SUCCESS('Teacher: teacher@campus.edu / teacher123'))

        # Create student
        if not User.objects.filter(email='student@campus.edu').exists():
            s_user = User.objects.create_user(username='student1', email='student@campus.edu',
                password='student123', first_name='Karim', last_name='Ahmed', role='student')
            StudentProfile.objects.create(user=s_user, student_id='STU2024001', department='CSE', year=2, semester=3)
            self.stdout.write(self.style.SUCCESS('Student: student@campus.edu / student123'))

        # Create alumni
        if not User.objects.filter(email='alumni@campus.edu').exists():
            a_user = User.objects.create_user(username='alumni1', email='alumni@campus.edu',
                password='alumni123', first_name='Nafisa', last_name='Islam', role='alumni')
            AlumniProfile.objects.create(user=a_user, alumni_id='ALM2020001', graduation_year=2020,
                profession='Software Engineer', company='BRAC IT Services')
            self.stdout.write(self.style.SUCCESS('Alumni: alumni@campus.edu / alumni123'))

        # Create courses
        teacher = User.objects.filter(role='teacher').first()
        course1, _ = Course.objects.get_or_create(course_id='CSE301', defaults={
            'course_name': 'Data Structures & Algorithms', 'department': dept_cse,
            'teacher': teacher, 'credit_hours': 3.0
        })
        course2, _ = Course.objects.get_or_create(course_id='CSE401', defaults={
            'course_name': 'Database Management Systems', 'department': dept_cse,
            'teacher': teacher, 'credit_hours': 3.0
        })
        # Enroll student
        student = User.objects.filter(role='student').first()
        if student:
            course1.students.add(student)
            course2.students.add(student)

        # Create assignments
        if not Assignment.objects.exists():
            Assignment.objects.create(
                title='Lab Report 1: Linked Lists', description='Implement a doubly linked list with all operations.',
                course=course1, uploaded_by=teacher,
                due_date=timezone.now() + timedelta(days=7), max_marks=20
            )
            Assignment.objects.create(
                title='ER Diagram Assignment', description='Design an ER diagram for a hospital management system.',
                course=course2, uploaded_by=teacher,
                due_date=timezone.now() + timedelta(days=3), max_marks=30
            )

        # Create routine
        if not Routine.objects.exists():
            Routine.objects.create(course=course1, day='sunday', start_time='08:00', end_time='09:30',
                department=dept_cse, semester=3, room_number='301')
            Routine.objects.create(course=course2, day='monday', start_time='10:00', end_time='11:30',
                department=dept_cse, semester=3, room_number='205')

        # Create books
        if not Book.objects.exists():
            books_data = [
                ('Introduction to Algorithms', 'Cormen, Leiserson, Rivest', 'Computer Science', 5),
                ('Database System Concepts', 'Silberschatz & Galvin', 'Computer Science', 3),
                ('Clean Code', 'Robert C. Martin', 'Software Engineering', 4),
                ('The Pragmatic Programmer', 'Hunt & Thomas', 'Software Engineering', 2),
                ('Computer Networks', 'Andrew Tanenbaum', 'Networking', 3),
            ]
            for title, author, category, copies in books_data:
                Book.objects.create(title=title, author=author, category=category,
                    total_copies=copies, available_copies=copies)

        # Create canteen
        canteen, _ = Canteen.objects.get_or_create(name='Main Cafeteria', defaults={'location': 'Ground Floor, Student Center'})
        if not MenuItem.objects.exists():
            menu_data = [
                ('Plain Rice', 'Steam rice with dal', 35),
                ('Chicken Biryani', 'Aromatic rice with chicken', 120),
                ('Egg Sandwich', 'Toasted bread with egg & veggies', 45),
                ('Tea', 'Hot milk tea', 15),
                ('Soft Drink', 'Chilled cola or juice', 30),
                ('Khichuri', 'Lentil rice with egg', 60),
            ]
            for name, desc, price in menu_data:
                MenuItem.objects.create(canteen=canteen, name=name, description=desc, price=price)

        # Create events
        if not Event.objects.exists():
            Event.objects.create(
                event_name='Annual Tech Fest 2026', description='Showcase your tech projects and compete with peers.',
                date=timezone.now().date() + timedelta(days=14), status='upcoming', max_participants=200
            )
            Event.objects.create(
                event_name='Alumni Reunion 2026', description='Annual alumni gathering and networking event.',
                date=timezone.now().date() + timedelta(days=30), status='upcoming', max_participants=300
            )

        # Create posts
        if not Post.objects.exists():
            admin = User.objects.filter(role='admin').first()
            Post.objects.create(
                title='Welcome to the New Semester!',
                content='We wish all students a productive and successful semester. Please check your course routines and assignment schedules.',
                post_type='notice', posted_by=admin
            )
            Post.objects.create(
                title='Library Hours Extended During Exams',
                content='The library will remain open until 10 PM during the upcoming examination period.',
                post_type='news', posted_by=admin
            )

        # Create classroom
        Classroom.objects.get_or_create(room_number='301', defaults={'building': 'Block A', 'capacity': 50})

        self.stdout.write(self.style.SUCCESS('\n✅ Seed data created successfully!'))
        self.stdout.write('─' * 40)
        self.stdout.write('🔑 Test Accounts:')
        self.stdout.write('  Admin:   admin@campus.edu   / admin123')
        self.stdout.write('  Teacher: teacher@campus.edu / teacher123')
        self.stdout.write('  Student: student@campus.edu / student123')
        self.stdout.write('  Alumni:  alumni@campus.edu  / alumni123')
