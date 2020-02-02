from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from tree.models import Tree


def index(request):
    pv1 = Tree.objects.get(id=1)
    result = get_child(pv1)
    return HttpResponse("Tree lock - {}".format(result))

def get_tree():
    pass


def get_child(parent):
    children = Tree.objects.filter(parent=parent)
    if children.count() == 0:
        return {'name': parent.name, 'children': []}
    else:
        children_list = []
        for child in children:
            children_list.append(get_child(child))

        return {'name': parent.name, 'children': children_list}


def get_root():
    roots = Tree.objects.filter(parent=None) # request all roots to verify the correctness of the structure.
    roots_count = roots.count()
    if roots_count > 1:
        raise Exception('Incorrect data structure, more then one roots in the tree')
    elif roots_count == 0:
        raise Exception('Incorrect data structure, no  one roots in the tree')
    else:
        return roots.first()





