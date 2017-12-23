import io
from pdfrw import PdfReader
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.units import inch

from .arrl_radiogram import ArrlRadiogram


def box_sides_in(sides_positions):
    """
    Return the side positions of the form fields in inches converted from
    PDF coords in order to use Canvas positioning
    """
    return [float(sides_positions[0]) / 72.0 * inch,
            float(sides_positions[1]) / 72.0 * inch,
            float(sides_positions[2]) / 72.0 * inch,
            float(sides_positions[3]) / 72.0 * inch]


def populate_pdf_form(template_file, message_class):
    """
    Read in a PDF with form fields and apply the string contents of the
    messageDict dictionary to the cooresponding form fields.
    """
    template = PdfReader(template_file)

    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    for page in template.Root.Pages.Kids:
        for field in page.Annots:
            label = field.T

            key = MessageClass.data_map.get(label[1:-1], '')

            if 'value' in key:
                value = str(key.get('value', 'Test'))
            else:
                value = "TEST"

            if 'padding_top' in key:
                padding_top = key.get('padding_top', '')
            else:
                padding_top = message_class.defaults.get('padding_top', '')

            styles = message_class.styles

            if 'align' in key:
                align = key.get('align', '')


            box_sides = box_sides_in(field.Rect)

            left = min(box_sides[0], box_sides[2])
            bottom = min(box_sides[1], box_sides[3])
            width = box_sides[2] - box_sides[0]
            height = box_sides[3] - box_sides[1]

            form_field = Frame(left,
                               bottom,
                               width,
                               height,
                               leftPadding=0,
                               bottomPadding=0,
                               rightPadding=0,
                               topPadding=padding_top,
                               showBoundary=0)

            story = [Paragraph(value, styles['default'])]
            story_inframe = KeepInFrame(width, height, story)

            form_field.addFromList([story_inframe], pdf)

        pdf.showPage()
    pdf.save()
    data.seek(0)
    return data


def write_formal_message(template_file, output_file, form_data):

    # Read in the template message format with form data fields
    template = PdfFileReader(open(template_file, "rb"))

    # Open a write object for outputting the final message
    output = PdfFileWriter()

    # Add the message template to the output PDF
    output.addPage(template.getPage(0))

    # Get the page inside of the output file
    page = output.getPage(0)

    # Apply the data we want to write out to the form
    output.updatePageFormFieldValues(page, form_data)

    # Write the output to a file
    outputStream = open(output_file, "wb")
    output.write(outputStream)
    outputStream.close()


returndata = populate_pdf_form('RADIOGRAM-2011-FORM.pdf', ArrlRadiogram)
new_pdf = PdfFileReader(returndata)
# read your existing PDF

# write_formal_message("RADIOGRAM-2011-FORM.pdf", "outfile.pdf", mydata)

existing_pdf = PdfFileReader(open("RADIOGRAM-2011-FORM.pdf", "rb"))
output = PdfFileWriter()


# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
output.removeLinks()

# finally, write "output" to a real file
outputStream = open("testform.pdf", "wb")
output.write(outputStream)
outputStream.close()
