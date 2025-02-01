import pathlib
import time
import asyncio

import re3data
from re3data import ReturnType
from re3data import AsyncClient

repository_summaries = re3data.repositories.list()
num_repositories = len(repository_summaries)

# for i, repository in enumerate(repositories, 1):
#     repo = re3data.repositories.get(repository.id, return_type=ReturnType.XML)
#     print(f"{i}/{num_repositories}", repository.id)

#     filename = pathlib.Path("repository_samples").joinpath(repository.id).with_suffix(".xml")
#     with open(filename, "w") as f:
#         f.write(repo)
#     time.sleep(0.5)

async def main():
    client = AsyncClient()
    for repo_summary in repository_summaries[:5]:
        repository_full = await client.repositories.get(repo_summary.id)
        print(repository_full.id, repository_full.repository_url)
        # response = await client._request(endpoint, "response")
        # print(response)

asyncio.run(main())
