# https://docs.python.org/3/library/csv.html
import csv

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    unesco_db = csv.reader(fhand)
    next(unesco_db)

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude, area_hectares, category, state, region, iso

    for row in unesco_db:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        try:
            ah = int(row[6])
        except:
            ah = None

        o = Site(
            name=row[0],
            description=row[1],
            justification=row[2],
            year=row[3],
            longitude=row[4],
            latitude=row[5],
            area_hectares=ah,
            category=c,
            state=s,
            region=r,
            iso=i
            )

        o.save()