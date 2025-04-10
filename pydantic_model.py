
from pydantic import BaseModel
from typing import Optional, List


class AdData(BaseModel):
    Post_owner: str
    Link: str
    Ad_title: str
    Ad_text: str
    Direct_links: list
    Small_links: list
    Ad_position: int




# Usage example:
# ad = AdData.create_ad(
#     post_owner="John Doe",
#     link="https://example.com",
#     title="Sample Ad",
#     text="This is a sample ad text",
#     direct_links=["https://link1.com", "https://link2.com"],
#     small_links=["https://small1.com", "https://small2.com"],
#     position=1
# )

# Or direct instantiation:
# ad = AdData(
#     Post_owner="John Doe",
#     Link="https://example.com",
#     Ad_title="Sample Ad",
#     Ad_text="This is a sample ad text",
#     Direct_links=["https://link1.com", "https://link2.com"],
#     Small_links=["https://small1.com", "https://small2.com"],
#     Ad_position=1
# )



