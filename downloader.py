import pytube

url = input("Enter video url: ")

path_of_folder = "downloads/"

pytube.YouTube(url).streams.get_highest_resolution().download(path_of_folder)


