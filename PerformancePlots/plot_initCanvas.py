print >> sys.stderr, "Set up canvas with header: ", canvasHeader

# execfile("tdrStyle.py")

c1 = ROOT.TCanvas("c1", "c1")
c1.SetCanvasSize(900,900)
ttext1 = ROOT.TPaveText(.05,.935,0.95,1.)
ttext1.SetFillColor(ROOT.kWhite)
ttext1.SetBorderSize(0)
ttext1.SetTextFont(42)
ttext1.SetTextSize(0.045)
ttext1.AddText(canvasHeader)
ttext1.Draw()
tpad = ROOT.TPad("pad", "pad", 0.0,0.0,1.0,0.93)
tpad.Draw()
tpad.cd()
