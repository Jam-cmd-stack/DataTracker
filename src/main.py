import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from init_db import DataRecord

DATABASE_URL = "postgresql://user:password@db:5432/datatracker"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.command()
@click.option('--action', type=click.Choice(['add', 'view', 'update', 'delete']), help='Action to perform')
@click.option('--name', help='Name of the record')
@click.option('--date', help='Date of the record (YYYY-MM-DD)')
@click.option('--value', type=float, help='Value of the record')
@click.option('--id', type=int, help='ID of the record to update or delete')
def main(action, name, date, value, id):
    session = Session()
    if action == 'add':
        record = DataRecord(name=name, date=date, value=value)
        session.add(record)
        session.commit()
        click.echo('Record added!')
    elif action == 'view':
        records = session.query(DataRecord).all()
        for record in records:
            click.echo(f'{record.id}: {record.name}, {record.date}, {record.value}')
    elif action == 'update':
        record = session.query(DataRecord).filter_by(id=id).first()
        if record:
            record.name = name or record.name
            record.date = date or record.date
            record.value = value or record.value
            session.commit()
            click.echo('Record updated!')
        else:
            click.echo('Record not found!')
    elif action == 'delete':
        record = session.query(DataRecord).filter_by(id=id).first()
        if record:
            session.delete(record)
            session.commit()
            click.echo('Record deleted!')
        else:
            click.echo('Record not found!')

if __name__ == '__main__':
    main()