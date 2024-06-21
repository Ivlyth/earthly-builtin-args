import bs4
import requests
from typing import List


class Category:
    def __init__(self, name: str) -> None:
        self.name = name.rstrip(" args")
        self.args: List[Arg] = []

    def __str__(self):
        return f'Category: {self.name}, has {len(self.args)} args'


class Arg:
    def __init__(self, name: str, description: str, example_value: str) -> None:
        self.name = name
        self.description = description
        self.example_value = example_value

    def __str__(self) -> str:
        return f'{self.name}: {self.example_value}'


def get_all_args() -> List[Category]:
    response = requests.get("https://docs.earthly.dev/docs/earthfile/builtin-args")
    if response.status_code != 200:
        raise Exception(f"fetch build-in args page failed with status code: {response.status_code}")
    parser = bs4.BeautifulSoup(response.text, features="html.parser")
    category_tags = parser.find_all("h3")
    table_tags = parser.find_all("table")
    if len(category_tags) != len(table_tags):
        raise Exception(f"There are {len(category_tags)} categories and {len(table_tags)} tables")
    categories: List[Category] = []
    for category_tag, table_tag in zip(category_tags, table_tags):
        category = Category(name=category_tag.text.strip())
        print(f"found a new category: {category.name}")
        table_body = table_tag.find("tbody")
        if table_body is None:
            raise Exception("<tbody> element not found (category: {category})")
        for index, arg_tag in enumerate(table_body.find_all("tr")):
            tds = arg_tag.find_all("td")
            if len(tds) < 3:
                raise Exception(f"expected 3 columns, but got {len(tds)} (category: {category.name}, row index: {index+1}, tag content: {arg_tag})")
            arg_name = tds[0].text.strip()
            arg_description = tds[1].text.strip()
            arg_example_value = tds[2].text.strip()
            arg = Arg(arg_name, arg_description, arg_example_value)
            category.args.append(arg)
            print(f"found a new ARG: {arg.name}")
        categories.append(category)
    return categories


def gen_earthfile(categories: List[Category]) -> None:
    from io import StringIO
    buf = StringIO()
    buf.write("VERSION 0.8\n")
    buf.write("FROM alpine:latest\n\n")
    buf.write("echo:\n")
    for category in categories:
        buf.write(f"    RUN echo \"# Category: {category.name}\" \n")
        for index, arg in enumerate(category.args):
            buf.write(f"    ARG {arg.name}\n")
            buf.write(f"    RUN echo \"{arg.name}'s value is: ${arg.name}\" >> args.txt\n")
    buf.write("    SAVE ARTIFACT args.txt AS LOCAL args.txt\n")
    s = buf.getvalue()
    print("generated Earthfile content is: ")
    print(s)
    open("Earthfile", "w").write(s)


if __name__ == '__main__':
    categories = get_all_args()
    gen_earthfile(categories)
