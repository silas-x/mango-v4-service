from mango_service_v4_py.api import MangoServiceV4Client

if __name__ == "__main__":

    mango_service_v4_client = MangoServiceV4Client()

    print("orders before cancelling")
    for order in mango_service_v4_client.get_orders():
        print(order.json(indent=4, sort_keys=True))
    print("")

    mango_service_v4_client.cancel_all_orders()
    print("orders after cancelling")
    for order in mango_service_v4_client.get_orders():
        print(order.json(indent=4, sort_keys=True))
