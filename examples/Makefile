NB_MASTER   = Notebook-Master.ipynb

NB_EMPTY    = Notebook-Empty.ipynb
NB_TASK     = Notebook-Task.ipynb
NB_SOLUTION = Notebook-Solution.ipynb

.PHONY: all clean
all: $(NB_SOLUTION) $(NB_TASK) $(NB_EMPTY)

$(NB_TASK): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep task --remove solution -o $@
	
$(NB_SOLUTION): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep solution --remove task -o $@

$(NB_EMPTY): $(NB_MASTER) Makefile
	../nbsplit/nbsplit.py $< --keep even-empty --remove all -o $@

clean:
	rm $(NB_SOLUTION) $(NB_TASK) $(NB_EMPTY)
