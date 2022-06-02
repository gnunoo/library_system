from django.test import TestCase,Client
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Post,Category

class TestView(TestCase):
    def setUp(self):
        self.client=Client()

        self.user_trump=User.objects.create_user(username='trump' ,password='somepassword')
        self.user_obama = User.objects.create_user(username='obama', password='somepassword')

        self.category_programming = Category.objects.create(name='programming', slug='programming')
        self.category_music = Category.objects.create(name='music', slug='music')

        self.post_001 == Post.objects.create(
            title='정보처리기능사',
            content='2020년 특별판',
            category=self.category_programming,

        )
        self.post_002 = Post.objects.create(
            title='자료구조',
            content='알기쉬운 자료구조',
            category=self.category_music,

        )
        self.post_003 = Post.objects.create(
            title='점프 투 파이썬 ',
            content='category가 없을 수 있죠',

        )

    def category_card_test(self, soup):
        categories_card = soup.find('div', id='categories-card')
        self.assertIn('Categories', categories_card.text)
        self.assertIn(f'{self.category_programming.name} ({self.category_programming.post_set.count()})',
                      categories_card.text)
        self.assertIn(f'{self.category_music.name} ({self.category_music.post_set.count()})', categories_card.text)
        self.assertIn(f'미분류 ', categories_card.text)

    def navar_test(self,soup):
        navbar = soup.nav
        self.assertIn('Book', navbar.text)

        home_btn=navbar.find('a',text='Home')
        self.assertEqual(home_btn.attrs['href'],'/')

        book_btn=navbar.find('a',text='Book')
        self.assertEqual(book_btn.attrs['href'],'/book/')

    def test_post_list(self):
        # 포스트가 있는 경우
        self.assertEqual(Post.objects.count(), 3)

        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.navbar_test(soup)
        self.category_card_test(soup)

        main_area = soup.find('div', id='main-area')
        self.assertNotIn('아직 게시물이 없습니다', main_area.text)

        post_001_card = main_area.find('div', id='post-1')
        self.assertIn(self.post_001.title, post_001_card.text)
        self.assertIn(self.post_001.category.name, post_001_card.text)


        post_002_card = main_area.find('div', id='post-2')
        self.assertIn(self.post_002.title, post_002_card.text)
        self.assertIn(self.post_002.category.name, post_002_card.text)


        post_003_card = main_area.find('div', id='post-3')
        self.assertIn('미분류', post_003_card.text)
        self.assertIn(self.post_003.title, post_003_card.text)


        self.assertIn(self.user_trump.username.upper(), main_area.text)
        self.assertIn(self.user_obma.username.upper(), main_area.text)

        # 포스트가 없는 경우
        Post.objects.all().delete()
        self.assertEqual(Post.objects.count(), 0)
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        main_area = soup.find('div', id='main-area')
        self.assertIn('아직 게시물이 없습니다', main_area.text)



    def post_detail(self):
        # 1.1. 포스트가 하나 있다.
        post_000 = Post.objects.create(
            title='정보처리기능사',
            content='2020년 특별판',
        )
        # 1.2. 그 포스트의 url은 '/blog/1/' 이다.
        self.assertEqual(self.post_001.get_absolute_url(), '/book/1/')

        # 2. 첫 번째 포스트의 상세 페이지 테스트
        # 2.1. 첫 번쨰 포스트의 url로 접근하면 정상적으로 작동한다.(status code:200)
        response = self.client.get(self.post_001.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.navar_test(soup)
        self.category_card_test(soup)
        # 2.3. 첫 번쨰 포스트의 제목이 웹 브라우저 탭 타이틀에 들어 있다.
        self.assertIn(self.post_001.title, soup.title.text)

        # 2.4. 첫 번쨰 포스트의 제목이 포스트 영역에 있다.
        main_area = soup.find('div', id='main-area')
        post_area = main_area.find('div', id='post-area')
        self.assertIn(self.post_001.title, post_area.text)
        self.assertIn(self.category_programming.name,post_area.text)



        # 2.6. 첫 번쨰 포스트 내용(content)이 포스트 영역에 있다.
        self.assertIn(self.post_001.content, post_area.text)

    def test_category_page(self):
        response = self.client.get(self.category_programming.get_absolute_url())
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        self.navbar_test(soup)
        self.category_card_test(soup)

        self.assertIn(self.category_programming.name, soup.h1.text)

        main_area = soup.find('div', id='main-area')
        self.assertIn(self.category_programming.name, main_area.text)
        self.assertIn(self.post_001.title, main_area.text)
        self.assertNotIn(self.post_002.title, main_area.text)
        self.assertNotIn(self.post_003.title, main_area.text)

    def test_create_post(self):
        # 로그인 하지 않으면 status coderk 200이면 안 된다!
        response = self.client.get('/book/create_post/')
        self.assertNotEqual(response.status_code, 200)

        self.client.login(username='trump',password='somepassword')

        response = self.client.get('/book/create_post/')
        self.assertEqual(response.status_code, 200)
        soup = BeautifulSoup(response.content, 'html.parser')

        self.assertEqual('Add Book - Book', soup.title.text)
        main_area = soup.find('div', id='main-area')
        self.assertIn('Create New Post', main_area.text)

        self.client.post(
            '/blog/create_post/',
            {
                'title': 'Post Form 만들기',
                'content': "Post Form 페이지를 만듭시다.",
                'tag_str': 'new tag; 한글 태그, python'

            }
        )

        last_post = Post.objects.last()
        self.assertEqual(last_post.title, "Post Form 만들기")
        self.assertEqual(last_post.author.username, 'obama')
