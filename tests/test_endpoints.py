def test_add_address(client):
    response = client.post("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    assert response.json['address'] == 'bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5'
    assert response.json['balance'] == 0
    assert len(response.json['txs']) == 2

def test_get_address(client):
    response = client.post("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    response_in_memory = client.get("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    assert response.json['address'] == 'bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5'
    assert response.json['balance'] == 0
    assert len(response.json['txs']) == 2

def test_remove_address(client):
    res = client.post("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    deleted_addr = client.delete("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    get_removed_addr = client.get("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    assert get_removed_addr.json == {}


## This test might fail, was in the middle of updating when I started getting rate limited by blockchain.info API
"""
def test_synchronize_address(client, mocker):
    res = client.post("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5")
    assert len(res.json['balance']) == 0
    with mocker.patch("app.get_address_info_from_blockchain", return_value = {"address": "bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5", "final_balance": 457, 'txs': [{'foo', 'bar'}]}):
        updated_res = client.post("/addresses/bc1q0sg9rdst255gtldsmcf8rk0764avqy2h2ksqs5/synchronize")
        assert updated_res.json['balance'] == 457
"""
