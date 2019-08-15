Follow these instructions to use:

* start a nsls2 conda environment (`conda activate name_of_env`) that is either analysis or collection
* type `ipython`
* `%run -i maketable.py`
* at this point, `epics` has not been imported into the ipython session as a fail safe. When ready, you will need to `import epics`
* use the main function `set_EPUioc_table()`.  The docstring has more information on how to use it (`set_EPUioc_table??`)
* if you encounter an issue with "memory" you may need to set the maximum sized array allow for EPICS. I am not sure if `! export....` commnad will work in ipython session. you may need to exit the session to run `export EPICS_CA_MAX_ARRAY_BYTES=100000000`.  You can increase the number of zeros if need be.
* The local copy on ws3 for SIX operator is also on the undcontrol ioc1 in the python sub-directory.  The ioc is where git manages version control of these python defintions.  `scp` the local changes to the ioc and push to git on the ioc for future tracking. https://www.computerhope.com/unix/scp.htm

Example Usage:

testing w/ conversion of first harmonic data to third harmonic data without writing lookup values to the IOC table

    `set_EPUioc_table('20190813_Gap_1stH_Phase28p5.csv', Emin=600, Emax=2000, Epts=22500, third_fm_first=True)`          

writing lookup values to ioc table 6 with default setttings

    `set_EPUioc_table('20190813_Gap_1stH_Phase28p5.csv',22500, 6, True)`


