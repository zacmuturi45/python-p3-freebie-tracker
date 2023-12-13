from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie

if __name__ == '__main__':

    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    dev1 = Dev(name='John Doe')
    company1 = Company(name='Techie', founding_year=2000)

    freebie1 = Freebie(item_name='T-shirt', value=20, dev=dev1, company=company1)
    freebie2 = Freebie(item_name='Stickers', value=5, dev=dev1, company=company1)


    session.query(Freebie).delete()
    session.commit()
    session.bulk_save_objects([freebie1, freebie2])
    session.commit()