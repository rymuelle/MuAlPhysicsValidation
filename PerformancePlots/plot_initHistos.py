print >> sys.stderr, "Initilize histograms"

iSample = -1

for sample in samples:
  iSample = iSample + 1
  
  label     = sample[2]
  color     = sample[3][0]
  
  iHisto = -1
  for histo in histos:
    iHisto = iHisto + 1
    histo_label  = histo[1]
    sample_label = samples[ iSample ][ 2 ]
    histo_name = "h_%s_%s" % ( histo_label, sample_label )
    histo[0].append( ROOT.TH1F(histo_name, histo[2], histo[5], histo[6], histo[7]) )
    histo[0][iSample].SetLineColor(color)
    histo[0][iSample].SetNdivisions(505, "X")
    histo[0][iSample].SetXTitle(histo[3])
    histo[0][iSample].SetYTitle(histo[4])

