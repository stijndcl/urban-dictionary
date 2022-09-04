import sys


__all__ = ["main"]


def main(argv=None):
    """Main function to invoke the command-line application"""
    if argv is None:
        argv = sys.argv[1:]

    print(argv)
