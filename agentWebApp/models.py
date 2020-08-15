# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from leaveDetails.models import LeaveHistory

#not sute why i am adding it here, need to create a new project for organization_details
class Organization(models.Model):
    name=models.CharField(max_length=10, default="abc")
    leave_History=models.ForeignKey(LeaveHistory, on_delete=models.SET_NULL, null=True)
class AgentDetails(models.Model):
    firstName=models.CharField(max_length=10)
    lastName=models.CharField(max_length=10)
    organization_details=models.ForeignKey(Organization)
