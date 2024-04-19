# Create your tests here. automated test cases

from django.test import TestCase
from .models import Note
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from django.urls import reverse

class NoteUploadTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.pdf_file = SimpleUploadedFile('test.pdf', b'test content')

    def test_note_upload(self):
        # Create a note with a PDF file attached
        note = Note.objects.create(title='Test Note', content='Test content', user=self.user, pdf_file=self.pdf_file)
        # Assert that the note was created successfully
        self.assertEqual(Note.objects.count(), 1)

class NoteDeleteTestCase(TestCase):
    def test_successful_deletion(self):
        response = self.client.delete(reverse('delete_note', kwargs={'note_id': 1}))
        self.assertEqual(response.status_code, 204)

    def test_non_existent_note(self):
        response = self.client.delete(reverse('delete_note', kwargs={'note_id': 999}))
        self.assertEqual(response.status_code, 404)

    def test_invalid_request_method(self):
        response = self.client.get(reverse('delete_note', kwargs={'note_id': 1}))
        self.assertEqual(response.status_code, 405)