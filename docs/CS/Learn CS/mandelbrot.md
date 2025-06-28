---
author: Lumi
author_gh_user: BHAAA-ZLM
read_time: 3min
publish_date: 28.06.2025
---

Mandelbrot set is a very interesting set of complex numbers that satisfy a particular property. The complex numbers $c$ for which the function

$$ f_c(z) = z^2 + c $$

does not diverge into infinity when iterated starting from $z = 0$, i.e. the function value of $f_c(0), f_c(f_c(0)), ...$ remains bounded by an absolute value.

Some complex numbers are contained in this set, and some might diverge. By colouring their diverging properties, you can get a very beautiful picture!

![Julia Set](../image/JULIA_SET.jpg)

The code for plotting this graph is listed as follows. This uses a programming language called [Processing](processing.org).

```python
# Change to regions of interest
x_MIN, x_MAX = -0.78, -0.73
y_MIN, y_MAX = -0.08, -0.03

x_RANGE = x_MAX - x_MIN
y_RANGE = y_MAX - y_MIN

SCREEN_SIZE = 300
COUNT = 100

color_grid = []  # Stores colors for each pixel

def setup():
    global x_scale, y_scale, color_grid
    size(SCREEN_SIZE, SCREEN_SIZE)
    noStroke()
    colorMode(HSB, 360, 100, 100)

    x_scale = float(x_RANGE) / (width - 1)
    y_scale = float(y_RANGE) / (height - 1)

    # Precompute colors
    for x in range(width):
        row = []
        for y in range(height):
            zx = x_MIN + x * x_scale
            zy = y_MAX - y * y_scale  # Flip Y-axis so y=0 is bottom
            z = [zx, zy]
            col = mandelbrot(z, COUNT, bound=2)

            if col == COUNT:
                c = color(0)
            else:
                hue = (200 - float(col) / COUNT * 360) % 360
                c = color(hue, 100, 100)
            row.append(c)
        color_grid.append(row)

def draw():
    global color_grid
    for x in range(width):
        for y in range(height):
            fill(color_grid[x][y])
            rect(x, y, 1, 1)

    noLoop()  # Stop after one draw

def mousePressed():
    if mouseButton == LEFT:
        filename = "pattern_x[{},{}]_y[{},{}].tif".format(x_MIN, x_MAX, y_MIN, y_MAX)
        save(filename)
        print("Saved to: {}".format(sketchPath(filename)))

def mandelbrot(z, num, bound=2):
    count = 0
    z1 = z[:]
    while count <= num:
        if cMagnitude(z1) > bound:
            return count
        z1 = cAdd(cMult(z1, z1), z)
        count += 1
    return num

def cAdd(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def cMult(a, b):
    return [a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]]

def cMagnitude(a):
    return sqrt(a[0] ** 2 + a[1] ** 2)
```