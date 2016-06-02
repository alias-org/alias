import alias

class DbWrapper(object):

    def __init__(self):
        try:
            from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
            from sqlalchemy.ext.declarative import declarative_base
            from sqlalchemy.orm import mapper, relationship
            from sqlalchemy.orm.collections import attribute_mapped_collection
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')

        self.metadata = MetaData()

        self.framework = Table('framework', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(250)))

        self.argument = Table('argument', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String(250)),
            Column('framework_id', Integer, ForeignKey('framework.id')))

        self.attack= Table('attack', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('attacker_id', Integer, ForeignKey('argument.id')),
            Column('target_id', Integer, ForeignKey('argument.id')))

        mapper(alias.ArgumentationFramework, self.framework, properties={
            'argument' : relationship(alias.Argument, backref='framework'),
            'arguments' : relationship(alias.Argument,
                collection_class=attribute_mapped_collection('name'),
                cascade="all, delete-orphan")
        })

        mapper(alias.Argument, self.argument, properties={
            'attacks' : relationship(alias.Argument,
                secondary=self.attack,
                primaryjoin=self.argument.c.id==self.attack.c.attacker_id,
                secondaryjoin=self.argument.c.id==self.attack.c.target_id,
                collection_class=set)
        })

    def to_sqlite(self, af, path):
        try:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
            from sqlalchemy.sql import exists
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')

        engine = create_engine('sqlite:///%s' %path)
        self.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.metadata.bind = engine
        session = DBSession()

        if session.query(exists().where(alias.ArgumentationFramework.name == af.name)).scalar():
            raise alias.DbException('Framework with name %s already exists in the database.' %af.name)
        else:
            session.add(af)
            for arg in af:
                session.add(af[arg])
            session.commit()
            print 'Writing to SQLite database successful.'

    def from_sqlite(self, af, path):
        try:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')


    def to_mysql(self, af, server='localhost:3306', db='test', u='', p=''):
        try:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker, query
            from sqlalchemy.sql import exists
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')

        address = 'mysql://%s:%s@%s/%s' % (u,p,server,db)
        engine = create_engine(address)
        self.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.metadata.bind = engine
        session = DBSession()

        if session.query(exists().where(alias.ArgumentationFramework.name == af.name)).scalar():
            raise alias.DbException('Framework with name %s already exists in the database.' %af.name)
        else:
            session.add(af)
            for arg in af:
                session.add(af[arg])
            session.commit()
            print 'Writing to MySQL database successful.'

    def from_mysql(self, af=None, server='localhost:3306', db='test', u='', p=''):
        try:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')

        address = 'mysql://%s:%s@%s/%s' % (u,p,server,db)
        engine = create_engine(address)
        self.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.metadata.bind = engine
        session = DBSession()
        res = session.query(alias.ArgumentationFramework).all()
        for f in res:
            print f.id

    def to_postgres(self):
        """
        TODO
        """

    def from_postgres(self):
        """
        TODO
        """
