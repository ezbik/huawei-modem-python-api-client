import huaweisms.api.common


XML_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    "<request>"
    "<dataswitch>{enable}</dataswitch>"
    "</request>"
)

XML_TEMPLATE_MODE = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    "<request>"
    "<NetworkMode>{NetworkMode}</NetworkMode>"
    "<NetworkBand>{NetworkBand}</NetworkBand>"
    "<LTEBand>{LTEBand}</LTEBand>"
    "</request>"
)

def connect_mobile(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    return switch_mobile_on(ctx)


def disconnect_mobile(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    return switch_mobile_off(ctx)


def get_mobile_status(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    result = huaweisms.api.common.get_from_url(url, ctx)
    if result and result.get("type") == "response":
        response = result["response"]
        if response and response.get("dataswitch") == "1":
            return "CONNECTED"
        if response and response.get("dataswitch") == "0":
            return "DISCONNECTED"
    return "UNKNOWN"


def switch_mobile_off(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    data = XML_TEMPLATE.format(enable=0)
    headers = {
        "__RequestVerificationToken": ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers)


def switch_mobile_on(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    data = XML_TEMPLATE.format(enable=1)
    headers = {
        "__RequestVerificationToken": ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers)

def set_mode(ctx, NetworkMode='00', NetworkBand='3FFFFFFF', LTEBand='7FFFFFFFFFFFFFFF' ):
    data = XML_TEMPLATE_MODE.format(NetworkMode=NetworkMode, NetworkBand=NetworkBand, LTEBand=LTEBand )
    headers = {
        "__RequestVerificationToken": ctx.token,
    }
    url = "{}/dialup/mobile-dataswitch".format(ctx.api_base_url)
    #print(data)
    return huaweisms.api.common.post_to_url(url, data, ctx, additional_headers=headers)

def profiles(ctx):
    # type: (huaweisms.api.common.ApiCtx) -> ...
    url = "{}/dialup/profiles".format(ctx.api_base_url)
    return huaweisms.api.common.get_from_url(url, ctx)


