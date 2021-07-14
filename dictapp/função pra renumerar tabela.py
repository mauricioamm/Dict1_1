#schema = '''
#    create table S (
#        id integer primary key autoincrement not null,
#        content text not null)'''

#def init(db):
#    db_ale.execute('drop table if exists dictapp_dictclass')

connection = sqlite3.connect('db.db')
c = connection.cursor()
#c.execute('drop table dictapp_dictclass')
c.execute('create temp table temp_S as select content from dictapp_dictclass order by id')
c.execute('drop table dictapp_dictclass')
c.execute('insert into dictapp_dictclass (content) '
            '  select content from temp_S order by rowid')
c.commit()

"""
db = sqlite3.connect(':memory:')
init(db)
dump(db)
db.execute('delete from S where id in (1,3)')
db.commit()
dump(db)
renumber(db)
dump(db)
"""