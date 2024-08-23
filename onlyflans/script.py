import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlyflans.settings')
django.setup()

from web.services import create_flan

flan_1 = create_flan("Flan Tradicional", "Un flan tradicional hecho con ingredientes frescos y naturales. Su textura suave y su sabor dulce y cremoso lo convierten en un deleite atemporal.", "https://imag.bonviveur.com/flan-de-huevo-casero.jpg", "flan-tradicional", False, 2500 )

flan_2 = create_flan("Flan de Café", "Una deliciosa variante del flan tradicional, infusionada con café colombiano de alta calidad. Perfecto para los amantes del café.", "https://imag.bonviveur.com/flan-de-cafe.jpg", "flan-cafe", True, 2950)

flan_3 = create_flan("Flan de Caramelo", "Nuestro flan clásico bañado en una rica y espesa capa de caramelo. El equilibrio perfecto entre lo dulce y lo cremoso.", "https://t1.uc.ltmcdn.com/es/posts/3/5/4/como_hacer_flan_de_caramelo_30453_orig.jpg", "flan-caramelo", False, 2500)

flan_4 = create_flan("Flan de Turrón", "Un exquisito flan que incorpora la dulzura y la textura distintiva del turrón. Perfecto para quienes buscan un postre que combine tradición y sabor en cada bocado.", "https://www.arrozsos.es/wp-content/uploads/2020/12/Flan-de-turro%CC%81n-con-pasas.jpg", "flan-turron", True, 3200)

flan_5 = create_flan("Flan De Chocolate", "Un flan con un profundo y rico sabor a chocolate, ideal para los amantes de los postres intensos y chocolatosos.", "https://imag.bonviveur.com/flan-de-chocolate.jpg", "flan-chocolate", False, 2950)

flan_6 = create_flan("Chocoflan", "Una sorprendente combinación de flan cremoso y pastel de chocolate esponjoso. Este postre de dos capas ofrece lo mejor de ambos mundos en cada bocado, con la dulzura y suavidad del flan complementando perfectamente la riqueza del chocolate.", "https://imag.bonviveur.com/chocoflan.webp", "chocoflan", True, 5200)

flan_7 = create_flan("Flan Familiar", "Flan en sus diferentes variedades, esta vez en tamaño familiar.", "https://dgari.com/wp-content/uploads/2021/08/flan-de-coco-y-caramelo.jpg", "flan-familiar", False, 12500)

flan_8 = create_flan("Flan De Queso de Burgos", "Un delicioso flan elaborado con auténtico Queso de Burgos, que aporta una textura suave y un sabor ligeramente salado. Ideal para aquellos que buscan una variante del flan tradicional con un toque de queso español.", "https://assets.tmecosys.com/image/upload/t_web600x528/img/recipe/ras/Assets/3EA492B0-ABCB-40A4-B6A1-D9FA3D800304/Derivates/9C44B11D-37A6-4806-8A47-C6AC4838B7E1.jpg", "flan-queso-burgos", True, 4500)