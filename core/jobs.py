from core.models import CronLog
import getpass


def add_entry():
    print('START')
    CronLog.objects.create(message=f'cron-job executed by {getpass.getuser()}')
    print('END')
