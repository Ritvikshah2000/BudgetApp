#used to handle custom queries.


from django.db.models import QuerySet, Manager
import datetime

#creating QuerySet and not writing code directly on manager, gives us freedom to use same code kn multiple managers
class GenericQuerySet(QuerySet):
    def filter_by_date(self, date_start, date_end):
        return self.filter(date_expired__range=[date_start, date_end]) #filter uqeryset with django ORM

    def unpaid(self):
        return self.filter(is_paid=False)


class GeneralManager(Manager):
    def get_queryset(self):
        return GenericQuerySet(self.model, using=self._db)
#the above gets query we created before and filter the model which is related