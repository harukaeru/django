from django.core.management import call_command


def call_com(apps, schema_editor):
    call_command('command', dry_run='False')
