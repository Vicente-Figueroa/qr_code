from rest_framework.views import APIView
from rest_framework.response import Response
import qrcode


class Home(APIView):
    def post(self, request):

        img = qrcode.make("Wena compare, estamos sacando un codigo QR")
        type(img)  # qrcode.image.pil.PilImage
        img.save("some_file.png")

        print(request.data["Hola"])
        return Response("usernames")

    def get(self, request):
        return Response("este es el get")
