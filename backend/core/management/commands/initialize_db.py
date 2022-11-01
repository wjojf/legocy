from django.core.management.base import BaseCommand
from core.models import LegoSeries, LegoSet
import json


class Command(BaseCommand):

    SERIES_FILEPATH = '/home/tikhon/dev/projects/legocy/backend/static/json/lego_series.json'
    SETS_FILEPATH = '/home/tikhon/dev/projects/legocy/backend/static/json/lego_sets.json'

    def parse(self, fp:str, ct):
        try:
            _json = json.load(open(fp,encoding='utf-8'))
        except Exception:
            print('Error loading {}'.format(fp))
            return 
        
        for _inst in _json:
            print(_inst)
            if ct == LegoSet:
                try:
                    _inst['series'] = LegoSeries.objects.get(name=_inst['series'])
                except:
                    continue
                
            try:
                obj, created = ct.objects.get_or_create(
                    **_inst
                )
                obj.save()
            except Exception as e:
                print(_inst, e)


    def handle(self, *args, **options):

        for fp, ct in ((self.SERIES_FILEPATH, LegoSeries), (self.SETS_FILEPATH, LegoSet)):
            self.parse(fp, ct)