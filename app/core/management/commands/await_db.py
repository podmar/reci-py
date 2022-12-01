"""
Custom Django command to await database. 
"""
import time

from psycopg2 import OperationalError as Psycopg2OperationalError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to await database. 
    """

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OperationalError, OperationalError):
                self.stdout.write("Database unvawailable, waiting 1 second.")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Connected to Database"))
