def getValid(client, utils) :
    return client.request(
        utils.BASE_URL + "/bus",
        "GET",
        header = {
            "Authorization": client.accessToken
        }
    )