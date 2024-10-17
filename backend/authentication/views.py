from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from . models import Income, Expense
from django.db.models import Sum


### AUTHENTICATION

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    User.objects.create_user(
        username = username,
        email = email,
        password = password
    )
    return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)
        token, created= Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successful', 'token':token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

### INCOME

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_income(request):
    amount = request.data.get('amount')
    source = request.data.get('source')
    notes = request.data.get('notes', None) # Defaults to none if notes are not provided

    Income.objects.create(
        user = request.user,
        amount = amount,
        source = source,
        notes = notes
    )
    return Response({'message': 'Income added successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_income(request):
    income_list = Income.objects.filter(user = request.user)
    income_data = [
        {
            "amount": income.amount,
            "source": income.source,
            "date": income.date,
            "notes": income.notes
        }
        for income in income_list
    ]
    return Response(income_data, status=status.HTTP_200_OK)

### EXPENSE

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_expense(request):
    amount = request.data.get('amount')
    description = request.data.get('description')
    category = request.data.get('category')
    notes = request.data.get('notes', None)

    Expense.objects.create(
        user = request.user,
        amount = amount,
        description = description,
        category = category,
        notes = notes
    )

    return Response({'message': 'Expense added successfully.'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_expense(request):
    expense_list = Expense.objects.filter(user=request.user)

    expense_data = [
        {
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "date": expense.date,
            "notes": expense.notes
        }
        for expense in expense_list
    ]

    return Response(expense_data, status=status.HTTP_200_OK)

### SUMMARY

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_summary(request):
    total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_expenses = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expenses

    return Response({
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance
    }, status=status.HTTP_200_OK)