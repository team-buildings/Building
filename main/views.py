from django.shortcuts import render
from django.http import HttpResponse
# import pdfkit
from django.template.loader import render_to_string
from django.template.loader import get_template
from xhtml2pdf import pisa
import io


# Create your views here.

def contract_generate(request):
    template = get_template('shartnoma.html')
    html = template.render({'data': 'some data'})
    result = io.BytesIO()
    pdf = pisa.CreatePDF(io.BytesIO(html.encode('utf-8')), dest=result)

    if pdf.err:
        return HttpResponse('Error generating PDF', status=500)

    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="document.pdf"'
    return response