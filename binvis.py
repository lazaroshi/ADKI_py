#!/usr/bin/env python
#Adapted from Aldo Corseti's original
#binvis code, located at his github at https://github.com/cortesi

import os.path, math, string, sys
import scurve
from scurve import progress, utils, draw
from PIL import Image
from PIL import ImageDraw

class _Color:
    def __init__(self, data, block):
        self.data, self.block = data, block
        s = list(set(data))
        s.sort()
        self.symbol_map = {v : i for (i, v) in enumerate(s)}

    def __len__(self):
        return len(self.data)

    def point(self, x):
        if self.block and (self.block[0]<=x<self.block[1]):
            return self.block[2]
        else:
            return self.getPoint(x)


class ColorGradient(_Color):
    def getPoint(self, x):
        c = ord(self.data[x])/255.0
        return [
            int(255*c),
            int(255*c),
            int(255*c)
        ]


class ColorHilbert(_Color):
    def __init__(self, data, block):
        _Color.__init__(self, data, block)
        self.csource = scurve.fromSize("hilbert", 3, 256**3)
        self.step = len(self.csource)/float(len(self.symbol_map))

    def getPoint(self, x):
        c = self.symbol_map[self.data[x]]
        return self.csource.point(int(c*self.step))


class ColorClass(_Color):
    def getPoint(self, x):
        c = ord(self.data[x])
        if c == 0:
            return [0, 0, 0]
        elif c == 255:
            return [255, 255, 255]
        elif chr(c) in string.printable:
            return [55, 126, 184]
        return [228, 26, 28]


class ColorEntropy(_Color):
    def getPoint(self, x):
        e = utils.entropy(self.data, 32, x, len(self.symbol_map))
        # http://www.wolframalpha.com/input/?i=plot+%284%28x-0.5%29-4%28x-0.5%29**2%29**4+from+0.5+to+1
        def curve(v):
            f = (4*v - 4*v**2)**4
            f = max(f, 0)
            return f
        r = curve(e-0.5) if e > 0.5 else 0
        b = e**2
        return [
            int(255*r),
            0,
            int(255*b)
        ]


def drawmap_unrolled(map, size, csource, name, prog):
    prog.set_target((size**2)*4)
    map = scurve.fromSize(map, 2, size**2)
    c = Image.new("RGB", (size, size*4))
    cd = ImageDraw.Draw(c)
    step = len(csource)/float(len(map)*4)

    sofar = 0
    for quad in range(4):
        for i, p in enumerate(map):
            off = (i + (quad * size**2))
            color = csource.point(
                        int(off * step)
                    )
            x, y = tuple(p)
            cd.point(
                (x, y + (size * quad)),
                fill=tuple(color)
            )
            if not sofar%100:
                prog.tick(sofar)
            sofar += 1
    c.save(name)


def drawmap_square(map, size, csource, name, prog):
    prog.set_target((size**2))
    map = scurve.fromSize(map, 2, size**2)
    c = Image.new("RGB", map.dimensions())
    cd = ImageDraw.Draw(c)
    step = len(csource)/float(len(map))
    for i, p in enumerate(map):
        color = csource.point(int(i*step))
        cd.point(tuple(p), fill=tuple(color))
        if not i%100:
            prog.tick(i)
    c.save(name)

#main now depends on ati.py
#args is guarinteed to only be one string,
#the .mp3 file being converted
def main(options, args):
    d = file(args).read()
    base = os.path.basename(args[0])
    if "." in base:
        base, _ = base.rsplit(".", 1)
    dst = base + options.suffix + ".png"

    if os.path.exists(dst) and len(args) < 2:
        print >> sys.stderr, "Refusing to over-write '%s'. Specify explicitly if you really want to do this."%dst
        sys.exit(1)

    block = None
    if options.block:
        parts = options.block.split(":")
        if len(parts) not in [2, 3]:
            raise ValueError("Invalid block specification.")
        s, e = int(parts[0], 16), int(parts[1], 16)
        if len(parts) == 3:
            c = draw.parseColor(parts[2])
        else:
            c = [255, 0, 0]
        block = (s, e, c)

    if options.color == "class":
        csource = ColorClass(d, block)
    elif options.color == "hilbert":
        csource = ColorHilbert(d, block)
    elif options.color == "gradient":
        csource = ColorGradient(d, block)
    else:
        csource = ColorEntropy(d, block)


    if options.progress:
        print dst

    if options.quiet or options.progress:
        prog = progress.Dummy()
    else:
        prog = progress.Progress(None)


    if options.type == "unrolled":
        drawmap_unrolled(options.map, options.size, csource, dst, prog)
    elif options.type == "square":
        drawmap_square(options.map, options.size, csource, dst, prog)
    prog.clear()

    #returns saved png name to ati
    return dst 