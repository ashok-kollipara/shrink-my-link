DEST := ${HOME}/.local/bin
BNAME := shrink.py
FNAME := shrink

install: prep
	cp $(FNAME) $(DEST)/$(FNAME)

prep:
	cp $(BNAME) $(FNAME)
	chmod +x $(FNAME)

uninstall:
	rm -f $(DEST)/$(FNAME) 

clean:
	rm -f $(FNAME)
