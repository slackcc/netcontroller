from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

c = Canvas('foo.pdf', pagesize=landscape(letter))
frame1 = Frame(0.25*inch, 0.25*inch, 4*inch, 4*inch, showBoundary=1)

styles = getSampleStyleSheet()
s = "foo bar " * 100
story = [Paragraph(s, styles['Normal'])]
frame1.addFromList([story], c)

c.save()
