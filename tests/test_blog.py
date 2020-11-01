import unittest
from app.models import Blog,User
from app import db
from flask_login import current_user


class BlogModelTest(unittest.TestCase):
    def setUp(self):
        self.user_felista = User(
            username='felista', password='felista123', email='felista@gmail.com')
        self.new_blog = Blog(
            id=1, title='Test', content='This is a test blog', user_id=self.user_felista.id)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title, 'Test')
        self.assertEquals(self.new_blog.content, 'This is a test blog')
        self.assertEquals(self.new_blog.user_id, self.user_felista.id)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all()) > 0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog = Blog.get_blog(1)
        self.assertTrue(len(got_blogs)==1)
