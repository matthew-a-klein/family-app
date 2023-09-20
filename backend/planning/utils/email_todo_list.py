from ..models import TodoListItem
from django.core.mail import send_mail
from backend.settings import EMAIL_HOST_USER



def email_todo_list(recipient):
    html_message = generate_todo_list_html()
    send_mail(
    subject="Your to do List",
    message="",
    from_email=EMAIL_HOST_USER,
    recipient_list=[recipient],
    fail_silently=False,
    html_message=html_message, 
   
    )
    
def generate_todo_list_html():
    items = TodoListItem.objects.all()  # Retrieve all items from the Item model
    
    # Create an HTML string
    html_content = f"<h3>This is your to do list for today</h3><ul>"
    
    for item in items:
        html_content += f"<li>{item.name}</li>"
    
    html_content += "</ul>"
    
    return html_content
    