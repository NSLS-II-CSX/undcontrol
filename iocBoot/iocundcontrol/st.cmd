#!../../bin/linux-x86_64/undcontrol

## You may have to change undcontrol to something else
## everywhere it appears in this file

#< envPaths

## Register all support components
dbLoadDatabase("../../dbd/undcontrol.dbd",0,0)
undcontrol_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("../../db/undcontrol.db","user=swilkins")

iocInit()

## Start any sequence programs
#seq sncundcontrol,"user=swilkins"
