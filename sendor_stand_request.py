import configuration
import requests
import data

# Создание заказа
def create_order(order_body):
    return requests.post (configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# Получение заказа по его номеру
def get_order(track_id):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_id}"
    response = requests.get(get_order_url)
    return response

# Автотест 1
def test_order_creation_and_retrieval():
    response = create_order(data.order_body)

    track_id = response.json()["track"]
    print("Заказ создан. Номер ID:", track_id)

    # Получение данных по его номеру
    order_response = get_order(track_id)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)