# pynoobies

This is simply a challenge taken from the CSAW Quals CTF. It was originally named pybabies.
The trick is to obtain any objects instance and from its super attributes grab a hold of `object`.
 From there you can find your way back down to classes containing modules `os` or `sys`. From there you can read any file on your file system.

Here is one example solution:

``` python
print(().__class__.__bases__[0].__subclasses__()[40]('/etc/passwd').read())
```
