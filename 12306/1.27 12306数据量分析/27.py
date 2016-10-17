# -*- coding: utf-8 -*-
import pymysql.cursors

if __name__ == '__main__':

    conn = None
    conn = pymysql.connect(host = 'localhost',
                                port = 3306,
                                user = '12306',
                                passwd = '12306',
                                db = '12306-train',
                                charset = 'utf8')

    print("open mysql succ")

    select = "select * from train_infos"
#    insert = "update books set `ip`={0}, `pv`={1} where `url` = '{2}'"

    schedules = {}
    with conn.cursor() as cursor:
        cursor.execute(select)
        count = 0
        for results in cursor.fetchall():
            if results[0] not in schedules:
                schedules[results[0]] = {results[1]:results[2]}
            else:
                schedules[results[0]][results[1]] = results[2]

    print len(schedules)

    routes = {}
    sum = 0
    for key in schedules:
        route = schedules[key]

        seq = sorted(route)
        len1 = len(seq)
        sum += len1 * (len1 - 1) / 2
        for i in range(0, len1):
            if route[seq[i]] not in routes:
                tmp = set()
                routes[route[seq[i]]] = tmp
            else:
                tmp = routes[route[seq[i]]]
            for j in range(i + 1, len1):
                tmp.add(route[seq[j]])

    print sum
    sum = 0
    for route in routes:
        print route.encode("utf-8")
        for s in routes[route]:
            print s.encode("utf-8"),
        print ""
        sum += len(route)
        
    print sum



# vim: set ts=4 sw=4 sts=4 tw=100 et:
