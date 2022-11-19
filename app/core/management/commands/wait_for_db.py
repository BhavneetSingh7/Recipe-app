"""
Custom Django command to fix race condition of DB
and connect to DB after DB has started.
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django custom command to wait for DB"""

    def handle(self, *args, **options):
        """Django command to wait for Database."""

        self.stdout.write('Waiting for Database....')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
