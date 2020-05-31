import argparse
import textwrap
from operator import itemgetter
from itertools import groupby

from pydmtx.plugins.base import ExportPlugin


parser = argparse.ArgumentParser(add_help=False)

parser.add_argument(
    "-m",
    "--module-size",
    type=float,
    default=10,
)

parser.add_argument(
    "-w",
    "--width",
    type=float,
)

parser.add_argument(
    "-h",
    "--height",
    type=float,
)

parser.add_argument(
    "-f",
    "--foreground",
    default="black",
)

parser.add_argument(
    "-b",
    "--background",
    default="white",
)

parser.add_argument(
    "-v",
    "--viewbox",
    action="store_true",
)

default_options = {
    "module_size": 10,
    "width": None,
    "height": None,
    "foreground": "black",
    "background": "white",
    "viewbox": False,
}


class ExportSVGPlugin(ExportPlugin):
    name = "ExportSVGPlugin"
    format_type = "svg"
    parser = parser

    def __init__(self, data):
        self.data = data
        self.nrow = len(data)
        self.ncol = len(data[0])

    def format(self, **options):
        options = {**default_options, **options}

        height, width = self._get_size(options["height"], options["width"], options["module_size"])

        if options["viewbox"]:
            size = ""
        else:
            size = f'width="{width}" height="{height}" preserveAspectRatio="none"'

        points = " ".join(map(lambda t: f"{t[0]},{t[1]}", self._generate_points()))

        svg = textwrap.dedent("""\
            <?xml version="1.0" standalone="yes"?>
            <svg {size} viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
                <rect width="100%" height="100%" fill="{background}"/>
                <polyline fill="{foreground}" stroke="none" points="{points}"/>
            </svg>
        """).format(
            size=size,
            width=self.ncol,
            height=self.nrow,
            background=options["background"],
            foreground=options["foreground"],
            points=points
        )

        return bytes(svg, encoding="UTF-8")

    def help(self):
        return textwrap.dedent("""\
            todo"""
        )

    def _get_size(self, height, width, module_size):
        if height is None and width is None:
            return self.nrow * module_size, self.ncol * module_size
        elif width is None:
            return height, height * (self.ncol / self.nrow)
        elif height is None:
            return width * (self.nrow / self.ncol), width
        else:
            return height, width

    def _generate_points(self):
        def _generate_points(y, row):
            for x, module in enumerate(row):
                yield (x, y - module)
                yield (x + 1, y - module)

        def _generate_optimized_path(y, row):
            for _, group in groupby(_generate_points(y, row), key=itemgetter(1)):
                first = last = next(group)

                for last in group:
                    pass

                yield first
                yield last

        for y, row in enumerate(self.data, 1):
            yield (0, y)
            yield from _generate_optimized_path(y, row)
            yield (self.ncol, y)
            yield (0, y)
