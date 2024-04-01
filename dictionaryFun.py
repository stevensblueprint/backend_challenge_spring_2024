from pydantic import BaseModel

class Item(BaseModel):
    name: str
    number: int


diction = {
    0: Item(
        name = "test1",
        number=25
    ),

    1: Item(
        name = "test2",
        number=13
    ),

    2: Item(
        name = "test3",
        number=13
    ),
    }

Selection = dict[
    str, str | int | list | bool | None
]

def query_by_anyData(
    name: str | None = None,
    number: int | None = None
) -> dict[str, Selection]:
    def check(queried: Item) -> bool:
            return all(
                (
                    name   is None or queried.name ==   name,
                    number is None or queried.number == number,
                )
            )

    selection = [X for X in diction.values() if check(X)]
    return {
        # return original query
        "query": {
            "name":   name,
            "number": number,

            },
        # return found volnteer as well
        "selection": selection,
    }

print(query_by_anyData(number=13))