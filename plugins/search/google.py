from api import message
import urllib

async def search(message_in):
    query = message_in.body.strip()

    # Check if query is nothing
    if not query:
        return message.Message('I need a topic to search for!')

    # Normalize query
    query = urllib.parse.quote(query)

    msg = "Google search:"
    url = "https://www.google.com/#q="
    url = '{}{}'.format(url, query)

    return message.Message('{} {}'.format(msg, url))