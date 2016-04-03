import os
from pprint import pprint  # noqa

import cfg
import models


TABLE_NAMES = [
    'data_src',
    'deriv_cd',
    'food_des',
    'langdesc',
    'nut_data',
    'weight',
    'datsrcln',
    'fd_group',
    'footnote',
    'langual',
    'nutr_def',
    'src_cd',
]


def main():
    db = _setup.alchemy()
    create_tables(db)
    for table_name in TABLE_NAMES:
        process_table(db, table_name)
    return


def process_table(db, table_name):
    table = getattr(models, table_name)
    fieldnames = [c.key for c in table.c]
    filename = get_filename(table_name)
    to_insert = []
    for i, fields in enumerate(iter_file_data(filename), 1):
        values = dict(zip(fieldnames, fields))
        to_insert.append(values)
        if len(to_insert) == 10000:
            print(i, end=' ... ', flush=True)
            db.conn.execute(table.insert(), to_insert)
            to_insert = []
    if len(to_insert):
        print(i, end='')
        db.conn.execute(table.insert(), to_insert)
    print()


def iter_file_data(filename):
    print('Processing file:', filename)
    with open(filename, encoding='iso-8859-1') as f:
        for line in f:
            yield parse_line(line)


def get_filename(table_name):
    filename = '{}.txt'.format(table_name.upper())
    return os.path.join(cfg.NUTRIENTS_USDA_SOURCE, filename)


def parse_line(line):
    """
        >>> parse_line('~01001~^~Butter, salted~^^0^~~^6.38')
        ['01001', 'Butter, salted', None, Decimal('0'), '', Decimal('6.38')]
    """
    line = line.rstrip('\r\n')
    fields = line.split('^')
    #  print(line)
    return [convert_field(field) for field in fields]


def convert_field(field):
    """
        >>> convert_field('~01001~')
        '01001'
        >>> convert_field('~~')
        ''
        >>> convert_field('')
        >>> convert_field('6.38')
        Decimal('6.38')
    """
    if not field:
        return None
    if field.startswith('~') and field.endswith('~'):
        field = field[1:-1]
    return field
    #  else:
    #      if not field:
    #          field = None
    #      else:
    #          print(field)
    #          field = Decimal(field)
    #  return field


def create_tables(db):
    models.metadata.drop_all(db.engine)
    models.metadata.create_all(db.engine)


if __name__ == '__main__':
    #  import doctest
    #  print(doctest.testmod())
    main()
