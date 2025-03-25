from django.shortcuts import render
from .models import PortfolioItem
from datetime import date
from .models import Verse_of_the_day
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from .models import Sermons
from .models import Ministry
from .models import Team
from .models import Event
from .models import Certificate
from django.contrib.auth.models import User
from .models import Usersstatus
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Create your views here.


def signup(request):
    if request.method =='POST':
       username=request.POST['username']
       email=request.POST['email']
       password1=request.POST['password1']
       password2=request.POST['password2']
       if password1==password2:
          if User.objects.filter(username=username).exists():
             messages.info(request,"Username Exists")
             return redirect('signup')
          elif User.objects.filter(email=email).exists():
               messages.info(request,"Email id Exits")
               return redirect('signup')
          else:
            user=User.objects.create_user(username=username,password=password1,email=email)
            user.save();
            user2=Usersstatus.objects.create(username=username,status='0')
            user2.save();
            messages.info(request,"Contact for Admin and Wait for Approval")
            return redirect('signup')
       else:
         messages.info(request,"Password not match")
         return redirect('signup') 
    return render(request,"signup.html")

def index(request):
    portfolio_items = PortfolioItem.objects.all()
    ministry = Ministry.objects.all()
    childministry=Ministry.objects.filter(category='childrens ministry').order_by('-id')[:1]
    youthministry=Ministry.objects.filter(category='youths ministry').order_by('-id')[:1]
    sportministry=Ministry.objects.filter(category='sports ministry').order_by('-id')[:1]
    menministry=Ministry.objects.filter(category='mens ministry').order_by('-id')[:1]
    womenministry=Ministry.objects.filter(category='womens ministry').order_by('-id')[:1]

#sermons
    listout=Sermons.objects.all().order_by('-id')[:6]


    # Get the current date
    today = date.today()
    # Initialize variables for the daily verse and reading
    daily_verse = None

    try:
        daily_verse = Verse_of_the_day.objects.get(date=today)
    except Verse_of_the_day.DoesNotExist:
        daily_verse = None  # or set a default value if necessary

    if request.method == "POST":
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        address = request.POST.get('address')
        message = request.POST.get('message')

        # Save data to the database
        contact_entry = Contact(name=name, mobile_number=mobile_number, address=address, message=message)
        contact_entry.save()

        messages.success(request, "Your message has been sent successfully!")


# our teams


    teams = Team.objects.all()
    
        

    return render(request,"index.html",{'portfolio_items' : portfolio_items ,'daily_verse': daily_verse,'listout' : listout,'ministry' : ministry,
                                        'childministry' : childministry,'youthministry' : youthministry,'sportministry' : sportministry,'menministry' : menministry,'womenministry' : womenministry,
                                        'teams' : teams,})

def blog(request):
    return render(request,"blog.html")

# def blog_details(request):
    return render(request,"blog-details.html")

def sermon(request,id):
    list=Sermons.objects.filter(id=id)
    listout=Sermons.objects.all().order_by('-id')[:5]
    return render(request,"service-details.html",{"list":list,"listout":listout,'active_sermon_id': id,})

def events(request):
    events=Event.objects.all().order_by('-date')[:1]
    return render(request,"event.html",{"event":events,})

# def member(request):
#     return render(request,"member.html",)


def base(request):
    return render(request,"base.html")

# def login(request):
#     return render(request,"login.html")

def child(request):
    childministry=Ministry.objects.filter(category='childrens ministry').order_by('-id')
    return render(request,"ministries/Childrens_ministry.html",{"childministry" : childministry})

def youth(request):
    youthministry=Ministry.objects.filter(category='youths ministry')
    return render(request,"ministries/youths_ministry.html",{"youthministry" : youthministry})

def sport(request):
    sportministry=Ministry.objects.filter(category='sports ministry')
    return render(request,"ministries/sports_ministry.html",{"sportministry" : sportministry})

def men(request):
    menministry=Ministry.objects.filter(category='mens ministry')
    return render(request,"ministries/mens_ministry.html",{"menministry" : menministry})

def women(request):
    womenministry=Ministry.objects.filter(category='womens ministry')
    return render(request,"ministries/womens_ministry.html",{"womenministry" : womenministry})

def sermon_details(request):

    sermons = Sermons.objects.all().order_by('-id')

    return render(request,"sermon_details.html",{'sermons': sermons,})
    

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Correct usage with two arguments
            if request.session.get('userlogin'):
               print("Session is active")
            if Usersstatus.objects.filter(username=username).filter(status='1'):
               request.session['userlogin'] = True
               return redirect("dashboard")  # Redirect to the home page after login
            else:
                messages.error(request,"you need to approvel from admin")
        
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")  # Show login form


@login_required
def dashboard(request):
    certfile=0
    username=request.user.username
    print("username",username)
    profile = ChurchMember.objects.filter(username=username)
    file=Certificate.objects.filter(name=username)
    if ChurchMember.objects.filter(username=username).exists():
       if Certificate.objects.filter(name=username).exists():
          certfile=1
          # Show success message
          getdetails=Certificate.objects.get(name=username)
          certificatestatus=getdetails.certificatestatus
          if certificatestatus == 0:
             messages.success(request, "Wait for Admin Approval")
       return render(request, "dashboard.html",{"profile":profile,"file":file,"certfile":certfile})
    else:
        return render(request, "member.html",)

def user_logout(request):
    print("INSIDE THE LOGOUT")
    request.session['userlogin'] = False
    return redirect("/")  # Redirect to login page after logout



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Sermons

def sermon_list(request):
    sermons = Sermons.objects.all()
    return render(request, 'sermons_list.html', {'sermons': sermons})

def sermon_detail(request, pk):
    sermon = get_object_or_404(Sermons, pk=pk)
    return render(request, 'sermon_detail.html', {'sermon': sermon})

def sermon_json(request):
    sermons = list(Sermons.objects.values())
    return JsonResponse({'sermons': sermons})


#memberships form
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import ChurchMember

# def member(request):
#     """Renders the church membership form page."""
#     return render(request, "member.html")

# def register_member(request):
#     """Handles church membership form submission."""
#     if request.method == "POST":
#         full_name = request.POST.get("full_name")
#         dob = request.POST.get("dob")
#         gender = request.POST.get("gender")
#         marital_status = request.POST.get("marital_status")
#         phone = request.POST.get("phone")
#         emergency_phone = request.POST.get("emergency_phone")
#         email = request.POST.get("email")
#         resident_name = request.POST.get("residentName")
#         street = request.POST.get("street")
#         city = request.POST.get("city")
#         postal_code = request.POST.get("postalCode")
#         door_number = request.POST.get("doorNumber")
#         area = request.POST.get("area")
#         district = request.POST.get("district")
#         church_transfer = request.POST.get("church_transfer", "")
#         previous_church = request.POST.get("previous_church", "")
#         ministry_interest = request.POST.get("ministry_interest")
#         occupation = request.POST.get("occupation")
#         agreement = request.POST.get("agreement") == "on"  # Checkbox handling

#         # Save to database
#         ChurchMember.objects.create(
#             full_name=full_name,
#             dob=dob,
#             gender=gender,
#             marital_status=marital_status,
#             phone=phone,
#             emergency_phone=emergency_phone,
#             email=email,
#             resident_name=resident_name,
#             street=street,
#             city=city,
#             postal_code=postal_code,
#             door_number=door_number,
#             area=area,
#             district=district,
#             church_transfer=church_transfer,
#             previous_church=previous_church,
#             ministry_interest=ministry_interest,
#             occupation=occupation,
#             agreement=agreement
#         )

#         # Display success message
#         messages.success(request, "Data submitted successfully!")

#         return redirect("member")  # Redirect back to form after submission

#     return render(request, "member.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ChurchMember

def member(request):
    if request.method == "POST":
        profile_image = request.FILES['profile_image']
        full_name = request.POST.get("full_name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        marital_status = request.POST.get("marital_status")
        phone = request.POST.get("phone")
        emergency_phone = request.POST.get("emergency_phone")
        email = request.POST.get("email")
        resident_name = request.POST.get("residentName")
        street = request.POST.get("street")
        city = request.POST.get("city")
        postal_code = request.POST.get("postalCode")
        door_number = request.POST.get("doorNumber")
        area = request.POST.get("area")
        district = request.POST.get("district")
        church_transfer = request.POST.get("church_transfer")
        previous_church = request.POST.get("previous_church")
        ministry_interest = request.POST.get("ministry_interest")
        occupation = request.POST.get("occupation")
        agreement = request.POST.get("agreement") == "on"

        # Save data in the database
        ChurchMember.objects.create(
            profile_image=profile_image,
            full_name=full_name,
            dob=dob,
            gender=gender,
            marital_status=marital_status,
            phone=phone,
            emergency_phone=emergency_phone,
            email=email,
            resident_name=resident_name,
            street=street,
            city=city,
            postal_code=postal_code,
            door_number=door_number,
            area=area,
            district=district,
            church_transfer=church_transfer,
            previous_church=previous_church,
            ministry_interest=ministry_interest,
            occupation=occupation,
            agreement=agreement,
            username=request.user.username,
        )

        # Show success message
        messages.success(request, "Data submitted successfully!")
        return redirect("member")  # Redirect back to form page after submission

    return render(request, "member.html")

from django.shortcuts import render

def register_member(request):
    return render(request, "register.html")  # Ensure 'register.html' exists inside templates folder


# member edit

def memberedit(request,id):
    edit=ChurchMember.objects.filter(id=id)

    if request.method == "POST":
        # profile_image = request.FILES['profile_image']
        full_name = request.POST.get("full_name")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        marital_status = request.POST.get("marital_status")
        phone = request.POST.get("phone")
        emergency_phone = request.POST.get("emergency_phone")
        email = request.POST.get("email")
        resident_name = request.POST.get("residentName")
        street = request.POST.get("street")
        city = request.POST.get("city")
        postal_code = request.POST.get("postalCode")
        door_number = request.POST.get("doorNumber")
        area = request.POST.get("area")
        district = request.POST.get("district")
        church_transfer = request.POST.get("church_transfer")
        previous_church = request.POST.get("previous_church")
        ministry_interest = request.POST.get("ministry_interest")
        occupation = request.POST.get("occupation")
        agreement = request.POST.get("agreement")
        print("fullname",full_name)
        # Save data in the database
        memberedit=ChurchMember.objects.get(id=id)
        # profile_image=profile_image,
        memberedit.full_name=full_name
        memberedit.gender=gender
        memberedit.marital_status=marital_status
        memberedit.phone=phone
        memberedit.emergency_phone=emergency_phone
        memberedit.email=email
        memberedit.resident_name=resident_name
        memberedit.street=street
        memberedit.city=city
        memberedit.postal_code=postal_code
        memberedit.door_number=door_number
        memberedit.area=area
        memberedit.district=district
        memberedit.church_transfer=church_transfer
        memberedit.previous_church=previous_church
        memberedit.ministry_interest=ministry_interest
        memberedit.occupation=occupation
        # memberedit.agreement=agreement,
        memberedit.save()
        if not dob:
              memberedit.dob=None,
        if request.FILES:
            profile_image=request.FILES.get('profile_image')
            membereditfile=ChurchMember.objects.get(id=id)
            if profile_image:
                membereditfile.profile_image=profile_image
            membereditfile.save()
            # Show success message
        messages.success(request, "Data submitted successfully!")
    return render(request, "memberedit.html",{"edit":edit})

def generate_certificate12(name):
    cert = Image.open("certificate.jpeg")
    draw = ImageDraw.Draw(cert)
    
    font = ImageFont.truetype("arial.ttf", 50)
    draw.text((550, 600), name, font=font, fill="black")

    directory = r"D:\python\myproject\church_project\media\store\images\certificate"  # Use raw string to handle backslashes
    if not os.path.exists(directory):
        os.makedirs(directory)

    img_io = BytesIO()
    cert.save(img_io, format="JPEG")
    img_io.seek(0)
    
    
    

    certificate_instance = Certificate(name=name)
    certificate_instance.certificate.save(f"{name}.jpeg", File(img_io), save=True)    
    
    # Use the full path when saving the file
    cert.save(os.path.join(directory, f"{name}.jpeg"))


# def generate_certificate(name):
#     # Load certificate template image
#     template_path = "certificate.png"
#     if not os.path.exists(template_path):
#         raise FileNotFoundError("Certificate template not found!")

#     cert = Image.open(template_path) 

#     # Draw text on certificate
#     draw = ImageDraw.Draw(cert)
    
#     try:
#         font = ImageFont.truetype("arial.ttf", 50)  
#     except IOError:
#         font = ImageFont.load_default()  

#     text_position = (550, 600)  
#     draw.text(text_position, name, font=font, fill="black")

#     # Save as temporary image
#     temp_image_path = f"{name}_temp.png"
#     cert.save(temp_image_path, format="PNG")

#     # Convert Image to PDF
#     pdf_io = BytesIO()
#     c = canvas.Canvas(pdf_io, pagesize=letter)
#     c.drawImage(temp_image_path, 50, 300, width=500, height=400)  # Adjust position & size
#     c.showPage()
#     c.save()

#     pdf_io.seek(0)  # Reset pointer

#     # Save to Django Model
#     certificate_instance = Certificate(name=name)
#     certificate_instance.certificate.save(f"{name}.pdf", File(pdf_io), save=True)
#     certificate_instance.save()  

#     # Remove temporary image
#     os.remove(temp_image_path)

#     print(f"Certificate saved as {certificate_instance.certificate.url}")


# def generate_certificate(name):
#     # Load certificate template image
#     template_path = "certificate.png"
#     if not os.path.exists(template_path):
#         raise FileNotFoundError("Certificate template not found!")

#     cert = Image.open(template_path)
#     draw = ImageDraw.Draw(cert)

#     # Define max width for text placement
#     max_width = 800  # Adjust based on your certificate template
#     text_y_position = 600  # Adjust based on template

#     # Dynamically adjust font size
#     font_size = 50  # Start with a large font size
#     font_path = "arial.ttf"  # Ensure the font file is available

#     try:
#         font = ImageFont.truetype(font_path, font_size)
#     except IOError:
#         font = ImageFont.load_default()

#     # Reduce font size until the text fits within max_width
#     while font.getsize(name)[0] > max_width and font_size > 10:
#         font_size -= 2
#         font = ImageFont.truetype(font_path, font_size)

#     # Center text horizontally
#     text_width = font.getsize(name)[0]
#     image_width = cert.width
#     text_x_position = (image_width - text_width) // 2  # Center horizontally

#     # Draw text
#     draw.text((text_x_position, text_y_position), name, font=font, fill="black")

#     # Save as temporary image
#     temp_image_path = f"{name}_temp.png"
#     cert.save(temp_image_path, format="PNG")

#     # Convert Image to PDF
#     pdf_io = BytesIO()
#     c = canvas.Canvas(pdf_io, pagesize=letter)
#     c.drawImage(temp_image_path, 50, 300, width=500, height=400)  # Adjust position & size
#     c.showPage()
#     c.save()

#     pdf_io.seek(0)  # Reset pointer

#     # Save to Django Model
#     certificate_instance = Certificate(name=name)
#     certificate_instance.certificate.save(f"{name}.pdf", File(pdf_io), save=True)
#     certificate_instance.save()

#     # Remove temporary image
#     os.remove(temp_image_path)

#     print(f"Certificate saved as {certificate_instance.certificate.url}")


def generate_certificate(name):
    # Load certificate template image
    template_path = "certificate.png"
    if not os.path.exists(template_path):
        raise FileNotFoundError("Certificate template not found!")

    cert = Image.open(template_path)
    draw = ImageDraw.Draw(cert)

    # Define max width for text placement
    max_width = 800  # Adjust based on your certificate template
    # text_y_position = 600  # Adjust based on template
    text_y_position = 1400

    # Dynamically adjust font size
    # font_size = 50  # Start with a large font size
    font_size = 100  # Start with a large font size
    font_path = "arial.ttf"  # Ensure the font file is available

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()

    # Reduce font size until the text fits within max_width
    while font.getbbox(name)[2] > max_width and font_size > 10:  # getbbox()[2] gives text width
        font_size -= 2
        font = ImageFont.truetype(font_path, font_size)

    # Center text horizontally
    text_width = font.getbbox(name)[2]  # Width of the text
    image_width = cert.width
    text_x_position = (image_width - text_width) // 2  # Center horizontally

    # Draw text
    draw.text((text_x_position, text_y_position), name, font=font, fill="black")

    # Save as temporary image
    temp_image_path = f"{name}_temp.png"
    cert.save(temp_image_path, format="PNG")

    # Convert Image to PDF
    pdf_io = BytesIO()
    c = canvas.Canvas(pdf_io, pagesize=letter)
    c.drawImage(temp_image_path, 50, 300, width=500, height=400)  # Adjust position & size
    # c.drawImage(temp_image_path, 50, 300, width=500, height=400)  # Adjust position & size
    c.showPage()
    c.save()

    pdf_io.seek(0)  # Reset pointer

    # Save to Django Model
    certificate_instance = Certificate(name=name)
    certificate_instance.certificate.save(f"{name}.pdf", File(pdf_io), save=True)
    certificate_instance.save()

    # Remove temporary image
    os.remove(temp_image_path)

    print(f"Certificate saved as {certificate_instance.certificate.url}")

def certificate(request):
    name=request.user.username
    generate_certificate(name)
    return redirect('dashboard')