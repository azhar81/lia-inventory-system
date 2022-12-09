from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    """
    The request is authenticated as a staff/admin, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_staff
        )

class IsJanitor(BasePermission):
  """
  The request is authenticated as a janitor.
  """

  def has_permission(self, request, view):
      return bool(
          request.user and
          request.user.employee.role == 'Janitor'
      )

class IsTechnician(BasePermission):
  """
  The request is authenticated as a janitor.
  """

  def has_permission(self, request, view):
      return bool(
          request.user and
          request.user.employee.role == 'Technician'
      )