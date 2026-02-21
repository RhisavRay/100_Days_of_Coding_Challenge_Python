def report():
    for key in helper_data.resources:
        if key == "coffee":
            print(f"{key}: {helper_data.resources[key]}g")
        else:
            print(f"{key}: {helper_data.resources[key]}ml")