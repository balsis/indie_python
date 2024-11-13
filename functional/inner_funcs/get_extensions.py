def get_extensions(file_list):

    def _get_extension(lst):
        return [i.split(".")[-1]  if "." in i else "" for i in file_list]

    return _get_extension(file_list)


print(get_extensions(["foo.txt", "bar.mp4", "python3"]))
