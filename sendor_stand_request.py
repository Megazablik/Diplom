import configuration
import requests
import data

# Создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body, headers=data.headers)

respone = create_order(data.order_body)
print(respone.status_code)

# Получение заказа по его номеру
def get_order(track_id):
   return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION + str (track_id), headers=data.headers)