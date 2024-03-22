

from django.db import models
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    BaseSiteSetting,
    register_setting,
)

# @register_setting
# class GenericSocialMediaSettings(BaseGenericSetting):
#     facebook = models.URLField()

from trim.models import fields

@register_setting(icon='placeholder')
class SiteBrandSettings(BaseSiteSetting):
    id = models.AutoField(primary_key=True)
    site_brand_name = fields.chars(
        help_text='The short website brand name such as "Acme"')
    site_brand_name = fields.chars(
        help_text='The full brand name such as "Acme Labs Incoporated"')

    class Meta:
        verbose_name = "Brand"


# @register_setting
# class SiteSpecificSocialMediaSettings(BaseSiteSetting):
#     facebook = models.URLField()