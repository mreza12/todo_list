import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_category_list_view():
    instance1 = test_helpers.create_task_category()
    instance2 = test_helpers.create_task_category()
    client = Client()
    url = reverse("task_category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_category_create_view():
    client = Client()
    url = reverse("task_category_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_category_detail_view():
    client = Client()
    instance = test_helpers.create_task_category()
    url = reverse("task_category_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_category_update_view():
    client = Client()
    instance = test_helpers.create_task_category()
    url = reverse("task_category_update", args=[instance.pk, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_task_list_view():
    instance1 = test_helpers.create_task_task()
    instance2 = test_helpers.create_task_task()
    client = Client()
    url = reverse("task_task_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_task_create_view():
    category = test_helpers.create_task_category()
    client = Client()
    url = reverse("task_task_create")
    data = {
        "note": "text",
        "done": True,
        "priority": "text",
        "name": "text",
        "category": category.pk,
    }
    print(data)
    response = client.post(url, data)
    assert response.status_code == 302


def tests_task_detail_view():
    client = Client()
    instance = test_helpers.create_task_task()
    url = reverse("task_task_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_task_update_view():
    category = test_helpers.create_task_category()
    client = Client()
    instance = test_helpers.create_task_task()
    url = reverse("task_task_update", args=[instance.pk, ])
    data = {
        "note": "text",
        "done": True,
        "priority": "text",
        "name": "text",
        "category": category.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
