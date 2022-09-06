import sys
import textwrap
from dataclasses import dataclass
from http import HTTPStatus

from aiohttp import ClientSession
from dacite import from_dict

__all__ = ["Definition", "get_definitions"]


BASE_URL = "https://api.urbandictionary.com/v0/define"


@dataclass
class Definition:
    """Wrapper class for a definition returned by the API"""

    definition: str
    permalink: str
    thumbs_down: int
    thumbs_up: int
    author: str
    word: str
    example: str

    def __post_init__(self):
        """Remove hyperlinks to other definitions"""
        self.definition = self.definition.replace("[", "").replace("]", "")
        self.example = self.example.replace("[", "").replace("]", "")

    def print(self):
        """Print this definition to stdout"""
        definition = "\n\t".join(textwrap.wrap(self.definition))
        print(
            f"{self.word}\n\n\t{definition}\n\nExample:\n\t{self.example}"
            f"\n\nAuthor: {self.author}\nUpvotes: {self.thumbs_up} | Downvotes: {self.thumbs_down}"
        )


async def get_definitions(http_client: ClientSession, term: str, page: int) -> list[Definition]:
    """Make an API request to fetch the definitions for [term]

    :param http_client: aiohttp client to use for the request
    :param term: term to look up in the dictionary
    :param page: number of the page to fetch (the API returns 10 results per page)
    """
    async with http_client.get(BASE_URL, params={"term": term, "page": page}) as response:
        if response.status != HTTPStatus.OK:
            print(f"Error fetching definitions (status {response.status}).", file=sys.stderr)
            sys.exit(1)

        data = await response.json()
        return list(map(lambda _definition: from_dict(Definition, _definition), data["list"]))
