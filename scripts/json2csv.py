import sys
import traceback
from shovel import CommandOptions, FileTransform


def json2csv():
    commandOptions = CommandOptions()
    try:
        args = commandOptions.parse_args()
        FileTransform.json2csv(args.source, args.target)
    except Exception as ex:
        print("failure, exception=%s" % str(ex))
        traceback.print_exc()
        commandOptions.print_usage()


if __name__ == "__main__":
    sys.exit(json2csv())
