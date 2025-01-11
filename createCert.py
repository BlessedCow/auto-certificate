from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register all fonts
pdfmetrics.registerFont(TTFont("Lucida Handwriting", "C:/Windows/Fonts/LHANDW.TTF"))
pdfmetrics.registerFont(TTFont("Lucida Bright", "C:/Windows/Fonts/LBRITE.TTF"))
pdfmetrics.registerFont(TTFont("Lucida Bright Demibold", "C:/Windows/Fonts/LBRITED.TTF"))

def generate_certificate(training, staff_name, date_completed, trainer_name, time_took):
    filename = f"{training}_{staff_name}.pdf"
    c = canvas.Canvas(filename, pagesize=(letter[1], letter[0]))  # Set page size to landscape

    # Set default font size and type
    default_font = ("Lucida Bright", 12)
    c.setFont(*default_font)

    # Define text positions
    text_positions = {
        "I, " + trainer_name + ", hereby certify that, ": (letter[1] / 2, 6.5 * inch),
        staff_name : (letter[1] / 2, 6 * inch),
        "Has completed the required training for: ": (letter[1] / 2, 5.5 * inch),
        training: (letter[1] / 2, 5 * inch),
        "Date Completed:": (letter[1] / 2, 4.5 * inch),
        
        "Trainer:": (letter[1] / 2, .9 * inch),
        "-------------------------": (letter[1] / 2, .66 * inch),
        trainer_name: (letter[1] / 2, .33 * inch),        
    }

    # Draw text at specified positions
    for text, position in text_positions.items():
        if text == staff_name:
            c.setFont("Lucida Bright Demibold", 12)  # Set font to bold for staff name
            c.drawCentredString(position[0], position[1], f"{text} {get_field_value(text, training, staff_name, date_completed, trainer_name, time_took)}")
            c.setFont(*default_font)  # Reset font back to default after drawing Staff Name
        elif text == trainer_name and position[1] == .33 * inch:
            c.setFont("Lucida Handwriting", 14)
            c.drawCentredString(position[0], position[1], f"{text} {get_field_value(text, training, staff_name, date_completed, trainer_name, time_took)}")   
        else:
            c.drawCentredString(position[0], position[1], f"{text} {get_field_value(text, training, staff_name, date_completed, trainer_name, time_took)}")

    # Draw "Time Took" value at the top right corner
    c.setFont(*default_font)  # Set font to default
    c.drawRightString(letter[1] - 0.5 * inch, letter[0] - 0.5 * inch, time_took)

    c.save()

def get_field_value(field, training, staff_name, date_completed, trainer_name, time_took):
    if field == "Training:":
        return training
    elif field == "Staff Name:":
        return staff_name
    elif field == "Date Completed:":
        return date_completed
    elif field == "Trainer:":
        return trainer_name
    else:
        return ""

# Example usage
training = "Python Programming"
staff_name = "John Doe"
date_completed = "03/07/2024"
trainer_name = "Jane Smith"
time_took = "2 Hours"

generate_certificate(training, staff_name, date_completed, trainer_name, time_took)
