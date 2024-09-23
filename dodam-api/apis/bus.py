def getValid(client, utils) :
    return client.request(
        utils.BASE_URL + "/bus",
        "GET",
        headers = {
            "Authorization": client.accessToken
        }
    )