![Supported Python versions](https://img.shields.io/badge/python-3.6+-blue.svg?style=flat-square&logo=python)
![License](https://img.shields.io/badge/license-GNU-green.svg?style=flat-square&logo=gnu)
![](https://img.shields.io/badge/Works%20in%20Linux-purple.svg?style=flat-square&logo=debian)

# ApkVuln

```
         (        )             (       ) 
   (     )\ )  ( /(             )\ ) ( /( 
   )\   (()/(  )\())(   (    ( (()/( )\())
((((_)(  /(_))((_)\ )\  )\   )\ /(_)|(_)\ 
 )\ _ )\(_)) |_ ((_|(_)((_) ((_|_))  _((_)
 (_)_\(_) _ \| |/ /\ \ / / | | | |  | \| |
  / _ \ |  _/  ' <  \ V /| |_| | |__| .` |
 /_/ \_\|_|   _|\_\  \_/  \___/|____|_|\_|

```

With ApkVuln you will obtain the .java files of an APK and they will be analyzed in search of possible vulnerabilities in the code, for it will make use of regular expressions.

 **Note**: The accuracy of the results will depend on the regular expressions. They are customizable.

# Dependencies

To run this app you need to install [Python 3.6+](https://www.python.org/) and [apkx](https://github.com/b-mueller/apkx).

For full operation, check signature version and AndroidManifest you need to install: [apksigner](https://developer.android.com/studio/command-line/apksigner) and [aapt](https://androidaapt.com/)

# How to extend

Adding a module with our own regular expressions is very easy, just create a .py file in regex, create our class that inherits from Template, for example:

```
from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"exprexion1", r"expresion1000"]
        file_type = ["xml", "html", "js", "java", "json"] # specifies the type of files to be applied
        desc = "This is the vulnerability description"
        super(Regex, self).__init__(pattern_list, "Vulnerability Test", file_type, desc)

```

# PoC

Here is an example of the tool analyzing the vulnerable Diva apk

![image](https://user-images.githubusercontent.com/16885065/121223998-66c18c80-c888-11eb-90fb-e65ba5280913.png)

 # Author 
 
 * Josue Encinar ([@JosueEncinar](https://twitter.com/josueencinar))

# Disclaimer!

The software is designed to leave no trace in the documents we upload to a domain. The author is not responsible for any illegitimate use.
