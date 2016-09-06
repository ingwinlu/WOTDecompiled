WOTDecompiled
=============

The instructions below did not work for upgrading to 0.9.15.1.1.
A full 're-dycompyle' was needed because too much changed.
Also uncomyple6 was used instead of uncompyle2.


Upgrade
=======

To update to a new game version, first the user needs to copy their res/scripts directory from the game client to the res directory for this repository (calling it scripts_new). Then the following script can be run.
```
RESULT=`diff -r res/scripts res/scripts_new/ --exclude=*.py -s | grep identical | cut -d' ' -f4 | sed s/pyc/py/g`; 
for LINE in $RESULT; 
  do mv $(echo $LINE | sed s/_new//g) $LINE; 
done
```

This script finds all files that have not changed and copies the already decompiled python files to the new directory. From there we need to replace the current script directory with script_new. Then run the next command to decompile all of the new scripts.
```
RESULT=`git status | grep deleted | cut -d':' -f2 | cut -d' ' -f5 | sed s/py/pyc/g`; 
for LINE in $RESULT; 
  do uncompyle2 $LINE &> $(echo $LINE | sed s/pyc/py/g); 
done
```
