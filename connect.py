from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('sqlite:///db.sqlite3')
metadata = MetaData(bind=engine)
table = Table('Users', metadata, autoload=True)

if 'username' in table.columns:
    print("A coluna 'settings' existe na tabela 'accounts'.")
else:
    print("A coluna 'settings' não existe na tabela 'accounts'.")