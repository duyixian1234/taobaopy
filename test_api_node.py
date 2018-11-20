try:
    from unittest import mock
except:
    import mock
import pytest

from taobaopy.taobao import TaoBaoAPIClient, TaoBaoAPINode


@pytest.fixture()
def client():
    mock_client = mock.Mock()
    mock_client.time_get.return_value = {'time_get_response': {}}
    mock_client.alibaba__xiami_api_rank_sina_newsong_get.return_value = {
        'alibaba_xiami_api_rank_sina_newsong_get_response': {}
    }
    yield mock_client


def test_taobao(client):
    taobao = TaoBaoAPINode(client=client, field='')
    assert taobao.time.get.field == 'time_get'
    assert taobao.time.get() == {'time_get_response': {}}
    client.time_get.assert_called_with()


def test_alibaba(client):
    alibaba = TaoBaoAPINode(client=client, field='alibaba_')
    assert alibaba.xiami.api.rank.sina.newsong.get.field == 'alibaba__xiami_api_rank_sina_newsong_get'
    assert alibaba.xiami.api.rank.sina.newsong.get(type='music_new') == {
        'alibaba_xiami_api_rank_sina_newsong_get_response': {}
    }
    client.alibaba__xiami_api_rank_sina_newsong_get.assert_called_with(
        type='music_new')
