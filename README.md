# Have You Been Pwned?


A python implementation which is used in the Computerphile episode Have You Been Pwned?, which can be viewed here: https://www.youtube.com/watch?v=hhUb5iknVJs.

The python command line tool fetches cracked passwords from the pwnedpasswords.com API and shows how many occurences have been found.

Note that a password that is entered is hashed with SHA1 and only the first 5 chars of this hash are sent to the API. This principle is called K-anonymity. Please read more about this subject here: https://en.wikipedia.org/wiki/K-anonymity.

# Requirements
- Python
- venv or virtualenv is recommanded

# Installation
- Create a virtualenv and activate it
- Run `pip install -r requirements.txt`

# Usage
- Type `python pwned.py <password>` in the commandline, where `<password>` is the password to test.

