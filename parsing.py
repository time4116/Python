import os


def video_finder(path):
    count = 0
    total = 0
    ext = ('.mp4', '.avi', '.mkv')
    GB = 1099511627775
    exclude = ['Windows', 'Riot Games', 'Program Files', 'Program Files (x86)', 'ProgramData', 'AppData', '$RECYCLE.BIN',
               'Windows10Upgrade', 'Sample']
    for root, dirs, filenames in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude]
        for filename in filenames:
            full = os.path.join(root, filename)
            if filename.endswith(ext) or os.stat(full).st_size > GB:
                count += 1
                total += os.stat(full).st_size / (1024.0 * 1024.0)
                print(root,filename)
    print('\nFiles: %s'
          '\nSizeGB: %s' % (count, total / 1024))

video_finder('C:')
