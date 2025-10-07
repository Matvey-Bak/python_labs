def format_record(rec: tuple[str, str, float]):
    if len(rec) == 3 and isinstance(rec, tuple):

        name, group, eval = rec

        if not isinstance(name, str):
            raise TypeError ("Ошибка в записи ФИО")
        if not isinstance(group, str):
            raise TypeError ("Ошибка в записи группы")
        if not isinstance(eval, float):
            raise TypeError ("Ошибка в записи типа GPA")
        
        clean_name = " ".join(name.strip().split())
        parts_initialos = clean_name.split()
        familia = parts_initialos[0].title()
        initiale = ".".join(first[0].upper() for first in parts_initialos[1:]) + '.'

        new_group = group.strip()

        new_eval = f"{eval:.2f}"

        itog = f"{familia} {initiale}, гр. {new_group}, GPA {new_eval}" 

        return itog
    
    else:
        raise TypeError ("Некорректные записи (пустое ФИО, пустая группа, неверный тип GPA")

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("Иванов Иван Иванович", "BIVT-25", "4.6")))
print(format_record(( "BIVT-25", 4.6)))




