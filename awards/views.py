from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm, ProfileForm, DesignForm, ContentForm, UsabilityForm
from .models import Project, Profile
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfSerializer, ProjectSerializer
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import status


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-posted_on')
    form = DesignForm()
    form = UsabilityForm()
    form = ContentForm()
    return render(request, 'index.html', locals())


# @login_required(login_url='/accounts/login/')
def new_project(request):
    """
    Function that enables one to upload projects
    """
    profile = Profile.objects.all()
    for profile in profile:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                pro = form.save(commit=False)
                pro.profile = profile
                pro.user = request.user
                pro.save()
            return redirect('landing')
        else:
            form = ProjectForm()
    return render(request, 'new_pro.html', {"form": form})


# @login_required(login_url='/accounts/login/')
def edit_profile(request):
    """
    Function that enables one to edit their profile information
    """
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('landing')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit-profile.html', {
        "form": form,
    })


# @login_required(login_url='/accounts/login/')
def view_project(request, id):
    """
    Function that enables one to view specific project
    """
    title = "View Project"
    project = Project.get_pro_by_id(id=id)

    return render(request, 'view_project.html', locals())


# @login_required(login_url='/accounts/login/')
def profile(request, user_id):
    """
    Function that enables one to see their profile
    """
    title = "Profile"
    pros = Project.get_pro_by_user(id=user_id).order_by('-posted_on')
    profiles = Profile.objects.get(user_id=user_id)
    users = User.objects.get(id=user_id)
    return render(request, 'profile/profile.html', locals())


def search_results(request):

    if 'pro' in request.GET and request.GET["pro"]:
        search_term = request.GET.get("pro")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {
            "message": message,
            "pros": searched_projects
        })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


class ProfList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, format=None):
        all_merchprof = Profile.objects.all()
        serializers = ProfSerializer(all_merchprof, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, format=None):
        all_merchproj = Project.objects.all()
        serializers = ProjectSerializer(all_merchproj, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# @login_required(login_url='/accounts/login/')
def add_design(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        form = DesignForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile
            rate.save()
        return redirect('landing')
    else:
        form = DesignForm()

    return render(request, 'index.html', {'form': form})


# @login_required(login_url='/accounts/login/')
def add_usability(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        form = UsabilityForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('landing')
    else:
        form = UsabilityForm()

    return render(request, 'index.html', {'form': form})


# @login_required(login_url='/accounts/login/')
def add_content(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.project = project
            rate.user_name = request.user
            rate.profile = request.user.profile

            rate.save()
        return redirect('landing')
    else:
        form = ContentForm()

    return render(request, 'index.html', {'form': form})
