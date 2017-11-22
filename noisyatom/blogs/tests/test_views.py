
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


from blogs.models import Post


class PostModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

    def create_post(self, title='Post new blog'):
        return Post.objects.create(title=title)

    def test_lis_views(self):
        url = reverse('blogs:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_detail_views(self):
        obj = self.create_post(title='Some new title for new test')
        response = self.client.get(obj.get_absolute_url())
        self.assertEqual(response.status_code, 200)


    def test_update_views(self):
        '''
            The reason of why we use 404 because in the  update_post I am using the if statment 
            say if not request.user.is_staff or superuser than get 404 if I change the if statment to
            if request.user.is_staff or superuser than change the 404 to 200 the same for the delete method
        '''
        obj = self.create_post(title='Some new title for new test')
        url = reverse('blogs:updated', kwargs={'slug': obj.slug})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 404)

    def test_update_blog_post_user_loged_in(self):
        '''
            Login our user, create a blog post and make sure we can get the blog post data from the page
        '''
        obj = self.create_post(title='Some new title for new test')     # This should go in the setup function
        print("***** We have the following users: {}".format(User.objects.all()))  # returns []
        login = self.client.login(username='testuser1', password='12345')


        print("***** We have logged in now and have the following users: {}".format(User.objects.all()))  # returns one user
        print("******The first index user has a login state of: {}".format(User.objects.all()[0].is_authenticated()))  # returns True


        url = reverse('blogs:updated', kwargs={'slug': obj.slug})
        print("***** We are looking up the URL: {}".format(url))
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_delete_views(self):
        obj = self.create_post(title='Some new title for new test')
        url = reverse('blogs:delete', kwargs={'slug': obj.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

