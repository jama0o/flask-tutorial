from . import BaseTestClass
from ..auth.models import User
from ..models import Post


class BlogClientTestCase(BaseTestClass):

    def test_index_with_no_posts(self):
        res = self.client.get('/')
        self.assertEqual(200, res.status_code)
        self.assertIn(b'No hay entradas', res.data)


class PostModelTestCase(BaseTestClass):

    def test_title_slug(self):
        with self.app.app_context():
            admin = User.get_by_email('admin@xyz.com')
            post = Post(user_id=admin.id, title='Post de prueba', content='Lorem Ipsum')
            post.save()
            self.assertEqual('post-de-prueba', post.title_slug)

    def test_title_slug_duplicated(self):
        with self.app.app_context():
            admin = User.get_by_email('admin@xyz.com')
            post = Post(user_id=admin.id, title='Prueba', content='Lorem Ipsum')
            post.save()
            post_2 = Post(user_id=admin.id, title='Prueba', content='Lorem Ipsum Lorem Ipsum')
            post_2.save()
            self.assertEqual('prueba-1', post_2.title_slug)
            post_3 = Post(user_id=admin.id, title='Prueba', content='Lorem Ipsum Lorem Ipsum')
            post_3.save()
            self.assertEqual('prueba-2', post_3.title_slug)
            posts = Post.get_all()
            self.assertEqual(3, len(posts))

    def test_index_with_posts(self):
        with self.app.app_context():
            with self.app.app_context():
                admin = User.get_by_email('admin@xyz.com')
                post = Post(user_id=admin.id, title='Post de prueba', content='Lorem Ipsum')
                post.save()
            res = self.client.get('/')
            self.assertEqual(200, res.status_code)
            self.assertNotIn(b'No hay entradas', res.data)

    def test_redirect_to_login(self):
        res = self.client.get('/admin/')
        self.assertEqual(302, res.status_code)
        self.assertIn('login', res.location)

    def test_unauthorized_access_to_admin(self):
        self.login('guest@xyz.com', '1111')
        res = self.client.get('/admin/')
        self.assertEqual(401, res.status_code)
        self.assertIn(b'Ooops!! No tienes permisos de acceso', res.data)