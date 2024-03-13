from numpy import *
from pyx import *

unit.set(uscale=0.2, vscale=0.2, wscale=1, xscale=0.2)
C = canvas.canvas()

N = 10
d = 5
state = [color.grey.white, color.grey.black]

C.stroke(path.line(0, 0, 0, d))
C.stroke(path.line(0, d, d, d))
C.stroke(path.line(d, d, 0, 0))
C.stroke(path.circle(0, 0, 1), [deco.filled([state[1]])])
C.stroke(path.circle(0, d, 1), [deco.filled([state[1]])])
C.stroke(path.circle(d, d, 1), [deco.filled([state[1]])])

C.writePDFfile('fig9-13-32.pdf')


