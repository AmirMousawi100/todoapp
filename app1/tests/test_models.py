from django.test import TestCase
from app1.models import ToDo
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class TestModelToDo(TestCase):

    @classmethod
    def setUpTestData(cls):
        date = datetime.date(1900, 12, 4)
        time = datetime.time(11, 23, 56)
        user = User(
            username = "leila100",
            password = "1234567890",
            first_name = "leila"
        )
        user.save()
        user0 = User.objects.get(username='leila100')
        todo = ToDo(
            todo_title = "todo1",
            todo_content = "test content",
            todo_date = date,
            todo_time = time,
            todo_done = False,
            todo_username = user0,
            count = 0
        )
        todo.save()
        

    def setUp(self):
        pass 

    def test_todo_title_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('todo_title').verbose_name
        self.assertEqual(field_label, "todo title") 

    def test_todo_content_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('todo_content').verbose_name
        self.assertEqual(field_label, "todo content")    

    def test_todo_date_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('todo_date').verbose_name
        self.assertEqual(field_label, "todo date") 

    def test_todo_time_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('todo_time').verbose_name
        self.assertEqual(field_label, "todo time")  

    def test_todo_done_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('todo_done').verbose_name
        self.assertEqual(field_label, "todo done")  

    def test_todo_username_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('todo_username').verbose_name
        self.assertEqual(field_label, "todo username")     

    def test_todo_count_label(self):
        todos = ToDo.objects.all()
        todo = todos[0]
        field_label = todo._meta.get_field('count').verbose_name
        self.assertEqual(field_label, "count")              

    def test_todo_title(self):
        todo = ToDo.objects.get(id=1)
        self.assertEqual(todo.todo_title, "todo1")    

    def test_todo_content(self):
         todo = ToDo.objects.get(id=1)
         self.assertEqual(todo.todo_content, "test content")

    def test_todo_date(self):
        todo = ToDo.objects.get(id=1)
        date = datetime.date(1900, 12, 4)
        self.assertEqual(todo.todo_date, date)  

    def test_todo_time(self):
        todo = ToDo.objects.get(id=1)
        time = datetime.time(11, 23, 56)
        self.assertEqual(todo.todo_time, time)   

    def test_todo_done(self):
        todo = ToDo.objects.get(id=1)
        self.assertEqual(todo.todo_done, False) 

    def test_todo_username(self):
        todo = ToDo.objects.get(id=1)
        user = User.objects.get(username="leila100")
        self.assertEqual(todo.todo_username, user.username) 

    def test_todo_count(self):
        todo = ToDo.objects.get(id=1)
        self.assertEqual(todo.count, 0)

    def test_todo_title_max_length(self):
        todo = ToDo.objects.get(id=1)  
        max_length = todo._meta.get_field('todo_title').max_length
        self.assertEqual(max_length, 300)

    def test_todo_content_max_length(self):
        todo = ToDo.objects.get(id=1)  
        max_length = todo._meta.get_field('todo_content').max_length
        self.assertEqual(max_length, 1000) 

    def test_todo_username_max_length(self):
        todo = ToDo.objects.get(id=1)  
        max_length = todo._meta.get_field('todo_username').max_length
        self.assertEqual(max_length, 100)    

    def test_todo_done_default(self):
        todo = ToDo.objects.get(id=1)  
        default = todo._meta.get_field('todo_done').default
        self.assertEqual(default, False)   

    def test_todo_count_default(self):
        todo = ToDo.objects.get(id=1)  
        default = todo._meta.get_field('count').default
        self.assertEqual(default, 0) 

    def test_todo_date_null(self):
        todo = ToDo.objects.get(id=1)  
        default = todo._meta.get_field('todo_date').null
        self.assertEqual(default, True)   

    def test_todo_time_null(self):
        todo = ToDo.objects.get(id=1)  
        default = todo._meta.get_field('todo_time').null
        self.assertEqual(default, True)             


                 

           

       