from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortURL
import string
import random

def home(request):
    short_link = None

    if request.method == "POST":
        original_url = request.POST.get("original_url", "").strip()

        if original_url.startswith(("http://", "https://")):
            short = ''.join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )
            link = ShortURL.objects.create(
                original_url=original_url,
                short_code=short
            )
            short_link = request.build_absolute_uri(f"/{link.short_code}")

    return render(request, "links/home.html", {
        "short_link": short_link
    })

def go_to_url(request, code):
    link = ShortURL.objects.filter(short_code=code).first()

    if link:
        return redirect(link.original_url)

    return HttpResponse("Short link not found", status=404)

