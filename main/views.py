from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(["GET"])
def get_info_social(request):
    info = Info.objects.last()
    info_ser = InfoSerializer(info)
    social_media = SocialMedia.objects.all()
    social_media_ser = SocialMediaSerializer(social_media, many=True)
    data = {
        "info": info_ser.data,
        "social_media": social_media_ser.data
    }
    return Response(data)


@api_view(['POST'])
def create_order(request):
    name = request.POST.get("name")
    phone_number = request.POST.get("phone_number")
    order = Order.objects.create(name=name, phone_number=phone_number)
    ser = OrderSerializer(order)
    return Response(ser.data)


@api_view(["GET"])
def get_discount(request):
    discount = Discount.objects.last()
    discount_ser = DiscountSerializer(discount)
    data = {
        "data": discount_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_product(request):
    product = Product.objects.all().order_by('-id')[:2]
    product_ser = ProductSerializer(product, many=True)
    data = {
        "data": product_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_about_product(request):
    about_product = AboutProduct.objects.all().order_by('-id')[:3]
    about_product_ser = AboutProductSerializer(about_product, many=True)
    data = {
        "data": about_product_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_about_company(request):
    about = AboutCompany.objects.last()
    about_ser = AboutCompanySerializer(about)
    data = {
        "data": about_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_who_use(request):
    who_use = WhoUse.objects.all()
    who_use_ser = WhoUseSerializer(who_use, many=True)
    data = {
        "data": who_use_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_how_to_use(request):
    how_to_use = HowToUse.objects.last()
    how_to_use_ser = HowToUseSerializer(how_to_use)
    data = {
        "data": how_to_use_ser.data,
    }
    return Response(data)


@api_view(["GET"])
def get_fact(request):
    fact = Fact.objects.all()
    fact_ser = FactSerializer(fact, many=True)
    data = {
        "data": fact_ser.data,
    }
    return Response(data)
