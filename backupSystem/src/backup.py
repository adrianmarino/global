#!/usr/local/bin/python3.1
from BackupHelper import BackupHelper
import sys

# ----------------------------------------------------------------
# Backup scripts
# ----------------------------------------------------------------
def showHelp():
    print('''Help:
    1) backup [options]
    2) restore path backTime [options]
        Restore path to back time.
        - path: file/Directory to restore.
        - backTime: back time to restore path.
    ''')

def showInvalidParametersMessage():
    print('Error, not exist arguments. View help for more information.')

# -----------------------------------------------------------------
# Backup functions
# ---------------------------------------------------------------
def backup(args):
    options = BackupHelper().getOptionArgs(args, 2)
    BackupHelper().generateReport(BackupHelper().backup(options))

def restore(args):
    options = BackupHelper().getOptionArgs(args, 4)
    print('Operation: ' + args[1]);
    print('BackTime: ' + args[2]);
    print('Path: ' + args[3]);
    BackupHelper().generateLocaleReport(BackupHelper().restore(args[3],args[2], options))

# -----------------------------------------------------------------
# Main point...
# -----------------------------------------------------------------
if BackupHelper().existBackupArgs(sys.argv):
    backup(sys.argv)
elif BackupHelper().existHelpArg(sys.argv):
    showHelp()
elif BackupHelper().existRestoreArgs(sys.argv):
    restore(sys.argv)
else:
    showInvalidParametersMessage()
