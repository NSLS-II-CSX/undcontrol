#!../../bin/linux-x86_64/undcontrol

## You may have to change undcontrol to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/undcontrol.dbd",0,0)
undcontrol_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadTemplate("${TOP}/db/interp.substitutions")
dbLoadRecords("${TOP}/db/bpms.db")
dbLoadRecords("${TOP}/db/ctrl.db")
dbLoadRecords("${TOP}/db/id.db")

system("install -m 777 -d $(TOP)/as/save") 
system("install -m 777 -d $(TOP)/as/req")

## autosave/restore machinery
save_restoreSet_Debug(0)
save_restoreSet_IncompleteSetsOk(1)
save_restoreSet_DatedBackupFiles(1)

set_savefile_path("${TOP}/as","/save")
set_requestfile_path("${TOP}/as","/req")

set_pass0_restoreFile("info_positions.sav")
set_pass1_restoreFile("info_settings.sav")

iocInit()

cd ${TOP}/as/req
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5 , "")
create_monitor_set("info_settings.req", 15 , "")

dbl > "${TOP}/records.dbl"
system("cp ${TOP}/records.dbl /cf-update/xf23ida-ioc1.undcontrol.dbl")
