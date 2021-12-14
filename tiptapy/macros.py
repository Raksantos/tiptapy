from html import escape
from urllib.parse import urlparse


def make_img_src(attrs):
    alt = attrs.get('alt', '').strip()
    height = attrs.get('height', '')
    width = attrs.get('width', '')
    fallback_url = attrs['src']['fallback']
    image_src = f'img src="{fallback_url}"'
    if alt:
        image_src += f' alt="{escape(alt)}"'
    if height and width:
        image_src += f'width="{width}" height="{height}"'

    return image_src


def build_link_handler(config):

    def handle_links(attrs):

        retval = None
        if attrs:
            url = attrs.get("href") or ""
            link = urlparse(url)
            if not link.netloc.endswith(config.DOMAIN):
                attrs["target"] = "_blank"
                attrs["rel"] = "noopener nofollow"
            retval = " ".join(
                f'{k}="{escape(v)}"' for k, v in attrs.items()
            )
        return retval

    return handle_links
