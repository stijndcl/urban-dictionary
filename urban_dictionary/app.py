import argparse
import sys

from aiohttp import ClientSession

from urban_dictionary.api import get_definitions

__all__ = ["main", "parse_arg"]


def parse_arg(argv: list[str]) -> str:
    """Parse the command line arguments to get the definition"""
    parser = argparse.ArgumentParser(prog="Urban Dictionary")
    parser.add_argument("term", help="The term to look up in the dictionary.", type=str)
    args = parser.parse_args(argv)
    return args.term


async def main(term: str):
    """Main command-line app"""
    async with ClientSession() as session:
        page = 1

        definitions = await get_definitions(session, term, page)

        if not definitions:
            print("No definitions found.")
            sys.exit(0)

        current_definition = 0

        definitions[current_definition].print()
