# # Ксения Дрыбина, 19-я когорта — Финальный проект. Инженер по тестированию плюс
import sendor_stand_request
import data

# Автотест 1

def test_order_creation_and_retrieval():
    #Создание заказа
    response = sendor_stand_request.create_order(data.order_body)
    track_id = response.json()["track"]
    print("Заказ создан. Номер ID:", track_id)

    # Получение данных по его номеру
    response_order = sendor_stand_request.get_order(track_id)

    assert response_order.status_code == 200, f"Ошибка: {response_order.status_code}"
    order_data = response_order.json()
    print("Данные заказа:")
    print(order_data)