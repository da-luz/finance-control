from django.urls import path

from control.views import (
    TransactionsListView,
    TransactionUpdateView,
    TransactionCreateView,

    CategoryUpdateView,
    CategoryCreateView,
)

urlpatterns = [
    path('', TransactionsListView.as_view(), name="transactions"),
    path('create/transaction/', TransactionCreateView.as_view(), name="new-transaction"),
    path('update/transaction/<int:pk>/', TransactionUpdateView.as_view(), name="edit-transactions"),

    path('create/category/', CategoryCreateView.as_view(), name="new-category"),
    path('update/category/<int:pk>/', CategoryUpdateView.as_view(), name="edit-category"),
]
