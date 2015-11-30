import os, sys, optparse, math

def writeCfg(fname, inputNames, pwd, i, wd, cfg):
    file(fname, "w").write("""#!/bin/sh

echo $SHELL

export CAFDIR=`pwd`
cd %s

export AFSDIR=`pwd`
export IJOB=%d
export INPUTFILES='%s'

eval `scramv1 run -sh`
cp %s $CAFDIR/
cd $CAFDIR/

cmsRun %s

cmsStage *root /store/group/alca_muonalign/aysen/%s/
rm *root

""" % (pwd, i, inputNames, cfg, cfg, wd))

working_dir = "refit_highpt_newGT_v1"
file_list = "SingleMuon_Run2015D_v3_v4_files.py"
njobs = 480
cfg = "refit_highpt_newGT_cfg.py"

print "working_dir =", working_dir
print "file_list =", file_list
print "njobs =", njobs
print "cfg =", cfg

os.system("rm -rf %s; mkdir %s" % (working_dir, working_dir))

execfile(file_list)

bsubfile = ["#!/bin/sh", ""]
bsubfile.append("cd %s" % working_dir)

for i in range(njobs):
    inputNames = " ".join(fileNames[len(fileNames)*i/njobs:len(fileNames)*(i+1)/njobs])
    analyzer = "%s/analyzer%03d.sh" % (working_dir, i)
    writeCfg(analyzer, inputNames, str(os.getcwdu()), i, working_dir, cfg)
    os.system("chmod +x %s" % analyzer)
    bsubfile.append("echo %s/analyzer%03d.sh" % (working_dir, i))
    bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"analyzer%03d\" -u a@b analyzer%03d.sh" % (i,i))

bsubfile.append("cd ..")
bsubfile.append("")
file("submit.sh", "w").write("\n".join(bsubfile))
os.system("chmod +x submit.sh")

