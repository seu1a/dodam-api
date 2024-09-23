def getMy(client, utils) :
    return client.request(
        utils.BASE_URL + "/night-study/my",
        "GET",
        headers = {
            "Authorization": client.accessToken
        }
    )