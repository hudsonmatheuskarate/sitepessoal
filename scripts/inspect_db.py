import sqlite3
db=r'c:\Users\anani\OneDrive\Documentos\sitepessoal\db.sqlite3'
con=sqlite3.connect(db)
cur=con.cursor()
cur.execute('select id,title,slug from main_bibliografia')
print('BIBS:',cur.fetchall())
cur.execute('select id,bibliografia_id,block_type,text,image,youtube_url,"order" from main_bibliografiablock')
rows=cur.fetchall()
print('BLOCKS:')
for r in rows:
    print(r)
con.close()
