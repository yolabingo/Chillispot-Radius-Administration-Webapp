from django.db import models

class RadiusAttribute(models.Model):
    username = models.CharField(max_length=64, default="changeme")
    op = models.CharField(max_length=2, default=':=', editable=False)
    attribute = models.CharField(max_length=32, default='Over-ride Me', editable=False)
    value = models.CharField( max_length=252, blank=True )

    def save(self, *args, **kwargs):
        self.attribute = 'User-Password'
        super(RadiusAttribute, self).save(*args, **kwargs)

    # Called by admin 
    def update_rad_value(self, user, val):
        self.username = user
        self.value = val
        self.save()
    
    class Meta:
        db_table = 'radcheck'

class RadiusPassword(RadiusAttribute):
    def save(self, *args, **kwargs):
        self.attribute = 'User-Password'
        super(RadiusAttribute, self).save(*args, **kwargs)

    class Meta:
        proxy = True

class RadiusSessionTimeout(RadiusAttribute):
    def save(self, *args, **kwargs):
        self.attribute = 'Session-Timeout'
        super(RadiusAttribute, self).save(*args, **kwargs)
    class Meta:
        proxy = True

class RadiusIdleLimit(RadiusAttribute):
    def save(self, *args, **kwargs):
        self.attribute = 'Idle-Limit'
        super(RadiusAttribute, self).save(*args, **kwargs)
    class Meta:
        proxy = True

class RadiusBandwidthUpLimit(RadiusAttribute):
    def save(self, *args, **kwargs):
        self.attribute = 'ChilliSpot-Bandwidth-Max-Up'
        super(RadiusAttribute, self).save(*args, **kwargs)
    class Meta:
        proxy = True

class RadiusBandwidthDownLimit(RadiusAttribute):
    def save(self, *args, **kwargs):
        self.attribute = 'ChilliSpot-Bandwidth-Max-Down'
        super(RadiusAttribute, self).save(*args, **kwargs)
    class Meta:
        proxy = True

class WifiUser(models.Model):
    username =  models.CharField( max_length=64 )
    first_name =  models.CharField( max_length=64 )
    last_name =  models.CharField( max_length=64 )

    password =  models.CharField( max_length=64 )
    session_timeout = models.CharField( max_length=64, blank=True, default='86400' )
    idle_limit = models.CharField( max_length=64, blank=True, default='7200' )
    limit_up = models.CharField( max_length=64, blank=True, default='0' )
    limit_down = models.CharField( max_length=64, blank=True, default='0' )


    radius_password = models.OneToOneField(RadiusPassword, editable=False, related_name='wifi_user')
    radius_session_timeout = models.OneToOneField(RadiusSessionTimeout, editable=False, related_name='wifi_user')
    radius_idle_limit = models.OneToOneField(RadiusIdleLimit, editable=False, related_name='wifi_user')
    radius_limit_up = models.OneToOneField(RadiusBandwidthUpLimit, editable=False, related_name='wifi_user')
    radius_limit_down = models.OneToOneField(RadiusBandwidthDownLimit, editable=False, related_name='wifi_user')
  
    def __unicode__(self):
        return u'%s' % (self.username)

    class Meta:
        verbose_name = 'Wi-Fi User'
    
