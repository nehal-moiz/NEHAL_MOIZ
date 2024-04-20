from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", x=15, y=80, w=180)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "", 50)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        name = input('Name: ')
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-150)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "", 20)
        self.set_text_color(255, 255, 255)
        self.cell(80)
        self.cell(30, -10, f'{name} took CS50', align="C")
        # Printing page number:
        #self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
