# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class LeaveHistory(models.Model):
    entitledAnnualLeaves=models.CharField(max_length=2)
    carryForwardAnnualLeaves=models.CharField(max_length=2)
    takenAnnualLeaves=models.CharField(max_length=2)
    remainingAnnualLeaves=models.CharField(max_length=2)
