#!/usr/bin/env python

import MySQLdb

class DataBase:
    #建立并初始化数据库
    def __init__(self, name, conn, cur):
        self.name = name
        self.conn = conn
        self.cur = cur
        try:
            cur.execute('create database if not exists ' + name)
            conn.select_db(name)
            conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                        
    #建表
    def createTable(self, name):
        try:
            ex = self.cur.execute
            if ex('show tables') == 0:
                ex('create table ' + name + '(id int, name varchar(20), sex int, age int, info varchar(50))')
                self.conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #插入一条记录
    def insertSingle(self, name, value):
        try:
            self.cur.execute('insert into ' + name + ' values(%s,%s,%s,%s,%s)', value)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #插入多条记录
    def insertSome(self, name, values):
        try:
            self.cur.executemany('insert into ' + name + ' values(%s,%s,%s,%s,%s)', values)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #修改一条记录
    def updateSingle(self, name, value):
        try:
            self.cur.execute('update ' + name + ' set name=%s, sex=%s, age=%s, info=%s where id=%s', value)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #修改多条记录
    def updateSome(self, name, values):
        try:
            self.cur.executemany('update ' + name + ' set name=%s, sex=%s, age=%s, info=%s where id=%s', values)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #计数
    def Count(self, name):
        try:
            count = self.cur.execute('select * from ' + name)
            return count
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #查询第一条记录
    def selectFirst(self, name):
        try:
            self.cur.execute('select * from ' + name )
            result = self.cur.fetchone()
            return result
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #查询最后一条记录
    def selectLast(self, name):
        try:
            self.cur.execute('select * from' + name )
            result = self.cur.fetchone()
            return result
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #查询后面的n条记录
    def selectNext(self, name, n):
        try:
            self.cur.execute('select * from ' + name )
            results = self.cur.fetchmany(n)
            return results
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #查询所有
    def selectAll(self, name):
        try:
            self.cur.execute('select * from ' + name )
            #重置游标位置
            self.cur.scroll(0, mode='absolute')
            results = self.cur.fetchall()
            return results
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #删除一条记录
    def deleteByID(self, name, id):
        try:
            self.cur.execute('delete from ' + name + ' where id=%s', id)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    
    #删除多条记录
    def deleteSome(self, name):
        pass
    
    #删除表格
    def cancelTable(self, name):
        try:
            self.cur.execute('cancel table ' + name)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])
            
    #撤销数据库
    def cancelDB(self, name):
        try:
            self.cur.execute('cancel database ' + name)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    #关闭连接并释放资源
    def __del__(self):
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()