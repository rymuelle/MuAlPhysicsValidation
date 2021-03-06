import os, sys, optparse, math

def writeCfg(fname, inputNames, pwd, i, wd):
    file(fname, "w").write("""#!/bin/sh

echo $SHELL

export CAFDIR=`pwd`
cd %s

export AFSDIR=`pwd`
export IJOB=%d
export INPUTFILES='%s'

eval `scramv1 run -sh`
cp muAlAnalyzer_Data_cfg.py $CAFDIR/
cd $CAFDIR/

cmsRun muAlAnalyzer_Data_cfg.py

cp out_*root $AFSDIR
rm *root

""" % (pwd, i, inputNames))

working_dir = sys.argv[1]
file_list = sys.argv[2]
njobs = int(sys.argv[3])

print "working_dir =", working_dir
print "file_list =", file_list
print "njobs =", njobs

os.system("rm -rf %s; mkdir %s" % (working_dir, working_dir))
os.system("cp muAlAnalyzer_Data_cfg.py %s" % working_dir)

execfile(file_list)

bsubfile = ["#!/bin/sh", ""]
bsubfile.append("cd %s" % working_dir)

for i in range(njobs):
    inputNames = " ".join(fileNames[len(fileNames)*i/njobs:len(fileNames)*(i+1)/njobs])
    analyzer = "%s/analyzer%03d.sh" % (working_dir, i)
    writeCfg(analyzer, inputNames, str(os.getcwdu()), i, working_dir)
    os.system("chmod +x %s" % analyzer)
    bsubfile.append("echo %s/analyzer%03d.sh" % (working_dir, i))
    bsubfile.append("bsub -R \"type==SLC6_64\" -q cmscaf1nd -J \"analyzer%03d\" -u a@b analyzer%03d.sh" % (i,i))

bsubfile.append("cd ..")
bsubfile.append("")
file("submit.sh", "w").write("\n".join(bsubfile))
os.system("chmod +x submit.sh")

