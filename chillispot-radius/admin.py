from django.contrib import admin
from chillispot-radius.models import  RadiusAttribute
from chillispot-radius.models import  RadiusPassword
from chillispot-radius.models import  RadiusSessionTimeout
from chillispot-radius.models import  RadiusIdleLimit
from chillispot-radius.models import  RadiusBandwidthUpLimit
from chillispot-radius.models import  RadiusBandwidthDownLimit
from chillispot-radius.models import  WifiUser

class WifiUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
    """
    Over-ride admin.ModelAdmin.save_model() to update radius attributes for this user.
    When creating a new WifiUser, we have to create the Radius Attributes first.
    Then, after saving [changes to] the WifiUser, we update the radius username and radius 
    attribute value.
    """
        if not change:
            # We need to create radcheck attributes when adding a new user
            new_attr = RadiusPassword()
            new_attr.save()
            obj.radius_password = new_attr

            new_attr = RadiusSessionTimeout()
            new_attr.save()
            obj.radius_session_timeout = new_attr

            new_attr = RadiusIdleLimit()
            new_attr.save()
            obj.radius_idle_limit = new_attr

            new_attr = RadiusBandwidthUpLimit()
            new_attr.save()
            obj.radius_limit_up = new_attr

            new_attr = RadiusBandwidthDownLimit()
            new_attr.save()
            obj.radius_limit_down = new_attr
        obj.save()
        # Upadate radcheck attributes
        obj.radius_password.update_rad_value(obj.username, obj.password)
        obj.radius_session_timeout.update_rad_value(obj.username, obj.session_timeout)
        obj.radius_idle_limit.update_rad_value(obj.username, obj.idle_limit)
        obj.radius_limit_up.update_rad_value(obj.username, obj.limit_up)
        obj.radius_limit_down.update_rad_value(obj.username, obj.limit_down)

admin.site.register(WifiUser, WifiUserAdmin)
admin.site.register(RadiusPassword)
admin.site.register(RadiusSessionTimeout)
