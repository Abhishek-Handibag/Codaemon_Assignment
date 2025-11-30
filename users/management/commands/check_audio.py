from django.core.management.base import BaseCommand
from users.models import User, AudioFile


class Command(BaseCommand):
    help = 'Check audio files status and reactivate inactive files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--activate',
            action='store_true',
            help='Activate all inactive audio files',
        )

    def handle(self, *args, **options):
        total_files = AudioFile.objects.count()
        active_files = AudioFile.objects.filter(is_active=True).count()
        inactive_files = AudioFile.objects.filter(is_active=False).count()

        self.stdout.write(self.style.SUCCESS(f'\n=== Audio Files Status ==='))
        self.stdout.write(f'Total files: {total_files}')
        self.stdout.write(self.style.SUCCESS(f'Active files: {active_files}'))
        self.stdout.write(self.style.WARNING(f'Inactive files: {inactive_files}'))

        if inactive_files > 0:
            self.stdout.write(self.style.WARNING(f'\nInactive audio files:'))
            for audio in AudioFile.objects.filter(is_active=False):
                self.stdout.write(f'  - ID: {audio.id}, Title: {audio.title}, User: {audio.user.username}')

            if options['activate']:
                AudioFile.objects.filter(is_active=False).update(is_active=True)
                self.stdout.write(self.style.SUCCESS(f'\n✓ Activated {inactive_files} audio files'))
            else:
                self.stdout.write(self.style.WARNING(f'\nRun with --activate to reactivate these files'))
