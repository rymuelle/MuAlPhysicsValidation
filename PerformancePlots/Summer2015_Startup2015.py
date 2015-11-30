execfile("plot_Start.py")
mainScriptName, ext = os.path.splitext(__file__)
execfile("plot_setArea.py")

folder = "/afs/cern.ch/work/a/aysen/public/MuAlAnalyzer/CMSSW_7_4_15_patch1/src/PhysVal/PerformancePlots/ROOT/"

maxEntries = 10000

#Color codes:  2 - red, 4 - blue, 6 - magenta, 7 - cyan, 8 - dark green
# 0 - header of canvas (first histo drawn on canvas sets the header)
# 1 - legend for the sample
# 2 - short name of the sample (used in names of plots)
# 3 - 2D array (1) color for the sample and (2) line style
# 4 - number of entries from the sample to process
# 5 - name of input file for the sample

samples = [
[ch_Data2015, "MuAl Summer 2015",    "Summer15", [ ROOT.kBlue, 24 ],
  maxEntries, folder+"SingleMuon_Run2015D_ZMu_v3_v4.root"], # 0
[ch_Data2015, "MuAl Run 2 Startup",    "StartRun2", [ ROOT.kRed, 24 ],
  maxEntries, folder+"SingleMuon_Run2015D_ZMu_v3_v4_MuAlRefit_v1.root"], # 0
]

execfile("plot_checkSamples.py")

pt_bin, pt_min, pt_max = 150, 0, 1500
 
execfile("plot_setHistos.py")

# additional histograms should be added here

execfile("plot_initHistos.py")

execfile("plot_analyzeSamples.py")

execfile("plot_fitHistos.py")
execfile("plot_fillProfiles.py")

# Don't combine more than 4 histos on one plot
combineHistos = [
  [ 0, 1 ],
]

execfile("plot_drawHistos.py")
