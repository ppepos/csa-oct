# memoryleaks

The challenge starts with `.docx` file. First thing to do was to run `file` on it.

``` bash
$ file memoryleak.docx 
memoryleak.docx: bzip2 compressed data, block size = 900k
```

``` bash
$ mv memoryleaks.docx memoryleaks.tar.bz2
$ tar xfvj memoryleaks.tar.bz2
```

You then obtain another `memoryleak` file. `file` it again.

``` bash
$ file memoryleak
memoryleak: gzip compressed data, from Unix, last modified: Tue Oct  7 23:31:02 2014
```

We get another archive, untar it.

``` bash
$ mv memoryleak memoryleak.tar.gz
$ tar xf memoryleak.tar.gz
$ file memoryleak
memoryleak: Zip archive data, at least v2.0 to extract
```

Unzip this:

``` bash
$ unzip memoryleak
```

We then obtain a Firefox memory dump. We can use `strings` to find all the strings in the binary.

``` bash
$ strings firefox.mem | grep -i 'flag'
```

And we find the flag: `flag{cd69b4957f06cd818d7bf3d61980e291}`

