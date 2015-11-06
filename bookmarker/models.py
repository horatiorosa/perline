from __future__ import unicode_literals

from django.db import models

import datetime

from django.utils import timezone


class Link(models.Model):
	link_url = models.URLField(blank=False, null=False, unique=False, max_length=50)
	link_name = models.CharField(max_length=50, null=False, blank=False)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	date_modified = models.DateTimeField('Date Modified', auto_now=True)
	tags = models.TextField('tags')

	def __str__(self):
		return u'{} {}'.format(self.link_name, self.link_url)


class User(models.Model):
	username = models.CharField(max_length=25)
	email = models.CharField(max_length=50, null=False, blank=False)
	password = models.CharField(max_length=25, null=False, blank=False)
	verified = models.BooleanField(default=False, null=False)
	approval_date = models.DateTimeField('Approved', null=True, blank=True)

	def __str__(self):
		return u'{} {}'.format(self.username, self.email)



class Bookmark(models.Model):
	user = models.ForeignKey(User)
	link = models.ForeignKey(Link)
	title = models.CharField(max_length=50)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	date_modified = models.DateTimeField('Date Modified', auto_now=True)

	def __str__(self):
		return self.title
