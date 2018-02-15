import sys
print(sys.version)


def make_car(name, model, **car_info):
    car = {}
    car["name"] = name
    car["model"] = model

    for key, value in car_info.items():
        car[key] = value

    return car


if __name__ == '__main__':
    car = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car)
