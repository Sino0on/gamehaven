from django.shortcuts import render
from game.models import HomePage, Contacts, About, Application, Game, Review, News, Feature, Phone
from game.forms import ApplcationForm
from game.utils import send_sms_code
from django.shortcuts import render


# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)


def home(request):
    if request.method == 'POST':
        form = ApplcationForm(request.POST)
        if form.is_valid():
            das = form.save()
            send_sms_code(das.email, f'{das.fullname} {das.comment}')
    home_page = HomePage.objects.all().first()
    contacts = Contacts.objects.all().first()
    about = About.objects.all().first()
    applications = Application.objects.all()
    games = Game.objects.all()
    reviews = Review.objects.all()
    news = News.objects.all()
    phones = Phone.objects.all()
    features = Feature.objects.all()
    form = ApplcationForm()
    context = {
        'home_page': home_page,
        'contacts': contacts,
        'about': about,
        'applications': applications,
        'games': games,
        'reviews': reviews,
        'news': news,
        'features': features,
        'phones': phones,
        'form': form,
    }

    return render(request, 'index.html', context)
