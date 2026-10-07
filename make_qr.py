# 사이트 주소가 바뀌면:  python make_qr.py https://새주소/   →  그 후 flyers/build_flyers.py 의 URL도 같이 수정하고 bash flyers/render.sh
import sys, segno
url = sys.argv[1] if len(sys.argv) > 1 else "https://daeyn92-ctrl.github.io/itda-books/"
q = segno.make(url, error="m")
q.save("img/qr-site.png", scale=14, border=2, dark="#0b2e4f", light="#ffffff")
q.save("img/qr-site.svg", scale=10, border=1, dark="#0b2e4f", light="#ffffff")
print("QR ->", url)
