#!/usr/local/bin/python3.1
from com.nonosoft.backup.BackupPath import BackupPath, ExcludeAction, \
    IncludeAction, NullAction
from com.nonosoft.util.LogLevel import ErrorLogLevel, WarnLogLevel, InfoLogLevel, \
    DebugLogLevel
#
#
# Set priotiry of backup execution. Internally use inux nice command to set
# process priority of rdiff-backup command.
PROCESS_PRIORITY = 19
#
# Log Level...
LOG_LEVEL = InfoLogLevel()
#
#
#
# ------------------------------------------------------------------------------
# Backup...
# ------------------------------------------------------------------------------
# Path of main backup repository...
# This is a local repository.
REPOSITORY_PATH = '/media/sda4/backup/local'
#
# Path of remote repository
# Is needed a ip of backup repository host.
# By example:
# REPOSITORY_PATH = "192.168.2.20::/media/sda4/backup/skynet"
#
#
# File with url paths to backup...
BACKUP_PATHS = [
#       BackupPath('/home/adrian/development'),
#       BackupPath('/home/adrian/documents'),
#       BackupPath('/home/adrian/wallpapers'),
        BackupPath('/media/sda4/apacheWebSite'),
        BackupPath('/media/sda4/repository'),
        BackupPath('/home/elnono'),
        BackupPath('/etc'),
        BackupPath('/boot/grub'),
        BackupPath('/usr/local/sbin'),
        BackupPath('/usr/local/bin')
    ]
#
#
#
# ------------------------------------------------------------------------------
# Mail Report
# ------------------------------------------------------------------------------
# Disable send mail with report of backup...
ENABLE_MAIL_REPORT = True
#
# For send backup report to user admin...
MAIL_SERVER = 'smtp.gmail.com'
MAIL_ADDRESS = MAIL_LOGIN_USER = 'adrianmarino@gmail.com'
MAIL_LOGIN_PASSWORD = '29042902'
#
#
#
# ------------------------------------------------------------------------------
# Local Report
# ------------------------------------------------------------------------------
# Enable local report generation if ...
ENABLE_LOCAL_REPORT = False
#
# Path where generate report of backup system...
REPORT_PATH = '/home/elnono/backup.report'
#
#
#
