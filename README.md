Simple little tail tool for watching logs coming out of a logstash tcp
socket.

You can filter the messages (using regex) by using the -s (source),
-S (source-host) flags and -t (type) flag

Usage
----------------------------------------
    logwatch [options]

Options
----------------------------------------
    -h --help                       Show this help
    -H --host=<host>                Host to connect to [default: localhost]
    -p --port=<port>                Port to connect to [default: 6000]
    -s --source=<source>            Source of messages to tail
    -S --source-host=<source-host>  Source host of messages to tail
    -t --type=<type>                Type of log message
