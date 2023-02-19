from django.test import TestCase
import pytest
import requests
# Create your tests here.

def test_example():
    r = requests.get('http://localhost:8000/')
    assert r.status_code == 200
        
    