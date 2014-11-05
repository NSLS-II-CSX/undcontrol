TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = undcontrol
# undcontrol.dbd will be created and installed
DBD += undcontrol.dbd

# undcontrol.dbd will be made up from these files:
undcontrol_DBD += base.dbd

# Include dbd files from all support applications:
undcontrol_DBD += interp.dbd

# Add all the support libraries needed by this IOC
#undcontrol_LIBS += xxx

# undcontrol_registerRecordDeviceDriver.cpp derives from undcontrol.dbd
undcontrol_SRCS += undcontrol_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
undcontrol_SRCS_DEFAULT += undcontrolMain.cpp
undcontrol_SRCS_DEFAULT += interp.c
undcontrol_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#undcontrol_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
undcontrol_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

