import pandas as pd  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, State, Region, Iso

def run():
    unesco_db = pd.read_csv('unesco/whc-sites-2018-clean.csv', index_col = False, thousands = ',')

    Site.objects.all().delete()
    Category.objects.all().delete()
    State.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    # Format
    # name, description, justification, year, longitude, latitude, area_hectares, category, state, region, iso

    for index, row in unesco_db.iterrows():
        print(row)

        c, created = Category.objects.get_or_create(name=row.category)
        s, created = State.objects.get_or_create(name=row.state)
        r, created = Region.objects.get_or_create(name=row.region)
        i, created = Iso.objects.get_or_create(name=row.iso)

        o = Site(
            name=row['name'],
            description=row.description,
            justification=row.justification,
            year=row.year, longitude=row.longitude,
            latitude=row.latitude,
            area_hectares=row.area_hectares,
            category=c,
            state=s,
            region=r,
            iso=i
            )

        o.save()