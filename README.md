# pydmtx-export-svg

ExportSVGPlugin is plugin for [pydmtx](https://github.com/pydmtx/pydmtx)

## Installation

```console
$ pip install pydmtx-export-svg
```

You should now see `svg` under `--format` in `$ pydmtx --help` output.

## Usage

```console
$ pydmtx "hello" --stdout --format svg -- --background yellow > output.svg
```

## Options

| Option | Description | Default value |
| :-- | :-- | :-- |
| `-m SIZE`, `--module-size SIZE` | - | `10` |
| `-w WIDTH`, `--width WIDTH` | - | auto |
| `-h HEIGHT`, `--height HEIGHT` | - | auto |
| `-f COLOR`, `--foreground COLOR` | Color of foreground. See color syntax for SVG [w3.org 🡕](https://www.w3.org/TR/SVGColor12/#Color_syntax) | `black` |
| `-b COLOR`, `--background COLOR` | Color of background. | `white` |
| `-v`, `--viewbox` | - | false |

## License

[MIT](LICENSE)
