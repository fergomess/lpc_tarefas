from django.http import HttpResponse

def index(request):
    html = """
                <h1>Atividade API</h1>
                <p>Aluna: Fernanda Gomes </p>
            """
    return HttpResponse(html)
