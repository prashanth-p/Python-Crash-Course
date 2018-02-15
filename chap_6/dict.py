from collections import OrderedDict

favorite_Languages = OrderedDict()

favorite_Languages["Prashanth"] = "python"
favorite_Languages["jude"] = "c++"
favorite_Languages["mary"] = "java"
favorite_Languages["zack"] = "haskell"

for name, language in favorite_Languages.items():
    print(name.title() + "\'s favorite language is "
          + language.title())
