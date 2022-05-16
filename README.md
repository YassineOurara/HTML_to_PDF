# HTML_to_PDF
Converting HTML to Pdf in Django

1_Installing xhtml2pdf
  pip install xhtml2pdf
  
2_Creating utils.py file

3_Creating a Template
    Now create a directory templates and inside this create a html file and named it as hello.html.
    Now write the code in hello.html .
   

4_Rendering Template

    Now for rendering template we have to create a view.
    Now inside  our app(HTMLtoPDF)  create a views.py file.
    If you are not familiar with what is view then don’t worry – Views are just python function. Views take user request and give them back something.
    Now write the code in views.py .

5_Defining a URL
    Write the code in urls.py.

6_Defining Template Directory in Settings
    And now this is the most important point to be noted.If we don’t do this then get a template not found error.For avoiding this error, 
    we have to set templates/ in settings.py file.It is essential to render the pdf.

7_Running Your Project
    python manage.py runserver
 


