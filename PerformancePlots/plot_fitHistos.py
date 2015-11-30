for histo in histos:
  if len( histo ) > 8:
    for h in histo[0]:
      hMean    = h.GetMean()
      hMeanErr = h.GetMeanError()
      hRms     = h.GetRMS()
      hRmsErr  = h.GetRMSError()
      hName    = h.GetName()
      hTitle   = h.GetTitle()
      print >> outFile1, hName, hTitle, "Histo Mean =", hMean, "+/-", hMeanErr, "Histo RMS =", hRms, "+/-", hRmsErr
      fitName = "fit" + h.GetName()
      if histo[8] == "gauss":
        fitGauss = ROOT.TF1( fitName,"[0]/[2]/sqrt(2.0*3.14159)*exp(-0.5*((x-[1])/[2])^2)", hMean-1.0*hRms, hMean+1.0*hRms )
        fitGauss.SetParName(0,"Norm")
        fitGauss.SetParName(1,"Mean")
        fitGauss.SetParName(2,"Sigma")
        fitGauss.SetParameter(0, h.Integral("width"))
        fitGauss.SetParameter(1, h.GetMean())
        fitGauss.SetParameter(2, h.GetRMS())
        fitGauss.SetLineColor( h.GetLineColor() )
        h.Fit(fitGauss,"QRM","same")
        fitMean    = fitGauss.GetParameter(1)
        fitMeanErr = fitGauss.GetParError(1)
        fitSigma   = fitGauss.GetParameter(2)
        fitSigma   = fitGauss.GetParError(2)
        print >> outFile1, hName, hTitle, "Fit Mean =", fitMean, "+/-", fitMeanErr, "Fit Sigma =", fitSigma, "+/-", fitSigma
