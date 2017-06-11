from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album, Order, Item, Client
from cart.cart import Cart
from django.contrib import messages


def album_list(request):
    if 'search_box' in request.REQUEST and request.REQUEST['search_box']:
        name = request.REQUEST['search_box']
        albums = Album.objects.all().filter(title__icontains=name).order_by('-title')
    else:
        albums = Album.objects.all().order_by('-title')
    context = {'albums': albums}
    return render(request, "index.html", context)


@login_required(login_url="login/")
def album(request, album_id):
    if request.method == 'POST':
        user = Client.objects.get(username=request.user)
        for name, value in request.REQUEST.iteritems():
            if 'Dodaj' in value:
                item_id = name
        item = Item.objects.get(id=item_id)
        if item.order:
            return render(request, "blad", {})
        else:
            order, _ = Order.objects.get_or_create(client=user, status=1)
            order.save()
            item.order = order
            item.save()
        cart = Item.objects.all().filter(order=order.id)
        context = {'cart': cart}
        return render(request, "basket.html", context)

    else:
        album_object = get_object_or_404(Album, id=album_id)
        items_list = Item.objects.all().filter(album=album_id, order__isnull=True)
        context = {"album": album_object, "items": items_list}
        return render(request, "album.html", context)


@login_required(login_url="login/")
def basket(request):
    user = Client.objects.get(username=request.user)
    order = Order.objects.get(client=user.id, status=1)
    if request.method == "POST":
        order.status = 2
        order.save()
        #messages.info(request, 'kupiono')
        return render(request, "index.html")


    cart = Item.objects.all().filter(order=order.id)
    print cart
    context = {'cart': cart}
    return render(request, "basket.html", context)


@login_required(login_url="login/")
def orders(request):
    user = Client.objects.get(username=request.user)
    orders_list = Order.objects.all().filter(client=user.id, status=2)
    context = {"orders": orders_list}
    return render(request, "orders.html", context)

def registration(request):
    pass


