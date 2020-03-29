export PATH := $(PATH):$(PWD):$(PWD)/drivers
export PYTHONPATH := $(PWD)

ifdef case
TEST=$(case)
else
TEST=main.py
endif

export TEST

chrome:
	DRIVER=chrome python $(TEST) -v

 firefox:
	DRIVER=firefox python $(TEST) -v

chrome_headless:
	HEADLESS=True DRIVER=chrome python $(TEST) -v

firefox_headless:
	HEADLESS=True DRIVER=firefox python $(TEST) -v

all: chrome firefox
all_headless: chrome_headless firefox_headless
test: chrome_headless firefox_headless
