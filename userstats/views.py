from django.shortcuts import render
from rest_framework.views import APIView
from expenses.models import expense
from income.models import Income
from rest_framework import status, response
import datetime


class IncomeSourcesSummaryStats(APIView):

    def get_source(self, inc):
        return inc.source

    def get_amount_for_source(self, income_lst, source):
        income = income_lst.filter(source=source)
        amount = 0
        for i in income:
            amount += i.amount
        return {'amount': str(amount)}

    def get(self, request):
        todays_date = datetime.date.today()
        one_year_ago = todays_date - datetime.timedelta(days=365)
        income = Income.objects.filter(owner=request.user, date__gte=one_year_ago, date__lte=todays_date)

        final = {}
        sources = list(set(map(self.get_source, income)))

        for src in sources:
            final[src] = self.get_amount_for_source(income, src)

        return response.Response({'income_source_data': final}, status=status.HTTP_200_OK)


class ExpenseSummaryStats(APIView):

    def get_category(self, exp):
        return exp.category

    def get_amount_for_category(self, exp_lst, category):
        new_exp_lst = exp_lst.filter(category=category)
        amount = 0
        for exp in new_exp_lst:
            amount += exp.amount
        return {'amount': str(amount)}

    def get(self, request):
        todays_date = datetime.date.today()
        one_year_ago = todays_date - datetime.timedelta(days=365)
        expenses = expense.objects.filter(owner=request.user, date__gte=one_year_ago, date__lte=todays_date)

        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for category in categories:
            final[category] = self.get_amount_for_category(expenses, category)

        return response.Response({'category_data': final}, status=status.HTTP_200_OK)

