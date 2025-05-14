from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Home pagega xush kelibsiz")

def x(request, raqam):
    return HttpResponse(f"Hello, world. You're at the polls index.{raqam}")
def say_joxa(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Joxa</title>
            <style>
                body {
                    background-color: #000;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .joxa-button {
                    background-color: skyblue;
                    color: white;
                    border: none;
                    padding: 20px 40px;
                    font-size: 48px;
                    font-weight: bold;
                    border-radius: 10px;
                    cursor: pointer;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
                    animation: spin 1s linear infinite; /* 1s = 10 tezlik */
                }
                @keyframes spin {
                    from { transform: rotate(0deg); }
                    to { transform: rotate(360deg); }
                }
            </style>
        </head>
        <body>
            <button class="joxa-button">Joxa</button>
        </body>
        </html>
    """)

def say_hello(request):
    return HttpResponse("Hello, world. You're at the polls index.")
