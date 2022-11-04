from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
  """
  Custom permission to only allow Admins to edit.
  """

  def is_admin(self, request):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    if request.method in permissions.SAFE_METHODS:
      return True

    print('------------------------------')
    print(request.user.is_staff)

    return True
