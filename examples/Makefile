NB_MASTER   = Notebook-Master.ipynb

NB_EMPTY    = Notebook-Empty.ipynb
NB_TASK     = Notebook-Task.ipynb
NB_SOLUTION = Notebook-Solution.ipynb
NB_NOKEEP   = Notebook-No-Keep.ipynb
NB_NOREMOVE = Notebook-No-Remove.ipynb

ALL_NB = $(NB_SOLUTION) $(NB_TASK) $(NB_EMPTY) $(NB_NOKEEP) $(NB_NOREMOVE)

.PHONY: all clean
all: $(ALL_NB)

$(NB_TASK): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep task --remove solution -o $@
	
$(NB_SOLUTION): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep solution --remove task -o $@

$(NB_EMPTY): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep even-empty --remove all -o $@

$(NB_NOKEEP): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --remove solution -o $@

$(NB_NOREMOVE): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep task -o $@

clean:
	rm $(ALL_NB)
