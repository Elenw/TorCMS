# -*- coding:utf-8 -*-

import config
from torcms.model.ext_tab import *
from torcms.model.ext_tab import TabApp
from torcms.model.mlabel_model import MLabel
from torcms.model.mlabel_model import MPost2Label


class MAppLabel(MLabel):
    def __init__(self):
        self.tab = TabLabel
        self.tab2 = TabApp2Label
        try:
            TabLabel.create_table()
        except:
            pass

    def get_by_slug(self, slug):
        return self.tab.get(name=slug)

    def catalog_record_number(self):
        return self.tab.select().count()

    def get_all(self):
         return self.tab.select()
    def update_count(self, sid , count):
         entry = self.tab.update(
                count=count
            ).where(self.tab.uid == sid)
         entry.execute()

    def get_all_by_count(self,  current_page_num=1):
         return self.tab.select().order_by(self.tab.count.asc()).paginate(current_page_num,config.page_num)

class MApp2Label(MPost2Label):
    def __init__(self):
        self.tab = TabApp2Label
        self.tab_label = TabLabel
        self.tab_post = TabApp
        self.mtag = MAppLabel()
        try:
            TabApp2Label.create_table()
        except:
            pass

    def query_count(self, uid):
        return self.tab.select().where(self.tab.tag == uid).count()