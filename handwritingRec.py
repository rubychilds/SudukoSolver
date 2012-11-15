import sys
import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('Microsoft.Ink, Version=1.7.2600.2180, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Drawing import Font, Color
from System.Windows.Forms import (Form, DockStyle, Panel, TextBox, Button,
                                  SplitContainer, Orientation)
from Microsoft.Ink import InkOverlay

f = Form()
f.Text = 'InkOverlay Example'

btn = Button()
btn.Text = 'Erase'

pnl = Panel()
pnl.BackColor = Color.Khaki
overlay = InkOverlay(pnl)
overlay.Enabled = True

tb = TextBox()
tb.Font = Font('serif', 20)
tb.Multiline = True

sc = SplitContainer()
sc.SplitterWidth = 10
sc.Orientation = Orientation.Horizontal

# Layout
f.Width = 600
f.Height = 400
sc.Dock = DockStyle.Fill
btn.Dock = DockStyle.Top
tb.Dock = DockStyle.Fill
pnl.Dock = DockStyle.Fill
f.Controls.Add(sc)
sc.Panel1.Controls.Add(btn)
sc.Panel1.Controls.Add(pnl)
sc.Panel2.Controls.Add(tb)

# Event handling
def OnStroke(sender, args):
    tb.Text = overlay.Ink.Strokes.ToString()
overlay.Stroke += OnStroke

def OnClick(sender, args):
    overlay.Ink.DeleteStrokes()
    pnl.Refresh()
    tb.Text = ''
btn.Click += OnClick

f.ShowDialog()