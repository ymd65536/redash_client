from .base import base_client as cli


class queries:
    def __init__(self, base_client) -> None:
        self.request_client = base_client

    def get_queries(self, page=1, page_size=25):
        """_summary_

        Returns:
            List: query list
        """
        res = cli.get(self.request_client, 'queries', params=dict(page=page, page_size=page_size))
        return res.json()
