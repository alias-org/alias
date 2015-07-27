import alias as al

class Dbwrapper(object):

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

        mapper(al.ArgumentationFramework, self.framework, properties={
            'argument' : relationship(al.Argument, backref='framework'),
            'arguments' : relationship(al.Argument,
                collection_class=attribute_mapped_collection('name'),
                cascade="all, delete-orphan")
        })

        mapper(al.Argument, self.argument, properties={
            'attacks' : relationship(al.Argument,
                secondary=self.attack,
                primaryjoin=self.argument.c.id==self.attack.c.attacker_id,
                secondaryjoin=self.argument.c.id==self.attack.c.target_id,
                collection_class=set)
        })

    def to_sqlite(self, af):
        try:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')

        engine = create_engine('sqlite:///sqlalchemy_example.db')
        self.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.metadata.bind = engine
        session = DBSession()
        session.add(af)
        for arg in af:
            session.add(af[arg])
        session.commit()

    def to_mysql(self, af, server, db, u, p):
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
        session.add(af)
        for arg in af:
            session.add(af[arg])
        session.commit()

    def to_postgres(self, af):
        pass