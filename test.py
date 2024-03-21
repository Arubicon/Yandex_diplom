import request
import data
# Алексей Грибов, 14-й поток — Инженер по тестированию плюс. Финальный проект.
def test_get_order_by_track():
    track = request.create_order()
    response = request.get_order_details(trackNumber=track)
    assert response['order'] is not None
    order = response['order']
    assert order['firstName'] == data.order_body['firstName']
    assert order['phone'] == data.order_body['phone']