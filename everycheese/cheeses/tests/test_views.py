from django.db.models.fields import CharField
from django.http import request, response
import pytest
from .factories import UserFactory
from pytest_django.asserts import assertContains
from django.urls import reverse
from .factories import CheeseFactory, cheese
from ..models import Cheese
from ..views import (
    CheeseCreatView,
    CheeseListView,
    CheeseDetailView,
    CheeseUpdateView
)
@pytest.fixture
def user():
    return UserFactory()

pytestmark = pytest.mark.django_db
# look on page 189 of wedge of django book for explanation
def test_good_cheese_list_view_expanded(rf):
    url = reverse("cheeses:list")
    request = rf.get(url)
    callable_obj = CheeseListView.as_view()
    response = callable_obj(request)
    assertContains(response, 'Cheese List')
# wrote better
def test_good_cheese_list_view(rf):
    request = rf.get(reverse("cheeses:list"))
    response = CheeseListView.as_view()(request)
    assertContains(response, 'Cheese List')

def test_good_cheese_detail_view(rf, cheese):
    cheese = CheeseFactory()
    url = reverse("cheeses:detail", kwargs={'slug':cheese.slug})
    request = rf.get(url)
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug = cheese.slug)
    assertContains(response, cheese.name)

def test_good_cheeses_create_view(client, user):
    client.force_login(user)
    url = reverse("cheeses:add")
    response = client.get(url)
    assert response.status_code == 200

def test_cheese_list_contains_2_cheeses(rf):
    cheese1 = CheeseFactory()
    cheese2 = CheeseFactory()
    request = rf.get(reverse('cheeses:list'))
    response = CheeseListView.as_view()(request)
    assertContains(response, cheese1.name)
    assertContains(response, cheese2.name)

def test_detail_contains_cheese_data(rf):
    cheese = CheeseFactory()
    url = reverse("cheeses:detail",
        kwargs= {'slug':cheese.slug})
    request = rf.get(url)
    callable_obj = CheeseDetailView.as_view()
    response = callable_obj(request, slug = cheese.slug)
    assertContains(response, cheese.name)
    assertContains(response, cheese.get_firmness_display())
    assertContains(response, cheese.country_of_origin.name)

def test_cheese_create_form_valid(client, user):
    client.force_login(user)
    form_data = {
        "name":"Paski Sir",
        "description":"salty cheese",
        "firmness":Cheese.Firmness.HARD,
    }
    
    url = reverse("cheeses:add")
    response = client.post(url, form_data)
    assert response.status_code == 302
    cheese = Cheese.objects.get(name = "Paski Sir")
    assert cheese.description == "salty cheese"
    assert cheese.firmness == Cheese.Firmness.HARD
    assert cheese.creator == user
    
def test_cheese_correct_title(client, user):
    client.force_login(user)
    response = client.get(reverse("cheeses:add"))
    assertContains(response, "Add Cheese")

def test_good_cheese_update_view(client, user, cheese):
    client.force_login(user)
    url = reverse("cheeses:update",
        kwargs={"slug":cheese.slug})
    response = client.get(url)
    assertContains(response, "Update Cheese")

def test_cheese_update(client, user, cheese):
    client.force_login(user)
    form_data = {
        "name":cheese.name,
        "description":"Something new",
        "firmness":cheese.firmness
    }
    url = reverse("cheeses:update",
        kwargs={"slug":cheese.slug})
    response = client.post(url, form_data)
    cheese.refresh_from_db()
    assert cheese.description == "Something new"