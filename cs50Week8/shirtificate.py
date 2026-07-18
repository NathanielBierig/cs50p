from fpdf import FPDF
import os


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page(format="a4", orientation="portrait")
    pdf.draw_shirt()
    pdf.draw_name(name)  

    filename = f"{name}'s_shirtificate.pdf"
    pdf.output(filename)
    print(f"Created File: {filename}")
    os.startfile(filename)


class PDF(FPDF):
    

    def header(self):
        self.set_font("Helvetica", "B", 40)
        self.cell(0, 20, "CS50 Shirtificate", align="C")
        self.ln(10)


    def draw_shirt(self):
        self.image(
        "shirtificate.png",
            x=10,
            y=60,
            w=190
    )

    def draw_name(self, name):
        self.set_font("Helvetica", "B", 32)
        self.set_text_color(255, 255, 255)
        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")
        


if __name__ == "__main__":
    main()