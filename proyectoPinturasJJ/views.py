from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Material, Budget, MaterialBudget
from .serializers import MaterialSerializer, BudgetSerializer


@api_view(['GET'])
def getMaterials(request):
    materials = Material.objects.all()
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data, 200)

@api_view(['GET'])
def getMaterial(request, uid):
    material = Material.objects.get(pk=uid)
    serializer = MaterialSerializer(material, many=False)
    if len(material) > 0:
        return Response(serializer.data, 200)
    return Response({"message":"No se pudo encontrar el material"})

@api_view(['GET'])
def getBudgets(request):
    budgets = Budget.objects.all()
    serializer = BudgetSerializer(budgets, many=True)
    if len(budgets) > 0:
        return Response(serializer.data, 200)
    return Response({"message": "No se pudo encontrar el material"})

@api_view(['GET'])
def getBudget(request, uid):
    budget = Budget.objects.get(pk=uid)
    if budget:
        materials = Material.objects.all()
        materials = MaterialSerializer(materials, many=True)
        serializer = BudgetSerializer(budget, many=False)
        data = serializer.data
        data["materials"] = materials.data
        return Response(data, 200)
    return Response({"message": "No se pudo encontrar el presupuesto"})

@api_view(['POST'])
def newMaterial(request):
    serializer = MaterialSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, 200)


@api_view(['POST'])
def newBudget(request):
    total_cost = 0
    materials = Material.objects.all()
    for material in materials:
        total_cost += (request.data["sqm"] * material.cost_sqm)
    new_budget = Budget(client_name=request.data["name"], sqm=request.data["sqm"], total_cost=total_cost, exists=True)
    new_budget.save()
    serializer = BudgetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, 200)
