import alias as al

class Dbwrapper(object):

    def __init__(self):
        try:
            from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
            from sqlalchemy.ext.declarative import declarative_base
            from sqlalchemy.orm import mapper, relationship
        except ImportError:
            raise ImportError('Interaction with SQL based databases requires SQLAlchemy')

        self.metadata = MetaData()

        self.framework = Table('framework', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String))

        self.argument = Table('argument', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('framework', Integer, ForeignKey('framework.id')))

        self.attack= Table('attack', self.metadata,
            Column('id', Integer, primary_key=True)
            Column('attacker_id', Integer, ForeignKey('argument.id'))
            Column('target_id'), Integer, ForeignKey('argument.id'))

        self.attack_association = Table('attack_association', self.metadata,
            Column('argument_id', Integer, ForeignKey('argument.id'), primary_key=True),
            Column('attack_id', Integer, ForeignKey('attack.id'), primary_key=True))

        self.labelling = Table('labelling', self.metadata,
            Column('id', Integer, primary_key=True),
            Column('name', String),
            Column('framework', Integer, ForeignKey('framework.id')))

        mapper(al.ArgumentationFramework, self.framework)
        mapper(al.Argument, self.argument)
        mapper(al.Labelling, self.labelling)

    def to_mysql(self, af):
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
        return session.query(al.ArgumentationFramework).all()

        