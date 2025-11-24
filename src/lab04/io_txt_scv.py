import csv
from typing import Union
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as file:
        return file.read()


def write_csv(
    rows: list[Union[tuple, list]],
    path: Union[str, Path],
    header: Union[tuple[str, ...], None] = None,
) -> None:
    if rows:
        first_row_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_row_length:
                raise ValueError(
                    f"Все строки должны иметь одинаковую длину. "
                    f"Строка 0 имеет длину {first_row_length}, "
                    f"строка {i} имеет длину {len(row)}"
                )

    if header and rows:
        if len(header) != len(rows[0]):
            raise ValueError(
                f"Заголовок имеет длину {len(header)}, "
                f"а строки данных имеют длину {len(rows[0])}"
            )

    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")

        if header:
            writer.writerow(header)

        writer.writerows(rows)
