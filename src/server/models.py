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

		
class Noun(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "nouns"
		

class Adjective(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "adjectives"
		
		
class Adverb(models.Model):
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "adverbs"
		


class EventAgent(models.Model):
	id = models.AutoField(primary_key=True)
	agent = models.ForeignKey('Noun')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_agents"
		

class EventPatient(models.Model):
	id = models.AutoField(primary_key=True)
	patient = models.ForeignKey('Noun')
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



class EventBeneficiary(models.Model):
	id = models.AutoField(primary_key=True)
	benificiary = models.ForeignKey('Noun')
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_beneficiaries"
		
		

class EventInstrument(models.Model):
	id = models.AutoField(primary_key=True)
	instrument = models.ForeignKey('Noun')
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_instruments"
		

class EventLocation(models.Model):
	id = models.AutoField(primary_key=True)
	location = models.ForeignKey('Noun')
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_locations"


class EventTime(models.Model):
	id = models.AutoField(primary_key=True)
	time = models.ForeignKey('Noun')
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_time"
		
		
class EventAdjective(models.Model):
	id = models.AutoField(primary_key=True)
	adjective = models.ForeignKey('Adjective')
	noun = models.ForeignKey('Noun')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_adjective"
		

class EventAdverb(models.Model):
	id = models.AutoField(primary_key=True)
	adverb = models.ForeignKey('Adverb')
	action = models.ForeignKey('Action')
	event = models.ForeignKey('Event')
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = "event_adverb"
		