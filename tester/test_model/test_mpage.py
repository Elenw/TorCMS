# -*- coding:utf-8 -*-

from torcms.core import tools
from torcms.model.mpage import MPage
import tornado.escape


class TestWiki():
    def setup(self):
        print('setup 方法执行于本类中每条用例之前')
        self.uu = MPage()
        self.raw_count = self.uu.get_counts()
        self.page_slug = 'aaa'

    def test_insert(self):
        raw_count = self.uu.get_counts()
        post_data = {
            'title':'title',
            'id_user':'Tome',
            'cnt_md':'## adslkfjasdf\n lasdfkjsadf',
            'view_count':1,

        }
        self.uu.insert_data(post_data)
        new_count = self.uu.get_counts()

        tt = self.uu.get_by_slug(self.page_slug)

        #assert tt.title == post_data['title'][0]
        #assert tt.cnt_md == tornado.escape.xhtml_unescape(post_data['cnt_md'][0])
        #assert raw_count + 1 == new_count

    def test_insert_2(self):
        '''Wiki insert: Test invalid title'''
        post_data = {
            'title': [''],
            'id_user':'Tome',
            'cnt_md':'## adslkfjasdf\n lasdfkjsadf',
            'view_count':1,
        }
        uu = self.uu.insert_data(post_data)
        assert uu == False

        post_data = {
            'title': ['1'],
            'id_user':'Tome',
            'cnt_md':'## adslkfjasdf\n lasdfkjsadf',
            'view_count':1,
        }
        uu = self.uu.insert_data(post_data)
        assert uu == False

        post_data = {
            'title': ['天'],
            'id_user':'Tome',
            'cnt_md':'## adslkfjasdf\n lasdfkjsadf',
            'view_count':1,
        }
        uu = self.uu.insert_data(post_data)
        assert uu == False


    def test_query_all(self):
        self.uu.query_all()
        assert True

    def test_get_by_slug(self):
        self.uu.get_by_slug('aa')
        assert True


    def test_upate(self):
        assert True

    def tearDown(self):
        print ("function teardown")
        tt = self.uu.get_by_slug(self.page_slug)
        if tt:
            self.uu.delete(tt.uid)
