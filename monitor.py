#!/usr/bin/python3

from subprocess import run, PIPE

class Monitor:
    def __init__(self):
        pass

    # Command to get UPS details
    def apcaccess(self):
        try:
            # Run subproccess
            proc = run(['apcaccess', '-u'], stdout=PIPE, stderr=PIPE)

            if proc.returncode != 0:
                # If exit with error, raise exception
                raise Exception('Failed to run apcaccess!')
            else:
                # Return output of process
                return {
                    'stdout': proc.stdout.decode('utf-8'),
                    'stderr': proc.stderr.decode('utf-8'),
                }
        except Exception as e:
            raise e

    # Get parsed UPS details in key/value dict
    def getParsed(self):
        # Get raw details from command
        data = self.apcaccess()
        # Split output into lines
        lines = data['stdout'].strip().split('\n')

        parsed = {}
        # Parse each line
        for line in lines:
            # Split line by key/value delimiter
            parts = line.split(':')

            # Key is the first part
            key = parts[0].strip()
            # Join the rest in case the value part also had the delimiter character
            value = ':'.join(parts[1:]).strip()

            # Add key/value pair to dict
            parsed[key] = value

        return parsed

    def isOnBattery(self):
        KEY = 'STATUS'
        VALUE = 'ONBATT'

        return self.getParsed()[KEY] == VALUE

    def getTimeOnBattery(self):
        KEY = 'TONBATT'

        return self.getParsed()[KEY]
