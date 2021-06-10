# -*-coding:utf-8-*-
# @作者：haiyu.ma
# @创建日期：2019-12-13 18:29
import psycopg2
from GC_API.tools.case_config import ReadConfig
from GC_API.tools import project_path


class DoPostgresql:
    def do_postgresql(self, query_sql):
        db_config = eval(ReadConfig.get_config(project_path.case_config_path, 'DB', 'db_config'))
        db = psycopg2.connect(**db_config)
        # 以列表嵌套字典的方式返回数据
        cursor = db.cursor()
        cursor.execute(query_sql)
        # 使用列表推到的形式简洁直观
        coloumns = [row[0] for row in cursor.description]
        result = [[str(item) for item in row] for row in cursor.fetchall()]
        dict_result = [dict(zip(coloumns, row)) for row in result]
        cursor.close()
        db.close()
        return dict_result


if __name__ == '__main__':
    res = DoPostgresql().do_postgresql('select * from cr_user;')
    # print(res)
    print(res[0])
