from rest_framework import routers

from .api import (
        WorkSpaceViewSet,
        AllNotesViewSet
    )

router = routers.DefaultRouter()
router.register(r'notes', AllNotesViewSet)
router.register(r'workspaces', WorkSpaceViewSet)

urlpatterns = router.urls
