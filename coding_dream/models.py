#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql
import settings


def use_sql(sql):
    conn = pymysql.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DATABASE,
        charset=settings.MYSQL_CHARSET
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute(sql)
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return data
