from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.db.models import Q


# Custome User Model
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username','created_by', 'is_active','is_staff','is_superuser',]
    prepopulated_fields = {'username': ('first_name', 'last_name',)}
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',),
        }),
    )

    # Django ModelAdmin Save Function Called when something be Saved
    def save_model(self, request, obj, form, change):

        """
                This function is called automatically when some data have ben changed or update by This Model
                When user Registered by Gmail then user is not active.
                When you active user from admin panel then user belongs to you, Permanently
                User created_by_id updates as your user_id
        """
        if getattr(obj, 'created_by', None) is None:
            if obj.id != request.user.created_by_id:
                if obj.email != request.user.email:
                    obj.created_by = request.user
        if getattr(obj, 'created_by', None) is not None:
            if obj.created_by_id != request.user.id:
                return
        obj.save()

    # Django ModelAdmin Delete Function Called when Something be Deleted
    def delete_model(self, request, obj):
        """
                This Function call automatically when somene going to delete some data by this Model
                User can only Delete or Deleted by that User that is Belongs to except first user created by terminal
        """
        if obj.id != request.user.created_by_id:
            if obj.created_by_id == request.user.id or (request.user.is_superuser and request.user.created_by_id is None):
                obj.delete()
        return None


    # Django ModelAdmin Function to Check Delete Permissions
    def has_delete_permission(self, request, obj=None):
        """
                This Function check delete permissions
                Hide Delete Button if Object don't have Delete Permission
                By this function i am only hide Delete button by self.user
                user can't be able to delete himself
        """
        return obj is None or obj.pk != request.user.id

    # Modifying Queryset Belongs to ModelAdmin
    def get_queryset(self, request):
        """
                Only show the results belongs to Logged in User
                if user is created by terminal then Show All results
        """
        qs = super(CustomUserAdmin, self).get_queryset(request)

        lookups = (
                Q(created_by=request.user) |
                Q(created_by=None) |
                Q(id=request.user.id)
        )
        if request.user.is_superuser and request.user.created_by_id is None:
            qry = qs.all()
        else:
            qry = qs.filter(lookups).exclude(is_superuser=True, created_by=None)
        return qry.distinct()

    # Django ModelAdmin Function to get Readonly Fields
    def get_readonly_fields(self, request, obj=None):
        """
                Return Readonly fields that is restricted to modify
                User can't be able to Change their user permission or group
                Except User Created by terminal
        """
        if obj and obj.pk == request.user.pk and request.user.created_by_id is None:
            return self.readonly_fields + ('is_active','is_staff','is_superuser',)

        if obj and obj.pk == request.user.pk and request.user.is_superuser and request.user.created_by_id is not None:
            return self.readonly_fields + ('is_active','is_staff','is_superuser','groups', 'user_permissions',)

        return self.readonly_fields

# Disable Multi Select and Delete Action
admin.site.disable_action('delete_selected')
# Register Custome User Admin
admin.site.register(User, CustomUserAdmin)