# coding:utf-8
# 文件作者： Leonard
# 创建时间：2023/3/27 9:25
'''
用python执行SQL
更新一行
'''
import pymysql


def main():
    no = int(input('要编辑的部门编号：'))
    loc = input('部门的新地址：')
    # 1.创建连接对象
    conn = pymysql.connect(host='120.77.222.217', port=3306,
                           user='root', password='123456',
                           db='hrs', charset='utf8')
    # print(conn)  # 打得出来是连上了，打不出来报错就有问题
    try:
        # 2.获得游标对象
        with conn.cursor() as cursor:
            # 3.执行SQL得到结果
            result = cursor.execute(
                'update tb_dept set dloc=%s where dno=%s',
                (loc, no)
            )
            if result == 1:
                print('更新成功')
            # 4.操作成功执行提交
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        # 4.操作失败执行回滚
        conn.rollback()
    finally:
        # 5.关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
