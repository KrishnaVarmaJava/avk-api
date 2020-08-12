# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class agentDetails(models.Model):
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)

    def __init__(self):
        return firstName
