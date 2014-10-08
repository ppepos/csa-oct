# easeasabc

This trick here is to look at the documentation for cmath.phase(). You will see that `cmath.phase(complex(-1.0, 0.0)) == cmath.pi`

Then you need to find how to pass negative values to `cmath.phase`. The trick lies in the fact that the values are cast
to c_int before being passed to `cmath.phase`. Therefore you can overflow the c_int with a positive python integer.

So the solution is:
```
python jail.py
challenge(0xFFFFFFFF,0)
```
