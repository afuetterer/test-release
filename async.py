

class AsyncClient(BaseClient):

    _client: httpx.AsyncClient

    def __init__(self) -> None:
        super().__init__(httpx.AsyncClient)
        self._repository_manager: RepositoryManager = RepositoryManager(self)

    async def _request(self, endpoint: str, return_type: str) -> Resource | Response | str:

        # print("hello from async")
        # print(self._client)

        """Send a HTTP GET request to the specified endpoint.

        Args:
            endpoint: The endpoint to send the request to.
            return_type: The type of response to expect.

        Returns:
            TODO A string representation of the response (if `return_type` is "dataclass") or the full response object.

        Raises:
            TODO httpx.RequestError: If the request fails or times out.
            ValueError: If an invalid `return_type` is provided.
        """
        if return_type not in ALLOWED_RETURN_TYPES:
            raise ValueError(f"Invalid `return_type`: {return_type}. Expected one of: {ALLOWED_RETURN_TYPES}")
        http_response = await self._client.get(endpoint)
        # print(http_response)

        response = _build_response(http_response)
        if return_type == "dataclass":
            return response.parsed
        if return_type == "xml":
            return http_response.text
        return response

    @property
    def repositories(self) -> RepositoryManager:
        """Get the repository manager for this client.

        Returns:
            The repository manager.
        """
        return self._repository_manager



# ---
import asyncio
import re3data
from re3data import AsyncClient

repos = re3data.repositories.list()

async def main():
    client = AsyncClient()

    for repo in repos:
        endpoint = repo.link.split("beta/")[-1]
        response = await client._request(endpoint, "response")
        print(response)

asyncio.run(main())
