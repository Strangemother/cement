from trim import urls
from . import views


app_name = 'mockups'

# urlpatterns = urls.paths_named(views,
#     name=('ClassNamedView', 'my/url/',),
# )

urlpatterns = urls.as_templates(
    one=('', 'mockups/one.html'),
    # crystal_mockup=('mockup/1/', 'mockup/crystal-1.html'),
    # home=('mockup/home/', 'mockup/home.html'),
    # v1_article=('mockup/article/', 'mockup/v1-article.html'),
    # advert_cell=('advert/1/', 'small_adverts.html')
)