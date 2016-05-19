# Muon Alignment Physics Validation

Checkout the physics validation code

    cmsrel CMSSW_8_0_8_patch1
    cd CMSSW_8_0_8_patch1/src/
    cmsenv
    git clone https://github.com/cms-mual/MuAlPhysicsValidation.git -b CMSSW_8_0_X

1. Refitting

1a. Change directory to MuAlRefit:

    cd MuAlPhysicsValidation/MuAlRefit

1b. Use **createJobs_newGT.py** to create a new python script.

1c. Check the output location in L21 in other options in L26-L29.

1d. Use **refit_newGT_cfg.py** to create a new python configuration file.

1e. Check the globaltag in L21 and additional conditions in L71-L87.

1f. Create and submit refit jobs:

    python createJobs_newGT.py
    source submit.sh
