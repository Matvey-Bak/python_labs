def format_record(rec: tuple[str, str, float]):
    name, group, eval = rec

    if not isinstance(name, str):
        return "ValueError"
    if not isinstance(group, str):
        return "ValueError"
    if not isinstance(eval, float):
        return "ValueError"
    
    clean_name = " ".join(name.strip().split())
    parts_initialos = clean_name.split()
    familia = parts_initialos[0].title()
    initiale = ".".join(first[0].upper() for first in parts_initialos[1:]) + '.'

    new_group = group.strip()

    new_eval = f"{eval:.2f}"

    itog = f"{familia} {initiale}, гр. {new_group}, GPA {new_eval}" 

    return itog

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))




