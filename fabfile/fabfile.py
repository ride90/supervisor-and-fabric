from fabric.api import local
from fabric.tasks import Task


class Start(Task):
    name = 'start'

    def run(self):
        print 'Start supervisor'
        local('supervisord')


class Stop(Task):
    name = 'stop'

    def run(self):
        print 'Stop supervisor'
        local('supervisorctl shutdown')