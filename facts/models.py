from django.db import models


class Fact(models.Model):
    factoid = models.TextField()
    date_added = models.DateTimeField('date added')
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.factoid


#class Picture(models.Model):
#    class Admin:
#        pass
#
#    name = models.CharField(max_length=50)
#    email = models.EmailField()
#    date_added = models.DateTimeField('date added')
#    filename = models.CharField(max_length=50)
#    fact_id = models.ForeignKey(Fact)
