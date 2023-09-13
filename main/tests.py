from django.test import TestCase, Client
# Create your tests here.

class mainTest(TestCase):
    context_key = {
        'name','amount','description','img','price','siswa','kelas'
    }
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    # mengecek apakah isi dari context sesuai dengan yang diharapkan/key context lengkap
    def test_main_context(self):
        response = Client().get('/main/')
        for key in self.context_key:
            self.assertIn(key, response.context)