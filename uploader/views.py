from django.shortcuts import render
from .models import Photo
from .form import PhotoForm
from django.shortcuts import redirect


def upload(request):

	if request.method == 'POST':
		form = PhotoForm(data=request.POST, files=request.FILES)

		# if form is valid we save name and picture and send user to success page
		if form.is_valid():
			form.save()
			context = {
				'obj' : form.instance
			}
			return render(request, "success.html", context)

	# this allows us to display all the pictures in the home page
	else:
		form = PhotoForm()
		pic = Photo.objects.all()
		context ={
			'pic' : pic,
			'form' : form
		}
		return render(request, "upload_form.html", context)


def edit(request, id):

	photo = Photo.objects.get(id=id)
	form = PhotoForm(instance=photo)

	if request.method == 'POST':

		# user hits cancel button
		if 'cancel' in request.POST:
			return redirect('/')

		# user hits delete button
		if 'delete' in request.POST:
			photo.delete()
			return redirect('/')

		# User hits save, we save updates and redirect to home page
		form = PhotoForm(data=request.POST, instance=photo, files=request.FILES)
		if form.is_valid():
			form.save()
			context = {
				'obj' : form.instance
			}
			return redirect('/')
	else:
		context ={
			'obj': form.instance,
			'form':form
		}
		return render(request, "edit.html", context)
