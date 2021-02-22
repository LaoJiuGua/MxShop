from rest_framework import permissions

class UserOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method == permissions.SAFE_METHODS:
            return True

        # obj相当于数据库中的model，这里要改成我们数据库中的user
        return obj.user == request.user
