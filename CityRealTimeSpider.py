# -*- coding: utf-8 -*-

import Spider

if __name__ == "__main__":
    obj = Spider.SpiderMain()
    obj.getCityRealTimeInfo()
    obj.con_cursor.close()
    obj.connection.commit()
    obj.connection.close()