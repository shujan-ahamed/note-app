from django.urls import path
from .views import Index, CreateNoteView, SignUpView, PrivateNoteView, NoteDeleteView, Search


urlpatterns = [
    path('public/', Index.as_view(), name="index"),
    path('create', CreateNoteView.as_view(), name="create-note"),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name="note-delete"),
    path('private_note', PrivateNoteView.as_view(), name="private-note"),
    path("signup", SignUpView.as_view(), name="signup"),
    path("search", Search.as_view(), name="search"),

]


