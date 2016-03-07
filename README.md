#Cleaner - clean up your pesky file extensions

The point of this simple tool is to clean up things that are annoying - namely anything that has extensions you don't want.

##How to use:

`python setup.py install` 

An example file:

```
from cleaner.clean import delete_all

delete_all(".",".pyc")
delete_all(".",".py~")
```
