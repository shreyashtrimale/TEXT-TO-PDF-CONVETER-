from fpdf import FPDF
import flet as ft
import os
import webbrowser  # for auto-opening PDF after save

def main(page: ft.Page):
    page.title = "PDF GENERATOR"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30

    # Text field for entering content
    content_textfield = ft.TextField(
        label="Enter your Content",
        multiline=True,
        min_lines=10,
        max_length=2000,  # allow more text
        width=600
    )

    # Text widget to show preview inside app
    preview_text = ft.Text("", size=14)

    def generate_pdf(e):
        # Validate input
        if not content_textfield.value.strip():
            content_textfield.error_text = "Content cannot be empty"
            page.update()
            return

        content_textfield.error_text = None
        page.update()

        # ✅ Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=16)

        # Add title
        pdf.cell(200, 10, txt="Generated PDF Document", ln=True, align="C")
        pdf.ln(10)  # Add space

        # Add user content
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content_textfield.value)

        # ✅ Save to Desktop folder
        filename = os.path.expanduser(
            r"C:\Users\91842\Desktop\pdftxt\generated_document.pdf"
        )
        pdf.output(filename)  # Proper file save

        # ✅ Show preview inside app
        preview_text.value = f"Preview:\n\n{content_textfield.value}"

        # ✅ Show success message
        page.snack_bar = ft.SnackBar(ft.Text(f"✅ PDF saved at: {filename}"))
        page.snack_bar.open = True
        page.update()

        # ✅ Auto-open the PDF in default viewer
        webbrowser.open_new(filename)

    # Title text in app
    title = ft.Text("PDF GENERATOR", size=30, weight="bold")

    # Button to generate PDF
    generate_btn = ft.ElevatedButton(
        text="Generate PDF",
        icon=ft.Icon(name="picture_as_pdf"),
        on_click=generate_pdf
    )

    # Add everything to the page
    page.add(
        ft.Column(
            [title, content_textfield, generate_btn, preview_text],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Run app
ft.app(target=main)
