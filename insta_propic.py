import os
import instaloader

def picture_download(username):
    parser = instaloader.Instaloader()

    os.chdir(os.path.join(os.path.expanduser('~'),'Downloads'))

    if os.path.isdir("Instagram Downloads"):
        os.chdir("Instagram Downloads")
        return parser.download_profile(username, profile_pic_only = TRUE)

    else:
        os.mkdir("Instagram Downloads")
        os.chdir("Instagram Downloads")
        return parser.download_profile(username, profile_pic_only = TRUE)


if __name__ == "__main__":
    user = input("Enter Insta Account: ")
    picture_download(user)
