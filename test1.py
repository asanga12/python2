pathtozip = "Python.zip"
directory="xx"

import zipfile
zip_ref=zipfile.ZipFile(pathtozip,'r')
zip_ref.extractall(directory)
zip_ref.close()
print(zip_ref)
