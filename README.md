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

 **Note**: The existing regular expressions are only an **example** to see the use of the tool, I focused on the script >> you can add your regular expressions. It's very easy, just look in the regex folder. Depending on the regular expressions you will find more or less false positives.

# Dependencies

Install [Python 3.6+](https://www.python.org/) and [apkx](https://github.com/b-mueller/apkx).

# How to extend

Adding a module with our own regular expressions is very easy, just create a .py file in regex, create our class that inherits from Template, for example:

```
from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"exprexion1", r"expresion1000"]
        super(Regex, self).__init__(pattern_list, "Vulnerability Test")

```

# PoC

Below, you can see a picture of the tool running:

![Apkvuln poc](https://1.bp.blogspot.com/-egYweDB8LnE/XodCH9yKwqI/AAAAAAAABFw/6tAdC2yJcQ4Y8bjuwkzuSsy10Jq-KVKBACNcBGAsYHQ/s1600/apk_analyzer.png)

Spanish post: https://www.boomernix.com/2020/04/apkvuln-analizador-estatico-de-apks.html

 # Author 
 
 * Josue Encinar ([@josueencinar](https://twitter.com/josueencinar))
