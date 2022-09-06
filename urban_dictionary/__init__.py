import asyncio
import sys

from urban_dictionary import app

__all__ = ["main"]


def main(argv=None):
    """Main function to invoke the command-line application"""
    if argv is None:
        argv = sys.argv[1:]

    term = app.parse_arg(argv)
    asyncio.run(app.main(term))
