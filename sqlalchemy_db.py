from sqlalchemy import create_engine, MetaData, Table, Column, Text, Integer

engine = create_engine('sqlite:///books.db', echo = True)
meta = MetaData()

books = Table(
    'Books', meta,
    Column('id', Integer, primary_key = True),
    Column('title', Text),
    Column('year', Integer)
)

meta.create_all(engine)

conn = engine.connect()

conn.execute(books.insert(),[
    {'title':'The Great Gatsby', 'year':1925},
    {'title':'Moby-Dick', 'year':1851},
    {'title':'1984', 'year':1949},
    {'title':'The Lord of the Rings', 'year':1954},
    {'title':'The Da Vinci Code', 'year':2003} 
])

b = books.select()
data = conn.execute(b).fetchall()

for row in data:
    print('Book name: {}'.format(row))
