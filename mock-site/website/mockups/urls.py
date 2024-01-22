from trim import urls
from . import views


app_name = 'mockups'

urlpatterns = urls.as_templates(
    sphinx=('', 'mockups/sphinx.html'),
    smokejumpers=('smokejumpers/', 'mockups/smokejumpers.html'),
    # smokejumpers_images=('smokejumpers/images/', 'mockups/smokejumpers-images.html'),
    cinderblock=('cinderblock/', 'mockups/cinderblock.html'),
    # crystal_mockup=('mockup/1/', 'mockup/crystal-1.html'),
    # home=('mockup/home/', 'mockup/home.html'),
    # v1_article=('mockup/article/', 'mockup/v1-article.html'),
    # advert_cell=('advert/1/', 'small_adverts.html')
    smokejumpers_design=('smokejumpers/design/', 'mockups/smokejumpers/smokejumpers-design.html'),
)

urlpatterns += urls.paths_named(views,
    smokejumpers_images=('SwatchImageListView', 'smokejumpers/images/',),
)