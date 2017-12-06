import os, re, time, logging

logging.basicConfig(filename='C:\\temp\\sortedpy.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

src = "C:\\src"
dest = "C:\\dest"
dest2 = "C:\\dest2"

ext = ('.mp4', '.avi', '.mkv')
exclude = []

'''
------------------
dest regex go here (Also add to list: regexlist_dest)
'''
regex0 = (r'^.*(.*?)[Ss]\d\d') # Start from the beginning of the string and end at SXX

'''
------------------
dest2 regex go here (Also add to list: regexlist_dest2)
'''
d_regex0 = (r'^.*(.*?)\b(19|20)\d{2}') # Start from the beginning of the string till the end of this date range (1900 - 2099)

regexlist_dest = [regex0]
regexlist_dest2 = [d_regex0]

def remove_empty():
    global exclude

    if exclude != []:
        #logging.debug("Clearing filename exclusion list: {}".format(exclude))
        exclude = []

    if os.listdir(root) == [] and root != src:

        logging.debug("______________Removing the following empty directory: {}".format(root))
        os.rmdir(root)
        # os.removedirs removes recursively

def regex_loop(regexlist):
    global pattern
    global gotmatch

    gotmatch = False
    for regex in regexlist:
        pattern = re.match(regex, filename)
        if pattern:
            gotmatch = True
            # print('MATCH: ' + filename)
            break

def regex_match(dest):

    foldername = (pattern.group())
    folderpath = dest + '\\' + foldername
    fullpath = folderpath + "\\" + filename

    os.makedirs(folderpath, exist_ok=True)

    if os.path.isfile(fullpath) != True:
        root_verbose = (root + '\\' + filename)
        # print('Original location: %s' % root_verbose)

        dest_verbose = (folderpath + '\\' + filename)
        # print('New location: %s' % (dest_verbose))
        try:
            os.rename((root + '\\' + filename), (folderpath + '\\' + filename))
            logging.debug(('Moving file to {}'.format(dest_verbose)))
        except WindowsError:
            time.sleep(13)

    else:
        logging.debug(('Removing {} because it already exists at the destination!'.format(filename)))
        os.remove(root + '\\' + filename)

while True:
    target = os.listdir(src)

    while not target:
        time.sleep(30)
        target = os.listdir(src)

    for root, dirs, filenames in os.walk(src):
        remove_empty()
        filenames[:] = [d for d in filenames if d not in exclude]
        #dirs[:] = [d for d in dirs if d not in excludedir]

        for filename in filenames:
            full = (root + '\\' + filename)
            now = time.time()
            ten_min_ago = now - 60 * 10  # 1800 seconds in 30 mins

            if os.path.getctime(full) < ten_min_ago:

                if filename.endswith(ext) is False or filename.endswith(ext) and os.path.getsize(full) < 50000000:

                    logging.debug('Removing file because it is not specified in the ext variable or is under 50MB: {}'.format(full))
                    os.remove(root + '\\' + filename)

                elif filename.endswith(ext):

                    regex_loop(regexlist_dest)

                    if gotmatch:
                        regex_match(dest)

                    else:
                        regex_loop(regexlist_dest2)

                        if gotmatch:
                            regex_match(dest2)

                        else:
                            exclude.append(filename)
                            logging.debug("______________No REGEX MATCH: {}".format(filename))
            else:
                exclude.append(filename)
                #print('file is not older than 30 minutes: ' + cppath)
                break
