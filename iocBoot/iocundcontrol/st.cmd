#!../../bin/linux-x86_64/undcontrol

## You may have to change undcontrol to something else
## everywhere it appears in this file

< envPaths

## Register all support components
dbLoadDatabase("../../dbd/undcontrol.dbd",0,0)
undcontrol_registerRecordDeviceDriver(pdbbase) 

## Load record instances
dbLoadRecords("${TOP}/db/interp.db","Sys=XF:23ID-ID,Dev={EPU:1-RLK},N=1000000,In=Val:Gap-I,Out=Enrgy-I,DOL=SR:C23-ID:G1A{EPU:1-Ax:Gap}-Mtr.RBV")
dbLoadRecords("${TOP}/db/interp.db","Sys=XF:23ID-ID,Dev={EPU:1-FLK},N=1000000,In=Enrgy-SP,Out=Val:Gap-SP")

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

