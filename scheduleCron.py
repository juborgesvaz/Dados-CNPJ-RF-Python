# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 15:44:57 2022

@author: DELL
"""

from crontab import CronTab
 
my_cron = CronTab(user = 'DELL')
job = my_cron.new(command = 'C:/Users/DELL/Documents/RF RIOT/script.py')

# The job takes place once every 30 minutes
# job.minute.every(30)

# The job takes place once every 1 day
job.day.every(1)

# Clearing the restrictions of a job
# job.clear() 

my_cron.write()
    
