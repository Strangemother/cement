from django.shortcuts import render
from trim.views import TemplateView

class ViewBreak(object):
    is_break = True
    def __init__(self, **kw):
        self.__dict__.update(kw)


class ImgDef(object):
    is_break = False

    def __init__(self, path, **kw):
        self.path = path
        self.__dict__.update(kw)


IMAGES = (
    ImgDef('a/a3.png'),
    ImgDef('a/a5.png'),
    ImgDef('a/a1.png'),
    ImgDef('a/a4.png'),
    ImgDef('a/a2.png'),

    ViewBreak(),
    ImgDef('c/12.png'),
    ImgDef('c/21.png'),
    ImgDef('c/24.png'),
    ImgDef('c/22.png'),

    ViewBreak(),
    ImgDef('card-a.png'),
    ImgDef('card-b.png'),
    ImgDef('card-c.png'),
    ImgDef('cartoon-a.png'),
    ImgDef('cartoon-b.png'),
    ImgDef('high-a.png'),
    ImgDef('high-b.png'),
    ImgDef('high-c.png'),
    ImgDef('spot-a.png'),

    ViewBreak(
        footer_template_name='mockups/smokejumpers/viewbreak-heros.html'
        ),
    ImgDef('hero/15.png'),
    ImgDef('hero/18.png'),
    ImgDef('hero/19.png'),
    ImgDef('hero/10.png'),
    ImgDef('hero/17.png'),
    ImgDef('hero/25.png'),
)


class SwatchImageListView(TemplateView):
    template_name = 'mockups/smokejumpers-images.html'

    def get_context_data(self, **kwargs):
        kwargs['definitions'] = self.get_image_definitions()
        return super().get_context_data(**kwargs)

    def get_image_definitions(self):
        return IMAGES