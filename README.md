<p align="center">
  <a href="https://github.com/lupaxa-developers-toolbox">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/organisations/developers-toolbox/readme-logo.png" alt="Developers Toolbox" />
  </a>
</p>

<h1 align="center">Draw Lines</h1>

Draw a coloured rule in the terminal. Put optional text on the left, in the
centre, or on the right. The fill character, padding, width, and colour are
all optional.

## Install

```bash
pip install lupaxa-draw-lines
```

Requires Python 3.10+. The only runtime dependency is `colorama`.

## Library

```python
from lupaxa.draw_lines import draw_line
```

### Solid Rule

Empty text draws one unbroken line. This one is 90 dashes.

```python
print(draw_line(width=90))
```

### Centred Text

The words sit in the middle. `fill_char=" "` uses spaces instead of dashes.

```python
print(draw_line(text="Hello, World!", position="center", fill_char=" ", width=90))
```

### Text on the Left

The words sit flush left. The default `pad` of `2` puts two dashes before them, then a space.

```python
print(draw_line(text="Hello, World!", position="left", width=90))
```

### Text on the Right

The same padding sits on the right edge, and the dashes fill in from the left.

```python
print(draw_line(text="Hello, World!", position="right", width=90))
```

### Cyan Text

Only the words are coloured. The dashes stay plain.

```python
print(draw_line(text="Hello, World!", position="right", width=90, color="cyan"))
```

### Bold Text

`bold` is a bright style with no hue of its own.

```python
print(draw_line(text="Hello, World!", position="right", width=90, color="bold"))
```

### Cyan and Bold

Join a colour and `bold` with `+`. Order can be `cyan+bold` or `bold+cyan`.

```python
print(draw_line(text="Hello, World!", position="right", width=90, color="cyan+bold"))
```

### Colour with Extra Characters

Spaces and punctuation are ignored, so this is the same call as `cyan+bold`.

```python
print(draw_line(text="Hello, World!", position="right", width=90, color="cyan   +    bold#$%"))
```

### Terminal Width

Leave `width` at its default of `-1` and the line matches the terminal, minus one column.

```python
print(draw_line(text="Hello, World!", position="center"))
```

### No Side Padding

`pad=0` drops the extra dashes beside left or right text. A single space still separates the words from the rule.

```python
print(draw_line(text="Hello, World!", position="left", pad=0, width=90))
```

### Parameters

| Parameter   | Default  | What it Does                                                                                                                     |
| ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `text`      | `""`     | Text on the line. An empty string draws one unbroken rule.                                                                       |
| `position`  | `center` | `left`, `center`, or `right`. Any other value raises `ValueError`.                                                               |
| `fill_char` | `-`      | Rule and padding character. Only the first character is used.                                                                    |
| `pad`       | `2`      | Fill characters beside left or right text. Centred text always has one space on each side. A negative value raises `ValueError`. |
| `width`     | `-1`     | Column count. `-1` uses the terminal width minus one column. `0` returns an empty string.                                        |
| `color`     | `""`     | Colour of the text. A name, `bold`, or both joined with `+`. Empty leaves the text uncoloured.                                   |

## Colour

Pass a colour name, `bold`, or both joined with `+`. Spaces and punctuation
are ignored, so `cyan + bold#$%` is the same as `cyan+bold`.

| Name      | What it Does                                                             |
| --------- | ------------------------------------------------------------------------ |
| `black`   | Black foreground.                                                        |
| `blue`    | Blue foreground.                                                         |
| `cyan`    | Cyan foreground.                                                         |
| `green`   | Green foreground.                                                        |
| `grey`    | Grey foreground.                                                         |
| `magenta` | Magenta foreground.                                                      |
| `red`     | Red foreground.                                                          |
| `white`   | White foreground.                                                        |
| `yellow`  | Yellow foreground.                                                       |
| `bold`    | Bright style. Use alone, or with a colour as `cyan+bold` or `bold+cyan`. |
| `reset`   | Clears colour and style.                                                 |

## Development

```bash
make init
make python-install-dev
make python-check
```

<a href="https://github.com/the-lupaxa-project">
    <img src="https://raw.githubusercontent.com/the-lupaxa-project/brand-assets/master/logos/components/footer-for-child-orgs.svg" alt="The Lupaxa Project Footer" width="100%" />
</a>
