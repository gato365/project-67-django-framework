from django.shortcuts import render



## Fake Posts
posts = [
    {
        'author': 'John Doe',
        'title': 'The First Post',
        'content': 'This is the content of the first post.',
        'date_posted': '2023-04-01'
    },
    {
        'author': 'Jane Smith',
        'title': 'Exploring Python',
        'content': 'Python has numerous applications, from web development to data science.',
        'date_posted': '2023-04-02'
    },
    {
        'author': 'Mike Johnson',
        'title': 'Django for Beginners',
        'content': 'Django makes it easier to build Web applications quickly and with less code.',
        'date_posted': '2023-04-03'
    },
    {
        'author': 'Emily Davis',
        'title': 'Understanding REST APIs',
        'content': 'REST APIs allow different systems to communicate with each other over HTTP.',
        'date_posted': '2023-04-04'
    }
]

# Create your views here.


def home(request):
    context = {
        'posts': posts 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')