from __future__ import absolute_import
from __future__ import print_function

import sys

from argparse import ArgumentParser
from django.db import connection
from django.core.management.base import BaseCommand

from typing import Any

CLEAR_QUERY = """
DELETE FROM ONLY analytics_installationcount;
ALTER SEQUENCE analytics_installation_id_seq RESTART WITH 1;
DELETE FROM ONLY analytics_realmcount;
ALTER SEQUENCE analytics_realmcount_id_seq RESTART WITH 1;
DELETE FROM ONLY analytics_usercount;
ALTER SEQUENCE analytics_usercount_id_seq RESTART WITH 1;
DELETE FROM ONLY analytics_streamcount;
ALTER SEQUENCE analytics_streamcount_id_seq RESTART WITH 1;
DELETE FROM ONLY analytics_huddlecount
ALTER SEQUENCE analytics_huddlecount_id_seq RESTART WITH 1;
"""

class Command(BaseCommand):
    help = """Clear Analytics tables."""

    def add_arguments(self, parser):
        # type: (ArgumentParser) -> None
        parser.add_argument('--force',
                            action='store_true',
                            help="Clear analytics Tables.")

    def handle(self, *args, **options):
        # type: (*Any, **Any) -> None
        if options['force']:
            cursor = connection.cursor()
            cursor.execute(CLEAR_QUERY)
            cursor.close()
        else:
            print("Would delete all data from analytics tables (!); use --force to do so.")
            sys.exit(1)

