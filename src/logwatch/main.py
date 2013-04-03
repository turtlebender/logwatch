"""
Usage:
    logwatch [options]

Options:
    -h --help                       Show this help
    -H --host=<host>                Host to connect to [default: localhost]
    -p --port=<port>                Port to connect to [default: 6000]
    -s --source=<source>            Source of messages to tail
    -S --source-host=<source-host>  Source host of messages to tail
    -t --type=<type>                Type of log message
"""
import json
import re
import signal
import socket
import sys

from docopt import docopt
from clint.textui import colored


def field_match(pattern, field):
    """
    Does the field match the pattern
    """
    if pattern:
        return re.match(pattern, field)
    return True


def tail(host, port, source=None, source_host=None, log_type=None):
    """
    Start to tail the logs
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    def signal_handler(signal, frame):
        s.close()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        message = json.loads(s.makefile().readline())
        if field_match(source,
                message['@source']) and field_match(source_host,
                        message['@source_host']) and field_match(log_type,
                            message['@type']):
            print "[{0}]:  {1}".format(colored.blue(message['@source_host']),
                    message['@message'])


def main():
    """
    Process arguments and run
    """
    arguments = docopt(__doc__)
    tail(arguments['--host'], int(arguments['--port']),
            arguments['--source'], arguments['--source-host'],
            arguments['--type'])


if __name__ == '__main__':
    main()
