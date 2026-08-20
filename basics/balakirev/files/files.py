paths = ['/home/user/Documents/document.txt',
         '/home/user/Pictures/image.jpg',
         '/home/user/Music/song.mp3',
         '/var/log/syslog.log',
         '/etc/apache2/apache2.conf',
         ]
try:
    with open("files.txt", mode='w', encoding='utf-8') as f:
        f.writelines(paths)
        f.seek(0)
        path = f.readline()
except FileNotFoundError:
    pass