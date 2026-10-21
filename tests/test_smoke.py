import django


def test_django_setup():
    assert django.VERSION >= (4, 0)
