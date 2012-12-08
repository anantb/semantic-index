from django.db import models

'''
Semantic Index Models

@author: Anant Bhardwaj
@date: Dec 08, 2012
'''




class Event(models.Model):
	id = models.AutoField(primary_key=True)

	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "events"



class Action(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "actions"

		
class Object(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "objects"
		

class Adjective(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "adjectives"
		
		
class Adverb(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "adverbs"
		


class EventAgent(models.Model):
	id = models.AutoField(primary_key=True)
	agent = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_agents"
		

class EventPatient(models.Model):
	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_patients"
		

class EventAction(models.Model):
	id = models.AutoField(primary_key=True)
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_actions"



class EventBenificiary(models.Model):
	id = models.AutoField(primary_key=True)
	benificiary = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_benificiary"
		
		

class EventInstrument(models.Model):
	id = models.AutoField(primary_key=True)
	instrument = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_instruments"
		

class EventLocation(models.Model):
	id = models.AutoField(primary_key=True)
	location = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_location"


class EventTime(models.Model):
	id = models.AutoField(primary_key=True)
	location = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_time"
		
		
class EventAdjective(models.Model):
	id = models.AutoField(primary_key=True)
	adjective = models.ForeignKey('Adjective')
	obj = models.ForeignKey('Object')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_adjective"
		

class EventAdverb(models.Model):
	id = models.AutoField(primary_key=True)
	adjverb = models.ForeignKey('Adverb')
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_adverb"
		