from mockito import when,mock,verifyStubbedInvocationsAreUsed
from mock1 import *
def test_fetch():
    url="https://www.google.com"
    response=mock({"text":"Ok"},spec=requests.Response)
    session=mock(requests.Session)
    when(session).get(url).thenReturn(response)
    when(requests).Session().thenReturn(session)
    r=fetch(url)
    assert r.text=='Ok'
    verifyStubbedInvocationsAreUsed()

test_fetch()