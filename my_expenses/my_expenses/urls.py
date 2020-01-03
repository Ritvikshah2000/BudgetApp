# bound views with the path we want on browser

from django.contrib import admin
from django.urls import path
from expenses.views import (HomepageView, BillListView,
                            PayrollListView, ExpensesListView,
                            report_view
                            )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'),

    path('bills/', BillListView.as_view(), name='bills_view'), # is for dynamic use call on the template when we need this url
    path('payroll/', PayrollListView.as_view(), name='payroll_view'),
    path('expenses/', ExpensesListView.as_view(), name='expenses_view'),
    path('reports/', report_view, name='reports_view')

]