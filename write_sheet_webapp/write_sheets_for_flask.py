from read_sheets.read_sheets import load_google_sheets_to_list


def get_value_for_flask():
    sheet_list = load_google_sheets_to_list()
    memory = []
    for item in sheet_list:
        memory.append([item.get("id"), item.get("number_order"), item.get('price'), item.get('date_delivery')])
    return memory


