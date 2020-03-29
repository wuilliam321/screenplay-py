# screenplay-py
Screen Play Implementation for Automation in Python

## Requirements

 * Python 3.x
 * `virtualenv` (optional)
 * Chrome driver [download link](https://sites.google.com/a/chromium.org/chromedriver/downloads)
 * Firefox driver [download link](https://github.com/mozilla/geckodriver/releases)


### Drivers
Download the drivers and store into the given `drivers` folder

### Install dependencies

```
pip install -r requirements.txt
```

## Activate your env (optional)
Create the env:
```
python -m venv env
```

Activate the env
```
source env/bin/activate 
```

## Running All Tests

If you want to run all tests:
```
make test
```

### Chrome
```
make chrome
```

### Firefox
```
make firefox
```

### Chrome Headless
```
make chrome_headless
```

### Firefox Headless
```
make firefox_headless
```

### All
```
make all
```

### All Headless
```
make all_headless
```

## Running A Specific Test
```
make chrome case=cases/my_case_test.py
make firefox case=cases/my_case_test.py
make chrome_headless case=cases/my_case_test.py
```