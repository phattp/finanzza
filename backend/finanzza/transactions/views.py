from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db.models import DecimalField, Sum, When, Case, F, Q
from .models import Transaction
from .serializers import TransactionSerializer


# Transaction Viewset
class TransactionView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return self.request.user.transactions.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        total_income = Transaction.objects.all().aggregate(
            total_income=Sum(Case(When(category=Transaction.INCOME, then='amount'), output_field=DecimalField(max_digits=20, decimal_places=2))))
        total_expense = Transaction.objects.all().aggregate(
            total_expense=Sum(Case(When(category=Transaction.EXPENSE, then='amount'), output_field=DecimalField(max_digits=20, decimal_places=2))))
        net_total = total_income['total_income'] - \
            total_expense['total_expense']

        response_data = {
            'total_income': total_income['total_income'],
            'total_expense': total_expense['total_expense'],
            'net_total': net_total,
            'result': serializer.data
        }

        return Response(response_data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
