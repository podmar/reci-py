"""
Test custom Django commands.
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.await_db.Command.check')
class CommandTests(SimpleTestCase):
    """ Testing custom Django commands. 
    """

    def test_await_db(self, patched_check):
        """Test the commnads that awaits the db when starting the app. 
        """
        patched_check.return_value = True
        call_command("await_db")

        patched_check.assert_called_once_with(database=["default"])
