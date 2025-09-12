from typing import Any, List

# def date_to_string(r:  list[dict[str, Any]]) -> List[str]:
#     dates = []
#     for i in r:
#         date_obj = datetime.strptime(i['date'], '%Y-%m-%d')
#         formatted_date = date_obj.strftime('%b %-d')
#         dates.append(formatted_date)
#
#     return dates


def extract_key_as_list(r: list[dict[str, Any]], key: str) -> List[str]:
    return [i[key] for i in r]
