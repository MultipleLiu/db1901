# coding:utf-8
# 文件作者： Leonard
# 创建时间：2023/3/27 9:25
'''
用python执行SQL
添加一行
'''
import pymysql


def main():
    conn = pymysql.connect(host='120.77.222.217', port=3306,
                           user='root', password='123456',
                           db='hrs', charset='utf8')
    # print(conn)  # 打得出来是连上了，打不出来报错就有问题
    try:
        with conn.cursor() as cursor:  # 上下文语法,离开上下文自动关闭
            result = cursor.execute('insert into tb_dept values (90, "销售2部","重庆")')
            if result == 1:
                print('添加成功')
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()
if __name__ == '__main__':
    main()
