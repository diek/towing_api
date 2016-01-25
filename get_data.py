import csv
import collections
import data_config


def get_state_data():
    car_state = collections.defaultdict(int)
    STATE_RESULTS = {'children': []}

    for line in csv.DictReader(data_config.DATA.splitlines(), skipinitialspace=True):
        state = line['State']
        if len(state) == 0:
            state = '_NA'
        car_state[state] += 1

    for k, v in car_state.items():
        if k != 'IL':
            if v > 9:
                if k in data_config.STATE:
                    state_l = data_config.STATE[k]
                else:
                    state_l = "Not Identified"
                STATE_RESULTS['children'].append({
                    'symbol': k,
                    'name': state_l,
                    'value': str(v)
                })

    return STATE_RESULTS


def get_make_data():
    car_make = collections.defaultdict(int)
    MAKE_RESULTS = {'children': []}

    for line in csv.DictReader(data_config.DATA.splitlines(), skipinitialspace=True):
        make = line['Make']
        if len(make) == 0:
            make = '_NA'
        car_make[make] += 1

    for k, v in car_make.items():
        if v > 25:
            if k in data_config.MAKE_CODE:
                make_l = data_config.MAKE_CODE[k]
            else:
                make_l = k + " unknown"
            MAKE_RESULTS['children'].append({
                'symbol': k,
                'name': make_l,
                'value': str(v)
            })
    return MAKE_RESULTS


def get_color_data():
    car_color = collections.defaultdict(int)
    COLOR_RESULTS = {'children': []}

    for line in csv.DictReader(data_config.DATA.splitlines(), skipinitialspace=True):
        color = line['Color']
        if len(color) == 0:
            color = '_NA'
        car_color[color] += 1

    for k, v in car_color.items():
        if v > 25:
            if k in data_config.COLOR_CODE:
                color_l = data_config.COLOR_CODE[k]
            else:
                color_l = k + " unknown"
            COLOR_RESULTS['children'].append({
                'symbol': k,
                'name': color_l,
                'value': str(v)
            })
    return COLOR_RESULTS


def get_data():
    RESULTS = {'data': []}
    for line in csv.DictReader(data_config.DATA.splitlines(), skipinitialspace=True):
        RESULTS['data'].append({
            'tow_date': line['Tow Date'],
            'make': line['Make'],
            'vehicle_type': line['Style'],
            'color': line['Color'],
            'state': line['State'],
            'impound_address': line['Towed to Address'],
            'impound_ph': line['Tow Facility Phone'],
            'inventory_num': line['Inventory Number']
        })
    return RESULTS
