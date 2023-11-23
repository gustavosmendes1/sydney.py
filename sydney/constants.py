USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2151.72"

CREATE_HEADERS = {
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://edgeservices.bing.com/edgesvc/shell",
    "Sec-Ch-Ua": '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",    
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": USER_AGENT,
    "X-Edge-Shopping-Flag": "0",
}

CHATHUB_HEADERS = {
    "Pragma": "no-cache",
    "Origin": "https://edgeservices.bing.com",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": USER_AGENT,
    "Cache-Control": "no-cache",
    "Connection": "Upgrade",
}

KBLOB_HEADERS = {
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "multipart/form-data",
    "Referer": "https://www.bing.com/",
    "User-Agent": USER_AGENT,
}

BUNDLE_VERSION = "1.1359.7"

BING_CREATE_CONVERSATION_URL = (
    f"https://edgeservices.bing.com/edgesvc/turing/conversation/chats?bundleVersion={BUNDLE_VERSION}"
)
BING_GET_CONVERSATIONS_URL = "https://www.bing.com/turing/conversation/chats"
BING_CHATHUB_URL = "wss://sydney.bing.com/sydney/ChatHub"
BING_KBLOB_URL = "https://www.bing.com/images/kblob"
BING_BLOB_URL = "https://www.bing.com/images/blob?bcid="

DELIMETER = "\x1e"  # Record separator character.
