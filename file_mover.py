import os


def file_mover(path, dest):
    ext = ('.mp4', '.avi', '.mkv')
    exclude = ['Windows', 'Program Files', 'Program Files (x86)', 'ProgramData', 'AppData', '$RECYCLE.BIN',
               'Sample']
    for root, dirs, filenames in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude]
        for filename in filenames:
            if filename.endswith(ext):
                dir = root.split('\\')[-1]
                dest = (dest + dir)
                os.makedirs(dest, exist_ok=True)
                if os.path.isfile(dest + '\\' + filename) != True:
                    os.rename((root + '\\' + filename), (dest + '\\' + filename))
                    print(('Moving video file to %s' % filename))
                else:
                    print(('Removing %s because it already exists at the destination!' % filename))
                    os.remove(root + '\\' + filename)
