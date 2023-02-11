import pytest
from django.test import RequestFactory, TestCase

from tests.factories import CommentFactory
from Apres_Ski_API.views.comment import CommentViewSet

class CommentViewTests(TestCase):
  def test_comment_200_OK(self):
    comment = CommentFactory()
    request = RequestFactory().get(f"api/v1/comment/{comment.pk}")
    view = CommentViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=comment.pk)
    assert response.status_code == 200
    assert response.data['id'] == comment.id

  def test_comment_get_all(self): 
    CommentFactory.create_batch(4)
    request = RequestFactory().get(f"api/v1/comment/")
    view = CommentViewSet.as_view({'get': 'list'})
    response = view(request)
    assert response.status_code == 200 
    assert len(response.data) == 4


  def test_commment_post(self): 

    comment = {"comment": "Terrible food", "restaurant": , "user": }
    request = RequestFactory().post("api/v1/comment/", comment)
    view = CommentViewSet.as_view({'post': 'create'})
    assert not Comment.objects.exists()
    data = json.dumps(comment)
    response = view(request, data)
    assert response.status_code == 201
    assert Comment.objects.count() == 1
    assert Comment.objects.get(pk = 1).comment == "Terrible food"

  def test_comment_delete(self):
    comment = CommentFactory()
    assert Comment.objects.count() == 1
    request = RequestFactory().delete(f"api/v1/comment/{comment.pk}")
    view = CommentViewSet.as_view({'delete': 'destroy'})
    response = view(request, pk=comment.pk)
    assert not Comment.objcts.exists()
    assert response.status_code == 204

  def test_comment_patch(self): 
    comment = CommentFactory(comment = 'Actually good food')
    comment_update = {"data": {"type": "Comment", "id": f"{comment.pk}", "attributes": {"comment": "Terrible food" } } }
    data = json.dumps(comment_update)
    request = RequestFactory().patch(f"api/v1/comment/{comment.pk}", data, content_type='application/vnd.api+json')
    view = CommentViewSet.as_view({'patch': 'partial_update'})
    response = view(request, pk=comment.pk)
    updated_comment = Comment.objects.get(pk = comment.pk)
    assert updated_comment.coment == "Terrible food"
    assert response.status_code == 200 

  def test_user_404(self):
    comment = CommentFactory()
    request = RequestFactory().get(f"api/v1/comment/{comment.pk + 1}")
    view = CommentViewSet.as_view({'get': 'retrieve'})
    response = view(request, pk=comment.pk + 1)
    assert response.status_code == 404
    