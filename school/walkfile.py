import os
def walk_through_files(path, file_extension='.zip'):
   for (dirpath, dirnames, filenames) in os.walk(path):
      for filename in filenames:
         if filename.endswith(file_extension): 
            yield os.path.join(dirpath, filename)
for fname in walk_through_files("."):
    print(fname)