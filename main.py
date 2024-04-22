import vk_api


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk)
    album_id = int(input())
    upload.photo('static/img/phot.PNG', album_id)




if __name__ == '__main__':
    main()
