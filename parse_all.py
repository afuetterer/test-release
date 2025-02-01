import pathlib
from re3data._response import PARSER
from re3data._resources import Re3Data

from rich import print

xml_path = pathlib.Path("repository_samples")

files = list(xml_path.glob("*.xml"))

for xml_file in files:
    repository = PARSER.from_path(xml_file, Re3Data).repository[0]
    print(xml_file, repository.id)
    # software_names = [s.software_name for s in repository.software]
    # # print(software_names)
    # if software_names:
    #     print(xml_file, repository.id)
    #     print(software_names)

